#!/usr/bin/env python3

import sys
from time import sleep
from os import listdir
from os.path import isfile, join
from re import match

# supply path via Templater user function definition: <path>/obs_todo_migr.py <% tp.file.folder(true) %>
daily_notes_dir = sys.argv[1]

unchecked = r"- \[ \]"
prevnote = []
open_todos = []
carryover_tally = "." # append each time todo is migrated

files = [f for f in listdir(daily_notes_dir) if isfile(join(daily_notes_dir, f))]

if len(files) >= 2:
    files.sort(reverse=True)
    prevfile = files[1] # need second newest file since new note exists when this is called

    # avoid race by waiting for the obs_dates_nav script which may be invoked at same time
    sleep(2)

    # grab unchecked todos to move to new day, remove from previous day's note
    with open(daily_notes_dir+"/"+prevfile, 'r+') as f:
        lines = f.readlines()
        for line in lines:
            if match(unchecked, line):
                open_todos.append(line)
            else:
                prevnote.append(line)
        f.seek(0)
        for line in prevnote:
            f.write(line)
        f.truncate()

    # Templater plugin completes macro from sdout
    for todo in open_todos:
        print(todo[:-1] + carryover_tally)
else:
    print('- [ ]')
