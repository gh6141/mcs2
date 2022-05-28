#!/home/kongou4313/miniconda3/envs/py38/bin/python3.8
# coding: utf-8
import sys, os
#import cgitb  #cgitbでトレースバックを生成する

print("Content-Type: text/html\n\n")
print("OK")

sys.path.insert(0, '/home/kongou4313/miniconda3/envs/py38/bin')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mcs.settings'
from wsgiref.handlers import CGIHandler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
CGIHandler().run(application)
