import png
import glob
import numpy as np
from pds4_tools import pds4_read 

for i in glob.glob('*.*L'):                      # traverse file
    data = pds4_read(i,quiet=True)               # read pds
    img = np.array(data[0].data)                 # to array
    img = img.reshape(-1,2352*3)                 # reshape            
    img16 = np.array(np.uint16(img*256))         # to 16bits
    png.from_array(img16,'RGB').save(f"{i}.png") # to png & save
