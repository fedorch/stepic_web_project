def app(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return  ['Hello, world!\r\n', environ['QUERY_STRING']]
