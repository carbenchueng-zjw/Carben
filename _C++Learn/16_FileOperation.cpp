//
// Created by kabun  on 10/21/21.
//

#include <iostream>
#include <string>
#include <fstream>
using namespace std;

//文本文件  写文件
//void WriteTest()
//{
//    ofstream ofs;
//    ofs.open("../test.txt",ios::out);
//
//    ofs<<"asdasdasd"<<endl;
//    ofs<<"a111```````"<<endl;
//    ofs<<"=========="<<endl;
//    ofs.close();
//}
//读文件
//void ReadTest()
//{
//    ifstream ifs;
//    ifs.open("../test.txt",ios::in);
//    if (!ifs.is_open())
//    {
//        cout<<"打开失败了" <<endl;
//        return;
//    }
    //第一种读取方式：
//    char buf[1024] = {0};
//    while (ifs>>buf)
//    {
//        cout << buf << endl;
//    }

    //第二种读取方式：
//    char buf[1024] = {0};
//    while (ifs.getline(buf, sizeof(buf)))
//    {
//        cout << buf << endl;
//    }

    //第三种读取方式：
//    string buf;
//    while (getline(ifs,buf))
//    {
//        cout << buf << endl;
//    }

    //第四种读取方式：(不推荐，它是一个一个字符读)
//    char c;
//    while ((c = ifs.get())!=EOF)//EOF: end of file
//    {
//        cout << c;
//    }
//
//    ifs.close();
//}

//二进制 读写文件
class Person
{
public:
    char m_name[64];
    int m_age;
};
void Test()
{
    //可以直接打开
    ofstream ofs("../Person.txt",ios::out|ios::binary);
    ifstream ifs("../Person.txt",ios::in|ios::binary);
//    ofs.open("../Person.txt",ios::out|ios::binary);
    Person p = {"zhangsan",18};
    //写
    ofs.write((const char *)&p, sizeof(Person));
    //读
    if (!ifs.is_open())
    {
        cout <<"打开失败"<<endl;
    }
    ifs.read((char *)&p,sizeof(Person));
    cout <<p.m_name<<p.m_age<<endl;

    ofs.close();
}


int main()
{
//    WriteTest();
//    ReadTest();
    Test();
    return 0;
}


