import urllib
import ast
import signal
import sys

ascii_art = """\


  jjj                        iii      
        aa aa rr rr  vv   vv      sss 
  jjj  aa aaa rrr  r  vv vv  iii s    
  jjj aa  aaa rr       vvv   iii  sss 
  jjj  aaa aa rr        v    iii     s
jjjj                              sss 

Press Ctrl+C to quit
"""
print(ascii_art)

while True:
	try:
		user_input = raw_input('query> ')
	
		url = "http://localhost:5000/search/?q=" + user_input
		# opening the url
		output_raw = urllib.urlopen(url).read()
		output_dict = ast.literal_eval(output_raw)
		print(output_dict["text"])

	except KeyboardInterrupt:
		print('\nSee ya!')
		sys.exit(0)	
	
