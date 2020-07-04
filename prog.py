import os
#Write your code here

s = os.getcwd()
s1 = "New Folder"
s2 = "New Folder2"
path = os.path.join(s,s1)
path2 = os.path.join(s,s2)
os.mkdir(path)
os.chdir(path)
q = os.getcwd()
os.chdir("..")
w1 = os.getcwd()
os.rename(s1,s2)
os.chdir(path2)
p = os.getcwd()
os.chdir("..")
os.rmdir(path2)
w = os.getcwd()

with open('.hidden.txt','w') as outfile:
     outfile.write(s)
with open('.hidden1.txt', 'w') as outfile:
     outfile.write(q)
with open('.hidden2.txt', 'w') as outfile:
     outfile.write(p)
with open('.hidden3.txt', 'w') as outfile:
     outfile.write(w)


