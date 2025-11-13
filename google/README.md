# Google Fonts Files

[https://github.com/google/fonts](https://github.com/google/fonts)

```
find /Users/march/cdn/google/fonts -type f -name "OFL.txt" -delete
find /Users/march/cdn/google/fonts -type f -name "LICENSE.txt" -delete
find /Users/march/cdn/google/fonts -type f -name "DESCRIPTION.en_us.html" -delete
find /Users/march/cdn/google/fonts -type f -name "config.yaml" -delete
find /Users/march/cdn/google/fonts -type f -name "METADATA.pb" -delete
find /Users/march/cdn/google/fonts -type f -name "ARTICLE.en_us.html" -delete
find /Users/march/cdn/google/fonts -type f -name "*.png" -delete
find /Users/march/cdn/google/fonts -type f -name "*.gif" -delete
find /Users/march/cdn/google/fonts -type f -name "*.jpg" -delete
find /Users/march/cdn/google/fonts -type f -name "*.mp4" -delete
find /Users/march/cdn/google/fonts -type f -name "*.svg" -delete
find /Users/march/cdn/google/fonts -type f -name "*.jpeg" -delete
find /Users/march/cdn/google/fonts -type f -name "*.txt" -delete
find /Users/march/cdn/google/fonts -type f -name "*.yaml" -delete
find /Users/march/cdn/google/fonts -type d -empty -delete

python3 generate_md5_json.py ./fonts
python3 generate_md5_json.py ./fonts --include .ttf,.otf
```