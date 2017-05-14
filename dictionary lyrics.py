# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 20:27:34 2016

@author: mathias
"""

def lyrics_to_frequencies(lyrics):
    myDict = {}
    """
    breaking checking if a word already appears in the dictionary if not start counting, if not start adding it
    """
    
    for word in lyrics:
        if word in myDict:
            myDict[word] +=1
        else:
            myDict[word] = 1
    return myDict
    

she_loves_you = ("She loves you, yeah, yeah, yeah She loves you, yeah, yeah, yeah She loves you, yeah, yeah, yeah You think you've lost your love Well, I saw her yesterday-yi-yay It's you she's thinking of And she told me what to say-yi-yay She says she loves you and you know that can't be bad Yes, she loves you and you know you should be glad She said you hurt her so She almost lost her mind And now she says she knows You're not the hurting kind She says she loves you and you know that can't be bad Yes, she loves you and you know you should be glad Oo, she loves you, yeah, yeah, yeah She loves you, yeah, yeah, yeah With a love like that You know you should be glad You know it's up to you I think it's only fair Pride can hurt you too Apologize to her Because she loves you and you know that can't be bad Yes, she loves you and you know you should be glad Oo, she loves you, yeah, yeah, yeah She loves you, yeah, yeah, yeah With a love like that You know you should be glad With a love like that you know you should be glad With a love like that you know you should be glad Yeah, yeah, yeah, Yeah, yeah, yeah, yeah").split(" ")


beatles = lyrics_to_frequencies(she_loves_you)


def most_common_word(freq):
    values = freq.values() #take the frequency values from the individual words and save them
    best = max(values) #check the maximum value of the dictionary
    word = []
    
    for k in freq:
        if freq[k] == best: #for each word in the dict, check if the frequency value is the same as the max value
            word.append(k) #create new list of most common words
            
    return (word, best)
    
    
def words_often(freqs, minTimes):
    results = []
    
    done = False
    
    while not done:
        temp = most_common_word(freqs) #find most common words in the dictionary (see above)
        if temp[1] >= minTimes: #if words occures more often then the min amount of times that I set do,
            results.append(temp) #add this word as result
            for w in temp[0]: #once done remove every further times it occures
                del(freqs[w])
        else:
            done = True
    return results   
       
print(words_often(beatles, 5))