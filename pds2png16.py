import png
import glob
import numpy as np
from pds4_tools import pds4_read   

for i in glob.glob('*.*L'):                     # traverse file
    data = pds4_read(i,quiet=True)              # read pds
    img = np.array(data[0].data)                # to array
    img16 = np.array(np.uint16(img*32))         # to 16bits
    png.from_array(img16,'L').save(f"{i}.png")  # to png & save
