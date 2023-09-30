import requests

if __name__ == '__main__':
    with open('site.html', 'r') as file:
        site = file.read()

    regexa = '<h3>'
    regexb = '</h3>'
    for line in site.split('\n'):
        if "h3" in line:
            start = line.find(regexa) + len(regexa)
            end = line.find(regexb)
            title = line[start:end]

            print(title)
