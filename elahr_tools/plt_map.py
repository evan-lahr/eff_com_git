"""
Code to plot a 4-band geotiff downloaded from planet.com
"""
# module imports
import rasterio
import matplotlib.pyplot as plt
import numpy as np
# local imports
import my_module as mymod
import sys, os
sys.path.append(os.path.abspath('shared'))


myplace = 'elahr' # *** YOU NEED TO EDIT THIS ***
# input directory
in_dir = '../' + myplace + '_data/'
# make sure the output directory exists
out_dir = '../' + myplace + '_output/'
mymod.make_dir(out_dir)
# define the input filename
image_file = in_dir + '20200401_023002_1043_3B_AnalyticMS.tif'
# this is planet's planetscope BGRN 3 m res imagery

# define the output filename
out_fn = out_dir + 'map_test.txt'
# open the output file for writing
outfile = open(out_fn, 'w')


# Load red and NIR bands - note all PlanetScope 4-band images have band order BGRN
with rasterio.open(image_file) as src:
    band_blue = src.read(1)
    band_green = src.read(2)
    band_red = src.read(3)
    band_nir = src.read(4)


# Function to normalize the grid values
def normalize(array):
    """Normalizes numpy arrays into scale 0.0 - 1.0"""
    array_min, array_max = array.min(), array.max()
    return ((array - array_min)/(array_max - array_min))



# normalize rgb. bands 0 to 1
blun=normalize(band_blue)
gren=normalize(band_green)
redn=normalize(band_red)
nirn=normalize(band_nir)

# Create RGB natural color composite
rgb = np.dstack((redn, gren, blun))





fig = plt.figure(figsize=(12,8))
ax1 = plt.subplot2grid((4,4), (0, 0), colspan=4, rowspan=3)
plt.imshow(rgb)
ax1.set_title('True Color Composite from 4-band PlanetScope Data')
plt.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    left=False,         # ticks along the left edge are off
    right=False,         # ticks along the right edge are off
    labelleft=False,
    labelbottom=False) # labels along the bottom edge are off



ax2 = plt.subplot2grid((4,4), (3, 0), colspan=1, rowspan=1)
plt.imshow(redn, cmap='Reds')
ax2.set_title('Red Band')
plt.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    left=False,         # ticks along the left edge are off
    right=False,         # ticks along the right edge are off
    labelleft=False,
    labelbottom=False) # labels along the bottom edge are off

ax3 = plt.subplot2grid((4,4), (3, 1), colspan=1, rowspan=1)
plt.imshow(blun, cmap='Blues')
ax3.set_title('Blue Band')
plt.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    left=False,         # ticks along the left edge are off
    right=False,         # ticks along the right edge are off
    labelleft=False,
    labelbottom=False) # labels along the bottom edge are off

ax4 = plt.subplot2grid((4,4), (3, 2), colspan=1, rowspan=1)
plt.imshow(gren, cmap='Greens')
ax4.set_title('Green Band')
plt.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    left=False,         # ticks along the left edge are off
    right=False,         # ticks along the right edge are off
    labelleft=False,
    labelbottom=False) # labels along the bottom edge are off

ax5 = plt.subplot2grid((4,4), (3, 3), colspan=1, rowspan=1)
plt.imshow(nirn, cmap='binary')
ax5.set_title('NIR Band')
plt.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    left=False,         # ticks along the left edge are off
    right=False,         # ticks along the right edge are off
    labelleft=False,
    labelbottom=False) # labels along the bottom edge are off

fig.tight_layout()
plt.savefig('AFTER.png',dpi=300)

plt.show()

