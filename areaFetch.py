#!/usr/bin/env python

import treq
from lxml.html import html5parser
from twisted.internet.task import react

areas = {}


def fetch(url, headers={}):
    if headers is not {}:
        d = treq.get(url, headers)
    else:
        d = treq.get(url)
    d.addCallback(lambda response: response.text())
    d.addCallback(print_response)
    return d


def print_response(text):
    return text


def parse(text):
    print "len is %s" % len(text)
    return html5parser.document_fromstring(text)


def addAreas(parsed):
    elems = parsed.xpath(
        "//h:select[contains(@name, '$ddlSuburb')]/h:option",
        namespaces={'h': 'http://www.w3.org/1999/xhtml'})
    for elem in elems:
        k = elem.get('value')
        v = elem.text
        areas[k] = v
    return parsed


def main(reactor):
    citypowerURI = 'https://www.citypower.co.za/customers/' \
        'Pages/Load_Shedding.aspx'
    resp = fetch(citypowerURI)
    resp.addCallback(parse)
    resp.addCallback(addAreas)
    return resp

react(main)
