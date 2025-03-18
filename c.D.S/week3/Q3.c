#include<stdio.h>
#include<stdlib.h>
typedef int Elem;

int main(){
    int n,k1,k2,t1,t2;
    scanf("%d %d %d %d %d",&n,&k1,&k2,&t1,&t2);
    int array[2][n],pool[k1][k2];
    for(int i=0;i<n;i++){
        scanf("%d",&array[0][i]);
    }
    for(int i=0;i<n;i++){
        scanf("%d",&array[1][i]);
    }
    int kmax=(n-k2)/t2;
    for(int k=0;k<=kmax;k++){
        for(int i=0;i<k1;i++){
            for(int j=0;j<k2;j++){
                pool[i][j]=array[i][j+k*t2];
            }
        }
        MaxPool(k1,k2,pool);
    }
    if(k1==1&&t1==1){
        for(int k=kmax;k>=0;k--){
            for(int i=0;i<k1;i++){
                for(int j=0;j<k2;j++){
                    pool[i][j]=array[i+t1][j+k*t2];
                }
            }
            MaxPool(k1,k2,pool);
        }
    }
    return 0;
}

void MaxPool(int k1,int k2,int pool[k1][k2]){
    int max=-1024;
    for(int i=0;i<k1;i++){
        for(int j=0;j<k2;j++){
            if(pool[i][j]>max)
                max=pool[i][j];
        }
    }
    printf("%d ",max);
    return;
}