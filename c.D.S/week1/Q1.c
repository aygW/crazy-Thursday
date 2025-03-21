/*#include <stdio.h>
#include <stdlib.h>
int main(){
    int input[1000];
    int flag=0;
    while(scanf("%d",&input[flag])==1){
        flag++;
    }
    int b[flag],a[flag],c[flag];
    int bb=0,aa=0,cc=0,mod;
    for(int i=0;i<flag;i++){
        mod=input[i]%3;
        if(mod==2||mod==-1){
            b[bb]=input[i];
            bb++;
        }else if(mod==0){
            a[aa]=input[i];
            aa++;
        }else if(mod==1||mod==-2){
            c[cc]=input[i];
            cc++;
        }
    }
    int output[flag];
    for(int j=0;j<bb;j++){
        output[j]=b[j];
    }
    for(int j=0;j<aa;j++){
        output[j+bb]=a[j];
    }
    for(int j=0;j<cc;j++){
        output[j+bb+aa]=c[j];
    }
    for(int j=0;j<flag;j++){
        printf("%d ",output[j]);
    }
    return 0;
}*/
#include <stdio.h>
#include <ctype.h>
int main(){
    int input[1000];
    int flag=0;
    char ch;
    for(int i=0;i<1000;i++){
        scanf("%d",&input[i]);
        flag++;
        scanf("%c",&ch);
        if(ch=='\n')
            break;
    }
    int b[flag],a[flag],c[flag];
    int bb=0,aa=0,cc=0,mod;
    for(int i=0;i<flag;i++){
        mod=input[i]%3;
        if(mod==2||mod==-1){
            b[bb]=input[i];
            bb++;
        }else if(mod==0){
            a[aa]=input[i];
            aa++;
        }else if(mod==1||mod==-2){
            c[cc]=input[i];
            cc++;
        }
    }
    int output[flag];
    for(int j=0;j<bb;j++){
        output[j]=b[j];
    }
    for(int j=0;j<aa;j++){
        output[j+bb]=a[j];
    }
    for(int j=0;j<cc;j++){
        output[j+bb+aa]=c[j];
    }
    for(int j=0;j<flag;j++){
        printf("%d ",output[j]);
    }
    return 0;
}
