# for i,v in enumerate(['tic','tac','toe']):
#     print(i,v)

# mylist = ["a","b","c","d",]
# print(list(enumerate(mylist)))

# mylist = {i:j for i,j in enumerate('Im live in seoul and this is my homeplace'.split())}

# for i in mylist:
#     print({i: mylist[i]})

alist = ['nam','chang','hyun']
blist = ['one','two','three']

for i,(a,b) in enumerate(zip(alist,blist)):
    print(i, a,b)