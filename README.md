# GSMArena data and scraper scripts
Currently the data is in a csv format, I want to improve the scraping process and include all the device specs, and save them in json format, since that seems most appropriate, because specs are dynamic. I could create a table for all the possible specs but that seems much harder especially since some elements do not have identifiable attributes or tags. I will see how to improve it so that I also do not get banned(So far, I have not haha).

## Initialization
```bash
git clone this
cd this
python -m venv .venv
.venv/Scripts/activate # If on Windows/Powershell
source .venv/bin/activate # If Mac/Linux or any bash shell
pip install -r requirements.txt
```
Data is already available in the data folder but if you want to modify the scripts and run the data yourself
```bash
python script_name.py
```

