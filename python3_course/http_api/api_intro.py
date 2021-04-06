import requests

start_time = input('Enter start time (format yyyy-mm-dd): ')
end_time = input('Enter end time (format yyyy-mm-dd): ')
latitude = input('Enter latitude (format x.xx): ')
longitude = input('Enter longitude (format x.xx): ')
max_radius_km = input('Enter max radius km: ')
min_magnitude = input('Enter min magnitude: ')

# start_time='2019-01-01'
# end_time='2019-02-01'
# latitude='51.51'
# longitude='-0.12'
# max_radius_km='2000'
# min_magnitude='2'

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
res = requests.get(url, headers={'Accept':'application/json'},	params=
	{
	'format': 'geojson',
	'starttime': start_time,
	'endtime': end_time,
	'latitude': latitude,
	'longitude': longitude,
	'maxradiuskm': max_radius_km,
	'minmagnitude': min_magnitude
	})

# print(type(res.json()))
# print(type(res.text))

data = res.json()
list_of_earthquakes = []
count = 0
for number in data['features']:
	if data['features'][count]['properties']['mag'] > int(min_magnitude):
		list_of_earthquakes.append(data['features'][count]['properties']['place'])
		print(f"{count + 1} Place: {data['features'][count]['properties']['place']}. Magnitude: {data['features'][count]['properties']['mag']}")
		count += 1



# print(data['features'][len([])]['properties']['mag'])




