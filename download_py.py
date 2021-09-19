#!/usr/bin/python2

import requests ,optparse


def get_link():
    parser=optparse.OptionParser()
    parser.add_option("-l","--link",dest="url",help="direct link of file to download .pdf")
    (url,argument)=parser.parse_args()
    return url

def download(url):
    try:
        get_request=requests.get(url)
        name_url=url.split("/")[-1]
        print(name_url)
        with open(name_url,"wb") as file:
            file.write(get_request.content)
    except:
        print("[-]Print Valid Link")
        
       


def start():
    url_link=get_link()
    try:	
        download(url_link.url)
    except:
        url_link=input("[+]Enter link:")
        download(url_link)

start()



