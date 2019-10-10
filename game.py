ls=0
while 1:
 nls=int(os.popen('ls -l key.a').read().split()[4])
 z=open('key.a')
 z.read(ls)
 fs+=z.read(nls-ls)
 z.close()
 ls=nls

