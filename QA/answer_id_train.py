import numpy as np;
from numpy import *
glove_matrix  = np.load("glove.npy")
vocab = np.fromfile("vocab.dat",dtype=float)
context_file = open("train.ids.context");
context_string = context_file.read();
contexts = context_string.split("\n")
print(size(contexts),contexts[size(contexts)-1])
for i in range(size(contexts)-1):
    st = contexts[i].split(" ");
    contexts[i] = list(map(int, st))
    
answer_file = open("train.span");
answer_string = answer_file.read();
answers = answer_string.split("\n")
print(size(answers),answers[81402])
for i in range(size(answers)-1):
    ans = answers[i].split(" ");
    ans1 = list(map(int, ans))
    if ans1[0] > ans1[1]:
        t=ans1[0]
        ans1[0]=ans1[1]
        ans1[1]=t
    answers[i] = contexts[i][ans1[0]:ans1[1]+1]

#np.savetxt("train.ids.answer",np.array(answers),fmt='%s', delimiter=' ',newline="\n")
thefile=open("train.ids.answer","w")
for item in answers:
    thefile.write("%s\n" % ' '.join(map(str,item)))
thefile.close()

print(answers[81402],answers[81401],answers[81400])
answer_file1 = open("train.ids.answer");
answer_string1 = answer_file1.read();
answers2 = answer_string1.split("\n")
for i in range(size(answers2)-2):
    st = answers2[i].split(" ");
    answers2[i] = list(map(int, st))
print(answers2[0],answers2[1],answers2[81402],answers2[81403])
