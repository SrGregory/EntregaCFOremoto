import json
import urllib.request
from indicator.models import Uf

def run():
	main_api = 'https://mindicador.cl/api/uf/'
	x = 1
	a = 1977
	i = 0
	while (x != -1):
		try:
			i = i + 1
			url = main_api + str(a)
			response = urllib.request.urlopen(url)
			content = response.read()
			data = json.loads(content.decode('utf8'))
			date = str(data['serie'][i]['fecha'])
			value = str(data['serie'][i]['valor'])
			name = str(data['nombre'])
			both = Uf(name=name, date=date, value=value)
			print(both.name, both.date, both.value)
			both.save()

		except IndexError:
			a = a + 1
			i = 0

		

		if (a == 2020):
			x = -1
