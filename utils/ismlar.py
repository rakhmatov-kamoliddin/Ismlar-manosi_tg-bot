
import requests
from bs4 import BeautifulSoup



def ismlar_manosi(ism):
    URL=f'https://ismlar.com/name/{ism}'

    page=requests.get(URL)

    soup=BeautifulSoup(page.content,'html.parser')
    all_name = soup.find_all('div',class_='p-4 rounded-2xl mb-4 space-y-4 bg-cyan-100')
    users=[]
    for i in all_name:
        data={}
        name=i.find('h1',class_="font-bold text-2xl text-cyan-500 text-cyan-500").text
        data['name']=name.strip()
        
        name_mean = i.find('div',class_='space-y-4').text
        data['name_mean']=name_mean.strip()
        users.append(data)
        # print(name,name_mean)
    return users
        

# print(ismlar_manosi('Ramazon'))
