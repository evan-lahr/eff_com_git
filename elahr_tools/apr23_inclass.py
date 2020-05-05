"""
Code to test input and (filtered) output of a text file.
"""

# imports
import sys, os
sys.path.append(os.path.abspath('shared'))
import my_module as mymod
import matplotlib.pyplot as plt


myplace = 'elahr' # *** YOU NEED TO EDIT THIS ***

# input directory
in_dir = '../' + myplace + '_data/'

# make sure the output directory exists
out_dir = '../' + myplace + '_output/'
mymod.make_dir(out_dir)

# define the input filename
in_fn = in_dir + '2017-01-0118.ctd'
# this is some Canadian CTD data, formatted in a strict but
# difficult-to-use way

# define the output filename
out_fn = out_dir + 'out_test2.txt'


# go through the input file one line at a time, and just
# write decimal versions of the latitude and longitude
# to the output file
f=open(in_fn, 'r', errors='ignore')
print(f)

#    lines = f.readlines()
#    x = [float(line.split()[0]) for line in lines]
#    y = [float(line.split()[1]) for line in lines]
#plt.plot(x ,y)
#plt.show()