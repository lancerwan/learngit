import sys
import os

def readfile(filename):
	f=open(filename.'r')
	line=f.read()
	print line
def main():
	if len(sys.argv)==2:
	  filename=sys.argv[1]
	  if not os.path.isfile(filename):
	    print '[-]'+filename+' does not exist.'
	    exit(0)
	else:
	  print '[-] Usage: ' + str(sys.argv[0]) + ' <filename>'
	  exit(0)
	print '[+] Reading from : ' + filename
	readfile(filename)
if __name__=='__main__':
	main() 

