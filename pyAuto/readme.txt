由于解释器有bug，故需在httplib模块最后加如下代码

def patch_http_response_read(func):
    def inner(*args):
        try:
            return func(*args)
        except IncompleteRead, e:
            return ''.join(e.partial)
    return inner
HTTPResponse.read = patch_http_response_read(HTTPResponse.read)