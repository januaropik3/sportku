#!/usr/bin/env python3
"""
SportKu M3U Scraper - Clean Version
===================================

Professional IPTV M3U scraper with logo management and monitoring.
Clean, optimized, and production-ready.

Author: SportKu Team
License: MIT
"""

import os
import re
import json
import logging
import hashlib
import asyncio
import aiohttp
import aiofiles
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import urlparse
from dataclasses import dataclass


@dataclass
class Channel:
    """Channel data structure"""
    name: str
    group: str
    logo_url: str
    stream_url: str
    tvg_id: str = ""
    tvg_name: str = ""
    local_logo_path: str = ""
    
    def to_m3u_line(self, base_logo_url: str = "") -> str:
        """Convert channel to M3U format line"""
        logo = f"{base_logo_url}/{self.local_logo_path}" if self.local_logo_path and base_logo_url else self.logo_url
        
        extinf_parts = ['#EXTINF:-1']
        
        if self.tvg_id:
            extinf_parts.append(f'tvg-id="{self.tvg_id}"')
        if self.tvg_name:
            extinf_parts.append(f'tvg-name="{self.tvg_name}"')
        if logo:
            extinf_parts.append(f'tvg-logo="{logo}"')
        if self.group:
            extinf_parts.append(f'group-title="{self.group}"')
            
        extinf_parts.append(self.name)
        
        return f"{' '.join(extinf_parts)}\n{self.stream_url}"


