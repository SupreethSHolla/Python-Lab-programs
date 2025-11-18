# Q: Why is a dictionary used here?
def characterCount(sentence):
    c = {}
    for w in sentence:
        if w in c:
            c[w] += 1
        else:
            c[w] = 1
    return c


s = "Programming is an Art"
print(characterCount(s))
