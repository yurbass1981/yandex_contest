def longest_word(text):
    words = text.split()

    return max(words, key=len)



rezult = longest_word(input())
print(rezult) 
# rezult = longest_word('The Tower of Londonn was built in the 15th century')

