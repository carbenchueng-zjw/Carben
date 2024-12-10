#include <iostream>

using namespace std;


//运算符
int main()
{
//    加减乘除
    int a = 10;
    int b = 3;
    int c = 0;
    int d = 20;

    cout <<"a/b=:" << a/b << endl;//除法会去掉小数位且不会四舍五入，结果可以为小叔，注意被除数（分母）不能为0
    cout <<"c/a=:" << c/a << endl;
    cout <<"a%d=:" << a%d << endl;//跟除法一样，而且两个小数之间不能取模运算
//
////    前置递增
    ++a;
    cout <<"a=:" << a << endl;
////    前置递减
//    --a;
//    cout <<"a=:" << a << endl;
////    后置递增
//    b++;
//    cout <<"b=:" << b << endl;
////    后置递减
//    b--;
//    cout <<"b=:" << b << endl;
////    前置，后置的区别
////    前置：先让变量+1，然后进行表达式运算
//    int a2 = 10;
//    int b2 = ++a2 *10;//先a2+1=11,再拿a2=11*100=110;
//    cout <<"b2=:" << b2 << endl;
//    cout <<"a2=:" << a2 << endl;
////    后置：先进行表达式运算，然后再让变量+1
//    int a3 = 10;
//    int b3 = a3++ *10;//先让a3*10，b3=100,再让a3+1,a3=11
//    cout <<"b3=:" << b3 << endl;
//    cout <<"a3:" << a3 << endl;

//    逻辑运算符(返回值是0。1，就是真和假)：非！(取反)，与&& 或｜｜
//    cout <<"！a:" << !a << endl;
//    cout <<"a｜｜b :" << (!a||b)<< endl;
//    cout <<"!a&&b :" << (!a&&b)<< endl;

    return 0;
}

