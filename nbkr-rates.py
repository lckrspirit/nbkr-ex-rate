#!/bin/python3

import requests
import xml.etree.ElementTree as ET

url_nbkr = 'https://www.nbkr.kg/XML/daily.xml'
resp = requests.get(url_nbkr).text
root_xml = ET.fromstring(resp)

rates = {}
for item in root_xml.iter('Currency'):
	for nominal in item.attrib.values():
		value_sp = item.find('Value').text.split(",")
		value = '.'.join(value_sp[0:])
		num = float(value)
		rates[nominal] = value
num = float(rates.get('USD'))
print(type(num))
