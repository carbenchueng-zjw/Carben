//
// Created by kabun  on 10/16/21.
//

#include <iostream>
#include <string>
using namespace std;
//继承：减少重复性的代码
//语法：class 子类 : 继承方式 父类
//继承中：先构造父类，然后子类，析构相反
//class BASEPAGE
//{
//public:
//    void func()
//    {
//        cout << "base学科视频" << endl;
//    }
//    int m_a;
//protected:
//    int m_b;
//private:
//    int m_c;
//};
//
//class SON :public BASEPAGE
//{
//public:
//    void func()
//    {
//        m_a = 10;
//        m_b = 20;
////        m_c = 20;//父类私有不能继承
//        cout << "son学科视频" <<endl;
//    }
//    int m_a;
//};
//class SON2 : protected BASEPAGE
//{
//public:
//    void func()
//    {
//        m_a = 10;
//        m_b = 20;
////        m_c = 20;//父类私有不能继承
////        cout << "son学科视频" <<endl;
//    }
//};
//class PYTHON:public BASEPAGE
//{
//public:
//    void Content()
//    {
//        cout << "python学科视频" <<endl;
//    }
//};
//
//void test01()
//{
//    SON s1;
//    s1.m_a = 100;
////    s1.m_b = 100;//保护权限，类外访问不了
//    cout << s1.m_a <<endl;//同名成员属性
//    cout << s1.BASEPAGE::m_a <<endl;//同名成员属性
//    //子类的同名成员函数会隐藏掉父类中所有的同名成员函数
//    // （包括重载的），要访问必须要加作用域
//    s1.func();
//    s1.BASEPAGE::func();
//
//    SON2 s2;
////    s2.m_a;//不能访问
//}
//int main()
//{
//    test01();
//    return 0;
//}

//静态成员属性
//静态成员函数
//class ASS
//{
//public:
//    static int m_a;
//    static void as()
//    {
//        cout << "父类父类" <<endl;
//    }
//};
//int ASS::m_a = 100;
//class BON: public ASS
//{
//public:
//    static int m_a;
//    static void as()
//    {
//        cout << "子类子类" <<endl;
//    }
//};
//int BON::m_a = 200;
//void test01()
//{
//    BON b;
//    cout << b.m_a<<endl;
//    cout << b.ASS::m_a<<endl;
//    //通过类名访问
//    cout << BON::m_a<<endl;
//    cout << BON::ASS::m_a<<endl;
//
//}
//void test02()
//{
//    BON b;
//    b.as();
//    b.ASS::as();
//    BON::ASS::as();
//}
//int main()
//{
////    test01();
//    test02();
//    return 0;
//}


//多继承
//class BASE01
//{
//public:
//    int m_b;
//    BASE01()
//    {
//        m_b=10;
//    }
//};
//class BASE02
//{
//public:
//    int m_b;
//    BASE02()
//    {
//        m_b=20;
//    }
//};
////语法
//class BASE03 : public BASE02, public BASE01
//{
//public:
//    int m_c;
//    int m_d;
//    BASE03()
//    {
//        m_c=30;
//        m_d=60;
//    }
//};
//
//void test()
//{
//    BASE03 b03;
//    cout << sizeof(b03)<<endl;
//    cout << b03.BASE01::m_b<<endl;
//    cout << b03.BASE02::m_b<<endl;
//}
//int main()
//{
//    test();
//    return 0;
//}

//菱形继承
//class Animal
//{
//public:
//    int m_age;
//
//};
////利用虚继承解决菱形继承问题：virtual
//class Sheep : virtual public Animal
//{
//
//};
//class Tuo : virtual public Animal
//{
//
//};
//class SheepTuo : public Sheep,public Tuo
//{
//
//};
//
//void test01()
//{
//    SheepTuo st;
//    st.Sheep::m_age=11;
//    st.Tuo::m_age=22;
//    //菱形继承，加作用域
//    cout << st.Sheep::m_age << endl;
//    cout << st.Tuo::m_age << endl;
//    cout << st.m_age << endl;
//}
//int main()
//{
//    test01();
//    return 0;
//}