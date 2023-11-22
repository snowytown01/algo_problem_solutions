#include <stdio.h>
#include <time.h>

int maxprice[1000];

int max(a, b){
    return a>b ? a:b;
}

int main(){
    int buying_quant;
    int price[1000] = {0};
    scanf("%d", &buying_quant);

    for(int i=1; i<=buying_quant; i++){
        scanf("%d", &price[i]);
    }

    int start, end;
    start = clock();

    for(int i=1; i<=buying_quant; i++){ //i가 가지려하는 카드의개수
        for(int j=1; j<=i; j++){
            maxprice[i] = max(maxprice[i], price[j] + maxprice[i-j]);
        }
    }// 결국 maxprice[i] 에는 (예전maxprice에 + 다양한 price를 추가적으로 더한것)의 모든조합의경우중에서 가장 큰값이 저장되게 된다.

    //정리하면,
    //maxprice[i+1] = 
    //price[1] + maxprice[i-1]
    //price[2] + maxprice[i-2]  이 4개중에서 최대값
    //price[3] + maxprice[i-3]  이걸 for문으로 표현하면됨
    //price[4] + maxprice[i-4]
    

    printf("%d\n", maxprice[buying_quant]);

    end = clock();
    float res = (float)(end-start)/CLOCKS_PER_SEC;

    printf("time: %f",res);
}