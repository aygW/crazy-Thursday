from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from scipy.sparse import csr_matrix
import re

class DocumentToMatrix:
    def __init__(self,method='count',max_features=20,ngram_range=(1,1),file_set={'1':{}}):
        """
        初始化文档转换器。

        :param method:选择使用'count'或'tfidf'方法。
        :param max_features:最大特征数（词汇表大小）。
        :param ngram_range:n-gram 范围，默认为(1,1)表示只使用单个词。
        :param file_set:需要转换的文档集合。
        """
        self.method=method
        self.max_features=max_features
        self.ngram_range=ngram_range
        self.vectorizer=None
        self.file_set=file_set

    def fit_transform(self,file_path):
        """
        将文档转换为词频特征矩阵。

        :param file_path:需转换的文档路径。
        :return:文档-词语的词频矩阵。
        """
        if(self.method=='count'):
            self.vectorizer=CountVectorizer(max_features=self.max_features,ngram_range=self.ngram_range)
        elif self.method=='tfidf':
            self.vectorizer=TfidfVectorizer(max_features=self.max_features,ngram_range=self.ngram_range)
        else:
            raise ValueError("方法不存在。")

        with open(file_path,'r',encoding='utf-8') as f:
            string=f.read()
        strlist=string.split('\n')
        
        matrix=self.vectorizer.fit_transform(strlist)
        return csr_matrix(matrix).toarray()

    def get_fea_names(self):
        """
        获取特征名称（词汇表）。

        :return:词汇表列表。
        """
        if(self.vectorizer is None):
            raise ValueError("词汇表未初始化。")
        return self.vectorizer.get_feature_names_out()

    def alloc_dict(self):
        """
        获取词汇表。
        
        :return:存储所有特征矩阵和特征词对的二层字典。
        """
        matr_dict={ID:{} for ID in self.file_set}
        spli=r"[./]"
        for ID in self.file_set.keys():
            for file in self.file_set[ID]:
                time=re.split(spli,file)[-2]
                fre_matr=self.fit_transform(file)
                fea_nam=self.get_fea_names()
                matr_dict[ID][time]=(fre_matr,fea_nam)
        return matr_dict