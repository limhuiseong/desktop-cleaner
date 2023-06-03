import os
import glob

files = glob.glob(os.path.expanduser('~/Desktop') + '/*')

for file in files:
    os.remove(file)