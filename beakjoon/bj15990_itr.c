#include <stdio.h>
#define MAX_LEN 100000

int nofc[MAX_LEN] = {0, 1, 1, 3, 3};

int main(){
    int line;
    int data[MAX_LEN];
    scanf("%d", &line);
    for(int i=0; i<line; i++){
        scanf("%d", &data[i]);
    }

    // 경우의수 = 이전수의 경우의수 + 거기에 1만더하기
    //          이전수의 이전수 경우의수 + 거기에 2만 더하기
    //          이전수 이전수 이전수 경우 + 거기에 3만더하기
    //          즉, 이전수 + 이전수 이전수 + 이전수 이전수 이전수 경우

    for(int i=5; i<=data[0]; i++){
        nofc[i] = nofc[i-1] + nofc[i-2] + nofc[i-3] - 3;
    }

    printf("%d", nofc[data[0]]);
    

    return 0;
}