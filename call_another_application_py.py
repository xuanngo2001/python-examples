#!/bin/python3

import subprocess
subprocess.call( ["sed -i -e 's/hello/helloworld/g' inputfile.txt", shell=True] )

