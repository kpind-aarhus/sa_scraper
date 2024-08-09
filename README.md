# sa_scraper
A webscraper for downloading images from the Danish National Archives' online service, Arkivalier online. \
Please ask the National Archives for permission before downloading vast amounts of data, and please use the scraper outside of peak hours (which is usually during daylight hours). \
You can read more about conditions and Arkivalier online (in Danish) here: https://www.rigsarkivet.dk/arkivalieronline/ \
The script requires the Python library requests.

## How it works
The scraper is fairly simple. If you want to download an entire collection of images (for example a protocol), you access it through Arkivarlier online, find the first and last images of the collection and inspect their link id. \
**NB: The script only works as intended if the image ID's in a collection are consecutive.** \
For the 1623 protocol of the A line of the court books of Viborg Landsting, these are their first and last images: \
https://www.sa.dk/ao-soegesider/da/billedviser?epid=17044802#134559,37782505 \
https://www.sa.dk/ao-soegesider/da/billedviser?epid=17044802#134559,37782993 \
The actual ID's we are interested in are the last digits after the comma: 37782505 and 37782993. \
These ID's are inserted into the script, but since the range() function in Python excludes the stopping-point, the last ID needs to be 37782994. \
After running the script, the download folder should have images ranged from 37782505 to 37782993. Enjoy.
