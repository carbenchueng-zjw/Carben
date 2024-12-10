//
// Created by kabun  on 10/9/21.
//

#include <iostream>
#include <string>
using namespace std;

struct c2//默认公共访问权限
{
    int m_a;
};

class CIRCLE//默认私有访问权限
{

public://公共权限
    //属性
    int r=0;
    float pi=0;
    //行为
    double CalculateZC()
    {
        int a = 3;
        return 2*pi*r;
    }

};

//设置私有的成员属性
class STUDENT
{
private://
    int id =0;
    int age =12;
public://可读可写
    string name;
//    void PrintStudent(int id=0,string name)
    void PrintStudent()
    {
        cout <<"学生的学号：："<< id << endl <<"学生的姓名：："<<name<<endl;
    }

    //给姓名赋值
    void SetName(string new_name)
    {
        name = new_name;
    }

    string GetName()
    {
        return name;
    }

    int GetAge()//只读
    {
        return age;
    }
    int SetLover(string words)//只写
    {
        string my_words = words;
    }
};

int main()
{
    //实例化
    CIRCLE c1;
    STUDENT s1;
    c1.r=5;
    c1.pi=3.14;
//    cout << c1.CalculateZC()<<endl;

//    s1.id=100;//私有访问不了
    s1.name="积极";
    cout <<s1.GetName() <<endl;
    cout <<s1.GetAge() <<endl;
    s1.SetLover("优月");
//    cout <<s1.SetLover() <<endl;//报错，没有读取的权限
//    s1.PrintStudent();
//    s1.SetName("飞飞");
//    s1.PrintStudent();

    return 0;
}