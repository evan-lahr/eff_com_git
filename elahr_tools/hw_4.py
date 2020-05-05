"""
This script does the following:
    1) creates arrays, 
    2) manipulates them, 
    3) saves arrays as pickle files in output directory
    4) Uses argparse to allow user options
"""


#import modules
import numpy as np
import pickle
import sys, os
import argparse


"""
3. Add some command line functions with ArgParse: If -v=True, quit this program
"""

def boolean_string(s):
    # this function helps with getting Boolean input
    if s not in ['False', 'True']:
        raise ValueError('Not a valid boolean string')
    return s == 'False' # note use of ==

parser = argparse.ArgumentParser()

#do you want to run this program? True=YES
parser.add_argument('-run', '--run', default=True, type=boolean_string)
args = parser.parse_args()

# IF STATEMENT TO RUN/NOT RUN CODE BELOW
if args.run:
    sys.exit()
    



"""
Import local files, set output directory
"""
# local imports
sys.path.append(os.path.abspath('../shared'))
import my_module as mymod
from importlib import reload
reload(mymod)

# make sure the output directory exists
this_dir = os.path.abspath('.').split('/')[-1]
this_parent = os.path.abspath('.').split('/')[-2]
out_dir = '../../' + this_parent + '/elahr_output'
print('Creating ' + out_dir + ', if needed')
mymod.make_dir(out_dir)




"""
1. create and print matrices, try 5 methods
"""
a=np.array([[1,2,3,4,5],[6,7,8,9,-1]])
b=np.linspace(1.0, 5.0, 10).reshape((2,5))

#print('\na =')
#print(a)
#print('\nb =')
#print(b)

#1) perform matrix operations/manipulation, print results
c=a*b
print('\na*b =')
print(c)

#2) index matrix
print('\nlast index of c=')
print(c[1,4])

#3,4) make an array copy which does and does not update

#b=a.copy()     saves a copy b that does not update.
#b=a            saves a copy b that updates as a changes.

#b=a
b=a.copy()
a[0,0]=150

print('\na =')
print(a)
print('\nb =')
print(b)

#5) nan a value, convert to float, try to compute a summary stat (returns the val as nan).
b=b.astype(float)
b[0,0]=np.nan
print('\nb =')
print(b)
d=np.mean(b)
print(d)




"""
2. Have the code save some output to your output directory as a pickle file, and have it read that file back in.  Have the code make the output directory if needed.
"""
# save it as a pickle file
out_fn = out_dir + '/pickled_array.p'
pickle.dump(b, open(out_fn, 'wb')) # 'wb' is for write binary

# read the array back in
newb = pickle.load(open(out_fn, 'rb')) # 'rb is for read binary

print('\nIs the loaded newb what we expected it to be?')
print(newb)
print('\nYep!')








