def findingA(sentence):
    w = sentence
    output = lambda w: w[w.find('a'):]
    return(output)

s = input()
final = findingA(s)
print(final)
# print((lambda w: w[w.find('a'):])(input()))