import json
import os
from sys import argv
from pprint import pprint

assets = []

for vid in argv[1:]:
    print(vid)
    basename = os.path.basename(vid)
    assets.append(
        {
            "timeOfDay": "sunset",
            "accessibilityLabel": "London",
            "title": basename,
            "scene": "city",
            "id": basename,
            "url-4K-SDR": f"https://static.ioloop.io/{basename}",
            "url-1080-SDR": "",
            "url-1080-H264": "",
            "pointsOfInterest": {},
        }
    )

doc = {"assets": assets}
json.dump(doc, open("entries.json", "w"))
pprint(doc)
