import getpass 

state = 's0' #first state is s0 as shown in attached drawing
while True:
  string = getpass.getpass("Input: ") #hides inputs (doesn't echo inputs)

  if string == "": #end loop if nothing is inputted
    break

#the rest of the code is composed of if/else statements based on the attached state transition diagram
  if state == 's0':
    if string == '1':
      state = 'got1'
    else:
      state = 's0'
    continue #make sure to continue to next input1

  if state == 'got1':
    if string == '8':
      state = 'got18'
    elif string == '1':
      state = 'got1'
    else:
      state = 's0'
    continue

  if state == 'got18':
    if string == '2':
      state = 'got182'
    elif string == '1':
      state = 'got1'
    else:
      state = 's0'
    continue

  if state == 'got182':
    if string == '8':
      state = 'got1828'
    elif string == '1':
      state = 'got1'
    else:
      state = 's0'
    continue

  if state == 'got1828':
    if string == '2':
      state = 'got18282'
    elif string == '1':
      state = 'got1'
    else:
      state = 's0'
    continue

  if state == 'got18282':
    if string == '1':
      state = 'unlock'
      print('unlock')
    elif string == '4':
      state = 'lock'
      print('lock')
    else:
      state = 's0'
    continue

#repeat cycle

  if state == 'unlock':
    if string == '1':
      state = 'got1'
    else:
      state = 's0'
    continue

  if state == 'lock':
    if string == '1':
      state = 'got1'
    else:
      state = 's0'
    continue
