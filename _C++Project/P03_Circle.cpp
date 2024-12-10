//
// Created by kabun  on 10/11/21.
//

#include "P03_Circle.h"
#include <iostream>
#include <string>
#include <cmath>

using namespace std;


void CIRCLE::Setr(int s_l)
{
    m_r = s_l;
}

int CIRCLE::Getr()
{
    return m_r;
}
void CIRCLE::SetCenter(POINT center)
{
    m_center = center;
}

POINT CIRCLE::GetCenter()
{
    return m_center;
}