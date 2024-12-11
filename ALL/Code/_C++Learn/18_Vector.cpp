//
// Created by kabun  on 11/4/21.
//

#include <iostream>
#include <vector>
//#include <string>
#include <algorithm>//标准算法的头文件
using namespace std;

//void pr(int val)
//{
//    cout << val << endl;
//}
//
//void test01()
//{
//    vector<int> v;
//    v.push_back(10);
//    v.push_back(20);
//    v.push_back(30);
    //起始迭代器，指向容器中第一个内容
    //第一种
//    vector<int>::iterator itbe = v.begin();
//    vector<int>::iterator iten = v.end();
//
//    while (itbe!=iten)
//    {
//        cout << *itbe << endl;
//        itbe++;
//    }

//第二种
//    for(vector<int>::iterator itbe = v.begin();itbe!=v.end();itbe++)
//    {
//            cout << *itbe << endl;
//    }

    //第三种
//    for_each(v.begin(),v.end(),pr);
//}

//int main()
//{
//    test01();
//    return 0;
//}


//自定义数据类型
//class Person
//{
//public:
//    string m_name;
//    int m_val;
//
//    Person(string na,int i)
//    {
//        this->m_name = na;
//        this->m_val = i;
//    }
//};
//
//void test()
//{
//    vector<Person> v;
//    Person p1("asd",10);
//    Person p2("bbb",20);
//    Person p3("ccc",30);
//
//    v.push_back(p1);
//    v.push_back(p2);
//    v.push_back(p3);
//
//    for(vector<Person>::iterator it = v.begin();it!=v.end();it++)
//    {
//        cout << "姓名：："<<it->m_name <<
//        "   年龄：："<< it->m_val <<endl;
//    }
//}
//
////存放自定义类型 指针
//void test01()
//{
//    vector<Person*> v;
//    Person p1("asd",10);
//    Person p2("bbb",20);
//    Person p3("ccc",30);
//
//    v.push_back(&p1);
//    v.push_back(&p2);
//    v.push_back(&p3);
//
//    for(vector<Person*>::iterator it = v.begin();it!=v.end();it++)
//    {
//        cout << "姓名：："<<(*it)->m_name <<
//             "   年龄：："<<(*it)->m_val <<endl;
//    }
//}
//
//int main()
//{
//
////    test();
//    test01();
//    return 0;
//}


////容器嵌套容器
//void test()
//{
//    vector<vector<int>> v;
//    vector<int> v1;
//    vector<int> v2;
//    vector<int> v3;
//
//    for(int i =0;i<3;i++)
//    {
//        v1.push_back(i+1);
//        v2.push_back(i+2);
//        v3.push_back(i+3);
//    }
//    v.push_back(v1);
//    v.push_back(v2);
//    v.push_back(v3);
//    for(vector<vector<int>>::iterator it = v.begin();it!=v.end();it++)
//    {
//        for(vector<int>::iterator vit = (*it).begin();vit!=(*it).end();vit++)
//        {
//            cout <<(*vit)<< "\t";
//        }
//        cout<<endl;
//    }
//}
//
//int main()
//{
//
//    test();
////    test01();
//    return 0;
//}