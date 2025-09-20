# Channel Logos Directory

This directory will contain all downloaded channel logos after running the scraper.

## Logo Management:

- Logos are downloaded from original sources
- Filenames are generated using MD5 hash for uniqueness
- Supported formats: PNG, JPG, JPEG, GIF, WEBP
- Duplicate logos are automatically deduplicated

## Directory Structure Example:

```
logos/
├── abc123def456.png    # Logo for Channel 1
├── def456ghi789.jpg    # Logo for Channel 2  
├── ghi789jkl012.png    # Logo for Channel 3
└── ...
```

## Usage in M3U:

The logos are referenced in the generated M3U file using GitHub raw URLs:
```
https://raw.githubusercontent.com/januaropik3/sportku/main/logos/abc123def456.png
```

**Note:** Logo files will be automatically downloaded when you run the scraper.