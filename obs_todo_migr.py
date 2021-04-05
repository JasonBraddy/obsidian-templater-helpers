#!/usr/bin/env python3

from os import listdir
from os.path import isfile, join
from re import match

daily_notes_dir = "path/to/daily/notes"
unchecked = r"- \[ \]"
prevnote = []
open_todos = []
carryover_tally = "." # append each time todo is migrated

files = [f for f in listdir(daily_notes_dir) if isfile(join(daily_notes_dir, f))]
files.sort(reverse=True)

prevfile = files[1] # need second newest file since new note exists when this is called

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
