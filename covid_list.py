import requests
from twill.commands import * 

url_base = 'https://docs.google.com/forms/d/e/1FAIpQLSdYXKTMQdRfOoHGPCwgL-Ro5T7EwGGJBoe7nuaaJk1NBL4z6A/viewform?usp=pp_url'

user = {'username1':'sodienthoai1',
		'username2':'sodienthoai2',
		'username3':'sodienthoai3'}

option3 = "entry.1684030856=Kh%C3%B4ng"
option4 = "entry.1376885249=Kh%C3%B4ng"
option5 = "entry.1583936313=kh%C3%B4ng"

for key, value in user.items():
	
	print(f'Khai bao y te cho : {key} , SDT: {value}')
	
	option1 = "entry.877086558=" + key
	option2 = "entry.1630808671=" + value
	
	option = '&' + option1
	option += '&' + option2
	option += '&' + option3
	option += '&' + option4
	option += '&' + option5

	url = url_base + option
	print(url)

	go(url)
	code(200)
	submit()
	print('---------------------------------------------')



# go(url)
# code(200)
# show()
# submit()



