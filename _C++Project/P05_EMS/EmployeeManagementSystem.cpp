//
// Created by kabun  on 10/24/21.
//
//#include <string>
#include "WorkerManager.h"
#include "Worker.h"
#include "Employee.h"
#include "Boss.h"
#include "Manager.h"
#include <iostream>
using namespace std;


int main()
{
//    Worker *worker = NULL;
//    worker = new Employee(1,"张三",1);
//    worker->ShowInfo();
//    delete worker;
//
//    worker = new Manager(2,"asd",2);
//    worker->ShowInfo();
//    delete worker;
//
//    worker = new Boss(3,"1231312",3);
//    worker->ShowInfo();
//    delete worker;

    WorkerManage wm;

    int select = 0;
    //显示菜单
    while (true)
    {
        wm.ShowMenu();
        cout << "请输入你需要的功能"<<endl;
        cin >> select;
        switch (select) {
            case 1://添加联系人
                wm.AddEmp();
//                wm.Save();
                break;
            case 2://显示联系人
                wm.ShowEmp();
                break;
            case 3: //删除联系人
                wm.DelEmp();
//            {
//                int ret = wm.IsExist(5);
//                if (ret != -1) {
//                    cout << "存在" << endl;
//                } else {
//                    cout << "不存在" << endl;
//                }
//                break;
//            }
                break;
            case 4://修改联系人
                wm.ModEmp();
                break;
            case 5://查找联系人
                wm.FindEmp();
                break;
            case 6://排序
                wm.SortEmp();
                break;
            case 7://清空联系人
                wm.CleanFile();
                break;
            case 0://退出通讯录
                wm.ExitSystem();
                return 0;
            default:
//                system("clear");
                cout << "输入有误，请重新输入！！"<<endl;
        }
    }
}
