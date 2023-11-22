#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define MAX_STR_SIZE 1000000

typedef struct node{
    struct node *next;
    int data;
} TreeNode;

void insert(TreeNode *pre, int item){
    TreeNode *temp = malloc(sizeof(TreeNode));
    temp->data = item;
    temp->next = pre->next;
    pre->next = temp;
}

TreeNode *insert_first(TreeNode *head, int item){ //먼저 들어온 데이터가 맨뒤로 감
    TreeNode *temp = malloc(sizeof(TreeNode));
    temp -> data = item;
    temp -> next = head;
    head = temp;
    return head;
}

int main(){
    long long n, k;
    char str[MAX_STR_SIZE];
    fgets(str, sizeof(str), stdin);
    sscanf(str, "%lld %lld", &n, &k);

    // TreeNode *head = NULL;

    // for(int i=n; i>=1; i--){
    //     head = insert_first(head, i);
    // }

    // TreeNode *temp = head;
    // int count=0;
    // while(count < k){
    //     printf("%d ", temp->data);
    //     int digit = 0;
    //     int digitnum = temp->data;
    //     while(digitnum != 0){
    //         digitnum = digitnum / 10;
    //         digit++;
    //     }

    //     count += digit;

    //     if(count >= k) break;

    //     temp = temp->next;
    // }

    // int destdigit = count - k + 1;
    // int result = (temp->data)/pow(10, destdigit-1);
    // result = result%10;

    // printf("%d\n", result);

    //연결리스트를 쓰는 이유가 중간에 값을 집어넣기 쉽기때문인데, 이건 연속적으로 숫자가 나열된것이기에 의미없음 배열로도 충분하다.
    //근데 배열에 제한이 100000 이기때문에 배열말고 그냥 그때그때 번호에대해서 생각

    long long count=0;
    long long thatnum;
    for(int i=1; i<=n; i++){
        printf("%d ", i);
        long long digit = 0;
        long long digitnum = i;
        while(digitnum != 0){
            digitnum = digitnum / 10;
            digit++;
        }

        count += digit;

        if(count >= k){
            thatnum = i;
            break;
        }
    }

    long long destdigit = count - k + 1;
    long long result = thatnum/pow(10, destdigit-1);
    result = result%10;
    
    printf("%lld\n", result);

    return 0;

}