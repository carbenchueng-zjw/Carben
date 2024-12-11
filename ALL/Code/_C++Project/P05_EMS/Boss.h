//
// Created by kabun  on 10/25/21.
//

#ifndef INC_3_CPP_BOSS_H
#define INC_3_CPP_BOSS_H

#endif //INC_3_CPP_BOSS_H
#include <iostream>
#include "Worker.h"
#pragma once
using namespace std;

class Boss:public Worker
{
public:
    Boss(int id, string name, int did);

    void ShowInfo();

    string GetDeptName();
};