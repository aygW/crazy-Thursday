#include<stdio.h>
#include<stdlib.h>
typedef int ElemType;
struct node{   
    ElemType data;
    struct node *rlink,*llink;
};
typedef struct node *DNodeptr;
typedef struct node DNode; 
DNodeptr list,p;
DNodeptr insertNode(DNodeptr,DNodeptr);
DNodeptr createList(ElemType*,int);
void deleteHead(DNodeptr*);
void deleteDNode(DNodeptr);
DNodeptr allocMemo(DNodeptr,ElemType);

int main(){
    ElemType* space=malloc(sizeof(ElemType));
    int a,b,count=0;
    char c,need[10];
    do{
        scanf("%d%c",&a,&c);
        count++;
        space=realloc(space,sizeof(ElemType)*count);
        space[count-1]=a;
    }while(c!='\n');
    DNodeptr head=createList(space,count);
    free(space);
    while(fgets(need,sizeof(need),stdin)){
        if(sscanf(need,"%d",&b)!=1)
            break;
        head=allocMemo(head,b);
    }
    free(head);
    return 0;
}

DNodeptr insertNode(DNodeptr list,DNodeptr p){
    list->llink->rlink=p;
    p->llink=list->llink;
    p->rlink=list;
    list->llink=p;
}
DNodeptr createList(ElemType* a,int n)
{
    DNodeptr list,p;
    list=(DNodeptr)malloc(sizeof(DNode));
    list->data=a[0];
    list->llink=list;
    list->rlink=list;
    for(int i=1;i<n;i++){
        p=(DNodeptr)malloc(sizeof(DNode));
        p->data=a[i];
        insertNode(list,p);
    }
    return list;
}
void deleteHead(DNodeptr* head){
    DNodeptr currentHead=*head;
    DNodeptr newHead=currentHead->rlink;
    DNodeptr tail=currentHead->llink;
    newHead->llink=tail;
    tail->rlink=newHead;
    //free(currentHead);
    *head=newHead;
}
void deleteDNode(DNodeptr q){
    q->llink->rlink=q->rlink;
    q->rlink->llink=q->llink;
    free(q);
}
DNodeptr allocMemo(DNodeptr a,ElemType b){
    DNodeptr p=a->rlink,q=a->llink,r,l,s=a->rlink,t;
    int sum=a->data;
    if(a->data>=b){
        a->data-=b;
        printf("%d\n",a->data);
        if(a->data==0){
            deleteHead(&a);
        }
        return a;
    }
    do{
        if(q->data>=b){
            q->data-=b;
            printf("%d\n",q->data);
            if(q->data==0)
                deleteDNode(q);
            return a;
        }
        if(p->data>=b){
            p->data-=b;
            printf("%d\n",p->data);
            if(p->data==0)
                deleteDNode(p);
            return a;
        }
        r=p,p=p->rlink;
        l=q,q=q->llink;
    }while(p->llink!=q->rlink&&p->llink!=q);
    do{
        sum+=s->data;
        t=s,s=s->rlink;
    }while(s!=a);
    if(sum>=b){
        sum-=b;
        do{
            t->data=0;
            s=t,t=t->llink;
        }while(t!=a);
        printf("%d\n",sum);
        a->data=sum;
        return a;
    }else
        printf("memory out");
        return a;
}