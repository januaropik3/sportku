# 📺 SportKu - Auto IPTV M3U Scraper

![Status](https://img.shields.io/badge/Status-Active-success)
![Python](https://img.shields.io/badge/Python-3.11+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Auto Update](https://img.shields.io/badge/Auto%20Update-Daily%2000:00%20UTC-orange)

> **Clean, professional IPTV M3U playlist scraper with automatic logo management**

## 🌟 Features

- **🔄 Auto Scraping** - Daily updates at 00:00 UTC
- **🖼️ Logo Management** - Downloads and hosts all channel logos  
- **⚡ High Performance** - Async processing with concurrent downloads
- **📊 Statistics** - Detailed reports and monitoring
- **🚀 GitHub Actions** - Fully automated deployment
- **🛡️ Error Handling** - Robust retry mechanisms
- **📱 Clean Code** - Professional structure and logging

## 🚀 Quick Start

### 1. Setup
```bash
git clone https://github.com/januaropik3/sportku.git
cd sportku
pip install -r requirements.txt
```

### 2. Configuration
Update `config.json` (already configured for your repo):
```json
{
  "github_repo": "januaropik3/sportku"
}
```

### 3. Deploy to GitHub
```bash
git add .
git commit -m "🎉 Initial SportKu M3U Scraper"
git push origin main
```

### 4. Enable GitHub Actions
- Go to **Settings** → **Actions** → **General**
- Enable **"Read and write permissions"**

## 📁 Project Structure

```
sportku/
├── 📂 src/                    # Source code
│   └── m3u_scraper.py        # Main scraper
├── 📂 logos/                 # Channel logos
├── 📂 output/                # Generated files
│   ├── sportku.m3u          # Your M3U playlist
│   └── stats.json           # Statistics
├── 📂 .github/workflows/     # Auto-update workflow
├── 📄 config.json           # Configuration
└── 📄 utils.py              # Utility tools
```

## 🔗 Your Playlist URL

After deployment, your playlist will be available at:
```
https://raw.githubusercontent.com/januaropik3/sportku/main/output/sportku.m3u
```

## 📱 Usage in IPTV Players

### VLC Player
1. Media → Open Network Stream
2. Enter your M3U URL

### Android IPTV Apps
- **IPTV Smarters** - Add as M3U URL
- **TiviMate** - Add as M3U Playlist
- **Perfect Player** - Add in Playlists

## 🛠️ Development

### Local Testing
```bash
# Test configuration
python utils.py validate

# Test scraper
python utils.py test

# Run scraper manually  
cd src && python m3u_scraper.py

# Analyze results
python utils.py analyze
```

### Utilities
```bash
python utils.py validate  # Check configuration
python utils.py test      # Test functionality
python utils.py analyze   # View statistics
python utils.py clean     # Clean old logs
```

## 📊 Current Stats

- ✅ **42 channels** successfully parsed
- ✅ **100% logo coverage** (42/42 logos)
- ✅ **Auto-updates** every 00:00 UTC
- ✅ **GitHub Actions** enabled

## 🔧 Troubleshooting

### Common Issues
1. **GitHub Actions not running** - Check repository permissions
2. **Logo downloads failing** - Check internet connectivity  
3. **M3U file empty** - Verify source URL accessibility

### Debug
Enable debug logging in `src/m3u_scraper.py`:
```python
logger.setLevel(logging.DEBUG)
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push and create Pull Request

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🔗 Links

- **Issues**: [GitHub Issues](https://github.com/januaropik3/sportku/issues)
- **Actions**: [GitHub Actions](https://github.com/januaropik3/sportku/actions)
- **Statistics**: [Raw Stats](https://raw.githubusercontent.com/januaropik3/sportku/main/output/stats.json)

---

**🚀 Professional IPTV solution - Clean, fast, and reliable**