import subprocess
import sys
from time import sleep

input_file = sys.argv[1:]  # the first argument is the script itself

def convert(input_file):
    output_file = input_file[0].replace('.ui', '.py')
    subprocess.call(["pyuic5", "-x", input_file, "-o", output_file])
    print ('INPUT:', input_file[0], '\nOUTPUT:', output_file)
    sleep(2)

convert(input_file)e
