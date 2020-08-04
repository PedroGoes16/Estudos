import urllib.request

def url_ok(url):
    r = urllib.request.head(url)
    return r.status_code == 200


url_ok(http://www.pudim.com.br/)

