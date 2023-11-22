#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 100000

typedef struct{
    int key;
} element;

typedef struct{
    element heap[MAX_SIZE];
    int heap_size;
} HeapType;

void insert_min_heap(HeapType *h, element item){
    int i;
    i = ++(h->heap_size);

    while(i != 1 && h->heap[i/2].key > item.key){
        h->heap[i] = h->heap[i/2];
        i /= 2;
    }
    h->heap[i] = item;
}

element delete_min_heap(HeapType *h){
    element noheaptoout;
    noheaptoout.key = 0;
    if(h->heap_size == 0) return noheaptoout;

    int parent = 1, child = 2;
    element temp, item;

    item = h->heap[1];
    temp = h->heap[(h->heap_size)--];

    while(child <= h->heap_size){
        if(child < h->heap_size && h->heap[child].key > h->heap[child+1].key) child++;
        if(h->heap[child].key >= temp.key) break;
        h->heap[parent] = h->heap[child];
        parent = child;
        child *= 2;
    }
    h->heap[parent] = temp;
    return item;
}

int main(){
    HeapType *h = malloc(sizeof(HeapType));
    h->heap_size = 0;
    int input_num, num;

    scanf("%d", &input_num);
    for(int i=0; i<input_num; i++){
        scanf("%d", &num);
        if(num == 0){
            printf("%d\n", delete_min_heap(h).key);
        }
        else{
            element item;
            item.key = num;
            insert_min_heap(h, item);
        }
    }  

    free(h);
}