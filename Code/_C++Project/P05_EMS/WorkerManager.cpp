//
// Created by kabun  on 10/24/21.
//

#include "WorkerManager.h"

WorkerManage::WorkerManage()
{
    //文件不存在
    ifstream ifs;
    ifs.open(FILENAME,ios::in);
    if (!ifs.is_open())
    {
        cout<< "文件不存在" <<endl;
        this->m_emp_num=0;//初始化人数
        this->m_emparray=NULL;//初始化指针
        this->m_File= true;
        ifs.close();
        return;
    }

//    文件存在，数据为空
    char ch;
    ifs>>ch;
    if(ifs.eof())
    {
        //读完文件
        cout<< "文件为空" <<endl;
        this->m_emp_num=0;//初始化人数
        this->m_emparray=NULL;//初始化指针
        this->m_File= true;
        ifs.close();
        return;
    }
    //文件存在 记录数据
    int num = this->GetEmpNum();
    cout << "职工人数是：" <<num<< endl;
    this->m_emp_num=num;
    //开辟空间
    this->m_emparray = new Worker*[this->m_emp_num];
    //将文件中的数据，存到数组中
    this->InitEmp();
    //测试代码
//    for(int i =0;i<this->m_emp_num;i++)
//    {
//        cout <<this->m_emparray[i]->m_id
//        <<this->m_emparray[i]->m_name
//        <<this->m_emparray[i]->m_dep_id<<endl;
//    }
}

void WorkerManage::ShowMenu()
{
    cout<< "********************" <<endl;
    cout<< "*******欢迎使用******" <<endl;
    cout<< "****1:增加职工信息****" <<endl;
    cout<< "****2:显示职工信息****" <<endl;
    cout<< "****3:删除职工信息****" <<endl;
    cout<< "****4:修改职工信息****" <<endl;
    cout<< "****5:查找职工信息****" <<endl;
    cout<< "****6:按照编号排序****" <<endl;
    cout<< "****7:清空所有文档****" <<endl;
    cout<< "********************" <<endl;

}

void WorkerManage::ExitSystem()
{
    cout << "感谢使用，祝您生活愉快！！"<<endl;

    exit(0);
}

void WorkerManage::AddEmp()
{
    cout << "请输入添加职工的数量！！"<<endl;
    int add_num = 0;
    cin>>add_num;
    if(add_num>0)
    {
        //计算新空间的人数
        int newSize = this->m_emp_num+add_num;
        //开辟新空间
        Worker ** newSpace=  new Worker*[newSize];
        //
        if(this->m_emparray!=NULL)
        {
            for (int i ; i<this->m_emp_num;i++)
            {
                newSpace[i] = this->m_emparray[i];
            }
        }
        //批量添加数据
        for (int i ; i<add_num;i++)
        {
            int m_id;
            string m_name;
            int m_dep_id;

            cout << "请输入第"<<i+1<<"个新职工编号" << endl;
            cin>>m_id;
            cout << "请输入第"<<i+1<<"个新职工姓名" << endl;
            cin>>m_name;
            cout << "请输入第"<<i+1<<"个新职工部门" << endl;
            cout << "1：员工" << endl;
            cout << "2：经理" << endl;
            cout << "3：老板" << endl;
            cin>>m_dep_id;

            Worker *worker = NULL;
            switch (m_dep_id)
            {
                case 1:
                    worker = new Employee(m_id,m_name,1);
                    break;
                case 2:
                    worker = new Manager(m_id,m_name,2);
                    break;
                case 3:
                    worker = new Boss(m_id,m_name,3);
                    break;
                default:
                    break;
            }
            //将职工的指针保存到数组中
            newSpace[this->m_emp_num+i] = worker;
        }
        //释放原有空间
        delete[] this->m_emparray;
        //更改新空间
        this->m_emparray = newSpace;
        //更新职工人数
        this->m_emp_num = newSize;
        //成功添加后，保存到文件中
        this->Save();
        //更新职工不为空
        this->m_File= false;
        //提示添加成功
        cout <<"成功添加"<<add_num<<"名新职工" <<endl;

    } else
    {
        cout << "输入有误，请重新输入！！"<<endl;
    }
}

