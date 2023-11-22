#include <stdio.h>
#include <stdlib.h>
#define MAX_VERTICES 2000
#define MAX_STACK_SIZE 10000
#define TRUE 1
#define FALSE 0

struct graphtype{
    int n;
    int adj_mat[MAX_VERTICES][MAX_VERTICES];
};

int visited[MAX_VERTICES] = {FALSE, };
int record_stack[MAX_STACK_SIZE] = {-1, };
int top = -1;
int flag = 0;

void pop(){
    if(top > -1) record_stack[top--] = -1;
}

void push(int x){
    if(top < MAX_STACK_SIZE) record_stack[++top] = x;
}

void init(struct graphtype *g){
    g -> n = 0;
    for(int r=0; r<MAX_VERTICES; r++){
        for(int c=0; c<MAX_VERTICES; c++){
            g -> adj_mat[r][c] = 0;
        }
    }
}

void insert_vertex(struct graphtype *g){
    if(g -> n + 1 > MAX_VERTICES){
        printf("exceeded max_vertices\n");
        return;
    }
    g -> n++;
}

void insert_edge(struct graphtype *g, int tr, int tc){
    if(tr >= g -> n || tc >= g -> n){
        printf("exceeded n\n");
        return;
    }
    g -> adj_mat[tr][tc] = 1;
    g -> adj_mat[tc][tr] = 1;
}

void dfs(struct graphtype *g, int v){
    visited[v] = TRUE;
    push(v);
    if(top == 4 && flag != 1){
        printf("1\n");
        flag = 1;
    }
    for(int x=0; x<g->n; x++){
        printf("%d ", record_stack[x]);
        if(x == g->n) printf("\n");
    }

    for(int w=0; w<g->n; w++){
        if(g->adj_mat[v][w] && !visited[w]){
            dfs(g, w);
        }
    }
    pop();
}

int main(){
    char str[10000];
    int numofpep, numofline, tr, tc;
    struct graphtype *g = malloc(sizeof(struct graphtype));
    init(g);

    //맨첫번째줄 입력
    fgets(str, sizeof(str), stdin);
    sscanf(str, "%d %d", &numofpep, &numofline);
    for(int i=0; i<numofpep; i++){
        insert_vertex(g);
    }

    //그 뒤부터 입력
    for(int i=0; i<numofline; i++){
        fgets(str, sizeof(str), stdin);
        sscanf(str, "%d %d", &tr, &tc);

        insert_edge(g, tr, tc);
    }

    //그래프 탐색하며 어떤x에 대해 x-y-z-w-v 의관계를 가지는것을 찾는다.
    dfs(g, 0);
    if(flag == 0) printf("0\n");
}