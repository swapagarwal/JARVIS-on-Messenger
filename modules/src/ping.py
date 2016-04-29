import subprocess
import platform

def process(input, entities=None):

    output = {'input': input}

    host = entities['host'][0]['value']

    if not host:
        output['success'] = False
        output['output'] = "Please specify a host"

        return output

    ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    args = "ping " + " " + ping_str + " " + host
    need_sh = False if platform.system().lower() == "windows" else True

    text =  'System reachable' if subprocess.call(args, shell=need_sh) == 0 else 'System unrechable'

    output['output'] = test
    output['success'] = True

    return output

