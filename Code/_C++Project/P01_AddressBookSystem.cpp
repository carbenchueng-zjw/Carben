//
// Created by kabun  on 10/7/21.
//

#include <iostream>
#include <ctime>
#include <string>
#include <stdlib.h>
using namespace std;

#define MAX 1000

struct Person
{
    string name;
    int sex=0;
    int age=0;
    string addr;
    string phone;
};

struct AddressBooks
{
    Person person_arrary[MAX];
    int size=0;
};

//添加联系人
void AddPerson(AddressBooks * abs)
{
    //判断通讯录是否满了
    if(abs->size == MAX)
    {
        cout << "通讯录已满，不能添加"<<endl;
        return;
    }
    else
    {
        //添加联系人
        //姓名
        string n_name;
        cout << "请输入姓名"<<endl;
        cin>>n_name;
        abs->person_arrary[abs->size].name = n_name;        //添加联系人
        //性别
        cout << "请输入性别:1==男，2==女"<<endl;
        int n_sex=0;
        while (true)
        {
            cin>>n_sex;
            if (n_sex ==1||n_sex==2)
            {
                abs->person_arrary[abs->size].sex = n_sex;
                break;
            }
            cout << "输入有误，请重新输入！！"<<endl;
        }
        //年龄
        int n_age=0;
        cout << "请输入年龄"<<endl;
        cin>>n_age;
        abs->person_arrary[abs->size].age = n_age;        //添加联系人
        //地址
        string n_addr;
        cout << "请输入地址"<<endl;
        cin>>n_addr;
        abs->person_arrary[abs->size].addr = n_addr;        //添加联系人
        //电话
        string n_phone;
        cout << "请输入电话"<<endl;
        cin>>n_phone;
        abs->person_arrary[abs->size].phone = n_phone;

        //更新通讯录
        abs->size++;
        cout << "恭喜，添加成功！！"<<endl;
//        system("cls");
    }
}

//显示联系人
void ShowPerson(AddressBooks * abs)
{
//    system("cls");
    if (abs->size>0)
    {
        for (int i=0; i<abs->size; i++)
        {
            cout <<"姓名："<<abs->person_arrary[i].name;
            cout <<"\t年龄："<<(abs->person_arrary[i].sex==1?"男":"女");
            cout <<"\t性别："<<abs->person_arrary[i].age;
            cout <<"\t地址："<<abs->person_arrary[i].addr;
            cout <<"\t电话："<<abs->person_arrary[i].phone<<endl;
        }
    }
    else
    {
        cout << "通讯录为空"<<endl;
    }
}

//查找联系人
int IsExist(AddressBooks * abs,string name)
{
    for (int i=0; i<abs->size; i++)
    {
        if(abs->person_arrary[i].name == name)
        {
//            cout << "找到了！！"<<endl;
            return i;
        }
    }
    return -1;
}

//删除联系人
void DelPerson(AddressBooks * abs)
{
    cout << "请输入你要删除的人的姓名"<<endl;
    string name;
    cin>>name;
//    ret ==-1找不到此人,  ret !=1找到了此人
    int ret = IsExist(abs,name);
    if (ret!=-1)
    {
        for (int i =ret;i<abs->size;i++)
        {
            //数据前移覆盖
            abs->person_arrary[i] =abs->person_arrary[i+1];
        }
        abs->size--;//更新通讯录中的人数
        cout << "删除成功！！"<<endl;
    }
    else
    {
        cout << "没有这个人！！"<<endl;
    }
}

//查找联系人
void FindPerson(AddressBooks * abs)
{
    cout << "请输入你要查找的人的姓名"<<endl;
    string name;
    cin>>name;
    int ret = IsExist(abs,name);
    if (ret!=-1)
    {
        cout <<"姓名："<<abs->person_arrary[ret].name;
        cout <<"\t性别："<<abs->person_arrary[ret].sex;
        cout <<"\t年龄："<<abs->person_arrary[ret].age;
        cout <<"\t地址："<<abs->person_arrary[ret].addr;
        cout <<"\t电话："<<abs->person_arrary[ret].phone<<endl;
    }
    else
    {
        cout << "没有这个人！！"<<endl;
    }
    system("cls");
}

