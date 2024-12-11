//
// Created by kabun on 2021/11/22.
//

#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
//一元谓词
class GreatFive
{
public:
    bool operator()(int val)
    {
        return val>5;
    }
};

void test01()
{
    vector<int> v;
    for(int i=0;i<10;i++)
    {
        v.push_back(i);
    }
    //查找大于5的数字
    //GreatFive是匿名函数对象
    vector<int>::iterator it = find_if(v.begin(),v.end(),GreatFive());
    if(it==v.end())
    {
        cout << "没有找到" <<endl;
    }
    else
    {
        cout << "找到了："<<*it <<endl;
    }

}

//二元谓词
class MyCon
{
public:
    bool operator()(int v1,int v2)
    {
        return v1>v2;
    }
};

void test02() {
    vector<int> v;
    v.push_back(3);
    v.push_back(4);
    v.push_back(5);
    v.push_back(1);

    sort(v.begin(),v.end());
    for(vector<int>::iterator it=v.begin();it!=v.end();it++)
    {
        cout << "找到了："<<*it;
    }
    cout<<endl;

    //使用函数对象改为大到小
    sort(v.begin(),v.end(),MyCon());
    for(vector<int>::iterator it=v.begin();it!=v.end();it++)
    {
        cout << "找到了："<<*it;
    }
    cout<<endl;
}

int main()
{
//    test01();
    test02();
//    cin.get();
    return 0;
}