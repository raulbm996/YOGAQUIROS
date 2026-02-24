import urllib.request
import re

url = "https://yogaquiros.com/"
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    img_urls = re.findall(r'http[s]?://[^\"]+?\.(?:jpg|jpeg|png|webp)', html)
    bg_urls = re.findall(r'url\([\'\"]?(http[s]?://[^\'\"]+?\.(?:jpg|jpeg|png|webp))[\'\"]?\)', html)
    
    all_urls = list(set(img_urls + bg_urls))
    for u in all_urls:
        if 'yogaquiros.com' in u:
            print(u)
except Exception as e:
    print(e)