class M3UScraper:
    """Clean M3U scraper with professional logging"""
    
    def __init__(self, config_path: str = "config.json"):
        """Initialize scraper with configuration"""
        # Setup paths
        self.base_dir = Path(__file__).parent.parent
        self.logos_dir = self.base_dir / "logos"
        self.output_dir = self.base_dir / "output"
        self.logs_dir = self.base_dir / "logs"
        
        # Create directories
        for dir_path in [self.logos_dir, self.output_dir, self.logs_dir]:
            dir_path.mkdir(exist_ok=True)
            
        # Load config and setup
        self.config = self._load_config(config_path)
        self.session: Optional[aiohttp.ClientSession] = None
        self.logger = self._setup_logger()
    
    def _load_config(self, config_path: str) -> Dict:
        """Load configuration from JSON file"""
        default_config = {
            "source_url": "https://raw.githubusercontent.com/abusaeeidx/CricHd-playlists-Auto-Update-permanent/refs/heads/main/ALL.m3u",
            "github_repo": "januaropik3/sportku",
            "output_filename": "sportku.m3u",
            "max_concurrent_downloads": 10,
            "request_timeout": 30,
            "retry_attempts": 3,
            "logo_formats": [".png", ".jpg", ".jpeg", ".gif", ".webp"],
            "user_agent": "SportKu-Scraper/1.0"
        }
        
        try:
            config_file = Path(config_path)
            if config_file.exists():
                with open(config_file, 'r', encoding='utf-8') as f:
                    user_config = json.load(f)
                    default_config.update(user_config)
        except Exception as e:
            print(f"Warning: Could not load config: {e}")
            
        return default_config
    
    def _setup_logger(self) -> logging.Logger:
        """Setup clean logging system"""
        logger = logging.getLogger('sportku_scraper')
        logger.setLevel(logging.INFO)
        
        if not logger.handlers:
            # Console handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            
            # File handler
            log_file = self.logs_dir / f"scraper_{datetime.now().strftime('%Y%m%d')}.log"
            file_handler = logging.FileHandler(log_file, encoding='utf-8')
            file_handler.setLevel(logging.DEBUG)
            
            # Clean formatter
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            console_handler.setFormatter(formatter)
            file_handler.setFormatter(formatter)
            
            logger.addHandler(console_handler)
            logger.addHandler(file_handler)
        
        return logger
    
    async def __aenter__(self):
        """Async context manager entry"""
        connector = aiohttp.TCPConnector(limit=50, limit_per_host=10)
        timeout = aiohttp.ClientTimeout(total=self.config['request_timeout'])
        
        self.session = aiohttp.ClientSession(
            connector=connector,
            timeout=timeout,
            headers={'User-Agent': self.config['user_agent']}
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit"""
        if self.session:
            await self.session.close()
    
    async def fetch_m3u_content(self) -> str:
        """Fetch M3U content from source URL"""
        self.logger.info(f"Fetching M3U from source...")
        
        for attempt in range(self.config['retry_attempts']):
            try:
                async with self.session.get(self.config['source_url']) as response:
                    if response.status == 200:
                        content = await response.text(encoding='utf-8')
                        self.logger.info(f"Successfully fetched {len(content)} characters")
                        return content
                    else:
                        raise aiohttp.ClientError(f"HTTP {response.status}")
                        
            except Exception as e:
                self.logger.warning(f"Attempt {attempt + 1} failed: {e}")
                if attempt == self.config['retry_attempts'] - 1:
                    raise
                await asyncio.sleep(2 ** attempt)
    
    def parse_m3u_content(self, content: str) -> List[Channel]:
        """Parse M3U content and extract channels"""
        self.logger.info("Parsing M3U content...")
        
        channels = []
        lines = content.strip().split('\n')
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            if line.startswith('#EXTINF:'):
                extinf_data = self._parse_extinf_line(line)
                
                i += 1
                if i < len(lines):
                    stream_url = lines[i].strip()
                    
                    if stream_url and not stream_url.startswith('#'):
                        channel = Channel(
                            name=extinf_data.get('name', 'Unknown'),
                            group=extinf_data.get('group-title', 'General'),
                            logo_url=extinf_data.get('tvg-logo', ''),
                            stream_url=stream_url,
                            tvg_id=extinf_data.get('tvg-id', ''),
                            tvg_name=extinf_data.get('tvg-name', '')
                        )
                        channels.append(channel)
            
            i += 1
        
        self.logger.info(f"Parsed {len(channels)} channels")
        return channels
    
    def _parse_extinf_line(self, line: str) -> Dict[str, str]:
        """Parse EXTINF line attributes"""
        data = {}
        
        # Extract channel name
        if ',' in line:
            name_part = line.split(',', 1)[1].strip()
            data['name'] = name_part
        
        # Extract attributes with regex
        patterns = {
            'tvg-id': r'tvg-id="([^"]*)"',
            'tvg-name': r'tvg-name="([^"]*)"',
            'tvg-logo': r'tvg-logo="([^"]*)"',
            'group-title': r'group-title="([^"]*)"'
        }
        
        for key, pattern in patterns.items():
            match = re.search(pattern, line, re.IGNORECASE)
            if match:
                data[key] = match.group(1)
        
        return data
    
    async def download_logo(self, channel: Channel) -> bool:
        """Download individual channel logo"""
        if not channel.logo_url:
            return False
        
        try:
            # Generate unique filename
            url_hash = hashlib.md5(channel.logo_url.encode()).hexdigest()[:12]
            parsed_url = urlparse(channel.logo_url)
            
            extension = Path(parsed_url.path).suffix.lower()
            if not extension or extension not in self.config['logo_formats']:
                extension = '.png'
            
            filename = f"{url_hash}{extension}"
            logo_path = self.logos_dir / filename
            
            # Skip if exists
            if logo_path.exists():
                channel.local_logo_path = filename
                return True
            
            # Download logo
            async with self.session.get(channel.logo_url) as response:
                if response.status == 200:
                    content = await response.read()
                    
                    async with aiofiles.open(logo_path, 'wb') as f:
                        await f.write(content)
                    
                    channel.local_logo_path = filename
                    return True
                    
        except Exception as e:
            self.logger.debug(f"Logo download failed for {channel.name}: {e}")
        
        return False
    
    async def download_logos(self, channels: List[Channel]) -> None:
        """Download all channel logos concurrently"""
        self.logger.info("Downloading channel logos...")
        
        # Limit concurrent downloads
        semaphore = asyncio.Semaphore(self.config['max_concurrent_downloads'])
        
        async def download_with_semaphore(channel):
            async with semaphore:
                return await self.download_logo(channel)
        
        # Process downloads
        tasks = [download_with_semaphore(channel) for channel in channels if channel.logo_url]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        success_count = sum(1 for result in results if result is True)
        self.logger.info(f"Downloaded {success_count}/{len(tasks)} logos successfully")
    
    def generate_m3u_file(self, channels: List[Channel]) -> str:
        """Generate clean M3U file content"""
        self.logger.info("Generating M3U file...")
        
        base_logo_url = f"https://raw.githubusercontent.com/{self.config['github_repo']}/main/logos"
        
        lines = [
            '#EXTM3U',
            f'# SportKu Auto Scraper - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
            f'# Total channels: {len(channels)}',
            ''
        ]
        
        for channel in channels:
            lines.append(channel.to_m3u_line(base_logo_url))
            lines.append('')
        
        self.logger.info(f"Generated M3U with {len(channels)} channels")
        return '\n'.join(lines)
    
    async def save_output(self, content: str, channels: List[Channel]) -> None:
        """Save M3U file and statistics"""
        # Save M3U file
        output_file = self.output_dir / self.config['output_filename']
        async with aiofiles.open(output_file, 'w', encoding='utf-8') as f:
            await f.write(content)
        
        self.logger.info(f"Saved M3U file: {output_file}")
        
        # Generate and save statistics
        stats = {
            'total_channels': len(channels),
            'channels_with_logos': sum(1 for ch in channels if ch.local_logo_path),
            'logo_coverage_percent': round(sum(1 for ch in channels if ch.local_logo_path) / len(channels) * 100, 1),
            'groups': {},
            'generated_at': datetime.now().isoformat(),
            'source_url': self.config['source_url']
        }
        
        # Group statistics
        for channel in channels:
            group = channel.group or 'Unknown'
            stats['groups'][group] = stats['groups'].get(group, 0) + 1
        
        stats_file = self.output_dir / "stats.json"
        async with aiofiles.open(stats_file, 'w', encoding='utf-8') as f:
            await f.write(json.dumps(stats, indent=2, ensure_ascii=False))
        
        self.logger.info("Statistics saved")
    
    async def run_scraper(self) -> None:
        """Main scraper execution - clean and simple"""
        try:
            self.logger.info("=== SportKu M3U Scraper Started ===")
            
            # Fetch and parse M3U
            m3u_content = await self.fetch_m3u_content()
            channels = self.parse_m3u_content(m3u_content)
            
            if not channels:
                raise ValueError("No channels found in M3U content")
            
            # Download logos
            await self.download_logos(channels)
            
            # Generate and save output
            output_content = self.generate_m3u_file(channels)
            await self.save_output(output_content, channels)
            
            # Success summary
            logo_count = sum(1 for ch in channels if ch.local_logo_path)
            self.logger.info("=== Scraper Completed Successfully ===")
            self.logger.info(f"Processed {len(channels)} channels")
            self.logger.info(f"Downloaded {logo_count} logos ({logo_count/len(channels)*100:.1f}% coverage)")
            
        except Exception as e:
            self.logger.error(f"Scraper failed: {e}", exc_info=True)
            raise


async def main():
    """Clean main entry point"""
    async with M3UScraper() as scraper:
        await scraper.run_scraper()


if __name__ == "__main__":
    asyncio.run(main())