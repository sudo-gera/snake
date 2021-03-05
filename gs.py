import os,time,random,sys
delay=float(sys.argv[1])
#term=os.get_terminal_size
get_terminal_size_cache=[]
get_terminal_size_counter=0
def term():
	global get_terminal_size_cache,get_terminal_size_counter
	if get_terminal_size_counter==0:
		get_terminal_size_cache=list(os.get_terminal_size())
		get_terminal_size_counter=32
	get_terminal_size_counter-=1
	return get_terminal_size_cache[:]
os.system('>char')
print('\n'*(term()[1]-2),)
ls=0
q=5
a=5
direction='d'
lf='d'
snake_dots=[[5,w] for w in range(5,30)][::-1]
small_food_y=random.randint(0,term()[1]*2-11)
small_food_x=random.randint(0,term()[0]-1)
bd=[]
bdc=0
bdi=0
bdl=0
bdm=5
bdw=200
fs=''
snake_len_max=len(snake_dots)
ons=[]
spc=0
lpl=[]
loul=''
while 1:
	time.sleep(1/delay)
	print('\x1b[H',end='')
	ns=snake_dots[:]
	ns+=[[small_food_x,small_food_y]]
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
	print('\x1b[35m',)
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
# print('\x1b['+str(term()[1]-2)+';0H'+'now:',len(snake_dots),'max:',snake_len_max,'aver:',averwnd='')
	if lpl!=[len(snake_dots),snake_len_max] or oue!=oub:
		print('\x1b['+str(term()[1]-2)+';0H'+'now:',len(snake_dots),'max:',snake_len_max,)
		lpl=[len(snake_dots),snake_len_max]
	if spc==0:
		print('\x1b['+str(term()[1]-4)+';0H'+'═'*term()[0],)
		spc=128
	print('\x1b[0;0H',end='')
	spc-=1
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
	#nls=int(os.popen('ls -l char').read().split()[4])
	nls=os.path.getsize('char')
	char=open('char','rb')
	char.read(ls)
	nfs=char.read(nls-ls)
	fs+=nfs.decode()
	char.close()
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
		fs=direction
	if 1:
		direction=fs[0]
		fs=fs[1:]
		if   direction=='w':
			if lf == 's':
				q+=1
			else:
				q-=1
				lf=direction
			q%=term()[1]*2-10
		elif direction=='a':
			if lf == 'd':
				a+=1
			else:
				a-=1
				lf=direction
			a%=term()[0]
		elif direction=='s':
			if  lf == 'w':
				q-=1
			else:
				q+=1
				lf=direction
			q%=term()[1]*2-10
		elif direction=='d':
			if lf == 'a':
				a-=1
			else:
				a+=1
				lf=direction
			a%=term()[0]
		elif direction=='p':
			print('\x1b[0m',)
			print('\x1b[0;0H'+' '*term()[0]*(term()[1]-2),)
			print('\x1b[0;0H',end='')
			exit()
	if [a,q] in snake_dots:
		snake_dots=snake_dots[snake_dots.index([a,q])+1:]
		snake_len_max=max(snake_len_max,len(snake_dots)+bdi)
	if small_food_x==a and small_food_y==q:
		bdc+=1
		small_food_y=random.randint(0,term()[1]*2-11)
		small_food_x=random.randint(0,term()[0]-1)
		snake_dots=snake_dots[:]+[[a,q]]
		snake_len_max=max(snake_len_max,len(snake_dots)+bdi)
	elif [a,q] in bd:
		bdi=15*bdl//bdw
		bdm=10*bdl//bdw+1
		bd=[]
		bdc=0
		bdl=0
		bdi-=1
		snake_dots=snake_dots[:]+[[a,q]]
		snake_len_max=max(snake_len_max,len(snake_dots)+bdi)
	elif bdi:
		bdi-=1
		snake_dots=snake_dots[:]+[[a,q]]
		snake_len_max=max(snake_len_max,len(snake_dots)+bdi)
	else:
		snake_dots=snake_dots[1:]+[[a,q]]
