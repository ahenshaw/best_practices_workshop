import numpy as np
from timer import Timer

csv_fn = r'/temp/foo.csv'
bin_fn = r'/temp/foo.bin'

with Timer('CSV read'):
    data = np.loadtxt(csv_fn, delimiter=',')

# save in binary format
with open(bin_fn, 'wb') as fh:
    np.save(fh, data)

with Timer('Binary read'):
    data = np.load(bin_fn)

