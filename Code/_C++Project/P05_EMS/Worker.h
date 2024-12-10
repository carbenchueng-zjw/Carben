//
// Created by kabun  on 10/25/21.
//

#ifndef INC_3_CPP_WORKER_H
#define INC_3_CPP_WORKER_H

#endif //INC_3_CPP_WORKER_H
#include <iostream>
#pragma once
using namespace std;


class Worker
{
public:
//    职工编号
    int m_id;
//    职工姓名
    string m_name;
//    职工部门
    int m_dep_id;
//    显示个人信息
    virtual void ShowInfo()=0;

    virtual string GetDeptName() = 0;

};
