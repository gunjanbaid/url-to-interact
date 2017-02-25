#!/usr/bin/env python
import os
import gevent.monkey
from bottle import request, route, run, view

gevent.monkey.patch_all()

# Original author
# https://github.com/data-8/connector-instructors/blob/gh-pages/connectortools/utils.py

def url_to_interact(url, url_type='datahub', https=False):
	"""Create an interact link from a URL in github or data-8.org.

	Parameters
	----------
	url : string
		The URL of the file/folder you want to convert to an interact link.
	url_type : one of 'datahub' | 'ds8' | 'data8'
		Whether the output URL should be attached to ds8 or data8.
	"""
	if url == "":
		return ""
	url = url.rstrip('//')
	if not any([i in url for i in ['data-8', 'data8.org']]):
		return "Error! Please provide a URL for a repo in the data-8 organization."
	if 'github.com' in url:
		repo_split = 'data-8/'
	elif 'data8.org' in url:
		repo_split = 'data8.org/'
	else:
		print("IHGSIRHGIOH")
		return "Error! Please provide a valid URL."
	repo_parts = url.split(repo_split)[-1].split('/')
	repo = repo_parts[0]
	if len(repo_parts) == 1:
		name = '*'
	else:
		name_split = repo + '/'
		name = url.split(name_split)[-1]
	pre = "https" if https is True else "http"
	url_int = "{0}://{1}.berkeley.edu/user-redirect/interact?repo={2}&path={3}".format(pre, url_type, repo, name)
	return url_int
	
@route('/', method=['GET', 'POST'])
@route('/interact', method=['GET', 'POST'])
@view('form_template')
def index():
	interact = url_to_interact(request.forms.url)
	error = "Error! " in interact or interact == ""
	show_url = interact != ""
	return dict(interact=interact, show_url=show_url, error=error)
	
run(server="gevent", host="0.0.0.0", port=os.environ.get("PORT", 5000), debug=True)
# run(host="localhost", port="8000")
