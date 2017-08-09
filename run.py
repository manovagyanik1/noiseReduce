import os  
import subprocess
directory = 'cleanedVideo'
if not os.path.exists(directory):
    os.makedirs(directory)

for fn in os.listdir('.'):
     if os.path.isfile(fn):
        if fn.lower().endswith('.mp4') or fn.lower().endswith('.mts'):
        	print(fn)
        	arg2 = directory + '/' +fn
        	command = 'noiseclean.sh '+fn + ' ' + arg2
        	print(command)
        	output = subprocess.check_output(['noiseclean.sh',str(fn),str(arg2)],shell=True)
        	print(output)
        	# Process = subprocess.Popen(['./noiseclean.sh',str(fn),str(arg2)],shell=True,stdin=subprocess.PIPE,stderr=PIPE)
        	# print Process.communicate()
        	# os.system(command)
        	# subprocess.call(['bash', 'noiseclean.sh', fn, arg2])