if __name__ == '__main__':

	from urllib.parse import quote
	import time,sys,tty,termios,os,sys
	from urllib.request import urlopen
	p=os.path.abspath(sys.argv[0])
	p=p[:-p[::-1].index('/')]
	os.system('python3 '+p+'gs.py '+sys.argv[1]+' &')
	while 1:
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		k=ch
		k=quote(k)
		urlopen('http://127.0.0.1:12843/'+k).read()
	#	a=open('char','a')
	#	a.write(k)
	#	a.close()
		if k == 'p':
			time.sleep(0.1)
			exit()
