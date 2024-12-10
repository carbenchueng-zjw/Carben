//
// Created by kabun  on 10/28/21.
//

#include <iostream>
#include "01_person.hpp"
using namespace std;

//template <typename t>//声明一个模版，t是一个通用的数据类型
//void ssswap(t &a ,t &b)
//{
//    t temp = a;
//    a = b;
//    b=temp;
//}
//void test()
//{
//    int a = 10;
//    double c = 0.3;
//    double d = 0.2;
//    int b = 20;
//
//    //第一种模版使用方法：自动类型推导
////    ssswap(a,b);
//    ssswap(c,d);
//    //第二种模版使用方法：指定类型
////    ssswap<int>(a,b);
//
//    cout << a<< "\t"<< b <<endl;
//    cout << c<< "\t"<< d<<endl;
//}
//template <typename s>
//void func()
//{
//    cout << "asdasdasd" <<endl;
//}
//
//template <typename s>
//void MySort(s arr[],int len)
//{
//    for(int i=0; i<len;i++)
//    {
//        int max =i;
//        for(int j=0; j<i+1;j++)
//        {
//            if(arr[max]<arr[j])
//            {
//                max = j;
//            }
//        }
//        if(max != i)
//        {
//            ssswap(arr[max],arr[i]);
//
//        }
//    }
//}
//
//void testO()
//{
//    char char_arr[] = "badcfe";
//    int num = sizeof(char_arr)/sizeof(char);
//    cout << num << endl;
////    int char_arr[] = {5,2,3,4,7,13,12,10,11};
////    int num = sizeof(char_arr)/sizeof(int);
//    MySort(char_arr,num);
//
//    for(int i=0; i<num;i++)
//    {
//        cout << char_arr[i]<<"  ";
//    }
//    cout<< endl;
//}
//
//int main()
//{
////    test();
//    testO();
////    func<int>();
//    return 0;
//}


//普通函数可以发生隐式类型转换，模版函数要指定类型才可以
//int Add(int a,int b)
//{
//    return a+b;
//}
//template <typename T>
//T Add02(T a,T b)
//{
//    return a+b;
//}
//
//int main()
//{
//    int a =3;
//    char s[] = "c";
////    int num = Add(a,s);
////    cout << num <<endl;
//    cout << Add02<int>(1,s) <<endl;
//    return 0;
//}


//int Add(int a,int b)
//void Add(int a,int b)
//{
//    cout << "不是模版" <<endl;
//}
//
//template <typename T>
//void Add(T a,T b)
//{
//    cout << "模版" <<endl;
//}
//
//class Person
//{
//public:
//    int age;
//    string name;
//    Person(string n,int a)
//    {
//        age = a;
//        name = n;
//    }
//};
//
//template <typename T>
//bool MyCompare(T &a,T &b)
//{
//    if(a==b)
//    {
//        return true;
//    }
//    else
//    {
//        return false;
//    }
//}

//利用具体化Person版本来实现代码，具体化有先调用
//template <> bool MyCompare(Person &a,Person &b)
//{
//    if(a.name==b.name)
//    {
//        return true;
//    }
//    else
//    {
//        return false;
//    }
//}
//
//int main()
//{
//    int a =3;
//    int b =2;
////    Add(a,b);
//
////    通过空模版参数列表，强制调用函数模版
////    Add<>(a,b);
//
//    Person p1("tom",10);
//    Person p2("tomm",10);
//    bool ret = MyCompare(p1,p2);
//    if(ret)
//    {
//        cout << "p1==p2"<<endl;
//    }
//    else
//    {
//        cout << "p1xxxxxxp2"<<endl;
//    }
//    return 0;
//}


//类模版:没有自动类型推导,但是可以有默认参数类型
//template <class name_type,class age_type=int>
////template <class name_type,class age_type>
//class Person
//{
//public:
//    age_type age;
//    name_type name;
//    Person(name_type n,age_type a)
//    {
//        this->age = a;
//        this->name = n;
//    }
//
//    void showow()
//    {
//        cout << this->name << this->age << endl;
//    }
//};
//
//int main()
//{
////    Person P("asd",100);//错误的，因为类模版不能自动推导
//    Person<string,int> p1("asdasd",11);
//    p1.showow();
//
//    Person<string> p2("11111",22);
//    p2.showow();
//    return 0;
//}


