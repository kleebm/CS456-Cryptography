#!/usr/bin/env python
# coding: utf-8

# # CS456 Cryptography
# ## Bryan Klee
# ### Student Id:0624280
# 
# Collaborated with Tyler Pawlaczyk

# In[1]:

#import numpy
#import matplotlib.pyplot as plt
from collections import Counter, OrderedDict

print("Assignment 1", __name__)

# In[2]:

def main():

    encrypted_message= """UERFHWAQAQWGUZXNSUMUZPYWUZNQDN
QZXYUMSNSQZRFHSWTQVFAAQVNYRGQV
ARPNQGNSQEUAMNSFIQLFABEFAFHAVA
RPNFXAWPSRVFHAMQEFANSUMEWYYNLQ
ZNRZUZQNQQZMQIQMNQAPYQWMQMHCIU
NNSQEFYYFLUZXUNQIMEFANSUMSFIQL
FABCRQIWUYEUAMNMQZGNSQMHCMNUNH
NUFZNWCYQEFANSQVUPSQAHMQGNFQZV
ARPNNSUMSFIQLFABMQVFZGUIPYQIQZ
NRFHAFLZVUPSQACWMQGFZVYWMMUVWY
UGQWMNSWNWAQBZFLZUZNSQYUNQAWNH
AQUNMSFHYGCQUIPYQIQZNQGUZWPAFX
AWIIUZXYWZXHWXQFERFHAVSFUVQWAA
WZXQEFAWZFZYUZQGQIFZMNAWNUFZFE
RFHAMRMNQINSUAGLAUNQWMIWYYAQPF
ANFZNSQMNWNUMNUVWYYQNNQAEAQKHQ
ZVUQMFEQZXYUMSWZGWNYQWMNFZQIFA
QZWNHAWYYWZXHWXQWZGGQNQAIUZQLS
UVSSWMIFAQQZNAFPRNSUMSFIQLFABU
MGHQCQEFAQNSQAQWGUZXCAQWB""".replace("\n","")

    print(encrypted_message)

# In[3]:


    character_frequency = Counter(encrypted_message)


# In[4]:


    print(character_frequency)


# In[5]:


    #plt.bar(character_frequency.keys(), character_frequency.values())


# In[6]:


    sorted_char_freq = sorted(character_frequency.items(), key=lambda kv: kv[1], reverse=True)


# In[7]:


    print(sorted_char_freq)


# In[8]:


    encrypt_key = []
    for key in sorted_char_freq:
        encrypt_key.append(key[0])


# In[9]:


    alpha_frequency = ["E" ,"T" ,"A" ,"O" ,"I" ,"N" ,"S" ,"R" ,"H" ,"D" ,"L" ,"C","U" 
                   ,"M", "F" , "Y","W","G","P","B","V","K","X","Q","J","Z"]


# In[10]:


    print(encrypt_key)


# In[11]:

    keys=encrypt_key
    values=alpha_frequency
    cypher=dict(zip(keys,values))
    print(cypher)


# In[12]:





# In[13]:


    decrypt(encrypt_key, alpha_frequency,encrypted_message)


# In[14]:


    alpha_frequency[11]='U'
    alpha_frequency[12]='C'
    decrypt(encrypt_key, alpha_frequency,encrypted_message)


# In[15]:


    alpha_frequency[2]='R'
    alpha_frequency[7]='A'
    print(alpha_frequency)
    decrypt(encrypt_key, alpha_frequency,encrypted_message)


# In[16]:


    alpha_frequency[6]='A'
    alpha_frequency[7]='S'
    decrypt(encrypt_key, alpha_frequency,encrypted_message)


# In[17]:


    alpha_frequency[9]='C'
    alpha_frequency[12]='D'
    print(alpha_frequency)
    decrypt(encrypt_key, alpha_frequency,encrypted_message)


# In[18]:


    alpha_frequency[16]='G'
    alpha_frequency[17]='W'
    print(alpha_frequency)
    decrypt(encrypt_key, alpha_frequency,encrypted_message)


# In[19]:


    alpha_frequency[17]='P'
    alpha_frequency[18]='W'
    print(alpha_frequency)
    decrypt(encrypt_key, alpha_frequency,encrypted_message)


# In[20]:


    alpha_frequency[9]='L'
    alpha_frequency[10]='C'
    print(alpha_frequency)
    decrypt(encrypt_key, alpha_frequency,encrypted_message)


# In[21]:


    alpha_frequency[21]='X'
    alpha_frequency[22]='K'
    print(alpha_frequency)
    decrypt(encrypt_key, alpha_frequency,encrypted_message)


# In[22]:


    alpha_frequency[20]='K'
    alpha_frequency[22]='V'
    print(alpha_frequency)
    decrypt(encrypt_key, alpha_frequency,encrypted_message)


