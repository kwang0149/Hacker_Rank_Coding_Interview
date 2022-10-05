# Enter your code here. Read input from STDIN. Print output to STDOUT
# input ('tipe something')
import re
while True:
    try:
        # operation combine
        none_formatted_words=input().rstrip()
        operation,tipe,word=none_formatted_words.split(';')
        # combine operation
        if operation=='C':
            # method
            list_word=word.split(' ')
            if tipe=='M':
                for i in range(len(list_word)):
                    if i>0:
                        list_word[i]=list_word[i].capitalize()
                valid_class_name=''.join(list_word)+'()'
                print (valid_class_name)
            # class
            elif tipe=='C':
                for i in range(len(list_word)):
                    list_word[i]=list_word[i].capitalize()
                valid_class_name=''.join(list_word)
                print (valid_class_name)
            # variable
            elif tipe=='V':
                for i in range(len(list_word)):
                    for i in range(len(list_word)):
                        if i>0:
                            list_word[i]=list_word[i].capitalize()
                valid_class_name=''.join(list_word)
                print (valid_class_name)
        # split operation
        elif operation=='S':
            # method
            if tipe=='M':
                kata=re.split('(?=[A-Z])', word)
                kata[len(kata)-1]=kata[len(kata)-1][:-2]
                for i in range(0,len(kata)):
                    kata[i]=kata[i].lower()
                print (' '.join(kata))
            # class
            elif tipe=='C':
                kata= re.findall('[A-Z][^A-Z]*',word)
                for i in range(0,len(kata)):
                    kata[i]=kata[i].lower()
                print (' '.join(kata))
            # variable
            elif tipe=='V':
                kata=re.split('(?=[A-Z])', word)
                for i in range(0,len(kata)):
                    kata[i]=kata[i].lower()
                print (' '.join(kata))
    except EOFError:
        break