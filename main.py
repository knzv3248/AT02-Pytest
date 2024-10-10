
def count_vowels(check_string):
    # список гласных букв: [A, E, I, O, U, А, Е, Ё, И, О, У, Ы, Э, Ю, Я]
    vowels_list = ["A", "E", "I", "O", "U",
                   "А", "Е", "Ё", "И", "О", "У", "Ы", "Э", "Ю", "Я"
                   ]

    s = check_string.upper()
    count = 0
    for i in s:
        if i in vowels_list:
            count += 1
    return count

print(count_vowels("hello, world$#"))
