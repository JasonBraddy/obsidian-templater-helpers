#!/usr/bin/env python3

from os import listdir
from os.path import isfile, join
import datetime
from re import sub

daily_notes_dir = "path/to/daily/notes"
placeholder = "-- this is today --"
today = datetime.date.today()

files = [f for f in listdir(daily_notes_dir) if isfile(join(daily_notes_dir, f))]
files.sort(reverse=True)

prevfile = files[1] # need second newest file since new note exists when this is called
prevday = prevfile.split('.')[0]

nextnav = "[[" + str(today) + "]] >>"

# open prevfile and replace placholder with link to today's note
with open(daily_notes_dir+"/"+prevfile, 'r+') as f:
    text = f.read()
    text = sub(placeholder, nextnav, text)
    f.seek(0)
    f.write(text)
    f.truncate()

# Templater plugin completes macro from sdout
print("<< [[" + str(prevday) + "]]    " + placeholder)
