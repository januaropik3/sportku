#!/usr/bin/env python3
"""
SportKu Utility Scripts - Clean Version
=======================================

Clean utility functions for testing and maintenance
"""

import json
import asyncio
from pathlib import Path
from src.m3u_scraper import M3UScraper


async def test_scraper():
    """Test scraper functionality"""
    print("🧪 Testing SportKu M3U Scraper...")
    
    try:
        async with M3UScraper() as scraper:
            # Test URL access
            print("📡 Testing source URL...")
            content = await scraper.fetch_m3u_content()
            print(f"✅ Fetched {len(content)} characters")
            
            # Test parsing
            print("📝 Testing M3U parsing...")
            channels = scraper.parse_m3u_content(content)
            print(f"✅ Parsed {len(channels)} channels")
            
            # Test logo downloads (first 3)
            if channels:
                print("🖼️ Testing logo downloads...")
                test_channels = channels[:3]
                await scraper.download_logos(test_channels)
                
                downloaded_count = sum(1 for ch in test_channels if ch.local_logo_path)
                print(f"✅ Downloaded {downloaded_count}/{len(test_channels)} test logos")
            
            print("🎉 All tests passed!")
            
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False
    
    return True


def analyze_playlist():
    """Analyze playlist statistics"""
    stats_file = Path("output/stats.json")
    
    if not stats_file.exists():
        print("❌ No stats file found. Run scraper first.")
        return
    
    with open(stats_file, 'r', encoding='utf-8') as f:
        stats = json.load(f)
    
    print("📊 SportKu Playlist Analysis")
    print("=" * 40)
    print(f"📺 Total Channels: {stats['total_channels']}")
    print(f"🖼️ Channels with Logos: {stats['channels_with_logos']}")
    print(f"📈 Logo Coverage: {stats.get('logo_coverage_percent', 'N/A')}%")
    print(f"🕒 Generated: {stats['generated_at'][:19]}")
    
    if stats.get('groups'):
        print(f"\n� Channel Groups:")
        for group, count in sorted(stats['groups'].items(), key=lambda x: x[1], reverse=True):
            print(f"  • {group}: {count} channels")


def validate_config():
    """Validate configuration"""
    config_file = Path("config.json")
    
    if not config_file.exists():
        print("❌ config.json not found!")
        return False
    
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        required_fields = ["source_url", "github_repo", "output_filename"]
        missing_fields = [field for field in required_fields if field not in config]
        
        if missing_fields:
            print(f"❌ Missing fields: {', '.join(missing_fields)}")
            return False
        
        print("✅ Configuration is valid!")
        print(f"📡 Source: {config['source_url'][:50]}...")
        print(f"📂 Repository: {config['github_repo']}")
        return True
        
    except Exception as e:
        print(f"❌ Config error: {e}")
        return False


def clean_old_logs():
    """Clean old log files"""
    logs_dir = Path("logs")
    if not logs_dir.exists():
        print("📁 No logs directory found")
        return
    
    log_files = list(logs_dir.glob("scraper_*.log"))
    if len(log_files) > 5:
        old_files = sorted(log_files)[:-5]
        for file in old_files:
            file.unlink()
            print(f"🗑️ Removed old log: {file.name}")
        print(f"✅ Cleaned {len(old_files)} old log files")
    else:
        print("✅ No cleanup needed")


async def main():
    """Main utility function"""
    import sys
    
    if len(sys.argv) < 2:
        print("🛠️ SportKu Utilities")
        print("=" * 30)
        print("Usage: python utils.py <command>")
        print("\nCommands:")
        print("  test      - Test scraper functionality")
        print("  analyze   - Analyze playlist statistics") 
        print("  validate  - Validate configuration")
        print("  clean     - Clean old log files")
        return
    
    command = sys.argv[1].lower()
    
    if command == "test":
        await test_scraper()
    elif command == "analyze":
        analyze_playlist()
    elif command == "validate":
        validate_config()
    elif command == "clean":
        clean_old_logs()
    else:
        print(f"❌ Unknown command: {command}")


if __name__ == "__main__":
    asyncio.run(main())