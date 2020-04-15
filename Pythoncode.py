# importing the requests library
import requests
import json

#Assigning mac address 
my_mac_addrs=raw_input("Enter your MAC adddress: ")
print(my_mac_addrs)

# api-endpoint
URL = "https://macaddress.io/"
response=requests.get(URL)
print(response.json())