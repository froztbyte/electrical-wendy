#!/usr/bin/env python

import treq
from lxml.html import html5parser
from twisted.internet.task import react


def fetch(url, headers={}, agent=False):
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
    return "x %s" % len(text)
    # return html5parser.document_fromstring(text)


def main(reactor):
    citypowerURI = 'https://www.citypower.co.za/customers/' \
        'Pages/Load_Shedding.aspx'
    resp = fetch(citypowerURI)
    resp.addCallback(parse)
    if 'x' in resp:
        print len(resp)

react(main)
