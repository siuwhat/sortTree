import os
import re
import fuck
import shit
pattern = re.compile(".*?git.*?")
pattern_txt = re.compile(".*?txt")
pattern_java = re.compile(".*?java")
for root, dirs, files in os.walk("github-zip"):
    for dir in dirs:
        if not re.findall(pattern, dir):
            with open(dir + ".txt", "w") as fp:
                for get in os.listdir(os.path.join(root, dir)):
                    if re.findall(pattern_java, get):
                        with open(os.path.join(root, dir, get), "r", encoding="utf-8") as rd:
                            reader = rd.read()
                            fp.write(reader + "\n")

for i in os.listdir():
    if  re.findall(pattern_txt, i):
        print(i)
        size = os.path.getsize(i)
        if size == 0:
            os.remove(i)