//修改联系人
void ModifyPerson(AddressBooks * abs)
{
    cout << "请输入你要修改的人的姓名"<<endl;
    string name;
    cin>>name;
    int ret = IsExist(abs,name);
    if (ret!=-1)
    {
        cout << "请输入你要修改的内容："
        <<"1--姓名"
        <<"\t2--年龄"
        <<"\t3--性别"
        <<"\t4--地址"
        <<"\t5--电话"<<endl;
        int change =0;
        cin>>change;
        if (change==1)
        {   //姓名
            cout << "请输入姓名" << endl;
            string n_name;
            cin >> n_name;
            abs->person_arrary[ret].name = n_name;        //添加联系人

        }
        else if(change==3)
        {
            //性别
            cout << "请输入性别:1==男，2==女"<<endl;
            int n_sex=0;
            while (true)
            {
                cin>>n_sex;
                if (n_sex ==1||n_sex==2)
                {
                    abs->person_arrary[ret].sex = n_sex;
                    break;
                }
                cout << "输入有误，请重新输入！！"<<endl;
            }
        }
        else if (change==2)
        {
            //年龄
            cout << "请输入年龄"<<endl;
            int n_age=0;
            cin>>n_age;
            abs->person_arrary[ret].age = n_age;        //添加联系人

        }
        else if (change==4)
        {
            //地址
            string n_addr;
            cout << "请输入地址"<<endl;
            cin>>n_addr;
            abs->person_arrary[ret].addr = n_addr;        //添加联系人

        }
        else if (change==5)
        {
            //电话
            string n_phone;
            cout << "请输入电话" << endl;
            cin >> n_phone;
            abs->person_arrary[ret].phone = n_phone;
            cout << "恭喜，修改成功！！" << endl;
        }
        else
        {
            cout << "输入有误，请重新输入！！" << endl;
        }
    }
    else
    {
        cout << "没有这个人！！"<<endl;
    }
}

void ClearPerson(AddressBooks * abs)
{
    cout << "请问确定要清空联系人吗？"<<endl
    << "1--是，2--不是"<<endl;
    int select =0;
    cin >> select;
    if (select==1)
    {
        abs->size = 0;
        cout << "已清空通讯录！！"<<endl;
    }
    else if(select==2)
    {
        cout << "返回上级菜单"<<endl;
    }
}

//显示菜单
void ShowMenu()
{
    cout << "\t*********************\n"
    << "\t*****1：添加联系人*****\t\n"
    << "\t*****2：显示联系人*****\t\n"
    << "\t*****3：删除联系人*****\t\n"
    << "\t*****4：查找联系人*****\t\n"
    << "\t*****5：修改联系人*****\t\n"
    << "\t*****6：清空联系人*****\t\n"
    << "\t*****0：退出通讯录*****\t\n"
    << "\t*********************\t" <<endl;
}

int main()
{
    //创建通讯录结构体变量
    AddressBooks abs;
    //初始化通讯录中的当前人数
    abs.size =0;

    int select = 0;
    //显示菜单
    while (true)
    {
        ShowMenu();
        cout << "请输入你需要的功能"<<endl;
        cin >> select;
        switch (select)
        {
            case 1://添加联系人
                AddPerson(&abs);//利用地址传递修改
                break;
            case 2://显示联系人
                ShowPerson(&abs);
                break;
            case 3://删除联系人
                DelPerson(&abs);
                break;
            case 4://查找联系人
                FindPerson(&abs);
                break;
            case 5://修改联系人
                ModifyPerson(&abs);
                break;
            case 6://清空联系人
                ClearPerson(&abs);
                break;
            case 0://退出通讯录
                cout << "感谢使用，祝您生活愉快！！"<<endl;
//                pause();
                return 0;
            default:
                cout << "输入有误，请重新输入！！"<<endl;
        }
    }
}