#!/usr/bin/env python

'''
eskom appears to have some kind of subblocks grouping on these areas

maybe it's useful
'''

from os.path import abspath, dirname, join
from pprint import pprint
from sys import argv

from helpers import cacheLoad

dirPath = dirname(abspath(argv[0]))
jsonDir = join(dirPath, 'json')
jsonPath = join(jsonDir, 'areas.json')

blocks = cacheLoad(jsonPath)

if len(argv) == 2:
    input = unicode(argv[1], 'utf-8')
    if input in blocks:
        print '%s areas found for input %s' % (len(blocks[input]), input)
        print '\n'.join('  - %s' % x for x in blocks[input])
    else:
        print 'No areas found for input %s' % input
else:
    pprint(blocks)
