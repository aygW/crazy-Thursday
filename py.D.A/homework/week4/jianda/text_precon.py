import pandas as pd
import re
import os

class DocumentPreConditionor:
    def __init__(self,accuracy='year',text="D:/week4.csv"):
        """
        初始化文档预处理器。

        :param accuracy:选择使用'year'、'month'、'day'或'hour'作为时间单位。
        :param text:需导入的文件。
        """
        self.accuracy=accuracy
        self.text=pd.read_csv(text)
        self.t_dict={'year':1,'month':2,'day':3,'hour':4}
        self.shop_ID=list(str(ID) for ID in set(self.text['shopID']))
        self.ID_dict={ID:{} for ID in self.shop_ID}
        self.com_dict={ID:set() for ID in self.shop_ID}

    def ensure_directory_exists(self,file_path):
        """
        确保文件路径存在。

        :param file_path:需检查的文件路径。
        """
        directory=os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        return
    def text_precon_period(self):
        """
        将导入文件中的评论根据其评论时间按所需的时间精度存入对应字典中。

        """
        ind=self.text[self.text['comment_time']==self.accuracy].index[0]
        comment=self.text.loc[ind,'cus_comment']
        ID=str(self.text.loc[ind,'shopID'])
        spli=r"[-/: ]"
        t_list=re.split(spli,self.accuracy)  
        spltime='-'.join(map(str,t_list[:self.t_dict[self.accuracy]]))
        if(spltime not in self.ID_dict[ID]):
            self.ID_dict[ID][spltime]=[comment]
        else:
            self.ID_dict[ID][spltime].append(comment)
        return
    def text_precon_alloc(self):
        """
        将评论按店铺ID和评论时间精度进行分类，写入对应时间的文件并保存到指定店铺ID的目录中。

        """
        self.text['comment_time'].apply(self.text_precon_period)
        for key in self.ID_dict:
            for keyy in self.ID_dict[key]:
                file_name='D:/git code collections/crazy-Thursday/py.D.A/homework/week4/jianda/Q1/'+self.accuracy+'ly-seperated/'+key+'/'+keyy+'.txt'
                self.ensure_directory_exists(file_name)
                with open(file_name,'w',encoding='utf-8') as f:
                    for com in self.ID_dict[key][keyy]:
                        f.write(str(com)+'\n')
                self.com_dict[key].update(file_name)
        return self.com_dict