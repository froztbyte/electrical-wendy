#!/usr/bin/env python

'''
eskom appears to have some kind of subblocks grouping on these areas

maybe it's useful
'''

from os.path import abspath, dirname, join
from sys import argv
import json

dirPath = dirname(abspath(argv[0]))
jsonDir = join(dirPath, 'json')
jsonPath = join(jsonDir, 'areas.json')

blocks = {}

try:
    j = json.loads(open(jsonPath, 'r').readlines()[0])
    for idx in j.iterkeys():
        item = j[idx]
        bl = item.split('-')[1].strip()
        if blocks.get(bl, None) is not None:
            blocks[bl].append(j[idx])
        else:
            blocks[bl] = [j[idx]]
    print repr(blocks)
except ValueError:
    pass
