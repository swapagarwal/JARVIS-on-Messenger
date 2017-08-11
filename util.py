'''
The GetConfig class abstracts retrieving a key or data file name from the
config file. Create a GetConfig using the name of the key as an argument.
It will attempt to retrieve the key file with that name and save it as a string
to the object's result data member. If retrieving the key raises an exception,
result will be set to False, so it is recommended to check the value of the
variable after creating a GetConfig object.

Usage:
accessor = util.GetConfig("NAME_OF_KEY_OR_DATA_FILE")
key_string = accessor.result
assert(key_string)

Return:
key_string is either a string representing the string associated with
NAME_OF_KEY_OR_DATA_FILE in config.py, or False.
'''

class GetConfig:

    def __init__(self, line_name):
        import os
        import config

        try:
            self.result = os.environ.get(line_name, config.api_keys[line_name])
        except:
            self.result = False