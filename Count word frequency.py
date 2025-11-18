filename = 'article.txt'

# Q: Why use a dictionary to store word counts?


def countWords(filename):
    d = {}
    file = open(filename, 'r')

    for line in file:
        words = line.strip().split()
        for word in words:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
    return d


d = countWords(filename)
print(d)
