from requests import get
from requests.exceptions import RequestException
from contextlib import closing

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}


def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_agood_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error('Error During request to {0} : {1}'.format(url, str(e)))
        return None


def is_agood_response(myResponse):
    content_type = myResponse.headers['Content-Type'].lower()
    return (content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    print(e)
