//
// Created by kabun on 2021/11/22.
//

#include <algorithm>
#include <iostream>
#include <vector>
#include <ctime>
#include <map>
#include <string>
using namespace std;

#define CEHUA 0
#define MEISHU 1
#define YANFA 2

class Worker
{
public:
    string mname;
    int msalary;
//    Worker(string name,int salary)
//    {
//        mname = name;
//        msalary = salary;
//    }

};

void CreatWorker(vector<Worker> &vw)
{
    string name_seed = "ABCDEFGHIJ";
    for(int i=0;i<10;i++)
    {
        Worker worker;
        worker.mname = "员工： ";
        worker.mname += name_seed[i];

        worker.msalary = rand()%10001+10000;
        vw.push_back(worker);
    }
}

void SetGroup(vector<Worker> &v,multimap<int,Worker> &m)
{
    for(vector<Worker>::iterator it=v.begin();it!=v.end();it++)
    {
        //产生编号
        int dep_id = rand()% 3;
        //插入编号
        m.insert(make_pair(dep_id,*it));
    }
}

void ShowWorker(multimap<int,Worker> &mw)
{
    cout<< "策划部门：" <<endl;
    multimap<int,Worker>::iterator pos = mw.find(CEHUA);
//    for(multimap<int,Worker>::iterator it=mw.begin();it!=mw.end();it++)
    int count = mw.count(CEHUA);
    int index = 0;
    for(; pos!=mw.end()&& index<count;pos++,index++)
    {
        cout << pos->second.mname
        <<"  工资： "<<pos->second.msalary<<endl;
    }

    cout<< "美术部门：" <<endl;
    pos = mw.find(MEISHU);
//    for(multimap<int,Worker>::iterator it=mw.begin();it!=mw.end();it++)
    count = mw.count(MEISHU);
    index = 0;
    for(; pos!=mw.end()&& index<count;pos++,index++)
    {
        cout << pos->second.mname
             <<"  工资： "<<pos->second.msalary<<endl;
    }

    cout<< "研发部门：" <<endl;
    pos = mw.find(YANFA);
//    for(multimap<int,Worker>::iterator it=mw.begin();it!=mw.end();it++)
    count = mw.count(YANFA);
    index = 0;
    for(; pos!=mw.end()&& index<count;pos++,index++)
    {
        cout << pos->second.mname
             <<"  工资： "<<pos->second.msalary<<endl;
    }
}

int main()
{
    srand((unsigned int)time(NULL));
    vector<Worker> vWorker;
    //创建员工
    CreatWorker(vWorker);
//    for(vector<Worker>::iterator it=vWorker.begin();it!=vWorker.end();it++)
//    {
//        cout << it->mname<<"  工资： "<<it->msalary<<endl;
//    }
    //员工分组
    multimap<int,Worker> mWorker;
    SetGroup(vWorker,mWorker);

    //分组显示员工
    ShowWorker(mWorker);

//    cin.get();
    return 0;
}