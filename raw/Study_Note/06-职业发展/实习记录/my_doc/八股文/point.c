#include <stdio.h>

/* 取消下方注释来激活对应的练习 */
//#define POINT_BASE      // 基础指针练习
#define POINT_ARITH     // 指针算术运算
//#define POINT_SWAP      // 指针作为函数参数
//#define POINT_STR       // 指针与字符串
//#define POINT_ARRAY     // 指针数组
//#define POINT_FUNC      // 函数指针
//#define POINT_MULTI     // 多级指针
//#define POINT_DYNAMIC   // 动态内存分配

#ifdef POINT_BASE
/* 1. 基础指针练习 */
int main() {
    int num = 10;
    int *ptr = &num;  // ptr指向num的地址

    printf("num的值: %d\n", num);  // 输出: num的值: 10
    printf("num的地址: %p\n", &num);  // 输出示例: num的地址: 0x... (具体地址随运行变化)
    printf("ptr存储的地址: %p\n", ptr);  // 输出示例: ptr存储的地址: 0x... (与num的地址相同)
    printf("ptr指向的值: %d\n", *ptr);  // 输出: ptr指向的值: 10

    return 0;
}
#endif

#ifdef POINT_ARITH
/* 2. 指针算术运算 */
int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int *ptr = arr;  // 指向数组第一个元素

    for(int i = 0; i < 5; i++) {
        printf("arr[%d] = %d, 地址: %p\n", i, *(ptr + i), ptr + i);  // 输出示例: arr[0] = 10, 地址: 0x...; arr[1] = 20, 地址: 0x...; ... (地址随运行变化)
    }

    return 0;
}
#endif

#ifdef POINT_SWAP
/* 3. 指针作为函数参数 */
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x = 5, y = 10;
    printf("交换前: x = %d, y = %d\n", x, y);  // 输出: 交换前: x = 5, y = 10
    swap(&x, &y);
    printf("交换后: x = %d, y = %d\n", x, y);  // 输出: 交换后: x = 10, y = 5
    return 0;
}
#endif

#ifdef POINT_STR
/* 4. 指针与字符串 */
int main() {
    char str[] = "Hello";
    char *ptr = str;

    while(*ptr != '\0') {
        printf("%c ", *ptr);  // 输出序列: H e l l o
        ptr++;  // 移动到下一个字符
    }

    return 0;
}
#endif

#ifdef POINT_ARRAY
/* 5. 指针数组 */
int main() {
    int a = 1, b = 2, c = 3;
    int *ptr_arr[] = {&a, &b, &c};  // 指针数组

    for(int i = 0; i < 3; i++) {
        printf("ptr_arr[%d]指向的值: %d\n", i, *ptr_arr[i]);  // 输出示例: ptr_arr[0]指向的值: 1; ptr_arr[1]指向的值: 2; ptr_arr[2]指向的值: 3
    }

    return 0;
}
#endif

#ifdef POINT_FUNC
/* 6. 函数指针 */
int add(int a, int b) { return a + b; }
int subtract(int a, int b) { return a - b; }

int main() {
    int (*operation)(int, int);  // 函数指针声明

    operation = add;
    printf("5 + 3 = %d\n", operation(5, 3));  // 输出: 5 + 3 = 8

    operation = subtract;
    printf("5 - 3 = %d\n", operation(5, 3));  // 输出: 5 - 3 = 2

    return 0;
}
#endif

#ifdef POINT_MULTI
/* 7. 多级指针 */
int main() {
    int num = 42;
    int *ptr = &num;
    int **pptr = &ptr;  // 指向指针的指针

    printf("num的值: %d\n", num);  // 输出: num的值: 42
    printf("通过ptr访问: %d\n", *ptr);  // 输出: 通过ptr访问: 42
  