from sklearn.decomposition import LatentDirichletAllocation
import pyLDAvis
import numpy as np
import pickle
import matplotlib.pyplot as plt
from pylab import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

class TextTopicAnalyzer:
    def __init__(self,feature_matrix,feature_names,n_topics=5):
        """
        初始化话题分析器。

        :param feature_matrix: 特征矩阵。
        :param feature_names:特征名称。
        :param n_topics:主题数目。
        """
        self.feature_matrix=feature_matrix
        self.feature_names=feature_names
        self.n_topics=n_topics
        self.lda_model=None
    def build_lda_model(self,flag=0):
        """
        构建LDA主题模型。

        """
        self.lda_model=LatentDirichletAllocation(n_components=self.n_topics,random_state=42)
        self.lda_model.fit(self.feature_matrix)
        '''if(flag==1):
            doc_topic_dists=self.lda_model.transform(self.feature_matrix)
            return doc_topic_dists'''
        if(flag==1):
            return self.lda_model
        return
    def display_topics(self,n_words=10):
        """
        显示每个主题的关键词。

        :param n_words:每个主题显示的词语数目。
        """
        if(self.lda_model is None):
            raise ValueError("LDA 模型尚未构建。")      
        
        for topic_idx,topic in enumerate(self.lda_model.components_):
            top_words_idx=topic.argsort()[:-n_words-1:-1]
            top_words=[self.feature_names[i] for i in top_words_idx]
            print(f"Topic {topic_idx+1}:{' '.join(top_words)}")
        return
    def visualize_lda_model(self):
        """
        使用 pyLDAvis 可视化 LDA 模型。

        """
        if(self.lda_model is None):
            raise ValueError("LDA 模型尚未构建。")
        
        topic_term_dists=self.lda_model.components_/self.lda_model.components_.sum(axis=1)[:,np.newaxis]
        doc_topic_dists=self.lda_model.transform(self.feature_matrix)
        doc_lengths=np.sum(self.feature_matrix, axis=1)  
        vocab=self.feature_names
        term_frequency=np.ravel(self.feature_matrix.sum(axis=0))
        mds='tsne'
        vis=pyLDAvis.prepare(topic_term_dists=topic_term_dists,
                            doc_topic_dists=doc_topic_dists,
                            doc_lengths=doc_lengths, 
                            vocab=vocab,
                            term_frequency=term_frequency,
                            mds=mds)
        pyLDAvis.display(vis)
        return
    def save(self,filename):
        """
        使用pickle保存LDA模型及其对应的词频矩阵与特征表示。

        :param filename:保存模型及特征表示的文件名。
        """
        with open(filename,'wb') as f:
            pickle.dump(self.lda_model,f)
            pickle.dump(self.feature_matrix,f)
            pickle.dump(self.feature_names,f)
    @staticmethod
    def load_lda(filename):
        """
        使用pickle加载LDA模型。

        :param filename:加载模型的文件名。
        """
        with open(filename,'rb') as f:
            lda_model=pickle.load(f)
        return lda_model
    @staticmethod
    def load_feature(filename):
        """
        使用pickle加载特征表示。

        :param filename:加载特征的文件名。
        """
        with open(filename,'rb') as f:
            feature_matrix=pickle.load(f)
            feature_names=pickle.load(f)
        return feature_matrix,feature_names
    def analyze_topics(self,n_words=10):
        """
        完整的LDA主题建模流程。

        :param n_words:每个主题显示的词语数目。
        """
        self.build_lda_model()
        self.display_topics(n_words=n_words)
        self.visualize_lda_model()
    def plot_perplexity(self,max_topics=20,fig1_name=None):
        """
        绘制困惑度随话题数目变化的曲线。

        :param max_topics:最大话题数目。
        """
        perplexities=[]
        for k in range(1,max_topics+1):
            lda=LatentDirichletAllocation(n_components=k,random_state=42)
            lda.fit(self.feature_matrix)
            perplexities.append(lda.perplexity(self.feature_matrix))

        plt.figure(figsize=(10,6))
        plt.plot(range(1,max_topics+1),perplexities,marker='o')
        plt.xlabel('话题数目')
        plt.ylabel('困惑度')
        plt.title('困惑度与话题数目曲线')
        plt.grid(True)
        plt.savefig(fig1_name,format='png',dpi=300)
        plt.show()