//
// Created by kabun  on 10/11/21.
//
#pragma once
#include <iostream>
#include <string>
#include <cmath>
#include "P03_Circle.h"
#include "P03_Piont.h"

using namespace std;

//class POINT
//{
//public:
//    void SetX(int s_l=0)
//    {
//        m_x = s_l;
//    }
//
//    int GetX()
//    {
//        return m_x;
//    }
//    void SetY(int s_w=0)
//    {
//        m_y = s_w;
//    }
//
//    int GetY()
//    {
//        return m_y;
//    }
//
//private:
//    int m_x=0;
//    int m_y=0;
//};
//
//class CIRCLE
//{
//public:
//    void Setr(int s_l=0)
//    {
//        m_r = s_l;
//    }
//
//    int Getr()
//    {
//        return m_r;
//    }
//    void SetCenter(POINT center)
//    {
//        m_center = center;
//    }
//
//    POINT GetCenter()
//    {
//        return m_center;
//    }
//
//private:
//    int m_r=0;
//    POINT m_center;
//};

void IsInCenter(CIRCLE &c,POINT &p)
{
    double distance =
    pow(c.GetCenter().GetX() - p.GetX(),2)+
    pow(c.GetCenter().GetY() - p.GetY(),2);

    double r_distance = pow(c.Getr(),2);
    if (distance == r_distance)
    {
        cout<< "点在圆上" << endl;
    }
    else if (distance > r_distance)
    {
        cout<< "点在圆外" << endl;
    }
    else
    {
        cout<< "点在圆内" << endl;
    }
}

int main()
{
    //创建圆
    CIRCLE c;
    c.Setr(10);
    POINT center;
    center.SetX(10);
    center.SetY(0);
    c.SetCenter(center);
    POINT p;
    p.SetX(10);
    p.SetY(10);

    IsInCenter(c,p);


    return 0;
}




















