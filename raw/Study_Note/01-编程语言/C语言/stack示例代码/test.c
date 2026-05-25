#include "stack.h"
#include <stdio.h>
void Stack_Test_pop(void){
    ST ps;
    STInit(&ps);
    STPush(&ps, 1);
    STPush(&ps, 2);
    STPush(&ps, 3);
    STPush(&ps, 4);
    STPush(&ps, 5);
    STPop(&ps);
    STPrint(&ps);
    STDestory(&ps);
}
void Stack_Test_push(void){
    ST ps;
    STInit(&ps);
    STPush(&ps, 1);
    STPush(&ps, 2);
    STPush(&ps, 3);
    STPush(&ps, 4);
    STPush(&ps, 5);
    STPrint(&ps);
    STDestory(&ps);
}
int main(){
    Stack_Test_pop();
    Stack_Test_push();
    return 0;
}