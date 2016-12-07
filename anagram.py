def anagram (word1,word2):
    word1=sorted(word1)
    word2=sorted(word2)
    if word1 == word2:
        print "This is an anagram", word1 , word2
    else:
        print "This is not an anagram", word1 , word2

anagram("cat","home")