# In[23]:


    alpha_frequency[10]='M'
    alpha_frequency[13]='C'
    print(alpha_frequency)
    decrypt(encrypt_key, alpha_frequency,encrypted_message)
    print("\n")


# In[34]:


#final substitution table
#decrypt()
#print(encrypt_key)
#print(alpha_frequency)
    print("Final Substitution Table: (encrypted letter:Original letter) ")
    print(cypher, "\n")


# IF YOU ARE READING THIS IN PLAIN TEXT ENGLISH THEN YOU HAVE CORRECTLY DECRYPTED THE FIRST HOMEWORK FOR OUR CRYPTOGRAPHY COURSE FOR THIS FALL TWENTY NINETEEN SEMESTER PLEASE SUBMIT THE FOLLOWING ITEMS FOR THIS HOMEWORK BY EMAIL 
# FIRST SEND THE SUBSTITUTION TABLE FOR THE CIPHER USED TO ENCRYPT THIS HOMEWORK 
# SECOND IMPLEMENT YOUR OWN CIPHER BASED ON CLASSICAL IDEAS THAT ARE KNOWN IN THE LITERATURE IT SHOULD BE IMPLEMENTED IN A PROGRAMMING LANGUAGE OF YOUR CHOICE ARRANGE FOR AN ONLINE DEMONSTRATION OF YOUR SYSTEM 
# THIRD WRITE A SMALL REPORT ON THE STATISTICAL LETTER FREQUENCIES OF ENGLISH AND AT LEAST ONE MORE NATURAL LANGUAGE AND DETERMINE WHICH HAS MORE ENTROPY 
# THIS HOMEWORK IS DUE BEFORE THE READING BREAK


# In[32]:

    print("My own cipher is a ceaser shift with an incrementing shift of 1, \n until it reaches 26 then resets to 1 ")
    encrypted = varCeaserCiph("the quick brown fox jumped over the lazy dog")
    decryptCeaser(encrypted)
    print("\n")
    
    newMessage = """IFYOUAREREADINGTHISINPLAINTEXTENGLISHTHENYOUHAVECORRECTLYDECRYPTEDTHE
FIRSTHOMEWORKFOROURCRYPTOGRAPHYCOURSEFORTHISFALLTWENTYNINETEENSEMESTERPLEASESUBMITTHE
FOLLOWINGITEMSFORTHISHOMEWORKBYEMAILFIRSTSENDTHESUBSTITUTIONTABLEFORTHECIPHERUSEDTO
ENCRYPTTHISHOMEWORKSECONDIMPLEMENTYOUROWNCIPHERBASEDONCLASSICALIDEASTHATAREKNOWNINTHE
LITERATUREITSHOULDBEIMPLEMENTEDINAPROGRAMMINGLANGUAGEOFYOURCHOICEARRANGEFORANONLINE
DEMONSTRATIONOFYOURSYSTEMTHIRDWRITEASMALLREPORTONTHESTATISTICALLETTERFREQUENCIESOFENGLISH
ANDATLEASTONEMORENATURALLANGUAGEANDDETERMINEWHICHHASMOREENTROPYTHISHOMEWORKISDUEBEFORETHE
READINGBREAK""".replace("\n", "")
    newMessage = newMessage.lower()
    #print(newMessage)
    newMessage = varCeaserCiph(newMessage)
    decryptCeaser(newMessage)
    
    

# In[ ]:

def decrypt(enc_key, alp_freq, enc_mess):
    keys=enc_key
    values=alp_freq
    cypher=dict(zip(keys,values))
    
    output2 = ""
    for char in enc_mess:
        output2 = output2 + cypher[char]

    print(output2)

#Ceaser shift with incrementing shifts, resetting after 26 letters
def varCeaserCiph(message):
    encryptedMessage = ""
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    counter = 1
    messaage = message.lower()
    for char in message:
        try:
            index = alpha.index(char)
            sub = alpha[(index + counter) % 26]
            encryptedMessage = encryptedMessage + sub
            #print(char)
            #print(sub)
            #print(counter)
            counter += 1
            if counter == 27:
                counter = 1
                
        except:
            encryptedMessage = encryptedMessage + " "
            
    print(encryptedMessage, "\n")
    return encryptedMessage


#Decrypts my ceaser shift function
def decryptCeaser(message):
    decryptMessage = ""
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    counter = 1
    for char in message:
        try:
            index = alpha.index(char)
            decryptMessage = decryptMessage + alpha[(index - counter) % 26]
            counter += 1
            if counter ==27:
                counter = 1
                
        except:
            decryptMessage = decryptMessage + " "
            
    print(decryptMessage, "\n")


if __name__ == '__main__':
    main()
