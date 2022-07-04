from yaml import load, dump, Loader, Dumper

def get_data() -> dict:
	with open('./src/settings.yml', 'r') as file: 	
		g = load(file.read(), Loader=Loader)
	return g

def set_data(data):
	with open('./src/settings.yml', 'w') as file:
		file.write(dump(data, Dumper=Dumper))
