import requests
import re

if __name__ == '__main__':
    with open('site.html', 'r') as file:
        site = file.read()

    regex = '<h3>(.+?)</h3>'
    for ver in re.findall(regex, site):
        print(ver)
        # if "pro" in ver:
        # print(ver)
