def word_count(sentence) :
    words = sentence.split()

    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

sentence = input("Enter your sentence : ") 
result = word_count(sentence) 

print(result)


