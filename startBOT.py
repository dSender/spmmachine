from main import yan, ok
from time import sleep
import requests
import re


proxy = {'https':'https://157.230.240.140:8080'}

def code_rev(code):
    last_code = code[0]
    with open('code.base', 'r') as file:
        text = file.readline()
        if str(text) == last_code:
            pass
        else:
            with open('code.base', 'w+') as file:
                file.write(last_code)
            yan(code[1])
            ok(code[1])

def main():
    request = str(requests.get('https://api.telegram.org/bot/getUpdates', proxies = proxy).text)
    compiler_ = re.compile(r'"text":".+",')
    last_update_ = re.findall(compiler_, request)[0]
    code_compil_ = re.compile(r'\d+')
    code = re.findall(code_compil_, last_update_)
    return code

while 1:
    code_rev(main())
    sleep(60)
