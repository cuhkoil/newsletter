# -*- coding: utf-8 -*-
'''
Usage:
    render <issue_id>

Parameters:
    <issue_id> can be 'ALL' to render all issues

Options:
    -h     Show this message
'''

import sys
#import base64
reload(sys)
sys.setdefaultencoding("utf-8")

import jinja2
from jinja2 import Template
import requests

def make_newsletter(url_source_json, issue_id, issue_date):
    data = {}
    res = requests.get(url_source_json).json()
    data['entries'] = res['feed']['entry']

    for e in data['entries']:
        e['gsx$description']['$t'] = e['gsx$description']['$t'].replace('\n', '<br>')

    data['issue_date'] = issue_date
    data['issue_id'] = issue_id
    #data['logo_base64'] = logo_base64

    template = Template(open('template.tpl.html').read())
    rendered = template.render(**data)
    open('issue/%s.html' % (issue_id), 'w').write(rendered)

def make_issues(url_list, predicate):
    res = requests.get(url_list).json()
    issue_list = res['feed']['entry']
    for issue in issue_list:
        if predicate(issue):
            #url_source_json = 'https://spreadsheets.google.com/feeds/list/1doNM4JLsUD33uFSRDeqEPd8XbnTlelm8A4SG7akOAFM/od6/public/values?alt=json'
            #issue_id = '20140718'
            #issue_date = 'July 18, 2014'
            url_source_json = issue['gsx$url']['$t']
            issue_id = issue['gsx$id']['$t']
            issue_date = issue['gsx$date']['$t']
            print 'making issue:', issue_date
            make_newsletter(url_source_json, issue_id, issue_date)

if __name__ == '__main__':
    from docopt import docopt
    arguments = docopt(__doc__)

    url_list = 'https://spreadsheets.google.com/feeds/list/1RXKzcnJhsm88-T-3DikGpRsOa1NJ8AVhMSHzPYaf8CI/od6/public/values?alt=json'

    if arguments['<issue_id>'] == 'ALL':
        make_issues(url_list, lambda x: True)
    else:
        make_issues(url_list, lambda x: x['gsx$id']['$t'] == arguments['<issue_id>'])


