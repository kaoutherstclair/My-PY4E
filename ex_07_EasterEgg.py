file_name= input ('Please enter file name: ')
if file_name=='na na boo boo':
    easter_egg= "NA NA BOO BOO TO YOU - You have been punk'd!"
    print (easter_egg)
    exit ()
else:
    try:
        handle=open (file_name)
    except:
        print ('File cannot be opened:', file_name)
        exit()
count=0
total=0
# This code is for for larger files:
for line in handle:
    line= line.rstrip()
    if not line.startswith ('X-DSPAM-Confidence:'): continue
    count=count+1
    con_string = line [20:28]
    confidence = float (con_string)
    total = total+confidence
average= total / count
print ('There are', count, ' lines.\n', 'The average confidence is:', average)
