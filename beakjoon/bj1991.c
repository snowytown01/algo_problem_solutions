#include <stdio.h>
#include <stdlib.h>

struct treenode{
    int data;
    struct treenode *left, *right;
};

struct treenode *create_node(char letter){
    struct treenode *temp = malloc(sizeof(struct treenode));
    temp -> data = letter;
    temp -> left = NULL;
    temp -> right = NULL;
    return temp;
}

//순환에서는 상호작용하는 집합들을 특정하는게 중요, 여기서는 root노드, 왼쪽군, 오른쪽군 이3개가 서로 상호작용
void preorder(struct treenode *root){
    if(root == NULL) return;
    printf("%c",root -> data);
    preorder(root -> left);
    preorder(root -> right);
}

void inorder(struct treenode *root){
    if(root == NULL) return;
    inorder(root -> left);
    printf("%c",root -> data);
    inorder(root -> right);
}

void postorder(struct treenode *root){
    if(root == NULL) return;
    postorder(root -> left);
    postorder(root -> right);
    printf("%c",root -> data);
}

int main(){
    char str[10000];
    int nodeamo;
    char newnodelett, leftlett, rightlett;

    fgets(str, sizeof(str), stdin);
    sscanf(str, "%d", &nodeamo);

    struct treenode *nodes[nodeamo]; //모든 선언된 노드들을 라인의 순서에 맞게 저장
    char linerec[nodeamo][2]; //nodeamo행 2열 배열선언
    
    for(int i=0; i<nodeamo; i++){
        fgets(str, sizeof(str), stdin);
        sscanf(str, "%c %c %c", &newnodelett, &leftlett, &rightlett);
        linerec[i][0] = leftlett;
        linerec[i][1] = rightlett;
        
        nodes[i] = create_node(newnodelett);
    }

    for(int i=0; i<nodeamo; i++){
        for(int j=0; j<nodeamo; j++){
            if(linerec[i][0] == nodes[j] -> data) nodes[i] -> left = nodes[j];
            if(linerec[i][1] == nodes[j] -> data) nodes[i] -> right = nodes[j];
        }
    }
    
    //전위순위먼저
    preorder(nodes[0]);
    printf("\n");
    inorder(nodes[0]);
    printf("\n");
    postorder(nodes[0]);
}