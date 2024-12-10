#include <iostream>
//#include <string>
using namespace std;

#include "05_FH.h"

/*1：#define  宏常量（不可被修改）
 *  define xxx xxx 一般定义在方法外面（即函数外面，全局）
 *
 *2:const   修饰的常量 （不可被修改）
 * 被修饰的变量也叫常量
 * const int month = 12;
 * 一般定义在方法里面（即函数里面）
 *
 * */
//#define  宏常量（不可被修改）
//#define Day 7
//
//int main() {
////    const   修饰的常量 （不可被修改）
//    const int month = 12;
////    month =24;
//    cout << "一周一共有" << Day <<  "天"  << endl;
//    cout << "一周一共有" << month <<  "个月份，"<< "每周有"<<Day<<"天"
//    << endl;
//    return 0;
//}



//数据类型，1字节=8bit
//int main()
//    {
//    整型：shot（2字节） int（4字节） long（4字节） long long(8字节)
//    short num_1 = 10000;
//    int num_2 = 10000;
//    long num_3 = 10000;
//    long long num_4 = 10000;
//    用sizeof(数据类型/变量)

//    浮点型：float(4字节,如果后面不写f，会默认双精度),double(8)
//    float f1 = 3.1415926f;
//    double f2 = 3.1415926;

//    字符型：char(1字节,只能用单引号,只能有一个字符且不能是中文)
//    char ch = 'c';

//    科学计数法：3e2（3*10的2次方，e=10，2就是次方数）
//    float f3 = 3e2;
//
//    科学计数法：3e-2（3*0.1的2次方，e=0.1，2就是次方数）
//    float f4 = 3e-2;//
//
//    转义字符（\n换行，\\,\t占8个空间,整齐地输出内容）
//    cout << "f4=====\n  ====:"<< endl;
//    cout << "f4=====\\  ====:"<< endl;
//    cout << "f\thelloworld:"<< endl;
//    cout << "f3\thelloworld"<< endl;
//    cout << "f33\thelloworld"<< endl;

//    字符串型：
//    char name[] = "asasdasd";//占用空间比string小
//    string str1 = "adsasd";

//    布尔类型（1字节）：true（表示为真，本质是1） false（表示为假，本质是0）
//    bool flag1 = true;
//    bool flag2 = false;

//
//    cout << "short占用的空间：" << sizeof(num_1) << endl;
//    cout << "int占用的空间：" << sizeof(num_2) << endl;
//    cout << "long占用的空间：" << sizeof(num_3) << endl;
//    cout << "long long占用的空间：" << sizeof(num_4) << endl;
//    cout << "float占用的空间：" << sizeof(f1) << endl;
//    cout << "double占用的空间：" << sizeof(f2) << endl;
//    cout << "字符型所占内存：" << sizeof(ch) << endl;
//    cout << "f3=:" << f3 << endl;
//    cout << "f4=:" << f4 << endl;
//    cout << int(ch) << endl;//查看ascii编码
//    cout << name << endl;
//    cout << str1 << endl;
//    cout << flag1 << endl;
//    cout << flag2 << endl;

//    int a = 11;
//    int b = 22;
//    swap(a,b);
//    return 0;
//}


