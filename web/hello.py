def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['\r\n'.join(environ['QUERY_STRING'].split('&'))]
