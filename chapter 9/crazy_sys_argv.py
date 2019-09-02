# this code is for a game crazy lib
import sys



def make_crazy_lib(filename):
    try:
        file=open(filename, 'r')
        text=''
        for line in file:
            text=text+process_line(line)
        file.close()

        return text

    except FileNotFoundError:
        print("Sorry, Couldn't find:", filename + '.')
    except IsADirectoryError:
        print("Sorry", filename, 'is a directory.')
    except:
        print('Sorry, could not read', filename) # value None will get returned



# a simple solution is to add 'Noun,' to placeholders. it does not encompass all the punctuations but it is fast.
# placeholders=['NOUN','ADJECTIVE','VERB_ING', 'VERB', 'NOUN,']
# I tested it and it worked.

placeholders=['NOUN','ADJECTIVE','VERB_ING', 'VERB']
def process_line(line):
    global placeholders
    processed_line=''

    words=line.split()

    for word in words:
        stripped=word.strip('.,;?!') # this will strip all punctuations
        if stripped in placeholders:
            answer = input('Enter a '+ stripped + ":")
            processed_line=processed_line + answer
            if word[-1] in '.,;?!':
                processed_line=processed_line +word[-1] +' ' # this code is to put the punctuation back at the end of the word
            else:
                processed_line=processed_line + ' '
        else:
            processed_line=processed_line + word + ' '

    return processed_line+ '\n'
def save_crazy_lib(filename,text):
    file=open(filename, 'w')
    file.write(text)
    file.close()

def main():
    if len(sys.argv) !=2:
        print("crazy_sys_argv.py need to be followed by the text you need to run. i.e: crazy_sys_argv.py lib.txt")
    else:
        filename=sys.argv[1]
        lib=make_crazy_lib(filename)
        if (lib!= None):
            save_crazy_lib('crazy_'+filename, lib)
if __name__=='__main__':
    main()
