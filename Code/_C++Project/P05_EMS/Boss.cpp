//
// Created by kabun  on 10/25/21.
//

#include "Boss.h"
Boss::Boss(int id, string name, int did){
    this->m_id = id;
    this->m_dep_id = did;
    this->m_name = name;
}

void Boss::ShowInfo()
{
    cout << "职工编号：\t"<< this->m_id<<endl;
    cout << "职工岗位：\t"<< this->GetDeptName()<<endl;
    cout << "职工姓名：\t"<< this->m_name<<endl;
    cout << "职责：\t\t管理公司所有事务 " <<endl;
}

string Boss::GetDeptName()
{
    return string("总裁");
}