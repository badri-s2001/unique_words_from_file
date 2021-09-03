import os

if os.stat("abc.txt").st_size == 0:
    print("Input text file is empty")

else:
    with open('abc.txt', 'r') as f:
        f_contents = f.read()
        list_words = f_contents.split()

        dict_words = {}

        for word in list_words:
            if not dict_words.get(word):
                dict_words[word] = len(word)

        sort_dict = dict(sorted(dict_words.items(), key=lambda kv: kv[1]))

        with open("output.txt", mode="w") as output:

            for key in sort_dict:
                output.write(f"{key} {sort_dict[key]}\n")

            output.close()

        f.close()
