import time,sys,tty,termios,os,sys
p=os.path.abspath(sys.argv[0])
p=p[:-p[::-1].index('/')]
os.system('python3 '+p+'gs.py '+sys.argv[1]+' &')
while 1:
<<<<<<< HEAD
 time.sleep(1/len(sys.argv[1]))
 print('\x1b[H',end='')
 ns=sn[:]
 ns+=[[ea,eq]]
 ns+=bd
 pns=[w for w in ns if w not in ons]
 mns=[w for w in ons if w not in ns]
 print('\x1b[33m',)
 for w in pns:
  if w[1]%2:
   if [w[0],w[1]-1] in ns:
    print('\x1b['+str(w[1]//2+1)+';'+str(w[0]+1)+'H█',)
   else:
    print('\x1b['+str(w[1]//2+1)+';'+str(w[0]+1)+'H▄',)
  else:
   if [w[0],w[1]+1] in ns:
    print('\x1b['+str(w[1]//2+1)+';'+str(w[0]+1)+'H█',)
   else:
    print('\x1b['+str(w[1]//2+1)+';'+str(w[0]+1)+'H▀',)
 for w in mns:
  if w[1]%2:
   if [w[0],w[1]-1] in ns:
    print('\x1b['+str(w[1]//2+1)+';'+str(w[0]+1)+'H▀',)
   else:
    print('\x1b['+str(w[1]//2+1)+';'+str(w[0]+1)+'H ',)
  else:
   if [w[0],w[1]+1] in ns:
    print('\x1b['+str(w[1]//2+1)+';'+str(w[0]+1)+'H▄',)
   else:
    print('\x1b['+str(w[1]//2+1)+';'+str(w[0]+1)+'H ',)
 ons=ns[:]
 oul='█'*(bdl*term()[0]//bdw)+int(bool(max(bdl,0)))*chr(9615-max(bdl,0)*term()[0]*8//bdw%8)
 oub=oue=0
 if len(loul)!=len(oul):
  print('\x1b['+str(term()[1]-3)+';0H'+'  '*term()[0],)
  print('\x1b['+str(term()[1]-3)+';0H'+oul,)
  loul=oul
 else:
  oub=0
  while oub<len(oul) and oul[oub]==loul[oub]:
   oub+=1
  oue=len(oul)
  while oue>oub and oul[oue-1]==loul[oue-1]:
   oue-=1
  print('\x1b['+str(term()[1]-3)+';'+str(oub)+'H'+oul[oub:oue],end='')
# print('\x1b['+str(term()[1]-2)+';0H'+'now:',len(sn),'max:',ma,'aver:',averwnd='')
 if lpl!=[len(sn),ma] or oue!=oub:
  print('\x1b['+str(term()[1]-2)+';0H'+'now:',len(sn),'max:',ma,)
  lpl=[len(sn),ma]
 if spc==0:
  print('\x1b['+str(term()[1]-4)+';0H'+'═'*term()[0],)
  spc=128
 print('\x1b[0;0H',end='')
 spc-=1
 print('\x1b[35m',)
 if bdc==bdm:
  bdq=random.randint(1,term()[1]*2-12)
  bda=random.randint(1,term()[0]-2)
  bd+=[[bda-1,bdq-1]]
  bd+=[[bda+1,bdq-1]]
  bd+=[[bda-1,bdq+1]]
  bd+=[[bda+1,bdq+1]]
  bd+=[[bda+1,bdq]]
  bd+=[[bda-1,bdq]]
  bd+=[[bda,bdq+1]]
  bd+=[[bda,bdq-1]]
  bd+=[[bda,bdq]]
  bdc=bdm+1
  bdl=bdw
 elif bdc==0:
  bd=[]
 if bdl==0:
  bd=[]
  bdc=0
 bdl-=1
 nls=int(os.popen('ls -l char').read().split()[4])
 z=open('char','rb')
 z.read(ls)
 nfs=z.read(nls-ls)
 fs+=nfs.decode()
 z.close()
 ls=nls
 if fs=='\x1b[A':
  fs='w'
 if fs=='\x1b[B':
  fs='s'
 if fs=='\x1b[C':
  fs='d'
 if fs=='\x1b[D':
  fs='a'
 fs=''.join([fff for fff in fs if fff in 'asdwp'])
 if fs== '':
  fs=f
 if 1:
  f=fs[0]
  fs=fs[1:]
  if   f=='w':
   if lf == 's':
    q+=1
   else:
    q-=1
    lf=f
   q%=term()[1]*2-10
  elif f=='a':
   if lf == 'd':
    a+=1
   else:
    a-=1
    lf=f
   a%=term()[0]
  elif f=='s':
   if  lf == 'w':
    q-=1
   else:
    q+=1
    lf=f
   q%=term()[1]*2-10
  elif f=='d':
   if lf == 'a':
    a-=1
   else:
    a+=1
    lf=f
   a%=term()[0]
  elif f=='p':
   print('\x1b[0m',)
   print('\x1b[0;0H'+' '*term()[0]*(term()[1]-2),)
   print('\x1b[0;0H',end='')
   exit()
 if [a,q] in sn:
  sn=sn[sn.index([a,q])+1:]
  ma=max(ma,len(sn)+bdi)
  #aver=(aver*llen+len(sn))/(llen+1)
  llen+=1
 if ea==a and eq==q:
  bdc+=1
  eq=random.randint(0,term()[1]*2-11)
  ea=random.randint(0,term()[0]-1)
  sn=sn[:]+[[a,q]]
  ma=max(ma,len(sn)+bdi)
  #aver=(aver*llen+len(sn))/(llen+1)
  llen+=1
 elif [a,q] in bd:
  bdi=15*bdl//bdw
  bdm=10*bdl//bdw+1
  bd=[]
  bdc=0
  bdl=0
  bdi-=1
  sn=sn[:]+[[a,q]]
  ma=max(ma,len(sn)+bdi)
  #aver=(aver*llen+len(sn))/(llen+1)
  llen+=1
 elif bdi:
  bdi-=1
  sn=sn[:]+[[a,q]]
  ma=max(ma,len(sn)+bdi)
  #aver=(aver*llen+len(sn))/(llen+1)
  llen+=1
 else:
  sn=sn[1:]+[[a,q]]
=======
 fd = sys.stdin.fileno()
 old_settings = termios.tcgetattr(fd)
 try:
  tty.setraw(sys.stdin.fileno())
  ch = sys.stdin.read(1)
 finally:
  termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
 k=ch
 a=open('char','a')
 a.write(k)
 a.close()
 if k == 'p':
  time.sleep(0.1)
  exit()
>>>>>>> 8a373fb9dab8909d19894396a27012c4bd745158
