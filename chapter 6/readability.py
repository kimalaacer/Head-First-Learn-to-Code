# this code is to check the readability of ch1 text

#f=open('ch6.txt','r')
#contents=f.read()
#print(contents)
import ch1_text
def count_syllables(words):
    count =0
    for word in words:
        word_count=count_syllables_in_word(word)
        count=count+word_count
    return count
def count_syllables_in_word(word):
    count=0
    endings='.,;!?:'
    last_char=word[-1]
    if last_char in endings:
        processed_word=word[0:-1]
    else:
        processed_word=word

    if len(processed_word)<=3:
        return 1

    if processed_word[-1] in 'eE':
        processed_word=processed_word[0:-1]

    vowels='aeiouAEIOU'
    prev_char_was_vowel=False
    for char in processed_word:
        if char in vowels:
            if not prev_char_was_vowel:
                count=count+1
            prev_char_was_vowel=True
        else:
            prev_char_was_vowel=False

    if processed_word[-1] in 'yY':
        count=count+1

    return count

def count_sentences(text):
    count=0
    # for char in text:
        # if char== '.' or char=='?' or char=='!' or char== ';' or char== ':':
            # count=count+1
        # else:
            # count=count
    # return(count)
    terminals='.;?!'
    for char in text:
        if char in terminals:
            count=count+1
    return count


count_sentences(ch1_text.text)

def output_results(score):
    if score>=90:
        print('Reading level of 5th grade. Easily understood by an average 11-year-old student.')
    elif score>=80:
        print('Reading level of 6th grade. Conversational English for consumers.')
    elif score>=70:
        print('Reading level of 7th grade.')
    elif score>=60:
        print('Reading level of 8th & 9th grade. Plain English. Easily understood by 13- to 15-year-old students.')
    elif score>=50:
        print('Reading level of 10th to 12th grade. Fairly difficult to read.')
    elif score>=30:
        print('Reading level of	College. Difficult to read.')
    else:
        print('Reading level of College graduate. Very difficult to read. Best understood by university graduates.')

def readability(text):
    total_words=0
    total_sentences=0
    total_syllables=0
    score=0
    words=text.split()
    total_words=len(words)
    total_sentences=count_sentences(text)
    total_syllables=count_syllables(words)

    score=(206.835 - 1.015*(total_words/total_sentences) - 84.6 * (total_syllables/total_words) )

    print(total_words, 'words')
    print(total_sentences, 'sentences')
    print(total_syllables, 'syllables')
    print(score,'reading ease score')
    output_results(score)

readability(ch1_text.text)
