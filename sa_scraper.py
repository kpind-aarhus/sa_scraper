import requests
from pathlib import Path

#Enter ID of first linkID and last linkID+1
id = range(37782505, 37782994)

#For each ID, the script access the link corresponding to the ID and downloads the image within and saves the image as this ID.
for i in id:
    res = requests.get(f'https://ao.sa.dk/ao/data.ashx?bid={i}')
    with open(Path('download', f'{i}.jpg'), 'wb') as f: #Check if the images are actually jpg
        f.write(res.content)

