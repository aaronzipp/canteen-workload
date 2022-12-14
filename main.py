import os
import time
from datetime import date, datetime

from bs4 import BeautifulSoup
from requests import get
from tqdm import trange

REPEATS = 40
WAITING_SECONDS = 300
URL = "https://mensa.liste.party"
FILEPATH = os.path.join("data", f"canteen-{date.today()}.csv")

if __name__ == "__main__":
    for _ in trange(REPEATS):
        response = get(URL)
        bs = BeautifulSoup(response.text, "html.parser")
        count = int(bs.find(id="current").text.replace(",", ""))
        current_time = datetime.now()
        with open(FILEPATH, "a") as file:
            file.write(f"{current_time},{count}\n")
        time.sleep(WAITING_SECONDS)
