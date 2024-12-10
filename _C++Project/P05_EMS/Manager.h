//
// Created by kabun  on 10/25/21.
//

#ifndef INC_3_CPP_MANAGER_H
#define INC_3_CPP_MANAGER_H

#endif //INC_3_CPP_MANAGER_H
#include <iostream>
#include "Worker.h"
#pragma once
using namespace std;

class Manager:public Worker
{
public:
    Manager(int id, string name, int did);

    void ShowInfo();

    string GetDeptName();
};