import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("D:/week3.csv")

with open("D:/emotion_lexicon/joy.txt") as joy:
    jy=joy.readlines()
jy=[word.rstrip() for word in jy]
with open("D:/emotion_lexicon/anger.txt") as anger:
    ag=anger.readlines()
ag=[word.rstrip() for word in ag]
with open("D:/emotion_lexicon/disgust.txt") as disgust:
    dg=disgust.readlines()
dg=[word.rstrip() for word in dg]
with open("D:/emotion_lexicon/fear.txt") as fear:
    fr=fear.readlines()
fr=[word.rstrip() for word in fr]
with open("D:/emotion_lexicon/sadness.txt") as sadness:
    sn=sadness.readlines()
sn=[word.rstrip() for word in sn]
emotion_dict={'joy':jy,'anger':ag,'disgust':dg,'fear':fr,'sadnss':sn}
'''ps=jy
ng=ag+dg+fr+sn
emo=ps+ng'''

#1
def emotion_analyzer():
    emo_dic=emotion_dict
    def mixed_emo_analysis(string):
        lis=string.split()
        emo_count={key:0 for key in emo_dic}
        total_count=0
        for word in lis:
            for key in emo_dic:
                if word in emo_dic[key]:
                    emo_count[key]+=1
                    total_count+=1
                    break
        if total_count==0:
            return {key:0 for key in emo_count}
        else:
            return {key:emo_count[key]/total_count for key in emo_count}
    def sole_emo_analysis(string):
        lis=string.split()
        emo_count={key:0 for key in emo_dic}
        for word in lis:
            for key in emo_dic:
                if word in emo_dic[key]:
                    emo_count[key]+=1
                    break
        emo_sorted=sorted(emo_count.items(),key=lambda x:x[-1],reverse=True)
        if emo_sorted[0][1]==0:
            return None
        else:
            if emo_sorted[0][1]>emo_sorted[1][1]:
                return emo_sorted[0][0]
            else:
                return [key for key in emo_count if emo_count[key]==emo_sorted[0][1]]
    return mixed_emo_analysis,sole_emo_analysis
mixed_emo,sole_emo=emotion_analyzer()

'''def mixed_emo_analysis():
    
    def inner1(string):
        lis=string.split()
        jy_num=ag_num=dg_num=fr_num=sn_num=emo_num=0
        for word in lis:
            if word in jy:
                jy_num+=1
            elif word in ag:
                ag_num+=1
            elif word in dg:
                dg_num+=1
            elif word in fr:
                fr_num+=1
            elif word in sn:
                sn_num+=1
            emo_num+=1
        if emo_num==0:
            print("No Emotional Expression!")
            return 0
        jy_r=jy_num/emo_num
        ag_r=ag_num/emo_num
        dg_r=dg_num/emo_num
        fr_r=fr_num/emo_num
        sn_r=sn_num/emo_num
        emo_list=[jy_r,ag_r,dg_r,fr_r,sn_r]
        print("joy,anger,disgust,fear,sadness的情绪向量为：",emo_list)
        return 0
    return inner1
mixed_emo=mixed_emo_analysis()'''
'''def sole_emo_analysis():
    def inner2(string):
        lis=string.split()
        jy_num=ag_num=dg_num=fr_num=sn_num=emo_num=0
        for word in lis:
            if word in jy:
                jy_num+=1
            elif word in ag:
                ag_num+=1
            elif word in dg:
                dg_num+=1
            elif word in fr:
                fr_num+=1
            elif word in sn:
                sn_num+=1
            emo_num+=1
        if emo_num==0:
            print("该评论没有情绪表现。")
            return 0
        emo_level={'joy':jy_num,'anger':ag_num,'disgust':dg_num,'fear':fr_num,'sadnss':sn_num}
        emo_sorted=sorted(emo_level.items(),key=lambda x:x[-1],reverse=True)
        if emo_sorted[0][1]>emo_sorted[1][1]:
            return emo_sorted[0][0]
            ''''''print('该评论的情绪应标记为'+emo_sorted[0][0]+'。')''''''
        else:
            return 0
            ''''''if emo_sorted[1][1]>emo_sorted[2][1]:
                print('该评论的情绪应标记为'+emo_sorted[0][0]+'和'+emo_sorted[1][0]+'。')
            else:
                if emo_sorted[2][1]>emo_sorted[3][1]:
                    print('该评论的情绪应标记为'+emo_sorted[0][0]+'，'+emo_sorted[1][0]+'和'+emo_sorted[2][0]+'。')
                else:
                    if emo_sorted[3][1]>emo_sorted[4][1]:
                        print('该评论的情绪应标记为'+emo_sorted[0][0]+'，'+emo_sorted[1][0]+'，'+emo_sorted[2][0]+'and'+emo_sorted[3][0]+'。')
                    else:
                        print('该评论包含各种情绪。')''''''
        return 0
    return inner2
sole_emo=sole_emo_analysis()'''

#2
posi_dict=['joy']
nega_dict=['anger','disgust','fear','sadnss']
emo_dict={'positive':posi_dict,'negative':nega_dict}

years=list(set(df['year']))
months=[i for i in range(1,25)]
weekdays=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
hours=[i for i in range(24)]
time_dict={'year':years,'month':months,'weekday':weekdays,'hour':hours}

def time_pattern(shop_ID,emo_pole,time_module):
    select_df=df[df['shopID']==shop_ID]   
    emotion=emo_dict[emo_pole]
    time=time_dict[time_module]
    emo_time={semo:[0]*len(time) for semo in emotion}

    for i in range(len(select_df)):
        string=df[i]['cus_comment']
        t_point=df[i][time_module]
        t_index=time.index(t_point)
        e_dire=sole_emo(string)
        if isinstance(e_dire,str):
            if e_dire in emotion:
                emo_time[e_dire][t_index]+=1
        elif isinstance(e_dire,list):
            for semo in e_dire:
                if e_dire in emotion:
                    emo_time[e_dire][t_index]+=1/len(e_dire)

    fig,ax=plt.subplots()
    bottom=[0 for i in range(len(time))]
    for e,ef in emo_time.items():
        ax.bar(time,ef,width=0.5,label=e,bottom=bottom)
        for i in range(len(bottom)):
            bottom[i]+=ef[i]
    ax.legend()
    plt.title("时间模式分析")
    plt.tight_layout() 
    plt.savefig("D:/git code collections/crazy-Thursday/crazy-Thursday-1/py.D.A/week3/jianda/时间模式分析.png", dpi=300)
    plt.show()

#3
df['mixed_emotion'] = df['cus_comment'].apply(mixed_emo)
df['joy_ratio'] = df['mixed_emotion'].apply(lambda x:x['joy'])
plt.figure(figsize=(10,6))
sns.scatterplot(x='joy_ratio',y='stars',data=df)
plt.title("情绪分析与评分对比")
plt.xlabel("joy_ratio")
plt.ylabel("stars")
plt.savefig("D:/git code collections/crazy-Thursday/crazy-Thursday-1/py.D.A/week3/jianda/情绪分析与评分对比.png", dpi=300)
plt.show()
