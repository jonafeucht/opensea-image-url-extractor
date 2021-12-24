# With help of puziyi
import json
from haralyzer import HarParser, HarPage

with open('opensea.io.har', 'r') as f:
    har_parser = HarParser(json.loads(f.read()))

data = har_parser.har_data["entries"]
image_urls = []

for entry in data:
    if entry["response"]["content"]["mimeType"].find("image/") == 0:
        image_urls.append(entry["request"]["url"])
     
with open('target_link.txt', 'w') as f:
    for link in image_urls:
        f.write("%s\n" % link)