def wordcount(textfile):
    file1 = open(textfile)  # Put your code here.
    num_words = {}

    for x in file1:  # x = each line
        indiv_word = x.rstrip().split()

        for word in indiv_word:  # for each word
            word = word.rstrip('.,?').lower()
            num_words[word] = num_words.get(word, 0) + 1
            # if word in num_words:
            #     num_words[word] += 1
            # else:
            #     num_words[word] = 1
            # write without using .get
            # check if key in dict
            # if so, do something
            # else...
    # print num_words
    return num_words

print wordcount("test.txt")
# print my_val

