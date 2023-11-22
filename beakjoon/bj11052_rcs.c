#include <stdio.h>
#include <time.h>

int buying_quant, k=0;
int caled_tp[10000];

void find_case(int price[], int having_quant, int sumofprice){
    for(int i=1; i<=buying_quant; i++){ //if문을 i개만큼 아래로 쭉 열거 bq=4, hq=0sp=0 개수는 1 2 3 4// 가격은 1 5 6 7
        if(buying_quant-having_quant >= i){
            having_quant += i;
            sumofprice += price[i-1];
            if(having_quant != buying_quant) find_case(price, having_quant, sumofprice);
            else caled_tp[k++] = sumofprice;
            having_quant -= i;
            sumofprice -= price[i-1];
        }
    }

}

int main(){
    char str[10000];
    int temp;
    fgets(str, sizeof(str), stdin);
    sscanf(str, "%d", &buying_quant);
    int price[buying_quant];
    int having_quant = 0, sumofprice = 0;
    
    for(int i=0; i<buying_quant; i++){
        scanf("%d", &temp);
        price[i] = temp;
    }

    int start, end;
    start = clock();
    find_case(price, having_quant, sumofprice);


    // for(int i=0; i<buying_quant; i++){
    //     printf("%d\n", price[i]);
    // }
    int max = 0;
    for(int i=0; i<k; i++){
        if(caled_tp[i] >= max) max = caled_tp[i];
    }
    printf("%d\n", max);

    end = clock();
    float res = (float)(end-start)/CLOCKS_PER_SEC;

    printf("time: %f",res);
}