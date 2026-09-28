#anagram mrans two nubmer oor string should be of same length contain same charter in same frequencies

def is_anagram(s1,s2):

    if len(s1) != len(s2):
       return False
    count =0
    freq = {}
    

    for ch in s1:
        if ch in freq:
            freq1[ch] +=1
        else:
            freq1[ch] =1
         

    for ch in s2:
            if ch in freq2:
                freq2[ch] +=1
            else:
                freq2[ch] =1

    if ( freq1 == freq2):
         return True
    
    return False
print(is_anagram("abc", "ab"))