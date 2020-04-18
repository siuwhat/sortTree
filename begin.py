import re
import logging
import requests
import urllib.request
import os




def get_html(repo_name, lang, branch):
    html = "http://www.github.com/" + repo_name + "/" + lang + "/"+"archive"+"/" + branch + ".zip"
    try:
        response = requests.get(html)
        print(response.status_code)
        print(html)
    except Exception as e:
        print(e)
        logging.error("无法连接主机")
    return html


def set_log():
    try:
        os.mkdir("Log")
        os.chdir("Log")
    except Exception as e:
        os.chdir("Log")


def download(url, path,repo_name):
    try:
        os.mkdir(path)
        os.chdir(path)
    except Exception as e:
        os.chdir(path)
        now_path = os.getcwd()+"\\" +repo_name+".zip"
    try:
        result = urllib.request.urlretrieve(url, now_path)
        print(result)
    except Exception as e:
        print("ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接。")
        logging.error("ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接。")

set_log()
project_name = os.getcwd().split("\\", -1)[-1]
logging.basicConfig(filename='../LOG/' + project_name + '.log',
                    format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG, filemode='a',
                    datefmt='%Y-%m-%d%I:%M:%S %p')

download(get_html("TheAlgorithms", "Java", "master"), "../github-zip", "TheAlgorithms")
