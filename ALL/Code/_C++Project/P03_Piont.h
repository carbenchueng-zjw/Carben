//
// Created by kabun  on 10/11/21.
//
#pragma once
#ifndef INC_3_CPP_P03_PIONT_H
#define INC_3_CPP_P03_PIONT_H
#include <iostream>
#include <string>
#include <cmath>

using namespace std;

class POINT
{
public:
    void SetX(int s_l=0);

    int GetX();

    void SetY(int s_w=0);

    int GetY();

private:
    int m_x=0;
    int m_y=0;
};
#endif //INC_3_CPP_P03_PIONT_H
