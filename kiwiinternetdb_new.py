#!/usr/bin/python3

import requests
import justext

response = requests.get("http://kiwisdr.com/public/")
if (len(response.text) < 1000):
   response = requests.get("http://kiwisdr.com/.public/")  
if response.status_code == 200:
	paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
	fd = open("kiwi.list", "w")
	for paragraph in paragraphs:
		if paragraph.text.find("http://") != -1 :
			#host = paragraph['text'][paragraph['text'].find("http://"):]
			host = paragraph.text[paragraph.text.find("http://"):]
			host = host[7:host.rfind(':')]
			#print("host is:", host)

			port = paragraph.text[paragraph.text.find(host):]
			port = port[len(host)+1:port.find(" ")]
			#print("port is:", port)

			passwd = ""
			#print("passwd is:", passwd)
			
			#desc = paragraph['text'][0:paragraph['text'].find("http://")]
			desc = paragraph.text[paragraph.text.find("KiwiSDR"):]
			#print("desc is:" , desc)
			string_to_write = ""
			string_to_write = host + ";" + port + ";" + passwd + ";" + desc + "\n";
			print(string_to_write)
			fd.write(string_to_write);
	fd.close()
			
