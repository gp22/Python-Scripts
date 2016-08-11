import requests
from requests import get

def getIpInfo():                                # get IP address info
    ipinfo = requests.get('http://ipinfo.io')
    ipinfo = ipinfo.json()
    return ipinfo

def main():
    data = getIpInfo()                          # get location info

    print("Your IP address is:", data['ip'])    # print location info
    print("Your city is:", data['city'])
    print("Your country is:", data['country'])

main()
