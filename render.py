# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import jinja2
from jinja2 import Template
import requests

url_source_json = 'https://spreadsheets.google.com/feeds/list/1doNM4JLsUD33uFSRDeqEPd8XbnTlelm8A4SG7akOAFM/od6/public/values?alt=json'

data = {}
res = requests.get(url_source_json).json()
data['entries'] = res['feed']['entry']

template = Template(open('template.tpl.html').read())
rendered = template.render(**data)
open('newsletter.html', 'w').write(rendered)
