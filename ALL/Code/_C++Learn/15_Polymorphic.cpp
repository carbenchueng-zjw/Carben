//
// Created by kabun  on 10/18/21.
//

#include <iostream>
#include <string>
using namespace std;

//class Animals
//{
//public:
//    virtual void speak()
//    {
//        cout << "动物在说话" << endl;
//    }
//};
//
//class Cat : public Animals
//{
//public:
//    void speak()
//    {
//        cout << "一起学喵叫！！！" << endl;
//    }
//};
////地址早绑定（在编译前决定函数地址，可以用晚绑定解决，父类变成虚函数）
//void DoSpeak(Animals &animals)
//{
//    animals.speak();
//}
//
//int main()
//{
//    Cat cat;
//    DoSpeak(cat);
//    return 0;
//}

//多肽计算器案例
//开闭原则：对扩展进行开放，对修改进行关闭
//class CALCULATOR
//{
//public:
//    int m_num1;
//    int m_num2;
//
//    virtual int GetResult()
//    {
//        return 0;
//    }
//};
////加法
//class AddCal:public CALCULATOR
//{
//public:
//    int GetResult()
//    {
//        return m_num1+m_num2;
//    }
//};
//class PlusCal:public CALCULATOR
//{
//public:
//    int GetResult()
//    {
//        return m_num1*m_num2;
//    }
//};
//
//void test()
//{
//    CALCULATOR *c = new PlusCal;
//    c->m_num1 = 10;
//    c->m_num2 = 20;
//    cout<< c->m_num1<<"*"<<c->m_num2<<"="<<c->GetResult()<<endl;
//    delete c;
//}
//
//int main()
//{
//    test();
//    return 0;
//}

//纯虚函数和抽象类
//class Base
//{
//public:
//    //纯虚函数，
//    virtual void func() = 0;
//
//};
//class Son:public Base
//{
//public:
//    void func()
//    {
//        cout << "ajskhdkjah"<<endl;
//    }
//
//};
//
//int main()
//{
//    Base *b = new Son;
//    b->func();
//
//    return 0;
//}

//虚析构，纯虚析构
class Animal
{
public:
    Animal()
    {
        cout << "Animal构造函数"<<endl;
    }
    //利用虚析构可以解决父类指针释放子类对象时不干净的问题
//    virtual ~Animal()
//    {
//        cout << "Animal析构函数"<<endl;
//    }
    virtual ~Animal()=0;//纯虚析构函数,需要函数实现，且这个类也属于抽象类，无法实例化
    virtual void speak()=0;

};
Animal::~Animal()
{
    cout << "Animal析构函数"<<endl;
}

class Cat :public Animal
{
public:
    string *m_name;
    Cat(string name)
    {
        cout << "cat构造函数"<<endl;
        m_name = new string (name);
    }
    void speak()
    {
        cout <<*m_name<< "小猫在说话"<<endl;
    }
    ~Cat()
    {
        if (m_name !=NULL)
        {
            cout << "cat析构函数"<<endl;
            delete m_name;
        }
    }
};
void test()
{
    Animal *a = new Cat("汤姆");
    a->speak();
    delete a;
}

int main()
{
    test();
    return 0;
}
























