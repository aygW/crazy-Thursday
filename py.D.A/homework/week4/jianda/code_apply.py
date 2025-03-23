from text_precon import DocumentPreConditionor
from text_fearepre import DocumentToMatrix
from text_topicana import TextTopicAnalyzer

#1
t_accuracy=str(input("请输入时间精度："))
t_text=str(input("请输入文本路径："))
t_text=t_text.replace('\\','/')
t_precon=DocumentPreConditionor(t_accuracy,t_text)
t_set=t_precon.text_precon_alloc()

#2
m_method=str(input("请输入方法："))
m_max_features=int(input("请输入最大特征数："))
m_ngram_range=tuple(map(int,input("请输入n-gram范围：").split()))
t_matrix=DocumentToMatrix(m_method,m_max_features,m_ngram_range)
matr_dict=t_matrix.fit_transform(t_set)

#样例展示
eg_ID=list(matr_dict.keys())[0]
eg_time=list(matr_dict[eg_ID].keys())[0]
eg_fre_matr,eg_fea_nam=matr_dict[eg_ID][eg_time]
print(eg_fre_matr)
print(eg_fea_nam)

#3、4、5
l_topic=int(input("请输入主题数："))
l_word=int(input("请输入词数："))
l_maxtopic=int(input("请输入最大主题数："))

eg_name='D:/git code collections/crazy-Thursday/py.D.A/homework/week4/jianda/Q1/'+eg_ID+'_'+eg_time+'_'+str(l_topic)+'_'+str(l_word)+'.pkl'
l_analyz=TextTopicAnalyzer(eg_fre_matr,eg_fea_nam,l_topic)
l_analyz.analyze_topics(l_word)
l_analyz.save(eg_name)
l_analyz.plot_perplexity(l_maxtopic)

#6
#?