# result = [i for i in range(10) if i%2==0]
# print(result)

# word_1 = ["A","B","C"]
# word_2 = ["D","E","A"]
#
# result = [i+j for i in word_1 for j in word_2 if (i!=j)]
# result.sort()
#
# print(result)

word_1 = 'Someday at ChristMas'.split()
stuff = [[w.upper(), w.lower(), len(w)] for w in word_1]

for i in stuff:
    print(i)
