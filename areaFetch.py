#!/usr/bin/env python

'''
This file will connect to the citypower.co.za site and attempt to scrape a
listing of all areas connected to loadshedding, as well as their numerical
identifiers.

The purpose of this information is to attempt to reuse it in scraping the
schedule times.
'''

from twisted.internet.task import react
from helpers import fetch, parse


def addAreas(parsed):
    areas = {}
    elems = parsed.xpath(
        "//h:select[contains(@name, '$ddlSuburb')]/h:option",
        namespaces={'h': 'http://www.w3.org/1999/xhtml'})
    for elem in elems:
        k = elem.get('value')
        v = elem.text
        if u'Select a suburb' not in v:
            areas[k] = v
    return areas


def areaCAS(areas):
    from sys import argv
    from os.path import (abspath, dirname,
                         exists, join, isdir)
    from os import makedirs
    import json

    dirPath = dirname(abspath(argv[0]))
    jsonDir = join(dirPath, 'json')
    jsonPath = join(jsonDir, 'areas.json')
    if not isdir(jsonDir):
        makedirs(jsonDir)
    else:
        if not exists(jsonPath):
            j = {}
        else:
            try:
                j = json.loads(jsonPath)
            except ValueError:
                j = {}
        if j != areas:
            with open(jsonPath, 'w') as f:
                f.write(json.dumps(areas))
    return areas


def main(reactor):
    citypowerURI = 'https://www.citypower.co.za/customers/' \
        'Pages/Load_Shedding.aspx'
    resp = fetch(citypowerURI)
    resp.addCallback(parse)
    resp.addCallback(addAreas)
    resp.addCallback(areaCAS)
    return resp

react(main)
