import random #to create random numbers
import numpy as np #to compute min/max/avg

count_array = [] #create empty array to store number of symbols for each test

for i in range(100): #repeat test 100 times to obtain significant results 
  count = 0 #start counting symbols
  state = 's0' #always begin with this state according to diagram
  while state != 'unlock': #end loop when lock is unlocked
    ran = random.randrange(10) #generate random number
    count = count+1 #count symbol

    #code below is similar to part 1 (I used integer format here instead of strings because it was easier, but can also be changed to string format like in part 1)
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
        count_array.append(count) #add final count of symbols for this one test to array
        #print('unlock')
        break #end loop because lock was unlocked
      else:
        state = 's0'
      continue

print("The minimum number of symbols generated before unlocking is:", np.min(count_array))
print("The maximum number of symbols generated before unlocking is:", np.max(count_array))
print("The average number of symbols generated before unlocking is:", np.trunc(np.mean(count_array)))