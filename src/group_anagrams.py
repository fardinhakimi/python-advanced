
def is_anagram(x, y):
    anagram = ''.join([c for c in x if c in y])
    return len(anagram) == len(x) and len(anagram) == len(y)


def group_anagrams(words):
    anagram_list = []
    already_matched = []

    for i in words:
        anagram_sub_list = []

        for j in words:
            if j not in already_matched:
                if is_anagram(i, j):
                    anagram_sub_list.append(j)
                    already_matched.append(j)
        if anagram_sub_list:
            anagram_list.append(anagram_sub_list)

    return anagram_list


if __name__ == '__main__':

    words = ['cinema', 'a', 'flop', 'iceman', 'maecyne','lofp','olfp']

    anagrams = {}

    for word in words:
        sorted_word = ''.join(sorted(word))

        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    print(list(anagrams.values()))

