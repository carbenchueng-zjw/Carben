//
// Created by kabun  on 10/4/21.
//
#include <iostream>
#include "05_FH.h"
using namespace std;

//函数
//创建加法的函数
int add(int num_1,int num_2)
{
    //num_1,num_2我们称为形参
    int sum = num_1+num_2;
    return sum;

}

//值传递
//实现两个数字交换的函数(无返回值类型的函数用void定义)
//void swapp(int num_1,int num_2)
//{
//    cout<< "交换前："<< num_1<<"\t"<<num_2 <<endl;
//    int temp = num_1;
//    num_1 = num_2;
//    num_2=temp;
//
//    cout<< "交换后："<< num_1<<"\t"<<num_2 <<endl;
//}

//函数的常见样式：
//1：无参无返
void test_01()
{
    cout << "无参无返" << endl;
}
//2：有参无返
void test_02(int b)
{
    cout << "有参无返\t" << b << endl;
}
//3：无参有返
int test_03()
{
    cout << "无参有返\t" << endl;
    return 100;
}
//3：无参有返
int test_04(int c)
{
    cout << "有参有返\t" << c << endl;
    return c;
}


//函数高级
//1:注意：默认参数只能放在最后或从最后开始倒序的添加
//2:如果函数声明有默认参数，那么函数的实现就不能有默认参数

//函数默认参数
//void func(int a, int b,int c=12);//会报错，因为声明已经有了默认参数
void func(int a,int b,int c=10)//c为默认参数
//注意：默认参数只能放在最后或从最后开始倒序的添加
{
    cout<< a+b<<endl;
}

//函数占位参数,只写数据类型
void func2(int a , int)
{
    cout << "hasdhasd" <<endl;
}

//函数重载,函数名可以相同，提高复用性
//注意
//1：同一个作用域
//2：需要函数的参数类型，个数，顺序的其中一个不同
//void test(int a)//6
//{
//    cout << "test(int a)" <<endl;
//}
void test(int &a)//1
{
    cout << "test(int &a)" <<endl;
}
void test(const int &a)//2
{
    cout << "test(const int &a)" <<endl;
}
void test(int a, float b)//3
{
    cout << "test(int a, float b)" <<endl;
}
void test(float b,int a)//4
{
    cout << "test(float b,int a)" <<endl;
}
void  test(const int &a,int b=10)//5
{
    cout << "test(const int &a,int b=10)" <<endl;
}

int main()
{
//    int num_1 = 10;
//    int num_2 = 20;
//    int r = add(num_1,num_2);//1,2我们称为实参
//    cout << r <<endl;
//    swapp(11,33);
//    test_01();
//    test_02(11);
//    int te02 = test_03();
//    cout << te02 << endl;
//    int te04 = test_04(1111);
//    cout << te04 << endl;

//    函数高级
//    函数默认参数
//    func(10,10);
    //函数占位参数
//    func2(19,1);
    //函数重载
//    int a =10;
//    test(10); //报错，出现二义性，2和5冲突，
//    test(&a); //报错，出现二义性，1和6冲突，





    return 0;
}