//
// Created by kabun  on 11/5/21.
//

#include <iostream>
#include <vector>
//#include <string>
#include <algorithm>//标准算法的头文件
using namespace std;



//int main()
//{
//    //默认构造
//    string name;
//    name = "asdfffffgfgfgf";
//    //使用字符串初始化
//    const char * str = "hello";
//    string s2(str);
////  拷贝构造
//    string s3(s2);
////  第四种
//    string s4(6,'b');//注意  一定要用单引号
//    cout<< sizeof(name) <<endl;
//    cout<< s2 <<endl;
//    cout<< s4 <<endl;
//}


//赋值操作
//int main()
//{
//    string st1;
//    st1 = "asdasd";
//    cout<< st1 <<endl;
//
//    string st2;
//    st2 =st1;
//    cout<< st2 <<endl;
//
//    string st3;
//    st3 = 'a';
//    cout<< st3 <<endl;
//
//    string st4;
//    st4.assign("ufcj");
//    cout<< st4 <<endl;
//
//    string st5;
//    st5.assign("ufcjyyyy",5);
//    cout<< st5 <<endl;
//
//    string st6;
//    st6.assign(st5);
//    cout<< st6 <<endl;
//
//    string st7;
//    st7.assign(10,'w');
//    cout<< st7 <<endl;

//    string ss(6,'b');//注意  一定要用单引号
//}

//字符串拼接
//int main()
//{
//    string st1;
//    st1 = "LOL";
//    st1 += " DNF";
//    cout<< st1 <<endl;
//
//    string st2;
//    st2 ="我爱玩游戏";
//    st2+=st1;
//    cout<< st2 <<endl;
//
//    string st3;
//    st3 = 'a';
//    st3.append("loveyyyy");
//    cout<< st3 <<endl;
//
//    string st5;
//    st5.append("ufcjyyyy",4);
//    cout<< st5 <<endl;
//
//    st2.append(st3,4,4);//(字符串，下标起始位置，选取个数)
//    cout<< st2 <<endl;
//
//}


//字符串查找，替换,比较，存取
int main()
{
    //查找
    string st1;
    st1 = "abcdefgdejk";
    int pos = st1.find("gr");//没有返回-1
    cout<< pos <<endl;

    int pos1 = st1.rfind("de");
    cout<< pos1 <<endl;

    //替换
    st1.replace(1,3,"111122");//(下标起始位置，末尾，要替换的内容)
    cout<< st1 <<endl;

    //比较
    string st2 = "asd";
    string st3 = "asd";
    string st4 = "asde";
//    if(st2.compare(st3)==0)
//    if(st2.compare(st4)==0)
//    {
//        cout << "相等" <<endl;
//    }

//    存取，字符串.size()返回字符串长度
    //读
//    for(int i=0;i<st1.size();i++)
//    {
//        cout <<st1[i] <<"  ";//第一种
//        cout <<st1.at(i) <<"  ";//第二种
//    }

    //写
//    st2[2] = 's';//第一种
//    st2.at(1)='x';//第二种
//    cout<< st2 <<endl;

    //插入
//    st2.insert(2,"11111");
//    st2.insert(2,3,'2');
//    cout<< st2 <<endl;
//    //删除
//    st2.erase(2,8);//下标起始位置，个数
//    cout<< st2 <<endl;

    //子串
//    string substr = st1.substr(1,3);//下标起始位置，选取个数
//    cout<< substr <<endl;
//
//    string name = "kabunchueng@icloud.com";
//    int index = name.find('@');
//    string sub_name = name.substr(0,index);
//    cout<< sub_name <<endl;

    return 0;

}
