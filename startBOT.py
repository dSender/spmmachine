from main import yan, ok, inst, auto_ru
from time import sleep
import requests
import re



proxy = {'https':'https://157.230.240.140:8080'}

def run_appl(phone):
    yan(phone)
    ok(phone)
    inst(phone)
    auto_ru(phone)

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
                run_appl(code[1])
                sleep(5)



def main():
    request = str(requests.get('https://api.telegram.org/bot <> /getUpdates', proxies = proxy).text)
    compiler_ = re.compile(r'"text":".+",')
    last_update_ = re.findall(compiler_, request)[-1]
    code_compil_ = re.compile(r'\d+')
    code = re.findall(code_compil_, last_update_)
    return code

while 1:
    code_rev(main())
    sleep(5)
