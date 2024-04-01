import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
if os.name == 'posix':
    os.system('clear')
else:
    os.system('cls')

print('''\x1b[38;5;82m
┓ ┓ ┓ ┓
┃ ┃ ┃ ┃
┻•┻•┻•┻
\033[0;34m--------------------------------------------\033[1;37m
[+] ABOUT SCRIPT: UNLIMITED WARP+
\033[1;37m[+] Author    : \033[1;32mSUDIPTO DEY
\033[0;34m--------------------------------------------
''')
referrer = input("\x1b[38;5;82m[\033[1;37m+\x1b[38;5;82m]\033[1;37m enter the warp+ id : ")

def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return "".join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)

def digitString(stringLength):
	try:
		digit = string.digits
		return "".join((random.choice(digit) for i in range(stringLength)))
	except Exception as error:
		print(error)

def run():
	try:
		install_id = genString(22)
		url=(f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg')
		body={
			"key": "{}=".format(genString(43)),
			"install_id": install_id,
			"fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
			"referrer": referrer,
			"warp_enabled": False,
			"tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
			"type": "Android",
			"locale": "es_ES",
		}
		data = json.dumps(body).encode('utf8')
		headers={
			'Content-Type': 'application/json; charset=UTF-8',
			'Host': 'api.cloudflareclient.com',
			'Connection': 'Keep-Alive',
			'Accept-Encoding': 'gzip',
			'User-Agent': 'okhttp/3.12.1',
		}
		req = urllib.request.Request(url, data, headers)
		response = urllib.request.urlopen(req)
		status_code = response.getcode()
		return(status_code)
	except Exception as error:
		print(error)
g = 0
b = 0

while True:
	result  = run()
	if result == 200:
		g+=1
		if os.name == 'posix':
			os.system('clear')
		else:
			os.system('cls')
		print("\x1b[38;5;82m")
		print("WARP-PLUS-CLOUDFLARE" + " power by SUDIPTO\n")
		animation = ["[■□□□□□□□□□] 10%", "[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"]
		for i in range(len(animation)):
			time.sleep(0.5)
			sys.stdout.write("\r[+] Preparing... " + animation[i % len(animation)])
			sys.stdout.flush()
		print(f"\n[=] WORK ON ID : {referrer}")
		print(f"[=] {g} GB has been successfully added to your account.")
		print(f"[=] Total: {g} Good {b} Bad")
		print(f"[=] After 21 seconds, a new request will be sent.")
		time.sleep(21)
		continue
	else:
		b+=1
		if os.name == 'posix':
			os.system('clear')
		else:
			os.system('cls')
		print("\x1b[38;5;82m")
		print("WARP-PLUS-CLOUDFLARE" + " power by SUDIPTO\n")
		print("[=] Error when connecting to server.")
		print(f"[#] Total: {g} Good {b} Bad")
		continue