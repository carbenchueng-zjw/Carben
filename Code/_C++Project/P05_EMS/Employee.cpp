//
// Created by kabun  on 10/25/21.
//

#include "Employee.h"

Employee::Employee(int id, string name, int did)
{
    this->m_id = id;
    this->m_dep_id = did;
    this->m_name = name;
}

void Employee::ShowInfo()
{
    cout << "职工编号：\t"<< this->m_id<<endl;
    cout << "职工岗位：\t"<< this->GetDeptName()<<endl;
    cout << "职工姓名：\t"<< this->m_name<<endl;
    cout << "职责：\t\t完成经理交给的任务" <<endl;
}

string Employee::GetDeptName()
{
    return string("普通员工");
}
