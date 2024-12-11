//
// Created by kabun  on 10/4/21.
//

#include<iostream>
#include<string>
#include<ctime>
using namespace std;

//1:创建数据类型
//struct Student
//{
//    //成员列表：姓名，年龄，分数
//    string name; int age=0; int score=0;
//}s3,ss,ssc;//2.3 在定义结构体的时候直接创建
//
//struct Teacher
//{
//    int id=0;
//    string name;
//    int age=0;
//    Student stuuu;
//};
//
////值传递
//void PrintStudent_1(Student sp)
//{
//    sp.age=100;
//    cout <<"子函数中 姓名:"<<sp.name
//    <<"子函数中 年龄:" << sp.age
//    <<"子函数中 分数:" << sp.score << endl;
//}
////地址传递
//void PrintStudent_2(Student *sp)
//{
//    sp->age=200;
//    cout <<"子函数中 姓名:"<<sp->name
//         <<"子函数中 年龄:" << sp->age
//         <<"子函数中 分数:" << sp->score << endl;
//}

//2：通过学生类型创建具体学生(可能是编辑器原因，不用加struct)
//2.1 struct SEUDENT s1
//2.2 struct SEUDENT s2 = {...};
//将函数中的值传递改为地址传递（指针），减少内存消耗，
// 因为值传递会复制所有的信息，但是无论里面有多少内容，
// 指针只占4字节而且不会复制新的副本
//void PrintStudentConst(const Student *sp)
//{
////    s->age = 1000;//会报错，因为有const
//    cout <<"函数中 姓名:"<<sp->name
//         <<"函数中 年龄:" << sp->age
//         <<"函数中 分数:" << sp->score << endl;
//}

//2.3 在定义结构体的时候直接创建,（在第十四行）

//结构体案例1:
//struct Student
//{
//    string s_name;
//    int score=0;
//};
//
//struct Teacher
//{
//    string t_name;
//    Student sarray[5];
//
//};
//
//void AlloCateSpace(Teacher tarray[],int len)
//{
//    string name_seed = "ABCDE";
//    //给老师复制
//    for (int i =0;i<len;i++)
//    {
//        tarray[i].t_name = "Teacher_";
//        tarray[i].t_name += name_seed[i];
//        //给每位老师的学生赋值
//        for (int l =0;l<5;l++)
//        {
//            tarray[i].sarray[l].s_name = "Student_";
//            tarray[i].sarray[l].s_name += name_seed[l];
//            int r_score = rand() %61+40;
////            int r_score = 66;
//            tarray[i].sarray[l].score = r_score;
//        }
//    }
//}
//
//void PrintInfo(Teacher tarray[],int len)
//{
//    for (int i =0;i<len;i++)
////    for (auto i : tarray )
//    {
//        cout<<"老师的姓名："<<tarray[i].t_name<<endl;
//        for (auto & l : tarray[i].sarray)
//        {
//            cout<<"老师带的学生的姓名："<<l.s_name
//                <<"\t老师带的学生的分数："<<l.score<<endl;
//        }
//        cout << endl;
//    }
//}

//结构体案例2:
//struct Hero
//{
//    string name;
//    string sex;
//    int age=0;
//};
//
//void BubbleSort(Hero heros[],int len)
//{
//    for (int i =0;i<len-1;i++)
//    {
//        for (int j =0;j<len-i-1;j++)
//        {
//            if (heros[j].age > heros[j+1].age)
//            {
//                Hero temp = heros[j];
//                heros[j] = heros[j+1];
//                heros[j+1] = temp;
//            }
//        }
//    }
//};
//
//void PrintHero(Hero heros[],int len)
//{
//    for (int i =0;i<len;i++)
//    {
//        cout << "姓名：" << heros[i].name
//             << "\t性别：" << heros[i].sex
//             << "\t年龄：" << heros[i].age << endl;
//    }
//}


int main()
{
//    //2.1 SEUDENT s1
//    Student s1;
//    s1.name = "张三";
//    s1.age = 11;
//    s1.score = 111;
//
//    //2.2 SEUDENT s2 = {...};
//    Student s2 = {"李四",22,222};
//
//    //2.3 在定义结构体的时候直接创建
//    s3.name = "王五";
//    s3.age = 55;
//    s3.score = 555;
//    结构体数组
//    Student stu_array[]={
//            {"哈哈",11,22},
//            {"哥哥",33,333},
//            {"mm",55,666},
//    };
    //修改
//    stu_array[2].name = "呵呵";
//    stu_array[2].age = 77;
//    stu_array[2].score = 888;
//    for (auto & i : stu_array)
//    {
//        cout <<"姓名:"<< i.name
//        <<"\t年龄:"<<i.age
//        <<"\t分数:"<<i.score
//        << endl;
//    }

//结构体指针
//    Student *p = &stu_array[1];
//    cout << p->name << endl;

//结构体嵌套结构体
//    Teacher Jay;
//    Jay.id = 1;
//    Jay.name = "周杰伦";
//    Jay.age = 33;
//    Jay.stuuu.name = "鸡蛋";
//    Jay.stuuu.score = 100;

//结构体做函数参数
//    PrintStudent_1(s2);//值传递
//    PrintStudent_2(&s2);//地址传递
//    cout << s2.age << endl;

//结构体中const的使用场景（防止误操作，信息被修改）
//    PrintStudentConst(&s2);//地址传递

//结构体案例1:
    //添加随机种子
//    srand((unsigned)time(0));
//    //1：创建3名老师的结构体数组
//    Teacher tarray[3];
//    //2：给结构体信息赋值
//    int len = sizeof(tarray)/ sizeof(tarray[0]);
//    AlloCateSpace(tarray,len);
//    //3：打印所有信息
//    PrintInfo(tarray,len);

//结构体案例2:
//    Hero heros[]=
//    {
//        {"刘备","男",40},
//        {"张飞","男",32},
//        {"关羽","男",33},
//        {"貂蝉","女",26},
//        {"黄月英","女",27},
//    };
//    int len = sizeof(heros)/ sizeof(heros[0]);
//    BubbleSort(heros,len);
//    PrintHero(heros,len);

//    int arr[] = {1,2,3,4,5,6};
//    for (auto &all :arr)
//    {
//        cout<< all <<endl;
//    }

    return 0;
}