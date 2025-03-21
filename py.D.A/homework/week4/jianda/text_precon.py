import pandas as pd
import re
import os

df=pd.read_csv("D:/week4.csv")
t_accuracy=str(input())
t_dict={'year':1,'month':2,'day':3,'hour':4}
shop_ID=list(str(ID) for ID in set(df['shopID']))
ID_dict={ID:{} for ID in shop_ID}
com_dict={ID:set() for ID in shop_ID}

def ensure_directory_exists(file_path):
    directory=os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
def text_precon_period(t_module):
    def inner(string):
        ind=df[df['comment_time']==string].index[0]
        comment=df.loc[ind,'cus_comment']
        ID=str(df.loc[ind,'shopID'])
        spli=r"[-/: ]"
        t_list=re.split(spli,string)  
        spltime='-'.join(map(str,t_list[:t_dict[t_module]]))
        if(spltime not in ID_dict[ID]):
            ID_dict[ID][spltime]=[comment]
        else:
            ID_dict[ID][spltime].append(comment)
    return inner
precon=text_precon_period(t_accuracy) 
df['comment_time'].apply(precon)

def text_precon_alloc(c_dict,t_module):
    for key in c_dict:
        for keyy in c_dict[key]:
            file_name='D:/git code collections/crazy-Thursday/py.D.A/homework/week4/jianda/Q1/'+t_module+'ly-seperated/'+key+'/'+keyy+'.txt'
            ensure_directory_exists(file_name)
            with open(file_name,'w',encoding='utf-8') as f:
                for com in c_dict[key][keyy]:
                    f.write(str(com)+'\n')
            com_dict[key].update(file_name)
    return
text_precon_alloc(ID_dict,t_accuracy)