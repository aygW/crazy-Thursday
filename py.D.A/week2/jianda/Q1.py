import jieba
from collections import Counter
from wordcloud import WordCloud
#from nltk.corpus import stopwords
import matplotlib.pyplot as plt

with open("D:\week2.txt",'r') as f:
    slist=f.readlines()
for i in range(10):
    print(slist[i])
print()

with open("D:\week2.txt",'r') as f:
    string=f.read()
sepS=list(jieba.cut(string)) #separated-string
Fsepstr=Counter(sepS) #frequency-of-separated-string

sorFsepstr=sorted(Fsepstr.items(),key=lambda x:x[-1],reverse=True) #sorted-frequency-of-separated-string
for i in range(10):
    print(sorFsepstr[i][0],sorFsepstr[i][1])
print()

with open("D:\week2.txt",'r') as f:
    restr=f.read() #reread-string
resepS=list(jieba.cut(restr)) #reseparated-string
#stwords=set(stopwords.words('chinese'))
with open("D:\cn_stopwords.txt",'r') as fstw:
    stwords=fstw.readlines()
filsepS=[word for word in resepS if word.lower() not in stwords] #filtered-separated-string
filFsepstr=Counter(filsepS) #filtered-frequency-of-separated-string
filsorFsepstr=sorted(filFsepstr.items(),key=lambda x:x[-1],reverse=True) #filtered-sorted-frequency-of-separated-string
for i in range(10):
    print(filsorFsepstr[i][0],sorFsepstr[i][1])
print()

fpath = 'STHeiti Light.ttc'
wd = WordCloud(font_path=fpath)
wd.fit_words(filsorFsepstr)
#wd.to_file('./wd.png')
plt.imshow(wd)
plt.axis('off')
plt.show()