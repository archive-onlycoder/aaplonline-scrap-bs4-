from types import ClassMethodDescriptorType
import requests
from bs4 import BeautifulSoup
import csv




with open('import.txt') as f:
    lines = f.readlines()


def gen_lead(data,count):
    data_header={
        'accept':'text/html',
        'accept-language':'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7,he;q=0.6',
        'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile':'?0',
        'sec-ch-ua-platform':'"Linux"',
        'sec-fetch-dest':'document',
        'sec-fetch-mode':'navigate',
        'sec-fetch-site':'none',
        'sec-fetch-user':'?1',
        'upgrade-insecure-requests':'1',
        'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    }
    x = requests.get(data,headers=data_header)
    f = open("data.html", "w")
    f.write(x.text)
    f.close() 


    email=member=website=name=street=state=zipcode=city=phone=''
    soup=BeautifulSoup(x.text,features="lxml")

    try:
        member=soup.find('ul', class_="list-group")
        member=member.find('span',class_="text-muted").text.replace('\n',' ').rstrip()
    except:
        pass


    try:
        name=soup.find('h1', class_="acadp-no-margin").text.replace('\n',' ').rstrip()
    except:
        pass

    try:
        email=soup.find('span', class_="acadp-email").text.replace('\n',' ').rstrip()
    except:
        pass

    try:
        website=soup.find('span', class_="acadp-website")
        website=website.find('a').text.rstrip()
    except:
        pass
    try:
        street=soup.find('span', class_="acadp-street-address").text.replace('\n',' ').rstrip('\n')
    except:
        pass
    try:
        city=soup.find('span', class_="acadp-city-address").text.replace('\n',' ').rstrip()
    except:
        pass
    try:
        zipcode=soup.find('span', class_="acadp-state-zipcode").text.replace('\n',' ').rstrip()
    except:
        pass
    try:
        state=soup.find('span', class_="acadp-state-address").text.replace('\n',' ').rstrip()
    except:
        pass
    try:
        phone=soup.find('span', class_="acadp-phone-number").text.replace('\n',' ').rstrip()
    except:
        pass

    
    data2=[count,name,data,member,email,phone,website,street,state,city,zipcode]
    with open('output.csv', mode='a') as open_file:
        open_writer = csv.writer(open_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        open_writer.writerow(data2)
    print(data2)
    


count=0
for line in lines: 
    gen_lead(line.strip(),count)
    count=count+1
