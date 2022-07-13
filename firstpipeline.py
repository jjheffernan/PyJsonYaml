# first pipeline

import json
import yaml

def do_json_to_yaml(filename):
	pass
	print('do json to yaml')
	f = open(filename)
	# step 2
	data = json.loads(f.read())
	# clean-up
	## print(type(data), data) #debug comment style
	temp_data = yaml.dump(data)
	output_filename = filename.replace('.json', '.yaml')
	print('output: ', output_filename)
	file_out = open(output_filename, "w")
	file_out.write(yaml.dump(data)
	f.close()	
	file_out.close()


if __name__ = '__main__':
	filename = 'donuts.json'
	do_json_to_yaml(filename)
