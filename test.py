# import time
# import re
# from urllib import request
# import requests
# url="https://api.github.com/repos/siuwhat/cnblogs"
# try:
#     r=requests.get(url)
#     time.sleep(10)
#     print(r.status_code)
#     repo_dict=r.json()
#     print(repo_dict['id'])
# except Exception as e:
#     print(e)
import re
str = '<h3><a href="/Python3WebSpider/DouYin" itemprop="name codeRepository">DouYin</a></h3>'
pattern = re.compile('<h3>.*?<a href=.*?itemprop="name codeRepository">(.*?)</a>.*?</h3>', re.S)
items = re.findall(pattern, str)
for item in items:
    zipurl = 'https://github.com/Python3WebSpider/' + item + '/archive/master.zip'
print(zipurl)
