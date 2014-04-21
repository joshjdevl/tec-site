import jinja2
import csv
from collections import defaultdict

templateLoader = jinja2.FileSystemLoader( searchpath="." )
templateEnv = jinja2.Environment( loader=templateLoader )

TEMPLATE_FILE = "template.html"
template = templateEnv.get_template( TEMPLATE_FILE )


with open('input.csv','rb') as csvfile:
    memberreader = csv.DictReader(csvfile,['name','major','imageurl','email','linkedinurl'])
    members = defaultdict(list)
    iter = 0
    for line in memberreader:
        line['iter'] = iter
        outputText = template.render( line )
        print outputText
        iter = iter + 1
