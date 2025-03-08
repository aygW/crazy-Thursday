#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<limits.h>
struct Node{
    int opk;
    int *numbers;
    int flag;
    struct Node *next;
};
int main(){
    int a,flag2=0;
    char c,ch;
    int *numlist=(int *)malloc(sizeof(int));
    struct Node *head,*p,*q;
    head=p=NULL;
    /*while((ch=getchar())!='\n'){
        int flag1=0;
        do{
            scanf("%d%c",&a,&c);
            numlist=realloc(numlist,sizeof(int)*(flag2+flag1+1));
            *(numlist+flag2+flag1)=a;
            flag1++;
        }while(c!='\n');
        if(head==NULL){
            head=p=(struct Node *)malloc(sizeof(struct Node));
        }else{
            p->next=(struct Node *)malloc(sizeof(struct Node));
            p=p->next;
        }
        p->opk=ch-'0';
        p->next=NULL;
        flag2+=flag1;
        p->flag=flag2;
        p->numbers=(int *)malloc(sizeof(int)*flag2);
        memcpy(p->numbers,numlist,flag2*sizeof(int));
    }*/
    char orinum[1024];
    while(fgets(orinum,1024,stdin)){
        int flag1=0;
        if(head==NULL){
            head=p=(struct Node *)malloc(sizeof(struct Node));
        }else{
            p->next=(struct Node *)malloc(sizeof(struct Node));
            p=p->next;
        }
        p->opk=-1;
        if(orinum[0]=='\n'){
            break;
        }
        char *orinums=strtok(orinum," ");
        while(orinums!=NULL){
            a=atoi(orinums);
            if((p->opk)<0){
                p->opk=a;
            }else{
                numlist=realloc(numlist,sizeof(int)*(flag2+flag1+1));
                *(numlist+flag2+flag1)=a;
                flag1++;
            }
            orinums=strtok(NULL," ");
        }
        free(orinums);
        p->next=NULL;
        flag2+=flag1;
        p->flag=flag2;
        p->numbers=(int *)malloc(sizeof(int)*flag2);
        memcpy(p->numbers,numlist,flag2*sizeof(int));
    }
    free(numlist);
    for(q=head;q!=NULL;q=q->next){
        int sornum[(q->opk)];
        for(int i=0;i<(q->opk);i++){
            sornum[i]=INT_MIN;
            for(int j=0;j<(q->flag);j++){
                if(*(q->numbers+j)>sornum[i]){
                    if(i==0||(i>0&&*(q->numbers+j)<sornum[i-1])){
                        sornum[i]=*(q->numbers+j);
                    }
                }
            }
        }
        free(q->numbers);
        printf("%d\n",sornum[(q->opk)-1]);
    }
    free(head);
    free(p);
    free(q);
    return 0;
}