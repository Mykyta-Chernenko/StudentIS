import datetime


class SimpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        from django.db import connection
        pre_time = datetime.datetime.now()
        response = self.get_response(request)
        try:
            if response._headers['content-type'][1] == 'text/html':
                after_time = datetime.datetime.now()
                response.content = response.content.\
                    replace(b"</body>", str.encode(
                    f'<div class="alert-info text-center">The number of queries is {len(connection.queries)}, '
                    f'taken time is {after_time - pre_time}</div></body>'))
        except:
            pass
        return response