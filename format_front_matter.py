"""
Take a directory of files and add requisite front 
matter template to the beginning of each file.

The front matter template includes files required 
by hugo: title, date and draft.
"""

import os
import time
import datetime as dt

infolder = ''
outfolder = ''

FRONT_MATTER_TEMPLATE = '''\
---
title: {title}
date: {modified}
created: {created}
draft: true
tags: [ ]
---

'''

for f in os.listdir(infolder):
    if f.startswith('.'):
        continue
    filepath = os.path.join(infolder, f)
    if os.path.isdir(filepath):
        continue
    filename, ext = os.path.splitext(f)
    title = filename.replace('_', ' ').title()
    
    created = time.ctime(os.path.getmtime(filepath))
    created = dt.datetime.strptime(created, "%a %b %d %H:%M:%S %Y").\
                                   strftime("%Y-%m-%dT%H:%M:%S")
    modified = time.ctime(os.path.getmtime(filepath))
    modified = dt.datetime.strptime(modified, "%a %b %d %H:%M:%S %Y").\
                                    strftime("%Y-%m-%dT%H:%M:%S")

    front_matter = FRONT_MATTER_TEMPLATE.format(
                            title=title, 
                            modified=modified,
                            created=created)
    print front_matter
    with open(filepath, 'r') as f2:
        content = f2.read()
    with open(os.path.join(outfolder, f), 'w') as f3:
        f3.write(front_matter+content)


    