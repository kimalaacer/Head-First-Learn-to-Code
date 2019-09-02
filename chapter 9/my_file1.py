my_file=open('lib.txt','r')
while True:
	line=my_file.readline()
	if line !='':
		print(line)
	else:
		break
my_file.close()
# or a more readable form, we can use for to iterate on each line:
my_file=open('lib.txt','r')
for line in my_file:
    print(line)
my_file.close()
