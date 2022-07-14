import firstpipeline
import sys
import j2y
import yaml
import json


def do_yaml_to_json(filename):
    # pass
    print('to yaml form json. ')
    # step 2
    f = open(filename)
    data = yaml.full_load(f.read())
    # cleaning
    temp_data = json.dumps(data)  # for printing
    ## print(type(data), data) #debug comment style
    output_filename = filename.replace('.yaml', '.json')
    print('output: ', output_filename)
    file_out = open(output_filename, "w")
    file_out.write(json.dumps(data))
    f.close()
    file_out.close()
    # return 'yaml' in filename


if __name__ == '__main__':
    # filename = 'donuts.json'
    # this allows you to run a script as a program, as well as a module
    if len(sys.argv) != 2:
        print("not enough arguments: ")
        exit()
    print('args ', sys.argv)
    filename = sys.argv[1]
    # filename = str(sys.argv)
    if firstpipeline.is_yaml(filename):
        do_yaml_to_json(filename)
    elif firstpipeline.is_json(filename):
        j2y.do_json_to_yaml(filename)
    else:
        print('incompatible file')
    # do_json_to_yaml(filename)
