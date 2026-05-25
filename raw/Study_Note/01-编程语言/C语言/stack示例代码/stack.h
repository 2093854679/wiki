#ifndef __STACK_H__
#define __STACK_H__
#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <stdbool.h>

typedef int STDataType;
typedef struct Stack{
    STDataType* a;//定义一个动态数组
    STDataType top;//用来确定栈顶位置（指向栈顶元素的下一个位置）
    STDataType capacity;//栈的容量
}ST;
// 初始化栈
void STInit(ST* ps);
// 栈的销毁
void STDestory(ST* ps);
 
// 栈只能从栈顶入栈，只能从栈顶出栈
 
 
// 栈的尾插
void STPush(ST* ps,STDataType x);
// 栈的删除
void STPop(ST* ps);
// 栈的个数
int STSize(ST* ps);
// 判断栈是否为空
bool STEmpty(ST* ps);
// 打印栈
void STPrint(ST* ps);
// 获取栈顶元素
STDataType STTop(ST* ps);
#endif