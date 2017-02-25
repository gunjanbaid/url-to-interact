#!/usr/bin/env python
from bottle import request, route, run, view


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
    # First define the repo name
    if url == "":
    	return 
    url = url.rstrip('//')
    if not any([i in url for i in ['data-8', 'data8.org']]):
        raise ValueError('Provide a URL attached to a data-8 repository')
    if 'github.com' in url:
        repo_split = 'data-8/'
    elif 'data8.org' in url:
        repo_split = 'data8.org/'
    else:
        raise ValueError('Provide a URL for github.com or data8.org')
    repo_parts = url.split(repo_split)[-1].split('/')
    repo = repo_parts[0]
    if len(repo_parts) == 1:
        name = '*'
    else:
        # if 'gh-pages' not in url:
        #     raise ValueError('url must use the gh-pages branch')
        # Now pull file path/name
        # name_split = 'gh-pages/' if 'github.com' in url else repo + '/'
        name_split = repo + '/'
        name = url.split(name_split)[-1]
    pre = 'https' if https is True else 'http'
    url_int = '{3}://{2}.berkeley.edu/user-redirect/interact?repo={0}&path={1}'.format(
        repo, name, url_type, pre)
    return url_int
    
@route('/', method=['GET', 'POST'])
@route('/interact', method=['GET', 'POST'])
@view('form_template')
def index():
	print(request.forms.url)
	interact = url_to_interact(request.forms.url)
	return dict(url=interact, show_url=request.method=='POST') 

run(server='gevent', host='0.0.0.0', port=os.environ.get('PORT', 5000), debug=True)
