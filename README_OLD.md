# 📺 SportKu - Auto IPTV M3U Scraper

![Status](https://img.shields.io/badge/Status-Active-success)
![Python](https://img.shields.io/badge/Python-3.11+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Auto Update](https://img.shields.io/badge/Auto%20Update-Daily%2012AM-orange)

> Modern and professional IPTV M3U playlist scraper with automatic logo management and GitHub deployment.

## 🌟 Features

- **🔄 Auto Scraping**: Automatically scrapes M3U playlists every day at 12:00 AM
- **🖼️ Logo Management**: Downloads and hosts channel logos in your repository  
- **⚡ Async Processing**: High-performance concurrent downloading
- **📊 Statistics**: Detailed processing statistics and reports
- **🚀 GitHub Actions**: Fully automated with GitHub Actions
- **📱 Modern Structure**: Professional project organization
- **🛡️ Error Handling**: Robust error handling and retry mechanisms
- **📝 Logging**: Comprehensive logging and monitoring

## 🚀 Quick Start

### 1. Setup Repository

1. **Fork/Clone this repository**
2. **Update configuration** in `config.json`:
   ```json
   {
     "github_repo": "januaropik3/sportku"  // Already configured for your repo
   }
   ```

### 2. GitHub Actions Setup

1. **Enable GitHub Actions** in your repository settings
2. **Set repository permissions**:
   - Go to Settings → Actions → General
   - Enable "Read and write permissions"
   - Enable "Allow GitHub Actions to create and approve pull requests"

### 3. Manual Run (Optional)

```bash
# Install dependencies
pip install -r requirements.txt

# Run scraper locally
cd src
python m3u_scraper.py
```

## 📁 Project Structure

```
sportku/
├── 📂 src/                    # Source code
│   └── m3u_scraper.py        # Main scraper script
├── 📂 logos/                 # Downloaded channel logos
├── 📂 output/                # Generated M3U files
│   ├── sportku.m3u          # Main playlist
│   └── stats.json           # Processing statistics
├── 📂 logs/                  # Application logs
├── 📂 .github/workflows/     # GitHub Actions
│   └── auto-update.yml      # Auto update workflow
├── 📄 config.json           # Configuration
├── 📄 requirements.txt      # Python dependencies
└── 📄 README.md            # This file
```

## ⚙️ Configuration

Edit `config.json` to customize behavior:

```json
{
  "source_url": "https://raw.githubusercontent.com/abusaeeidx/CricHd-playlists-Auto-Update-permanent/refs/heads/main/ALL.m3u",
  "github_repo": "your-username/sportku",
  "output_filename": "sportku.m3u",
  "max_concurrent_downloads": 10,
  "request_timeout": 30,
  "retry_attempts": 3,
  "logo_formats": [".png", ".jpg", ".jpeg", ".gif", ".webp"],
  "user_agent": "SportKu-Scraper/1.0"
}
```

## 🔗 Access Your Playlist

Once the scraper runs successfully, access your playlist at:

### 📺 Direct M3U Link
```
https://raw.githubusercontent.com/januaropik3/sportku/main/output/sportku.m3u
```

### 📊 Statistics
```
https://raw.githubusercontent.com/januaropik3/sportku/main/output/stats.json
```

## 📈 Features Details

### 🔄 Automatic Updates
- Runs daily at 12:00 AM UTC via GitHub Actions
- Checks for changes and only commits when needed
- Generates release notes with statistics

### 🖼️ Logo Management
- Downloads all channel logos locally
- Generates unique filenames to avoid conflicts
- Updates M3U to point to your repository's logos
- Supports multiple image formats

### ⚡ Performance
- Async/await architecture for high performance
- Concurrent downloads with configurable limits
- Retry mechanisms with exponential backoff
- Comprehensive error handling

### 📊 Monitoring
- Detailed logging with multiple levels
- Processing statistics and reports
- GitHub Actions status tracking
- Artifact uploads for debugging

## 🛠️ Development

### Local Development
```bash
# Clone repository
git clone https://github.com/januaropik3/sportku.git
cd sportku

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run scraper
cd src
python m3u_scraper.py
```

### Testing
```bash
# Test manual run
cd src
python -m pytest  # If you add tests

# Test GitHub Actions locally (with act)
act workflow_dispatch
```

## 📋 Usage in IPTV Players

### VLC Media Player
1. Open VLC
2. Media → Open Network Stream
3. Enter: `https://raw.githubusercontent.com/your-username/sportku/main/output/sportku.m3u`

### Android Players
- **IPTV Smarters**: Add as "M3U URL"
- **TiviMate**: Add as "M3U Playlist"  
- **Perfect Player**: Add in "Playlists"

### Other Players
Use the raw GitHub URL in any M3U-compatible IPTV player:
```
https://raw.githubusercontent.com/januaropik3/sportku/main/output/sportku.m3u
```

## 🔧 Troubleshooting

### Common Issues

1. **GitHub Actions not running**
   - Check repository permissions in Settings → Actions
   - Ensure workflow file is in `.github/workflows/`

2. **Logo downloads failing**
   - Check internet connectivity
   - Verify source URLs are accessible
   - Review logs in `logs/` directory

3. **M3U file empty**
   - Verify source URL is accessible
   - Check parsing logic for format changes
   - Review error logs

### Debug Mode
Enable detailed logging by modifying the logger level in `m3u_scraper.py`:
```python
logger.setLevel(logging.DEBUG)
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⭐ Acknowledgments

- **Source Data**: [CricHd-playlists-Auto-Update](https://github.com/abusaeeidx/CricHd-playlists-Auto-Update-permanent)
- **Inspiration**: Various IPTV community projects
- **Tools**: Python, GitHub Actions, aiohttp

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/januaropik3/sportku/issues)
- **Discussions**: [GitHub Discussions](https://github.com/januaropik3/sportku/discussions)

---

**⚡ Auto-generated playlist with love by SportKu Scraper**

> 🎯 **Latest Update**: Check the [Actions tab](https://github.com/januaropik3/sportku/actions) for the latest run status

![Footer](https://raw.githubusercontent.com/januaropik3/sportku/main/.github/banner.png)