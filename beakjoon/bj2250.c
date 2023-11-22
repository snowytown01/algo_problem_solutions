#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 100000

typedef struct TreeNode{
    int data, x;
    struct TreeNode *left, *right;
} TreeNode;

TreeNode *queue[MAX_SIZE];
int front = -1, rear = -1;

void enqueue(TreeNode *node){
    queue[++rear] = node;
}

TreeNode *dequeue(){
    TreeNode *result = queue[++front];
    return result;
}

TreeNode *maketree(TreeNode *root,int numofline){
    char str[10];
    int parent, child1, child2;
    enqueue(root);

    for(int i=0; i<numofline; i++){
        fgets(str, sizeof(str), stdin);
        sscanf(str, "%d %d %d", &parent, &child1, &child2);
        
        TreeNode *parentnode = dequeue();
        parentnode->data = parent;
        if(child1 != -1){
            TreeNode *left_temp = malloc(sizeof(TreeNode));
            left_temp->data = child1;
            parentnode->left = left_temp;
            enqueue(left_temp);
        }
        else parentnode->left = NULL;

        if(child2 != -1){
            TreeNode *right_temp = malloc(sizeof(TreeNode));
            right_temp->data = child2;
            parentnode->right = right_temp;
            enqueue(right_temp);
        }
        else parentnode->right = NULL;
    }
    return root;
}

void freenode(TreeNode *root){
    if(root != NULL){
        freenode(root->left);
        freenode(root->right);
        free(root); 
    }
}

void x_postorder(TreeNode *root){
    int i = 1;
    if(root != NULL){
        temp_postorder(root->left);
        temp_postorder(root->right);
        root->x = i++;
    }
}

TreeNode *level_queue[MAX_SIZE];
int level_front = -1, level_rear = -1;

void level_enqueue(TreeNode *node){
    level_queue[++rear];
}

TreeNode *level_dequeue(){
    return level_queue[++front];
}

void level_order(TreeNode *root){
    int i = 1;
    level_enqueue(root);
    while(level_front != level_rear){
        root = level_dequeue();
        if(root->left) level_enqueue(root->left);
        if(root->right) level_enqueue(root->right);
        if(i / 2 + 1 == 3){
            if(i % pow(2,level-1) == 0) int leftend = root->x;
            if(i+1 % pow(2,level-1) == 0)
            
        } 
        i++;
    }
}

int main(){
    int numofline;
    scanf("%d", &numofline);
    getchar();
    TreeNode *root = malloc(sizeof(TreeNode));
    
    if(numofline != 0){
        root = maketree(root, numofline);
        x_postorder(root);// 각 노드에 중위순회를 통해 x값을 부여

        
        freenode(root);
    }
}

//        1(root)
//     2          3
//   4  -1      5    6
// -1  -1    -1 -1 -1 -1
//6라인

// left left가 초기화가 되어있지 않다// 완료
// 선언되지않은 부분에 접근하면 튕김

// 중위순회하면 x축의 번호를 매길수있음 순회할때마다 해당 x값을 저장
// 레벨순회를 통해 한 레벨을 순회가끝나면 그 레벨에있던 노드의 x값을 빼서 배열에 저장
// 최종적으로 만든 배열중에 가장 큰수를 출력