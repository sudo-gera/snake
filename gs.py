import os,time,random,sys
delay=float(sys.argv[1])
class point:
	def __init__(s,dot):
		s.x,s.y=dot
	def __eq__(s,o):
		return [s.x,s.y]==[o.x,o.y]
	def __str__(s):
		return f'point({s.x},{s.y})'
	__repr__=__str__
	def __hash__(s):
		return hash((s.x,s.y))
	def __iter__(s):
		return [s.x,s.y].__iter__()
get_terminal_size_cache=[]
get_terminal_size_counter=0
def term():
	global get_terminal_size_cache,get_terminal_size_counter
	if get_terminal_size_counter==0:
		get_terminal_size_cache=list(os.get_terminal_size())
		get_terminal_size_counter=32
	get_terminal_size_counter-=1
	return get_terminal_size_cache[:]
def get_land_size():
	land_size=term()
	land_size[1]*2-10
	land_size=point(land_size)
	return land_size
dots=set()
def move_cursor(dot):
	print(end='\x1b['+str(dot.y//2)+';'+str(dot.x)+'H')
def put(dot,c):
	if bool(dot in dots)^bool(c):
		move_cursor(point([0,0]))
		print(dots,dot)
		move_cursor(dot)
		pair=dot
		pair.y+=1-pair.y%2*2
		#print(' ▀▄█ ▄▀█'[int(bool(dot.y%2))*4+int(bool(pair in dots))*2+int(bool(c))],end='')
		print('01234567'[int(bool(dot.y%2))*4+int(bool(pair in dots))*2+int(bool(c))],end='\n')
		time.sleep(0.5)
		if c:
			dots.add(point(dot))
		else:
			dots.remove(point(dot))
open('char','w').close()
print('\n'*(term()[1]-2),)
ls=0
head_y=5
head_x=5
direction='d'
last_direction='d'
snake_dots=[[5,w] for w in range(5,30)][::-1]
small_food_y=random.randint(0,term()[1]*2-11)
small_food_x=random.randint(0,term()[0]-1)
big_food_dots=[]
big_food_counter=0
big_food_to_grow_from_eaten_left=0
bdl=0
big_food_counter_max=5
bdw=200
fs=''
snake_len_max=len(snake_dots)
snake_dots_old=[]
spc=0
lpl=[]
loul=''
while 1:
	time.sleep(1/delay)
	print('\x1b[H',end='')
	snake_dots_new=snake_dots[:]
	snake_dots_new+=[[small_food_x,small_food_y]]
	snake_dots_new+=big_food_dots
	snake_dots_to_put=[w for w in snake_dots_new if w not in snake_dots_old]
	snake_dots_to_del=[w for w in snake_dots_old if w not in snake_dots_new]
	print('\x1b[33m',)
	if 0:
		for w in snake_dots_to_put:
			put(point(w),1)
		for w in snake_dots_to_del:
			put(point(w),0)
	else:
		for w in snake_dots_to_put:
			if w[1]%2:
				if [w[0],w[1]-1] in snake_dots_new:
					print('\x1b['+str(w[1]//2+1)+';'+str(w[0]+1)+'H█',)
				else:
					print('\x1b['+str(w[1]//2+1)+';'+str(w[0]+1)+'H▄',)
			else:
				if [w[0],w[1]+1] in snake_dots_new:
					print('\x1b['+str(w[1]//2+1)+';'+str(w[0]+1)+'H█',)
				else:
					print('\x1b['+str(w[1]//2+1)+';'+str(w[0]+1)+'H▀',)
		for w in snake_dots_to_del:
			if w[1]%2:
				if [w[0],w[1]-1] in snake_dots_new:
					print('\x1b['+str(w[1]//2+1)+';'+str(w[0]+1)+'H▀',)
				else:
					print('\x1b['+str(w[1]//2+1)+';'+str(w[0]+1)+'H ',)
			else:
				if [w[0],w[1]+1] in snake_dots_new:
					print('\x1b['+str(w[1]//2+1)+';'+str(w[0]+1)+'H▄',)
				else:
					print('\x1b['+str(w[1]//2+1)+';'+str(w[0]+1)+'H ',)
	snake_dots_old=snake_dots_new[:]
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
	if big_food_counter==big_food_counter_max:
		bdq=random.randint(1,term()[1]*2-12)
		bda=random.randint(1,term()[0]-2)
		big_food_dots+=[[bda-1,bdq-1]]
		big_food_dots+=[[bda+1,bdq-1]]
		big_food_dots+=[[bda-1,bdq+1]]
		big_food_dots+=[[bda+1,bdq+1]]
		big_food_dots+=[[bda+1,bdq]]
		big_food_dots+=[[bda-1,bdq]]
		big_food_dots+=[[bda,bdq+1]]
		big_food_dots+=[[bda,bdq-1]]
		big_food_dots+=[[bda,bdq]]
		big_food_counter=big_food_counter_max+1
		bdl=bdw
	elif big_food_counter==0:
		big_food_dots=[]
	if bdl==0:
		big_food_dots=[]
		big_food_counter=0
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
		fs='head_x'
	fs=''.join([fff for fff in fs if fff in 'asdwp'])
	if fs== '':
		fs=direction
	if 1:
		direction=fs[0]
		fs=fs[1:]
		if   direction=='w':
			if last_direction == 's':
				head_y+=1
			else:
				head_y-=1
				last_direction=direction
			head_y%=term()[1]*2-10
		elif direction=='a':
			if last_direction == 'd':
				head_x+=1
			else:
				head_x-=1
				last_direction=direction
			head_x%=term()[0]
		elif direction=='s':
			if  last_direction == 'w':
				head_y-=1
			else:
				head_y+=1
				last_direction=direction
			head_y%=term()[1]*2-10
		elif direction=='d':
			if last_direction == 'a':
				head_x-=1
			else:
				head_x+=1
				last_direction=direction
			head_x%=term()[0]
		elif direction=='p':
			print('\x1b[0m',)
			print('\x1b[0;0H'+' '*term()[0]*(term()[1]-2),)
			print('\x1b[0;0H',end='')
			exit()
	if [head_x,head_y] in snake_dots:
		snake_dots=snake_dots[snake_dots.index([head_x,head_y])+1:]
		snake_len_max=max(snake_len_max,len(snake_dots)+big_food_to_grow_from_eaten_left)
	if small_food_x==head_x and small_food_y==head_y:
		big_food_counter+=1
		small_food_y=random.randint(0,term()[1]*2-11)
		small_food_x=random.randint(0,term()[0]-1)
		snake_dots=snake_dots[:]+[[head_x,head_y]]
		snake_len_max=max(snake_len_max,len(snake_dots)+big_food_to_grow_from_eaten_left)
	elif [head_x,head_y] in big_food_dots:
		big_food_to_grow_from_eaten_left=15*bdl//bdw
		big_food_counter_max=10*bdl//bdw+1
		big_food_dots=[]
		big_food_counter=0
		bdl=0
		big_food_to_grow_from_eaten_left-=1
		snake_dots=snake_dots[:]+[[head_x,head_y]]
		snake_len_max=max(snake_len_max,len(snake_dots)+big_food_to_grow_from_eaten_left)
	elif big_food_to_grow_from_eaten_left:
		big_food_to_grow_from_eaten_left-=1
		snake_dots=snake_dots[:]+[[head_x,head_y]]
		snake_len_max=max(snake_len_max,len(snake_dots)+big_food_to_grow_from_eaten_left)
	else:
		snake_dots=snake_dots[1:]+[[head_x,head_y]]
