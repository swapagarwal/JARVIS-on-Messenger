import modules
import json

status_dict = {}

for mdl in modules.tests.__all__:
    module_name = mdl[mdl.find('_') + 1:]
    try:
        eval('modules.tests.' + mdl + '.' + mdl + '()')
        status_dict[module_name] = True
    except AssertionError:
        print('Tests failed on module ' + module_name + '. Either service down or bug in module.')
        status_dict[module_name] = False

with open('status.json', 'w') as status_file:
    json.dump(status_dict, status_file)
