import os
os.system("ls")

import subprocess
subprocess.run(["ls","-l","Lab1-hello-world.py"])
#subprocess.run(["ls","-l"])
#subprocess.run(["ls"])

command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])