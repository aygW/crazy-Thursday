from text_precon import DocumentPreConditionor
from text_fearepre import DocumentToMatrix
from text_topicana import TextTopicAnalyzer
import matplotlib.pyplot as plt
from pylab import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

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
t_matrix=DocumentToMatrix(m_method,m_max_features,m_ngram_range,t_set)
matr_dict=t_matrix.alloc_dict()

eg_ID=list(matr_dict.keys())[0]
eg_time=list(matr_dict[eg_ID].keys())[0]
eg_fre_matr,eg_fea_nam=matr_dict[eg_ID][eg_time]
print(eg_fre_matr)
print(eg_fea_nam)

#3、4、5
l_topic=int(input("请输入主题数："))
l_word=int(input("请输入词数："))
l_maxto=int(input("请输入最大主题数："))

eg_file_name='D:/git code collections/crazy-Thursday/py.D.A/homework/week4/jianda/Q1/'+t_accuracy+'ly-seperated/'+eg_ID+'_'+eg_time+'.pkl'
eg_fig1_name='D:/git code collections/crazy-Thursday/py.D.A/homework/week4/jianda/Q1/'+t_accuracy+'ly-seperated/'+eg_ID+'_'+eg_time+'.png'
l_analyz=TextTopicAnalyzer(eg_fre_matr,eg_fea_nam,l_topic)
l_analyz.analyze_topics(l_word)
l_analyz.save(eg_file_name)
l_analyz.plot_perplexity(l_maxto,eg_fig1_name)
#6
eg_freq_dict={time:[] for time in matr_dict[eg_ID]}
for time in matr_dict[eg_ID]:
    fre_matr,fea_nam=matr_dict[eg_ID][time]
    l_analyz=TextTopicAnalyzer(fre_matr,fea_nam,l_topic)
    lda=l_analyz.build_lda_model(1)
    if(lda is None):
            raise ValueError("LDA 模型尚未构建。")
    doc_topic_dist=lda.transform(fre_matr)
    topic_frequencies=doc_topic_dist[:,0]
    eg_freq_dict[time]=topic_frequencies[0]
eg_fig2_name='D:/git code collections/crazy-Thursday/py.D.A/homework/week4/jianda/Q1/'+t_accuracy+'ly-seperated/'+eg_ID+'-'+'话题热度变化'+'.png'
x=sorted(list(time for time in eg_freq_dict))
y=list(eg_freq_dict[time] for time in eg_freq_dict)
plt.figure(figsize=(10,6))
plt.plot(x,y,marker='o')
plt.xlabel('时间段')
plt.ylabel('话题热度')
plt.title('话题热度与时间变化曲线')
plt.grid(True)
plt.savefig(eg_fig2_name,format='png',dpi=300)
plt.show()