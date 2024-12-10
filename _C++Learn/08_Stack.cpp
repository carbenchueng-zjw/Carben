//
// Created by kabun  on 10/8/21.
//
#include <iostream>
using namespace std;
#define Max 100;



//全局变量，常量
int c = 22;
//2-1:const 修饰的全局变量，也叫全局常量
const int c_g_a = 10;

//栈区
int *func()
{
    int a =10;//局部变量,存放在栈区
    return &a;//返回局部变量，错误的
}
//堆区
int * fundui()
{
    int * g = new int(10);
    int * arr = new int[10];//创建10个元素的数组
    return g;
}

void test()
{
    //    堆区:返回的是地址
    int *g = fundui();
    cout << *g <<endl;
    cout << *g <<endl;
    cout << *g <<endl;

//    堆区的释放：delete
    delete g;
    cout << *g <<endl;
    cout << *g <<endl;
}

int main()
{
    //全局区:函数外的区域



    //局部变量:函数内定义的变量
    int a = 10;
    int b = 10;
//    cout << &a <<endl;
//    cout << &b <<endl;
//    cout << &c <<endl;

    //静态变量:加上static
    static int s_a = 3;
//    cout << &s_a <<endl;

//    常量
//    1:字符串常量
//    cout << &"hello world" <<endl;
//    2:const修饰的变量
//    2-1:const 修饰的全局变量，也叫全局常量
//    cout << &c_g_a <<endl;
//    2-2:const 修饰的局部变量，
    const int c_l_b = 10;
//    cout << &c_l_b <<endl;


    //栈区：不要返回局部变量的地址，因为栈区的数据由
    // 编译器管理和释放（函数会在执行完毕后释放）
    int * p = func();
//    cout << *p <<endl;//不能输出，因为被释放了
//    cout << *p <<endl;//不能输出，因为被释放了


//    堆区:返回的是地址
//    int *g = fundui();
//    cout << *g <<endl;
//    cout << *g <<endl;
//    cout << *g <<endl;
//
////    堆区的释放：delete
//    delete g;
//    cout << *g <<endl;
//    cout << *g <<endl;
    test();



    return 0;
}
