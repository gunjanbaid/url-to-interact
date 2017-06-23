#!/usr/bin/env python
import os
import gevent.monkey
from bottle import request, route, run, view

gevent.monkey.patch_all()

# Original source
# https://github.com/data-8/connector-instructors/blob/gh-pages/connectortools/utils.py
def url_to_interact(url, url_type, https=False):
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
	url = url.replace("https://", "")
	url_parts = url.split("/")
	if "data-8" not in url_parts:
		return "Error! Please provide a URL for a repo in the data-8 organization."

	org = url_parts[1]
	repo = url_parts[2]
	branch = url_parts[4]

	path_parts = url_parts[5:]
	path = ""
	for path_part in path_parts:
		path += path_part + "/"
	# removing final slash for file
	# and directory compatibility
	path = path[:len(path)-1]

	pre = "https" if https is True else "http"
	url_int = "{pre}://{url_type}.berkeley.edu/user-redirect/interact?repo={repo}&branch={branch}&path={path}"\
			  .format(pre=pre, url_type=url_type, repo=repo, branch=branch, path=path)
	return url_int
	
@route('/', method=['GET', 'POST'])
@route('/interact', method=['GET', 'POST'])
@view('form_template')
def index():
	interact = url_to_interact(request.forms.url, request.forms.urltype)
	show_url = interact != ""
	return dict(interact=interact, show_url=show_url)
	
run(server="gevent", host="0.0.0.0", port=os.environ.get("PORT", 5000), debug=True)
# run(host="localhost", port="8000")
