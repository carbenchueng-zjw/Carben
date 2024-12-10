//
// Created by kabun  on 10/14/21.
//

#include <iostream>
#include <string>
using namespace std;

//class BUILDING
//{
//    friend void GoodGay(BUILDING &build);
//public:
//    BUILDING()
//    {
//        m_stiiting_room = "客厅";
//        m_bed_room = "卧室";
//    }
//    string m_stiiting_room;
//
//private:
//
//    string m_bed_room;
//};
//
//void GoodGay(BUILDING &build)
//{
//    cout << build.m_bed_room <<endl;
//    cout << build.m_stiiting_room <<endl;
//}
//
//void  test01()
//{
//    BUILDING bbb;
//    GoodGay(bbb);
//}
//
//int main()
//{
//    test01();
//    return 0;
//}


//友元类
//class BUILDING;
//class GOODGAY
//{
//
//public:
//    GOODGAY();
//    void Visit();
//     BUILDING *bulid;
//};
//
//class BUILDING
//{
//    friend class GOODGAY;
//public:
//    BUILDING();
//
//    string m_stiiting_room;
//private:
//
//    string m_bed_room;
//};
////类外写成员函数
//BUILDING::BUILDING()
//{
//    m_stiiting_room = "客厅";
//    m_bed_room = "卧室";
//}
//GOODGAY::GOODGAY()
//{
//    bulid = new BUILDING;
//
//}
//
//void GOODGAY::Visit()
//{
//    cout<<"好基友类正在访问：："<< bulid->m_stiiting_room<<endl;
//    cout<<"好基友类正在访问：："<< bulid->m_bed_room<<endl;
//}
//
//void test01()
//{
//    GOODGAY gogay;
//    gogay.Visit();
//}
//
//int main()
//{
//    test01();
//    return 0;
//}


class BUILDING;
class GOODGAY
{

public:
    GOODGAY();
    void Visit01();//可以访问私有
    void Visit02(); //不能访问私有
    BUILDING *bulid;
};

class BUILDING
{
    friend void GOODGAY::Visit01();
public:
    BUILDING();

    string m_stiiting_room;
private:

    string m_bed_room;
};
//类外写成员函数
BUILDING::BUILDING()
{
    m_stiiting_room = "客厅";
    m_bed_room = "卧室";
}
GOODGAY::GOODGAY()
{
    bulid = new BUILDING;

}

void GOODGAY::Visit01()
{
    cout<<"好基友类正在访问：："<< bulid->m_stiiting_room<<endl;
    cout<<"好基友类正在访问：："<< bulid->m_bed_room<<endl;
}

void GOODGAY::Visit02()
{
    cout<<"好基友类正在访问：："<< bulid->m_stiiting_room<<endl;
//    cout<<"好基友类正在访问：："<< bulid->m_bed_room<<endl;
}

void test01()
{
    GOODGAY gogay;
    gogay.Visit01();
    gogay.Visit02();
}

int main()
{
    test01();
    return 0;
}
