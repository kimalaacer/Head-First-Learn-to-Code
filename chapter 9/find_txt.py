# check for only 1 text that has a word "needle" in it and then stops scanning.
# for multiple texts, remove break.

for i in range(0,1000):
    filename=str(i)+'.txt'
    file=open(filename, r)
    text=file.read()
    if needle in text:
        print('Found needle in file '+str(i)+'.txt')
        break
    file.close()
print('Scan complete')
