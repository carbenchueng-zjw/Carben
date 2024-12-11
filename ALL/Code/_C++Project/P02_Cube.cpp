//
// Created by kabun  on 10/10/21.
//

#include "P02_Cube.h"
#include <iostream>
#include <string>
using namespace std;

//创建立方体的类
//设计属性，行为
//获取立方体的面积，体积
//分别利用全局函数，成员函数判断两个立方体是否相等

class CUBE
{
public:
    void SetLong(int s_l=0)
    {
        c_long = s_l;
    }

    int GetLong()
    {
        return c_long;
    }
    void SetWidth(int s_w=0)
    {
        c_width = s_w;
    }

    int GetWidth()
    {
        return c_width;
    }

    void SetHigh(int s_h=0)
    {
        c_high = s_h;
    }

    int GetHigh()
    {
        return c_high;
    }
    //获取体积
    int CalvulaetV()
    {
        return c_long*c_width*c_high;
    }
    //获取表面积
    int CalvulaetS()
    {
        return 2*c_long*c_width+2*c_width*c_high+2*c_long*c_high;
    }

    bool IsSameByClass(CUBE &c)
    {
        if (c.GetHigh()==c_high &&
            c.GetLong()==c_long &&
            c.GetWidth()==c_width )
        {
            return true;
        }
        return false;
    }

private:
    int c_long=0;
    int c_width=0;
    int c_high=0;
};


//利用全局函数判断两个立方体是否相等
bool IsSame(CUBE &c1 ,CUBE &c2)
{
    if (c1.GetHigh()==c2.GetHigh() &&
        c1.GetLong()==c2.GetLong() &&
        c1.GetWidth()==c2.GetWidth() )
    {
        return true;
    }
    return false;
}

int main()
{
    CUBE C1;
    C1.SetLong(10);
    C1.SetWidth(10);
    C1.SetHigh(10);
    cout<<"立方体的表面积：："<< C1.CalvulaetS()<<endl;
    cout<<"立方体的体积：：" <<C1.CalvulaetV()<<endl;

    CUBE C2;
    C2.SetLong(10);
    C2.SetWidth(10);
    C2.SetHigh(11);
    //利用全局函数判断
    bool ret =  IsSame(C1,C2);
    if(ret)
    {
        cout << "C1,C2是相等的"<< endl;
    } else
    {
        cout << "C1,C2是bubububububu相等的"<< endl;
    }

    //利用成员函数判断
    ret = C1.IsSameByClass(C2);
    if(ret)
    {
        cout << "成员函数判断C1,C2是相等的"<< endl;
    } else
    {
        cout << "成员函数判断C1,C2是bubububububu相等的"<< endl;
    }


    return 0;
}