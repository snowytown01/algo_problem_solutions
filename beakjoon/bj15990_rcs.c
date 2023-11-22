#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_SIZE 100000

char store_id[MAX_SIZE][5]; // 5문자의id 
int store_loc[MAX_SIZE][2]; //x, y 참고로 이뒤에나오는 영업시간은 기본구현에선생각안함
int s_rear = -1;

char elim[MAX_SIZE][4]; // 4문자의이름
int fo[MAX_SIZE][7]; // 0년 1월 2일 3시 4분 5x 6y
int w_rear = -1;

int ordered_info[MAX_SIZE][8]; //0년 1월 2일 3시 4분 5주문금액 6x 7y
int ordered_info[MAX_SIZE][8]; //0년 1월 2일 3시 4분 5주문금액 6x 7y
int ordered_info[MAX_SIZE][8]; //0년 1월 2일 3시 4분 5주문금액 6x 7y
int ordered_info[MAX_SIZE][8]; //0년 1월 2일 3시 4분 5주문금액 6x 7y
int ordered_info[MAX_SIZE][8]; //0년 1월 2일 3시 4분 5주문금액 6x 7y
int ordered_info[MAX_SIZE][8]; //0년 1월 2일 3시 4분 5주문금액 6x 7y
int ordered_info[MAX_SIZE][8]; //0년 1월 2일 3시 4분 5주문금액 6x 7y

// # ctrl는 미세한조작
// ctrl왼오는 단어이동
// ctrlD는 단어선택/ ctrlL는 행선택
// ctrlBS는 단어삭제/ ctrlX는 행삭제

// # alt는 전체조작
// alt위아래 행이동
// alt쉬프트위아래 행복사

// # tab은자동완성선택

int main(){
    //m열의 레스토랑 정보를 
    int m;
    scanf("%d", &m);
    getchar();
    char str[MAX_SIZE];
    for(int i=0; i<m; i++){
        s_rear++;
        fgets(str, sizeof(str), stdin);
        sscanf(str, "%s %d %d", store_id[s_rear], &store_loc[s_rear][0], &store_loc[s_rear][1]);
    }
    //확인
    // for(int i=0; i<s_rear+1; i++){
    //     printf("%d %d\n", store_loc[i][0], store_loc[i][1]);
    // }
    // for(int i=0; i<s_rear+1; i++){
    //     printf("%s\n", store_id[i]);
    // }

    while(fgets(str, sizeof(str), stdin) != NULL){
        //먼저 배달원이 set-avail 할때 정보추가
        if(str[17] == 's'){
            w_rear++;
            char tempq[MAX_SIZE];
            sscanf(str, "%d-%d-%d %d:%d %s %s %d %d", &waitdeliman_info[w_rear][0], &waitdeliman_info[w_rear][1], &waitdeliman_info[w_rear][2], &waitdeliman_info[w_rear][3], &waitdeliman_info[w_rear][4], tempq, waitdeliman_id[w_rear], &waitdeliman_info[w_rear][5], &waitdeliman_info[w_rear][6]);
        }

        //order로 주문을 할때
        if(str[17] == 'o'){
            o_rear++;
            char tempq[MAX_SIZE];
            sscanf(str, "%d-%d-%d %d:%d %s %s %d %d %d", &ordered_info[o_rear][0], &ordered_info[o_rear][1], &ordered_info[o_rear][2], &ordered_info[o_rear][3], &ordered_info[o_rear][4], tempq, ordered_store[o_rear], &ordered_info[o_rear][5], &ordered_info[o_rear][6], &ordered_info[o_rear][7]);
            
            if(w_rear == -1){
                printf("%d-%02d-%02d %02d:%02d ERROR NO DELIVERY PERSON\n", ordered_info[o_rear][0], ordered_info[o_rear][1], ordered_info[o_rear][2], ordered_info[o_rear][3], ordered_info[o_rear][4]);
                o_rear--;
            }
            else{//주문을 수리하고 배달원id와 송료를 출력 배달원 내리기
                int delicost, searched_index;
                for(int i=0; i<s_rear+1; i++){
                    if(strcmp(store_id[i], ordered_store[o_rear]) == 0){
                        searched_index = i;
                    }
                }
                int delidist = abs(waitdeliman_info[w_rear][5] - store_loc[searched_index][0]) + abs(waitdeliman_info[w_rear][6] - store_loc[searched_index][1]) + abs(store_loc[searched_index][0] - ordered_info[o_rear][6]) + abs(store_loc[searched_index][1] - ordered_info[o_rear][7]);
                if(delidist>=0 && delidist<100) delicost = 300;
                if(delidist>=100 && delidist<1000) delicost = 600;
                if(delidist>=1000 && delidist<10000) delicost = 900;
                if(delidist>=10000) delicost = 1200;
                printf("%d-%02d-%02d %02d:%02d %s %d\n", ordered_info[o_rear][0], ordered_info[o_rear][1], ordered_info[o_rear][2], ordered_info[o_rear][3], ordered_info[o_rear][4], waitdeliman_id[w_rear], delicost);
                w_rear--;
                o_rear--;
            }
        }
    }
    
}