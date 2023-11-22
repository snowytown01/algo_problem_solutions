#include <stdio.h>
#define MAX_LEN 100000

int price[MAX_LEN];
int minprice[MAX_LEN];

int calmin(int i){
    int min = 1000000;
    for(int j=1; j<=i; j++){
        if(min >= price[j] + minprice[i-j]) min = price[j] + minprice[i-j];
    }
    return min;
}

int main(){
    int card2buy;
    scanf("%d", &card2buy);
    for(int i=1; i<=card2buy; i++){
        scanf("%d", &price[i]);
    }

    //min 새로운가격을 더한것과 비교해서 작으면 새롭게 min으로
    //위는 너무 지엽적으로 생각함

    for(int i=1; i<=card2buy; i++){
        minprice[i] = calmin(i);
    }

    printf("%d\n", minprice[card2buy]);
}