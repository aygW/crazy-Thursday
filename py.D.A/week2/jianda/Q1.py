import jieba
from collections import Counter
from wordcloud import WordCloud
#from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from pylab import mpl
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import Word2Vec
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

mpl.rcParams['font.sans-serif'] = ['SimHei']        # 指定默认字体为黑体 
# rcParams['font.sans-serif'] = ['SimSun']            #【若电脑上没有黑体，可指定默认字体为宋体】 
mpl.rcParams['axes.unicode_minus'] = False
#1
with open("D:\week2.txt",'r',encoding='utf-8',errors='ignore') as f1:
    slist=f1.readlines()
for i in range(10):
    print(slist[i])
print()
#2
with open("D:\week2.txt",'r',encoding='utf-8',errors='ignore') as f2:
    string=f2.read()
sepS=list(jieba.cut(string)) #separated-string
Fsepstr=Counter(sepS) #frequency-of-separated-string
#3
sorFsepstr=sorted(Fsepstr.items(),key=lambda x:x[-1],reverse=True) #sorted-frequency-of-separated-string
for i in range(10):
    print(sorFsepstr[i][0],sorFsepstr[i][1])
print()
#4
with open("D:\week2.txt",'r',encoding='utf-8',errors='ignore') as f3:
    restr=f3.read() #reread-string
resepS=list(jieba.cut(restr)) #reseparated-string
#stwords=set(stopwords.words('chinese'))
with open("D:\stopwords\stws.txt",'r',encoding='utf-8',errors='ignore') as fstw:
    stwords=fstw.readlines()
stwords=[word.rstrip() for word in stwords]
stwords.append("\n")
filsepS=[word for word in resepS if word.lower() not in stwords] #filtered-separated-string
filFsepstr=dict(Counter(filsepS)) #filtered-frequency-of-separated-string
filsorFsepstr=sorted(filFsepstr.items(),key=lambda x:x[-1],reverse=True) #filtered-sorted-frequency-of-separated-string
for i in range(10):
    print(filsorFsepstr[i][0],filsorFsepstr[i][1])
print()
#5
fpath='C:\Windows\Fonts\msyh.ttc'
wd=WordCloud(font_path=fpath,background_color='white')
wd.fit_words(filFsepstr)
wd.to_file("D:\git code collections\crazy-Thursday\crazy-Thursday-1\py.D.A\week2\jianda\Figure_1.png")
plt.imshow(wd)
plt.title("词频统计",fontsize=16)
plt.axis('off')
plt.show()
#6
nlp=spacy.load("zh_core_web_sm")
nlp.max_length=1300000
doc=nlp(' '.join(filsepS))
pos_freq=Counter(word.pos_ for word in doc)
print("词性\t频率")
for pos,freq in pos_freq.items():
    print(f"{pos}\t{freq}")
print()
nouns=[word.text for word in doc if word.pos_ == "NOUN"]
if nouns:
    nouns_text=" ".join(nouns)
wdd=WordCloud(font_path=fpath,background_color='white').generate(nouns_text)
wdd.to_file("D:\git code collections\crazy-Thursday\crazy-Thursday-1\py.D.A\week2\jianda\Figure_2.png")
plt.imshow(wdd)
plt.title("名词统计",fontsize=16)
plt.axis('off')
plt.show()
#7
bigrams=list(zip(filsepS,filsepS[1:]))
bigram_freq=Counter(bigrams)
mocombis=bigram_freq.most_common()#most-common-bigrams
print("Bigram 频率统计：")
for bigram,freq in mocombis:
    if(freq>100):
        print(f"{bigram}: {freq}")
bigram_text = " ".join(["_".join(bigram) for bigram,freq in bigram_freq.items()])
wddd=WordCloud(font_path=fpath,background_color='white').generate(bigram_text)
wddd.to_file("D:\git code collections\crazy-Thursday\crazy-Thursday-1\py.D.A\week2\jianda\Figure_3.png")
plt.imshow(wddd)
plt.title("Bigram统计",fontsize=16)
plt.axis('off')
plt.show()
#8
# 示例文本 slist
# 初始化 TF-IDF 向量化器
vectorizer = TfidfVectorizer()
# 计算 TF-IDF 矩阵
tfidf_matrix = vectorizer.fit_transform(slist)
# 获取特征词（词汇表）
feature_names = vectorizer.get_feature_names_out()
print("特征词：", feature_names)
# 获取 TF-IDF 分值
tfidf_scores = tfidf_matrix.toarray()
print("TF-IDF 分值：", tfidf_scores)
# 使用上面的 TF-IDF 矩阵
print("文本向量表示：")
for i, text in enumerate(slist):
    print(f"文本 {i+1} 的向量：{tfidf_scores[i]}")
# 分词后的文本
slist_split = [text.split() for text in slist]
# 训练 Word2Vec 模型
model = Word2Vec(sentences=slist_split, vector_size=100, window=5, min_count=1)
# 获取句子向量（平均词向量）
def get_sentence_vector(sentence, model):
    wordsss = sentence.split()
    vectors = [model.wv[word] for word in wordsss if word in model.wv]
    return np.mean(vectors, axis=0) if vectors else np.zeros(model.vector_size)
sentence_vectors = [get_sentence_vector(text, model) for text in slist]
print("句子向量表示：", sentence_vectors)
# 使用 TF-IDF 向量计算相似性
similarity_matrix = cosine_similarity(tfidf_matrix)
print("句子相似性矩阵：")
print(similarity_matrix)
# 使用 Word2Vec 句子向量计算相似性
sentence_similarity = cosine_similarity([sentence_vectors[0]], [sentence_vectors[1]])
print("句子 1 和句子 2 的相似性：", sentence_similarity[0][0])