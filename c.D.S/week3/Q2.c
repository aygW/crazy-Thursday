#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#define MAXSIZE 100
typedef char ElemType;
ElemType STACK[MAXSIZE];
int Top;
void initStack(){
    Top=-1;
}
int isEmpty(){
    return Top==-1;
}
int isFull(){
    return Top==MAXSIZE-1;
}
void push(ElemType[],ElemType);
ElemType pop(ElemType[]);
int Pri(ElemType);//+ - * / < > %
int main(){
    ElemType c;
    initStack();
    ElemType poppin;
    while((c=getchar())!='='){
        if(isalpha(c))
            printf("%c",c);
        else if(c==')'){
            while((poppin=pop(STACK))!='('){
                printf("%c",poppin);
            }
        }else{
            while(!isEmpty(STACK)&&STACK[Top]!='('&&Pri(STACK[Top])>=Pri(c)){
                poppin=pop(STACK);
                printf("%c",poppin);
            }
            push(STACK,c);
        }
    }
    while(!isEmpty(STACK)){
        poppin=pop(STACK);
        printf("%c",poppin);
    }
    return 0;
}
void push(ElemType s[],ElemType item){
    if(isFull(s))
        printf("Full Stack!");
    else
        s[++Top]=item;
}
ElemType pop(ElemType s[]){
    if(isEmpty(s)){
        printf("Empty Stack!");
        exit(-1);
    }else
        return s[Top--];
}
int Pri(ElemType a){
    switch(a){
        case'+':return 0;break;
        case'-':return 0;break;
        case'*':return 1;break;
        case'/':return 1;break;
        case'(':return 2;break;
        case')':return 2;break;
        case'%':return 1;break;
        case'<':return -1;break;
        case'>':return -1;break;
    }
}