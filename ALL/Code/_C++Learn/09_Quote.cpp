//
// Created by kabun  on 10/8/21.
//
#include <iostream>
using namespace std;


void swap(int &a,int &b)
{
    int temp = a;
    a = b;
    b = temp;
}

int & test01()
{
    int a =10;//存放在栈区
    return a;
}

int & test02()
{
    static int a =10;//存放在全局区，会在程序结束后才释放
    return a;
}

void ShowValue(const int &val)
{
//    val=2000;//因为有const，所以报错，不能被修改
    cout << "val::" << val <<endl;
}

int main()
{
    int a = 10;
    int c = 20;
    int &b = a;

//    int *i = &a;
//    *i= 100;
//    cout << b << endl;
//    cout << &b << endl;
//    cout << i << endl;
//    cout << *i << endl;
//    cout << a << endl;

//    cout << "a::" << a <<endl;
//    cout << "c::" << c <<endl;
//    swap(a,c);
//    cout << "a::" << a <<endl;
//    cout << "c::" << c <<endl;

    //1：不要返回局部变量的引用，全局可以
//    int &ref = test01();
//
//    cout << "ref::" << ref <<endl;
//    cout << "ref::" << ref <<endl;
    //2：函数的调用可以作为左值
//    int &ree = test02();//要注释掉test01，不然执行不到test02
//    cout << "ree::" << ree <<endl;
//    cout << "ree::" << ree <<endl;
//    test02() = 1000;//如果函数的返回值是引用，这个函数调用可以作为左值
//    cout << "ree::" << ree <<endl;
//    cout << "ree::" << ree <<endl;

//    常量引用：修饰形参，防止误操作
//    int &t = 10;//这是不行的，必须是一块合法的内存空间（变量）
//    const int &tt = 10;//这是行的，必须是一块合法的内存空间
    // （变量）,编译器将代码修改成：int temp =10; const int &tt=temp
//    tt = 20;//因为加了const，不能被修改
    ShowValue(a);
    cout << "a::" << a <<endl;

    return 0;

}





