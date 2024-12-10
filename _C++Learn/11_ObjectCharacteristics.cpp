//
// Created by kabun  on 10/12/21.
//

#include <iostream>
#include <string>
using namespace std;


//对象的初始化和清理
//1：构造函数进行初始化操作
//class Person
//{
//public:
////    1.1构造函数（
////    没有返回值，不用写viod，
////    函数名与类名相同，可以有参数,可以重载，
////    创建对象的时候自动调用且只调用一次）
//
//    Person()
//    {
//        cout << "无参（默认）构造函数的调用" << endl;
//    }
//
//    Person(int a)
//    {
//        age= a ;
//        cout << "有参构造函数的调用" << endl;
//    }
//    //拷贝构造函数
//    Person(const Person &p)
//    {
//        age =p.age;//将传入的人身上的所有属性拷贝到我的身上
//        cout << "拷贝构造函数的调用" << endl;
//    }
//
//
////2：析构函数进行清理操作
////    2.1析构函数（
////    没有返回值，不用写viod，
////    函数名与类名相同且在左边加上～，~xxx()
////    不可以有参数,不可以重载，
////    销毁对象前自动调用且只调用一次）
//    ~Person()
//    {
//        cout << "构造函数的调用" << endl;
//    }
//
//    int age=0;
//};
//
////调用：
//void test()
//{
////    括号法
//    Person p(10);
//    Person pp(p);//拷贝构造函数的调用
//
//    //注意1:调用默认构造函数的时候不要加()
//    cout << p.age << endl;
//    cout << pp.age << endl;
//
////    显示法
//    Person p1;
//    Person p2 = Person(20);//有参构造函数的调用
//    Person p3 = Person(p2);//拷贝构造函数的调用
////    Person(20);//匿名对象，当前行执行结束后，系统会立即回收它
//
//    //注意2:不要利用拷贝函数来初始化匿名对象
//
//    //    隐士转换法
//    Person p4 =10;// Person p4 = Person(10)
//    Person p5 =p4;// //拷贝构造函数的调用
//
//}
//
//int main()
//{
//
////    Person p;
////    string name;
////    cin>> name;
////    cout << name << endl;
//
//    test();
//
//    return 0;
//}


//拷贝构造函数的调用时机
//class Person
//{
//public:
//
//    Person()
//    {
//        cout << "无参（默认）构造函数的调用" << endl;
//    }
//
//    Person(int a)
//    {
//        age= a ;
//        cout << "有参构造函数的调用" << endl;
//    }
//    //拷贝构造函数
//    Person(const Person &p)
//    {
//        age =p.age;//将传入的人身上的所有属性拷贝到我的身上
//        cout << "拷贝构造函数的调用" << endl;
//    }
//
//    ~Person()
//    {
//        cout << "构造函数的调用" << endl;
//    }
//
//    int age=0;
//};
////1：使用一个已经创建完毕的对象来初始化一个新对象
//void test01()
//{
//    Person p1(20);
//    Person p2(p1);
//    cout << "p2的年龄为：："<<p2.age<<endl;
//}
////2：值传递的方式给函数参数传值
//void DoWork(Person p)
//{
////    Person p1(20);
////    Person p2(p1);
////    cout << "p2的年龄为：："<<p2.age<<endl;
//}
//void test02()
//{
//    Person p1;
//    DoWork(p1);
//}
//
////3：值的方式返回局部对象
//Person DoWork2()
//{
//    Person p1;
//    cout << (int*)&p1 <<endl;
//    return p1;
//}
//void test03()
//{
//    Person p=DoWork2();
//    cout << (int*)&p <<endl;
//}
//
//int main()
//{
////    test01();
////    test02();
//    test03();
//    return 0;
//}

//拷贝构造函数的调用规则

//1：只要创建了一个类，c++就会给每个类添加至少3个函数
//默认构造（空实现）
//析构函数（空实现）
//拷贝构造（值拷贝）

//2:如果我们写了有参构造函数，编译器就不再提供默认构造函数，但会依然提供拷贝构造函数
//class Person
//{
//public:
//
////    Person()
////    {
////        cout << "无参（默认）构造函数的调用" << endl;
////    }
//
////    Person(int a)
////    {
////        age= a ;
////        cout << "有参构造函数的调用" << endl;
////    }
////    //拷贝构造函数
//    Person(const Person &p)
//    {
//        age =p.age;//将传入的人身上的所有属性拷贝到我的身上
//        cout << "拷贝构造函数的调用" << endl;
//    }
//
//    ~Person()
//    {
//        cout << "构造函数的调用" << endl;
//    }
//
//    int age=0;
//};
////1：只要创建了一个类，c++就会给每个类添加至少3个函数
////void test01()
////{
////    Person p1;
////    p1.age =18;
////    Person p2(p1);
////}
//
////2:如果我们写了有参构造函数，编译器就不再提供默认构造函数，但会依然提供拷贝构造函数
////2:如果我们写了拷贝构造函数，编译器就不再提供其他构造函数
//void test02()
//{
//    Person p1;
////    p1.age =18;
////    Person p2(p1);
//
//}
//int main()
//{
////    test01();
//    test02();
////    test03();
//    return 0;
//}

