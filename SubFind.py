# -*- coding: utf-8 -*
#!/usr/bin/python
#Subdomain Finder !
# Coded Shin_Code
#My Friendo : JametKNTLS -  h0d3_g4n - Moslem And All Coders
# Blog : https://www.blog-gan.org          
#Buy coffee :
	# BTC = 31mtLHqhaXXyCMnT2EU73U8fwYwigiEEU1
	# PERFECT MONEY  = U22270614
#CONTACT ME :(
       # ICQ : https://icq.im/Shin403
       # Telegram : t.me/Shin_code
       # Youtube : Smile Of Beauty 
# Apakah kamu hanya bisa melakukan recode dengan mengganti nama author?
# Can you only recode by changing the author name?
import requests,re,time
from multiprocessing.dummy import Pool
from colorama import Fore
abang = '\033[31m'
ijo = '\033[32m'
kuning = '\033[33m'
birtu = '\033[34m'
ungu = '\033[35m'
biru = '\033[36m'
abu = '\033[37m'
putih = '\033[0m' 

#Thanks To dnsdumpster.com

def banner():
	#Thanks To dnsdumpster.com
	print(abang +"SUBDOMAIN FINDER"+putih)
	print("1. Single Domain")
	print("2. Mass Domain")
	#Coded By Shin_Code
banner()
	

choose = raw_input(ijo + 'Choose Number : '+putih)

def subfind(url):
	try:
		APIS = 'https://dnsdumpster.com'
		get_cook = requests.get(APIS)
		cokis = get_cook.headers['Set-Cookie'].replace('csrftoken=','')
		cookies = {
		'csrftoken' : cokis
		}
		headers = {'Connection': 'keep-alive',
		'Upgrade-Insecure-Requests': '1',
		'Origin': 'https://dnsdumpster.com',
		'Content-Type': 'application/x-www-form-urlencoded',
		'User-Agent': 'Mozilla/5.0 (Linux; Android 12; Redmi Note 9 Pro Build/SKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36',
		'Accept-Content': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'Sec-Fetch-Site': 'same-origin',
		'Sec-Fetch-Mode': 'navigate',
		'Sec-Fetch-User': '?1',
		'Sec-Fetch-Dest': 'document',
		'Referer': 'https://dnsdumpster.com',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		}
		get_data = re.findall('name="csrfmiddlewaretoken" value="(.*?)"',get_cook.content)
		data = {'csrfmiddlewaretoken': get_data[0],
		'targetip': url,
		'user': 'free'
		}
		get_subdomain = requests.post(APIS,data=data,cookies=cookies,headers=headers).content
		get_subd = re.findall('https://api.hackertarget.com/httpheaders/(.*?)" data-target="#myModal"><span class="glyphicon glyphicon-globe" data-toggle="tooltip" data-placement="top" title="Get HTTP Headers"></span></a>',get_subdomain)
		for for_subd in get_subd:
			res_subd = for_subd.replace("?q=","")
			print('Results ' + ijo + res_subd + putih)
			open('Subdomains.txt','a').write(res_subd+'\n')
	except Exception as e:
		print(e)
		pass
		
def Main():
	try:
		if choose =='1':
			url = raw_input('Input Domain :')
			subfind(url)
		if choose =='2':
			list = raw_input('Input List Domain :')
			che = open(list, 'r').read().replace('http://','').replace('https://','').splitlines()
			pp = Pool(10)
			pr = pp.map(subfind, che)
	except:
		pass

if __name__ == '__main__':
	Main()
#My Friendo : Shin_Code - JametKNTLS -  h0d3_g4n - Moslem And All Coders
			
			
