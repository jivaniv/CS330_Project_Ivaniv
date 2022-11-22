import random
import numpy as np

count_array = []

for i in range(100):
  count = 0
  state = 's0'
  while state != 'unlock':
    ran = random.randrange(10)
    count = count+1
    if state == 's0':
      if ran == 1:
        state = 'got1'
      else:
        state = 's0'
      continue

    if state == 'got1':
      if ran == 8:
        state = 'got18'
      elif ran == 1:
        state = 'got1'
      else:
        state = 's0'
      continue

    if state == 'got18':
      if ran == 2:
        state = 'got182'
      elif ran == 1:
        state = 'got1'
      else:
        state = 's0'
      continue

    if state == 'got182':
      if ran == 8:
        state = 'got1828'
      elif ran == 1:
        state = 'got1'
      else:
        state = 's0'
      continue

    if state == 'got1828':
      if ran == 2:
        state = 'got18282'
      elif ran == 1:
        state = 'got1'
      else:
        state = 's0'
      continue

    if state == 'got18282':
      if ran == 1:
        state = 'unlock'
        count_array.append(count)
        #print('unlock')
        break
      else:
        state = 's0'
      continue

print("The minimum number of symbols generated before unlocking is:", np.min(count_array))
print("The maximum number of symbols generated before unlocking is:", np.max(count_array))
print("The average number of symbols generated before unlocking is:", np.trunc(np.mean(count_array)))