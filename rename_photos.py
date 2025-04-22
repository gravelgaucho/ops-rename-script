import os
import re
from pathlib import Path
from shutil import move

pattern = re.compile(
    r"Screen Shot (\d{4})-(\d{2})-(\d{2}) at "
    r"(\d{1,2})\.(\d{2})\.(\d{2}) (AM|PM)\.png"
)

for file in Path('.').iterdir():
    match = pattern.fullmatch(file.name)
    if not match:
        continue

    yyyy, mm, dd, hh, minute, sec, ampm = match.groups()
    hh = int(hh) % 12 + (12 if ampm == 'PM' else 0)
    new_name = f"{yyyy}-{mm}-{dd}_{hh:02}-{minute}-{sec}.png"
    print(f"{file.name} → {new_name}")
    move(file, new_name)
