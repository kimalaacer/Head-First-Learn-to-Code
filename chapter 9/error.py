# error handling
try:
	filename='notthere.txt'
	file=open(filename,'r')
except:
	print('Sorry, an error occured opening', filename)
else:
	print('Glad we got that file open')
	file.close()
# notthere.txt does not exist, but lib.txt exist.
try:
	filename='lib.txt'
	file=open(filename,'r')
except:
	print('Sorry, an error occured opening', filename)
else:
	print('Glad we got that file open')
	file.close()
