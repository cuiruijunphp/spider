from DrissionPage import ChromiumPage, ChromiumOptions
import os, random, platform

co = ChromiumOptions()
if platform.system().lower() == 'linux':
    user_dir = f'/tmp/dp_user_{os.getpid()}_{random.randint(1000,9999)}'
    port = random.randint(30000, 40000)
    co.set_argument('--no-sandbox')
    co.set_argument('--headless=new')
    co.set_argument(f'--user-data-dir={user_dir}')
    co.set_argument(f'--remote-debugging-port={port}')

page = ChromiumPage(co)
page.get('https://www.baidu.com')
print(page.title)
page.close() 