import os
import re
from datetime import datetime

appdata = os.getenv('LOCALAPPDATA')

directory = os.path.join(appdata, r'..\LocalLow\Colossal Order\Cities Skylines II\Screenshots')

current_date = datetime.now()

pattern = re.compile(r"(\d{2})-([A-Za-z]+)-(\d{2}-\d{2}-\d{2}-\d{2})(.*)\.png")

months = {
    "January": "01", "February": "02", "March": "03",
    "April": "04", "May": "05", "June": "06",
    "July": "07", "August": "08", "September": "09",
    "October": "10", "November": "11", "December": "12"
}

for filename in os.listdir(directory):
    match = pattern.match(filename)
    if match:
        day = match.group(1)
        month_name = match.group(2)
        time_part = match.group(3)
        extra = match.group(4) or ""
        month = months.get(month_name, "01")
        new_date = f"2024-{month}-{day}"
        diff = (current_date - datetime(2024,int(month),int(day))).days
        if int(diff) < 0:
            year = "2023"
        else:
            year = "2024"
        new_date = f"{year}-{month}-{day}"
        new_filename = f"{new_date}_{time_part}{extra}.png"
        
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_filename)
        
        os.rename(old_file, new_file)
        print(f"Renamed: {filename} -> {new_filename}")

print("Renaming complete.")
