#!/usr/bin/env python3

import sys
from os import listdir
from os.path import isfile, join
import datetime
from re import sub

# supply path via Templater user function definition: <path>/obs_dates_nav.py <% tp.file.folder(true) %>
daily_notes_dir = sys.argv[1]

placeholder = "-- this is today --"
today = datetime.date.today()

files = [f for f in listdir(daily_notes_dir) if isfile(join(daily_notes_dir, f))]

if len(files) >= 2:
    files.sort(reverse=True)
    prevfile = files[1] # need second newest file since new note exists when this is called
    prevday = prevfile.split('.')[0]

    nextnav = '[[{}]] >>'.format(str(today))

    # open prevfile and replace placeholder with link to today's note
    with open(daily_notes_dir+"/"+prevfile, 'r+') as f:
        text = f.read()
        text = sub(placeholder, nextnav, text)
        f.seek(0)
        f.write(text)
        f.truncate()

    # Templater plugin completes macro from sdout
    print('<< [[{}]]    {}'.format(str(prevday), placeholder))
else:
    print(placeholder)
