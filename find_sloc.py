import os
import sys
import subprocess
import re

# compiled_objects list is obtained by <find . -name "*.o" -type f>
f = open("compiled_objects", 'r')

total_sloc = 0
for line in f:
#    print(line)
    c_file = line.strip()
    c_file = c_file[:-1] + 'c'
    try:
        result = subprocess.check_output(['sloccount', c_file])
        result = result.decode('UTF-8')
        number = re.search(r'.*Total Physical Source Lines of Code.*= (.*)', result)
        if number is not None:
            tmp = int(number.groups()[0].replace(',',''))
            print(c_file + " : " + str(tmp))
            total_sloc += tmp
    except subprocess.CalledProcessError:
        print(c_file + " file not found")



print("Total SloC: ", total_sloc)


