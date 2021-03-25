#!/usr/bin/env python
# coding: utf-8

# In[196]:


import re


# In[212]:


class Speech_2_text:
    def __init__(self,inp):
        self.inp=inp
    def convert_2_text(self,inp):
        mod=inp
        exist=['one','two','three','four','five','six','seven',' eight','nine','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety','hundred','thousand']
        replace=[1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,1000]
        numerals= {"single":1,"double":2,"triple":3,"quadruple":4,"quintuple":5,"sextuple":6,"septuple":7,"octuple":8,"nonuple":9,"decuple":10}
        ex_gen=['C M','P M','D M','A M']
        rep_gen=['CM','PM','DM','AM']
    #     numerical replacements
        for i,j in zip(exist,replace):
            mod=re.sub(i,str(j),mod)
        word=mod.split()
        for i in range(len(word)):
            if i!=0:
                if word[i]=='dollar' or word[i]=='dollars':    #dollar replacement
                    word[i-1]='$'+word[i-1]
                    word[i]=''
            if word[i] in numerals.keys() and i!=len(word):     #numeral replacement
                tmp=numerals[word[i]]
                if len(word[i+1])<=2:
                    word[i]=''
                    word[i+1]=re.sub('[,.!]','',word[i+1])
                    word[i+1]=tmp*word[i+1]
                i+=1
            else:
                pass
        mod=' '.join(word)
        for i,j in zip(ex_gen,rep_gen):                        #general words replacement
            mod=re.sub(i,j,mod)
            mod=re.sub(' +',' ',mod)                           #extra blank space replacement
        return mod    
def convert():
	inp=input('Enter the text you want to convert')
	speech_obj=Speech_2_text(inp)
	print('Converting')
	print(speech_obj.convert_2_text(inp))


# In[ ]:




