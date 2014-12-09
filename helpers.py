import treq
from lxml.html import html5parser


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
    return html5parser.document_fromstring(text)
