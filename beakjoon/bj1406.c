#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct node {
    struct node *next;
    char data;
};

//추가함수들
struct node *insert_from_first(struct node *head, char insertdata){
    struct node *temp = (struct node *)malloc(sizeof(struct node));
    temp -> data = insertdata;
    temp -> next = head;
    head = temp;
    return head;
}

void insert(struct node *pre, char insertdata){
    struct node *temp = malloc(sizeof(struct node));
    temp -> data = insertdata;
    temp -> next = pre -> next;
    pre -> next = temp;
}

//삭제함수들
struct node *delete_from_first(struct node *head){
    struct node *temp;
    if(head == NULL) return NULL;
    temp = head;
    head = temp -> next;
    free(temp);
    return head;
}

void delete(struct node *pre){
    struct node *temp;
    temp = pre -> next;
    pre -> next = temp -> next;
    free(temp);
}

//원하는 순번의 노드를 찾아주는 함수
struct node *find_node(struct node *head, int index){
    struct node *temp = head;
    for(int i=0; i<index; i++){
        temp = temp -> next;
    }
    return temp;
}

//쭉출력해주는 함수
void print_node(struct node *head){
    for(struct node *p = head; p != NULL; p = p -> next){
        printf("%c",p->data);
    }
}

int main(){
    char text[1000000];
    char temp_input[1000000];
    int command_times;
    
    //문자길이를 잡고, 커서값은 맨뒤
    fgets(text, sizeof(text), stdin);
    int cursor = strlen(text) - 1;
    int lenofword = cursor;

    //head노드 설정, 이 head가 앞에서 추가적인 노드를 입력받으므로 맨뒤 노드가 됨, 맨뒤노드의 next는 NULL
    struct node *head = (struct node *)malloc(sizeof(struct node));
    head -> data = text[lenofword-1];
    head -> next = NULL;

    //head노드에 나머지 모든 글자를 head을 통해 입력하므로 문자열의 뒤꺼부터 앞으로 입력
    for(int i=lenofword-2;i>=0;i--){
        head = insert_from_first(head, text[i]);
    }

    //명령어줄수입력받기
    fgets(temp_input,sizeof(temp_input), stdin);
    sscanf(temp_input, "%d", &command_times);

    //명령어 실행
    for(int i=0; i<command_times;i++){
        fgets(temp_input,sizeof(temp_input), stdin);
        if(temp_input[0] == 'L' && cursor != 0) cursor -= 1;
        if(temp_input[0] == 'D' && cursor != lenofword) cursor += 1;
        if(temp_input[0] == 'P'){
            if(cursor == 0) head = insert_from_first(head, temp_input[2]);
            else {
                struct node *pre = find_node(head, cursor-1);
                insert(pre, temp_input[2]);
            }
            cursor += 1;
            lenofword += 1;
        }
        if(temp_input[0] == 'B' && cursor != 0){
            if(cursor == 1) head = delete_from_first(head);
            else {
                struct node *pre = find_node(head, cursor-2);
                delete(pre);
            }
            cursor -= 1;
            lenofword -= 1;
        }
    }

    //문자출력
    print_node(head);

}