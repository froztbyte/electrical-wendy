#!/usr/bin/env python

'''
eskom appears to have some kind of subblocks grouping on these areas

maybe it's useful
'''

from os.path import abspath, dirname, join
from pprint import pprint
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
except ValueError:
    print "there was some issue with some value. I'm lazy."
    pass


if len(argv) == 2:
    input = unicode(argv[1], 'utf-8')
    if input in blocks:
        print '%s areas found for input %s' % (len(blocks[input]), input)
        print '\n'.join('  - %s' % x for x in blocks[input])
    else:
        print 'No areas found for input %s' % input
else:
    pprint(blocks)
