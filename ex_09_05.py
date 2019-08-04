inp=input ('Enter file name: ')
try:
    h=open (inp)
except:
    print('Invalid input !')
    exit()
domains_list=[]
for line in h:
    line=line.rstrip()
    #words=line.split()
    if line.startswith ('From:'):
        #print (line)
        delimiter='@'
        t=line.split(delimiter)
        #print (t[1])
        domains_list.append (t[1])
#print (domains_list)
d={}
for domain in domains_list:
    d [domain]=d.get (domain,0)+1
print (d)
