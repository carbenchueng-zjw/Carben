//
// Created by kabun  on 10/11/21.
//

#ifndef INC_3_CPP_P03_CIRCLE_H
#define INC_3_CPP_P03_CIRCLE_H
#include <iostream>
#include <string>
#include "P03_Piont.h"
#pragma once
using namespace std;

class CIRCLE
{
public:
    void Setr(int s_l=0);

    int Getr();

    void SetCenter(POINT center);

    POINT GetCenter();

private:
    int m_r=0;
    POINT m_center;
};

#endif //INC_3_CPP_P03_CIRCLE_H
