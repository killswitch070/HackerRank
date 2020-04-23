_=input()                               # not required
a=set(map(int,input().split()))         # creation of english set
_=input()                               # not required
b=set(map(int,input().split()))         # creation of French set
print(len(a.symmetric_difference(b)))   #length of symmetric diff b/w a & b
