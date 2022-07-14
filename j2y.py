"""
made from lecture notes by jj on 13 Jul 2022
"""
import json
import yaml
import sys
import firstpipeline
import y2j


def do_json_to_yaml(filename):
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
    file_out.write(yaml.dump(data))
    f.close()
    file_out.close()


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
        y2j.do_yaml_to_json(filename)
    elif firstpipeline.is_json(filename):
        do_json_to_yaml(filename)
    else:
        print('incompatible file')
    # do_json_to_yaml(filename)
