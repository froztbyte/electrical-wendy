import json
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


def cacheLoad(input):
    blocks = {}

    try:
        j = json.loads(open(input, 'r').readlines()[0])
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
    finally:
        return blocks
