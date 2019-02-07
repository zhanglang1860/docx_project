import numpy as np
import datetime
import pandas as pd
# npdtype = [('word', 'S35'), ('year', int), ('wordcount', int)]
# np_array = np.zeros((2,3,2), dtype=npdtype)
#
# word = 'word1'
# year = '2001'
# word_count = '21'
#
# tmp = np.array([('w',1,2)], dtype=npdtype)
# np_array=np.append(np_array, tmp)
# # print(np_array['word'])
#
# np_array = np.append(np_array, [['word1', int(year), int(word_count)]], axis=0)

dt = datetime.datetime(2012, 5, 1)
# A strange way to extract a Timestamp object, there's surely a better way?
ts = pd.DatetimeIndex([dt])[0]
dt64 = np.datetime64(dt)
print(dt64)