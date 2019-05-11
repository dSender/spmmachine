from main import yan, ok, inst, auto_ru
from time import sleep
import requests
import re



proxy = {'https':'https://157.230.240.140:8080'}


def run_appl(phone,i):
    yan(phone,i)
    ok(phone,i)
    inst(phone,i)
    auto_ru(phone,i)

def code_rev(code):
    last_code = code[0]
    with open('code.base', 'r') as file:
        text = file.readline()
        if str(text) == last_code:
            pass
        else:

            with open('code.base', 'w+') as file:
                file.write(last_code)
            for i in range(int(last_code)+1):
                run_appl(code[1],i)

def main():
    while 1:
        request = str(requests.get('https://api.telegram.org/bot< ENTER TELEGRAM API HERE >/getUpdates', proxies = proxy).text) # ******
        compiler_ = re.compile(r'"text":".+",')
        last_update_ = re.findall(compiler_, request)
        if len(last_update_) > 0:
            last_update_ = last_update_[-1]
            code_compil_ = re.compile(r'\d+')
            code = re.findall(code_compil_, last_update_)
            return code

while 1:
    code_rev(main())
    sleep(5)
