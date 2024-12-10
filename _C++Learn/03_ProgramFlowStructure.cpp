//
// Created by kabun  on 10/1/21.
//
#include <iostream>
#include <ctime>
#include "05_FH.h"
using namespace std;

//选择结构：if(注意，if后面不能加分号，冒号)
int main()
{
    int a =10;
    int b =20;
    swapp(a,b);

    //让用户输入分数，如果大于600属于考上一本大学，500～600之间是二本大学
    // 在屏幕上输出
//    int score = 0;
//    cout<< "请输入您的分数" <<endl;
//    cin >> score;
//
//    if (score >= 600)
//    {
//        if (score>700)
//        {
//
//            cout<< "分数大于700，考上北大" <<endl;
//        }
//        else if (score > 650)
//        {
//            cout<< "分数大于700，考上清华" <<endl;
//        }
//    }
//    else if (score >= 500)
//    {
//        cout<< "分数高于500，是二本大学" <<endl;
//    }
//    else if (score < 500)
//    {
//        cout<< "分数低于500，三流大学" <<endl;
//    }
//    else
//    {
//        cout<< "输入有误，请重新输出！！" <<endl;
//    }

//    三只小猪的体重
//    int score_1 = 0;
//    int score_2 = 0;
//    int score_3 = 0;
//    cout<< "请输入第一只小猪的体重" <<endl;
//    cin >> score_1;
//    cout<< "请输入第二只小猪的体重" <<endl;
//    cin >> score_2;
//    cout<< "请输入第三只小猪的体重" <<endl;
//    cin >> score_3;
//
//    if (score_1 > score_2)
//    {
//        if (score_1 > score_3)
//        {
//            cout<< "第一只小猪最重，为："<< score_1 <<endl;
//        }
//        else
//        {
//            cout<< "第三只小猪最重，为："<< score_3 <<endl;
//        }
//
//    }
//    else
//    {
//        if (score_2>score_3)
//        {
//            cout<< "第二只小猪最重，为："<< score_2 <<endl;
//        }
//        else
//        {
//            cout<< "第三只小猪最重，为："<< score_3 <<endl;
//        }
//    }

//    三目运算符，有返回值
//    创建a,b,c 。a，b做比较，大的就赋值给c
//    int a = 10;
//    int b = 20;
//    int c = 0;
//
////    a>b? c = a :c = b; //第一种
//    c = (a>b? a :b);  //第二种
//    cout << c << endl;

//    switch语句
//    缺点：只能判断整行，不能按范围，区间判断
//    优点：结构清晰，执行效率高
//    int score = 0;
//    cout<< "请输入分数(满分10分)" <<endl;
//    cin >> score;
//    switch (score)
//    {
//        case 10:
//            cout<< "这部电影真棒" <<endl;
//            break;
//        case 9:
//            cout<< "这部电影不错" <<endl;
//            break;
//        case 8:
//            cout<< "这部电影还行" <<endl;
//            break;
//        case 7:
//            cout<< "这部电影一般般" <<endl;
//            break;
//        default:
//            cout<< "这部电影很垃圾" <<endl;
//            break;
//    }

//    循环结构
//    添加随机数种子，利用当前系统时间生成随机数，防止每次随机数都一样
//    srand((unsigned)time(NULL));
//    int answer = rand()%100 +1;
//    cout<< answer <<endl;
//    int input = 0;
//    while
//    while (input != answer)
//    {
//        cout<< "请输入数字" <<endl;
//        cin >>input;
//        if (input == answer)
//        {
//            cout<< "恭喜，你猜对了" <<endl;
//            break;
//        }
//        else if (input < answer)
//        {
//            cout<< "你猜小了" <<endl;
//        }
//        else
//        {
//            cout<< "你猜大了" <<endl;
//        }
//
//    }

//    do while,先执行一次循环语句，再判断
//    int a = 0;
//    do
//    {
//        cout<< a <<endl;
//        a++;
//    }
//    while (a<10);

//    水仙花之数
//    int num = 100;
//    do
//    {
//        int a = 0;//获取个位数
//        int b = 0;//获取十位数
//        int c = 0;//获取百位数
//        a = num%10;
//        b = num/10%10;
//        c = num/100;
//        if (a*a*a + b*b*b + c*c*c == num)
//        {
//
//            cout <<num<<endl;
//        }
//        num++;
//    }while (num<1000);

//    for循环
//    for (int i = 0; i<10;i++)
//    {
//        cout << i << endl;
//    }

//    敲桌子，遇到7的倍数，十位有7，个位有7
//    for (int i = 1; i<=100;i++)
//    {
//        if (i%7==0||i%10 ==7 || i/10 ==7)
//        {
//            cout <<"i::"<<i<< "::敲桌子" << endl;
//        }
//    }

//    乘法表
//    for (int a =1;a<10;a++)
//    {
//        for (int b =1;b<=a;b++)
//        {
//            cout <<b<<"*"<<a<<"="<<a*b<<"\t";
//        }
//        cout << endl;
//    }

//    跳转语句：
//    break
//    for (int a =1;a<10;a++)
//    {
//        for (int b =1;b<10;b++)
//        {
//            if (b==5)
//            {
//                break;
//            }
//            cout <<"*";
//        }
//        cout << endl;
//    }

//    continue
//    for (int a =1;a<10;a++)
//    {
//        for (int b =1;b<=a;b++)
//        {
//            if (b==3)
//            {
//                continue;
//            }
//            cout <<b<<"*"<<a<<"="<<a*b<<"\t";
//        }
//        cout << endl;
//    }
//    for (int a =1;a<30;a++)
//    {
//        if (a%2!=0)
//        {
//            continue;
//        }
//        cout << a << endl;
//    }

//    goto
//    cout << "1：xxxxxx" << endl;
//    cout << "2：xxxxxx" << endl;
//    goto haha;
//    cout << "3：xxxxxx" << endl;
//    cout << "4：xxxxxx" << endl;
//    haha;
//    cout << "5：xxxxxx" << endl;
//    cout << "6：xxxxxx" << endl;


    return 0;

}