void WorkerManage::Save()
{
    ofstream ofs;
    ofs.open(FILENAME,ios::out);

    for(int i=0; i<this->m_emp_num;i++)
    {
        ofs << this->m_emparray[i]->m_id <<" "
            << this->m_emparray[i]->m_name <<" "
            << this->m_emparray[i]->m_dep_id <<" "<<endl;
    }
    ofs.close();
}

int WorkerManage::GetEmpNum()
{
    ifstream ifs;
    ifs.open(FILENAME,ios::in);
//    职工编号
    int m_id;
//    职工姓名
    string m_name;
//    职工部门
    int m_dep_id;
    int num=0;

    while (ifs>> m_id&&ifs>>m_name&&ifs>>m_dep_id)
    {
        num++;
    }
    return num;
}
//初始化职工
void WorkerManage::InitEmp()
{
    ifstream ifs;
    ifs.open(FILENAME,ios::in);
    //    职工编号
    int m_id;
//    职工姓名
    string m_name;
//    职工部门
    int m_dep_id;
    int index = 0;
    while (ifs>> m_id&&ifs>>m_name&&ifs>>m_dep_id)
    {
        Worker *worker =NULL;
        if(m_dep_id ==1)//普通职工
        {
            worker=new Employee(m_id,m_name,m_dep_id);
        }
        if(m_dep_id ==2)//经理
        {
            worker=new Manager(m_id,m_name,m_dep_id);
        }
        else//老板
        {
            worker=new Boss(m_id,m_name,m_dep_id);
        }
        this->m_emparray[index] = worker;
        index++;
    }
    ifs.close();
}
//显示职工信息
void WorkerManage::ShowEmp()
{
    if(this->m_File)
    {
        cout<< "空空空"<<endl;
    }
    else
    {
        for(int i=0; i<this->m_emp_num;i++)
        {
            this->m_emparray[i]->ShowInfo();
        }
    }
    system("clear");
}
//判断是否存在
int WorkerManage::IsExist(int id)
{
    int index = -1;

    for (int i=0; i<this->m_emp_num;i++)
    {
        if (this->m_emparray[i]->m_dep_id==id)
        {
            //找到职工
            index = i;
            break;
        }
    }
    return index;
}
//删除
void WorkerManage::DelEmp()
{
    if (this->m_File)
    {
        cout<< "空空空"<<endl;
    }
    else
    {
        //按照编号删除职工
        cout<< "请输入要删除的职工的编号"<<endl;
        int id = 0;
        cin >>id;

        int index = this->IsExist(id);

        if (index!=-1)//找到了删除
        {
            //数据前移
            for (int i =index;i<this->m_emp_num-1;i++)
            {
                this->m_emparray[i] = this->m_emparray[i+1];
            }
            this->m_emp_num--;
            this->Save();
            cout<< "删除成功"<<endl;
        }
        else
        {
            cout<< "删除失败，没有这个职工"<<endl;
        }
    }
}