//类模版和函数模版的函数创建时机
//class Person1
//{
//public:
//    void show1()
//    {
//        cout << "z1z1z1z1z1z1"<<endl;
//    }
//};
//class Person2
//{
//public:
//    void show2()
//    {
//        cout << "x2x2x2x2x2x2"<<endl;
//    }
//};
//template <class T>
//class Myclass
//{
//public:
//    T ooo;
//    void func1()
//    {
//        ooo.show1();
//    }
//    void func2()
//    {
//        ooo.show2();
//    }
//};
//
//int main()
//{
//    Myclass<Person1> m;
//    m.func1();
////    m.func2();
//    return 0;
//}


//类模版做函数参数
//template <class name_type,class age_type>
//class Person
//{
//public:
//    age_type age;
//    name_type name;
//    Person(name_type n,age_type a)
//    {
//        this->age = a;
//        this->name = n;
//    }
//
//    void showow()
//    {
//        cout << this->name << this->age << endl;
//    }
//};
//
////1：指定传入类型(最常用，可读性高)
//void PrintPerson(Person<string,int> &p1)
//{
//    p1.showow();
//}
//void test01()
//{
//    Person<string,int> p1("asd",1);
//    PrintPerson(p1);
//}
//
////2：参数模版化
//template <class T1,class T2>
//void PrintPerson2(Person<T1,T2> &p1)
//{
//    p1.showow();
//    cout <<"T1的类型："<< typeid(T1).name()<<endl;
//    cout <<"T2的类型："<< typeid(T2).name()<<endl;
//}
//void test02()
//{
//    Person<string,int> p2("zhuzhuzhuz",99);
//    PrintPerson2(p2);
//}
//
////3：整个类模版化
//template <class T>
//void PrintPerson3(T &p1)
//{
//    p1.showow();
//    cout <<"T的类型："<< typeid(T).name()<<endl;
//
//}
//void test03()
//{
//    Person<string,int> p3("tangsengsss",33);
//    PrintPerson3(p3);
//}
//
//int main()
//{
////    test01();
////    test02();
//    test03();
//    return 0;
//}


//类模版继承
//template <class T1,class T2>
//class Base
//{
//public:
//    T1 m_name;
//    T2 m_age;
//    Base(T1 name,T2 age);
//
//    void show_per();
//};
//
//template <class T1,class T2>
////class Sonn : public Base//必须要指定父类的数据类型才能继承
//class Sonn : public Base<T1,T2>
//{
//public:
//    Sonn(T1 name,T2 age)
//    {
////        cout << typeid(T1).name()<<endl;
////        cout << typeid(T2).name()<<endl;
//    }
//    void ShowPerson();
//    T1 m_name;
//    T2 m_age;
//};
//
//template <class T1,class T2>
//class Son
//{
//public:
//    Son(T1 name,T2 age)
//    {
////        this->m_name = name;
////        this->m_age = age;
//    }
//    void ShowPerson()
//    {
////        cout << m_name<<endl<<m_age<<endl;
//    }
//    T1 m_name;
//    T2 m_age;
//};
//
////构造函数的类外实现
//template <class T1,class T2>
//Base<T1,T2>::Base(T1 name,T2 age)
//{
//    this->m_name = name;
//    this->m_age = age;
//}
//template <class T1,class T2>
//void Base<T1,T2>::show_per()
//{
//    cout << m_name<<endl<<m_age<<endl;
//}
//
//int main()
//{
//    Base<string,int> b("asdasd",22);
//    b.show_per();
//
//    return 0;
//}


//person的份文件编写，两种解决方法：1：包含cpp文件#include "person.cpp"，
// 2：（常用）把cpp和h文件的内容写到一起，然后包含改为.hpp

//int main()
//{
//    Person<string,int> P("asd",11);
//    P.show_person();
//
//    return 0;
//}


//分文件编写和友元（建议类内实现）
template <class T>
class Personn;
//全局函数，类外实现,要写在友元的前面，然后类要加模版和声明
template <class T>
void ShowP2(Personn<T> p)
{
    cout << p.m_name<<endl;
}

template <class T>
class Personn
{
//    //全局函数，类内实现
//    friend void ShowP(Personn<T> p)
//    {
//        cout << p.m_name<<endl;
//    }
    //全局函数，类外实现:需要躺编译器提前知道这个函数的存在
    friend void ShowP2<>(Personn<T> p);
public:

    Personn(T name)
    {
        this->m_name = name;
    }

private:
    T m_name;
};


int main()
{
    Personn<string> p("asd");
//    ShowP(p);
    ShowP2(p);

    return 0;
}

