
#include "stack.h"

//初始化栈
void STInit(ST* ps){
    assert(ps);
    ps->a = NULL;
    ps->capacity = 0;
    ps->top = 0;//top等于0时说明栈顶位置指向栈顶元素的下一个位置
    //top等于-1时说明栈顶位置指向栈顶元素
}
//入栈
void STPush(ST* ps,STDataType x){
    assert(ps);
    if(ps->top == ps->capacity){//如果栈满了就扩容
        int newcapacity = ps->capacity == 0 ? 4 : ps->capacity * 2;
        STDataType* temp = (STDataType*)realloc(ps->a,sizeof(STDataType) * newcapacity);
        if(temp == NULL){
            perror("realloc fail");
            exit(-1);
        }
        ps->a = temp;
        ps->capacity = newcapacity;
    }
    //入栈
    ps->a[ps->top] = x;
    ps->top++;
}
//出栈
void STPop(ST* ps){
    assert(ps);
    assert(ps->top > 0);
    ps->top--;
}
//栈内数据格式
int STSize(ST *ps){
    assert(ps);
    return ps->top;
}
//获取栈顶元素
STDataType STTop(ST* ps){
    assert(ps);
    assert(ps->top > 0);
    return ps->a[ps->top - 1];
}
//判断栈是否为空
bool STEmpty(ST* ps){
    assert(ps);
    return ps->top == 0;
}
//栈的销毁
void STDestory(ST* ps){
    assert(ps);
    free(ps->a);
    ps->a = NULL;
    ps->capacity = ps->top = 0;
}
//栈数据打印
void STPrint(ST* ps){
    assert(ps);
    while(!STEmpty(ps)){
        printf("%d ", STTop(ps));
        STPop(ps);
    }
    printf("\n");
}