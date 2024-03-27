import requests
from pathlib import Path

#Enter ID of first linkID and last linkID+1.
id = range(37782505, 37782506)

#For each ID, the script access the link corresponding to the ID and downloads the image within and saves the image as this ID.
for i in id:
    res = requests.get(f'https://ao.sa.dk/ao/data.ashx?bid={i}')
    try:
        res.raise_for_status()
        with open(Path('download', f'{i}.jpg'), 'wb') as f: #Check the image format by downloading a sample if you are uncertain whether it is .jpg.
            f.write(res.content)
            print(f'{i}.jpg'+' downloaded')
    except:
        print("There was an error")
