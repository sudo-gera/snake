import os,time,random,sys
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from urllib.parse import unquote
from urllib.request import urlopen as u
from urllib.request import urlopen
from multiprocessing import Process
from urllib.parse import quote
import time,sys,tty,termios,os,sys
from urllib.request import urlopen
from subprocess import run

cache=''

class MyServer(BaseHTTPRequestHandler):
	# def do_GET(self):
	# 	path=self.path
	# 	if path[0]=='/':
	# 		path=path[1:]
	# 	global cache
	# 	cache+=path
	# 	self.send_response(200)
	# 	self.send_header("Content-type", "text/html; charset=utf-8")
	# 	self.end_headers()
	# 	self.wfile.write(cache.encode())

	# def do_POST(self):
	# 	path=self.path
	# 	if path[0]=='/':
	# 		path=path[1:]
	# 	global cache
	# 	cache+=path
	# 	self.send_response(200)
	# 	self.send_header("Content-type", "text/html; charset=utf-8")
	# 	self.end_headers()
	# 	self.wfile.write(cache.encode())

	def log_message(*a):
			pass

def runserver():
	hostName = '127.0.0.1'
	hostPort = random.randint(12800,12899)
	while 1:
		try:
			myServer = HTTPServer((hostName, hostPort), MyServer)
			break
		except Exception:
			hostPort+=1
	print(hostPort)

	from pathlib import Path
	home=str(Path.home())+'/'
	open(home+'.snake_port','w').write(f'{hostPort} {time.time()}')

	try:
	    myServer.serve_forever()
	except KeyboardInterrupt:
	    pass
	myServer.server_close()

if __name__ == '__main__':
	s_time=time.time()

	rsp=Process(target=runserver)
	rsp.start()

	from pathlib import Path
	home=str(Path.home())+'/'
	while 1:
		time.sleep(0.1)
		try:
			port,p_time=[float(w) for w in open(home+'.snake_port').read().split()]
		except Exception:
			port=None
			p_time=0
		if p_time>s_time:
			break
	port=int(port)
	print(port)

	p=os.path.abspath(sys.argv[0])
	p=p[:-p[::-1].index('/')]

	if len(sys.argv)<2:
		sys.argv.append('12')
	# os.system('python3 '+p+'gs.py '+sys.argv[1]+' '+str(port)+' &')
	while 1:
		k=input()
		# fd = sys.stdin.fileno()
		# old_settings = termios.tcgetattr(fd)
		# try:
		# 	tty.setraw(sys.stdin.fileno())
		# 	ch = sys.stdin.read(1)
		# finally:
		# 	termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		# k=ch
		# k=quote(k)
		# exec(open(home+'c/h.py').read())
		# urlopen(f'http://127.0.0.1:{port}/'+k).read()
	#	a=open('char','a')
	#	a.write(k)
	#	a.close()
		if k == 'p':
			time.sleep(0.1)
			rsp.kill()
			exit()