void WorkerManage::ModEmp()
{
    if(this->m_File)
    {
        cout<< "没有这个职工"<<endl;
    } else
    {
        cout<< "请输入要修改的职工的编号"<<endl;
        int id = 0;
        cin >>id;
        int index = this->IsExist(id);

        if (index!=-1)//找到了删除
        {
            //数据前移
            delete this->m_emparray[index];

            int new_id = 0;
            string new_name;
            int new_did = 0;

            cout<< "找到"<<id<<"这个职工"<<endl;
            cout<< "请输入新的编号"<<endl;
            cin>>new_id;
            cout<< "请输入新的姓名"<<endl;
            cin>>new_name;
            cout<< "请输入新的部门:1：员工，2：经理，3：老板"<<endl;
            cin>>new_did;

            Worker *worker = NULL;
            while(true)
            {

                if(new_did==1)
                {
                    worker = new Employee(new_id, new_name, new_did);
                    break;
                }
                else if(new_did==2)
                {
                    worker = new Manager(new_id, new_name, new_did);
                    break;
                }
                else if(new_did==3)
                {
                    worker = new Boss(new_id,new_name,new_did);
                    break;
                }
                cout<< "输入有误请重新输入"<<endl;
                cin>>new_did;
            }

            this->m_emparray[index] = worker;
            cout<< "修改成功"<<endl;
            this->Save();
        }
        else
        {
            cout<< "修改失败，没有这个职工"<<endl;
        }
    }
}
//按条件查找职工
void WorkerManage::FindEmp()
{
    if(this->m_File)
    {
        cout<< "空空空"<<endl;
    }
    else
    {
        cout<< "请输入查找方式：1，编号，2，姓名"<<endl;
        int select=0;
        cin>>select;

        if(select==1)
        {
            int id =0;
            cin>>id;
            cout<< "请输入要查找的员工的编号"<<endl;
            int ret = IsExist(id);

            if(ret !=-1)
            {
                cout<< "找到该员工，其信息如下"<<endl;
                this->m_emparray[ret]->ShowInfo();
            }
            else
            {
                cout<< "查找失败，没有这个职工"<<endl;
            }
        }
        else if(select==2)
        {
            string name;
            cout<< "请输入要查找的员工的姓名"<<endl;
            cin>>name;
            bool flag= false;

            for (int i =0;i<this->m_emp_num;i++)
            {
                if (this->m_emparray[i]->m_name ==name)
                {
                    this->m_emparray[i]->ShowInfo();
                    flag= true;
                }
            }
            if(flag== false)
            {
                cout<< "查找失败，没有这个职工"<<endl;
            }
        }

        else
        {
            cout<< "从新输入，从新输入，从新输入"<<endl;
        }
    }
}
void WorkerManage::SortEmp()
{
    if(this->m_File)
    {
        cout<< "空空空"<<endl;
    }
    else
    {
        cout<< "请选择排序方式，1：升序，2：降序"<<endl;
        int id =0;
        cin>>id;

        for(int i =0;i<this->m_emp_num;i++)
        {
            int min_or_max = i;
            for(int j =i+1;j<this->m_emp_num;j++)
            {
                if (id==1)
                {
                    if(this->m_emparray[min_or_max]->m_id>this->m_emparray[j]->m_id)
                    {
                        min_or_max = j;
                    }
                }
                else
                {
                    if(this->m_emparray[min_or_max]->m_id<this->m_emparray[j]->m_id)
                    {
                        min_or_max = j;
                    }
                }
            }
            if(i !=min_or_max)
            {
                Worker *temp = this->m_emparray[i];
                this->m_emparray[i] = this->m_emparray[min_or_max];
                this->m_emparray[min_or_max] = temp;
            }
        }
    }
    cout<< "排序成功"<<endl;
    this->Save();
    this->ShowEmp();
}
//清空
void WorkerManage::CleanFile()
{
    cout<< "确定清空吗？，1：确定，2：让我再考虑考虑"<<endl;
    int id =0;
    cin>>id;

    if(id==1)
    {
        //删除文件后重建
        ofstream ofs(FILENAME,ios::trunc);
        ofs.close();
        if(this->m_emparray!=NULL)
        {
            //删除堆区的每个职工对象
            for(int i =0;i<this->m_emp_num;i++)
            {
                delete[] this->m_emparray[i];
                this->m_emparray[i] = NULL;
            }
            delete[] this->m_emparray;
            this->m_emparray = NULL;
            this->m_emp_num=0;
            this->m_File= true;
        }
        cout<< "清空成功"<<endl;
    }
}

WorkerManage::~WorkerManage()
{
    if(this->m_emparray!=NULL)
    {
//        for(int i =0;i<this->m_emp_num;i++)
//        {
//            if(this->m_emparray[i]!=NULL)
//            {
//                delete[] this->m_emparray[i];
//            }
//        }
        delete[] this->m_emparray;
        this->m_emparray = NULL;
    }
}


