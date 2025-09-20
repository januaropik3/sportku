# 🚀 Deploy Instructions for SportKu

## Langkah-langkah untuk Upload ke GitHub Repository Anda

### 1. Setup Git Repository (Jika Belum Ada)

```bash
cd "C:\Users\MS\Desktop\sportku"
git init
git branch -M main
git remote add origin https://github.com/januaropik3/sportku.git
```

### 2. Add & Commit Semua File

```bash
git add .
git commit -m "🎉 Initial SportKu M3U Auto Scraper - Professional IPTV Solution"
```

### 3. Push ke GitHub

```bash
git push -u origin main
```

### 4. Enable GitHub Actions

1. Buka repository: https://github.com/januaropik3/sportku
2. Go to **Settings** → **Actions** → **General**
3. Set **"Workflow permissions"** to:
   - ✅ **"Read and write permissions"**
   - ✅ **"Allow GitHub Actions to create and approve pull requests"**

### 5. Test GitHub Actions (Manual Trigger)

1. Go to **Actions** tab
2. Click **"Auto Update SportKu M3U"**
3. Click **"Run workflow"** → **"Run workflow"**

## 📺 Access Your M3U Playlist

Setelah berhasil deploy dan run, playlist Anda akan tersedia di:

```
https://raw.githubusercontent.com/januaropik3/sportku/main/output/sportku.m3u
```

## 🔧 Monitoring & Status

- **Actions Status**: https://github.com/januaropik3/sportku/actions
- **Statistics**: https://raw.githubusercontent.com/januaropik3/sportku/main/output/stats.json
- **Latest Logs**: Check repository artifacts

## 🎯 Success Indicators

✅ **Repository uploaded successfully**  
✅ **GitHub Actions enabled**  
✅ **First workflow run completed**  
✅ **Files generated in output/ directory**  
✅ **Logo URLs working correctly**  

## ⏰ Automatic Updates

Scraper akan berjalan otomatis setiap hari jam **00:00 UTC** (sekitar **07:00 WIB**).

---

**🚀 Your SportKu IPTV solution is now ready for production!**