//深拷贝，浅拷贝
//拷浅贝容易产生堆区的内存重复释放，要用深拷贝来解决
//class Person
//{
//public:
//
//    Person()
//    {
//        cout << "无参（默认）构造函数的调用" << endl;
//    }
//
//    Person(int a,int hhigg)
//    {
//        age= a ;
//        high = new int(hhigg);
//        cout << "有参构造函数的调用" << endl;
//    }
//    //拷贝构造函数
//    Person(const Person &p)
//    {
//        age =p.age;//将传入的人身上的所有属性拷贝到我的身上
//        //深拷贝
//        high = new int(*p.high);
//        cout << "拷贝构造函数的调用" << endl;
//    }
//
//    ~Person()
//    {
//        //析构函数将堆区开辟的数据做释放操作
//        if (high!=NULL)
//        {
//            delete high;
//            high =NULL;
//        }
//        cout << "构造函数的调用" << endl;
//    }
//
//    int age=0;
//    int *high;
//};
//
//void test01()
//{
//    Person p1(22,160);
//    cout << p1.age <<*p1.high<< endl;
//
//    Person p2(p1);
//    cout << p2.age << *p2.high<< endl;
//}
//
//int main()
//{
//    test01();
//    return 0;
//}


//初始化列表
//class Person
//{
//public:
//    int m_a;
//    int m_b;
//    int m_c;
//    //初始化列表的属性
//    Person(int a,int b,int c):m_a(a),m_b(b),m_c(c)
//    {
//
//    }
//
////    Person(int a,int b,int c)
////    {
////        m_a = a;
////        m_b = b;
////        m_c = c;
////    }
//};
//
//void test01()
//{
//    Person p(22,11,33);
//    cout << "m_a = a::" <<p.m_a<< endl;
//    cout << "m_b = b::" <<p.m_b<< endl;
//    cout << "m_c = c::" <<p.m_c<< endl;
//
//}
//
//int main()
//{
//    test01();
//    return 0;
//}

//类对象作为成员类
//当其他类对象作为类成员，会先构造类对象再构造自身，析构函数相反
//class PHONE
//{
//public:
//    PHONE(string name):m_pname(name)
//    {
//        cout <<"PHONE的构造"<<endl;
//    }
//    ~PHONE()
//    {
//        cout <<"PHONE®的析构函数"<<endl;
//    }
//
//    string m_pname;
//};
//
//class PERSON
//{
//public:
//    PERSON(string name,string pname):m_name(name),m_phone(pname)
//    {
//        cout <<"PERSON的构造"<<endl;
//    }
//    ~PERSON()
//    {
//        cout <<"PERSON的析构函数"<<endl;
//    }
//
//    string m_name;
//    PHONE m_phone;
//};
//
//void test01()
//{
//    PERSON p("张三","华为PRO");
//    cout << p.m_name<< "ahahahah"<<endl;
//    cout << p.m_phone.m_pname<< "ahahahah"<<endl;
//}
//
//
//int main()
//{
//    test01();
//    return 0;
//}

//静态成员函数
//所有对象共享同一个函数
//静态成员函数只能访问静态成员变量
//成员变量和成员函数分开存储
//class PERSON
//{
//public:
//    //静态函数
//    static void func()
//    {
//        m_a = 10;
////        m_b = 100;//静态成员函数不能访问非静态成员变量
//        cout << "static void func()" <<endl;
//    }
//    static int m_a;//静态成员变量
//    int m_b = 200;
//};
//int PERSON::m_a = 0;
//class TTTT
//{
//};
//void test01()
//{
////    第一种调用
//    PERSON p;
//    TTTT t;//空对象占用空间为1，每个对象都有独立的内存位置和地址
//    cout<< sizeof(t) <<endl;
//    cout<< sizeof(p) <<endl;//因为静态成员变量，函数都不属于类上的
//    p.func();
////    第二种调用
//    PERSON::func();
//}
//int main()
//{
//    test01();
//    return 0;
//}

//this指针
//class PERSON
//{
//public:
//    PERSON(int age)
//    {
////        this指向被调用的成员函数所属的对象
//        this->age = age;
//    }
//    PERSON &PersonAdd(PERSON &p)
//    {
//        this->age += p.age;
//        return *this;
//    }
//    int age;
//};
//
////1：解决名称冲突
//void test01()
//{
//    PERSON p1(20);
//    cout << p1.age <<endl;
//}
////2：返回对象本身用*this
//void test02()
//{
//    PERSON p1(20);
//    PERSON p2(20);
//    PERSON *p = NULL;
//
//    //链式编程思想
//    p2.PersonAdd(p1).PersonAdd(p1).PersonAdd(p1);
//    cout << p2.age << endl;
//}
//int main()
//{
//    test01();
//    test02();
//    return 0;
//}

//常函数
//class PERSON
//{
//public:
////    在成员函数后面加const 修饰的是this指针，值和指向都不能修改
////    const PERSON *const this;
//    void haha() const
//    {
//        this->agee = 200;
////        age = 100; //报错
//    }
//    void hahaa()
//    {
//        this->agee = 200;
////        age = 100; //报错
//    }
//
//    int age;
//    mutable int agee;//特殊变量
//};
//void test()
//{
//    //常对象
//    const PERSON p1;
//    p1.hahaa();//报错，因为常对象只能调用常函数
//    p1.age = 300;
//    p1.agee = 300;
}

