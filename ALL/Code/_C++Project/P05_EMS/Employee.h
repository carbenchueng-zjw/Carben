//
// Created by kabun  on 10/25/21.
//

#ifndef INC_3_CPP_EMPLOYEE_H
#define INC_3_CPP_EMPLOYEE_H

#endif //INC_3_CPP_EMPLOYEE_H
//普通员工的文件
#include <iostream>
#include "Worker.h"
#pragma once
using namespace std;

class Employee:public Worker
{
public:
    Employee(int id, string name, int did);

    void ShowInfo();

    string GetDeptName();

};

