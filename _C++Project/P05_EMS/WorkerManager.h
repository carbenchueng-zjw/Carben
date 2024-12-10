//
// Created by kabun  on 10/24/21.
//

#ifndef INC_3_CPP_WORKERMANAGER_H
#define INC_3_CPP_WORKERMANAGER_H

#endif //INC_3_CPP_WORKERMANAGER_H
#include <iostream>
#include <fstream>
#include "Worker.h"
#include "Employee.h"
#include "Manager.h"
#include "Boss.h"
//#include <string>
#pragma once
#define FILENAME "../P05_EMS/Empfile.txt"

using namespace std;

class WorkerManage
{
public:
    WorkerManage();
    //显示菜单
    void ShowMenu();
    //退出
    void ExitSystem();
    //保存文件
    void Save();
    //添加
    void AddEmp();
    //统计文件中的人数
    int GetEmpNum();
    //初始化员工
    void InitEmp();
    //判断文件是否为空
    bool m_File;
    //判断职工是否存在,如果存在就返回职工所在的数组的位置，否则返回-1
    int IsExist(int i);
    //显示员工
    void ShowEmp();
    //删除员工
    void DelEmp();
    //修改信息
    void ModEmp();
    //查找员工
    void FindEmp();
    //排序
    void SortEmp();

    void CleanFile();
    //记录职工人数
    int m_emp_num;

    Worker ** m_emparray;

    ~WorkerManage();
};