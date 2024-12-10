//
// Created by kabun on 2021/11/19.
//
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <string>

using namespace std;
class MyCom
{
public:
    bool operator()(int v1,int v2)const
    {
        return v1>v2;
    }
};

//void Pring(map<int,int> m)
void Pring(map<int,int,MyCom> m)
//void Pring(set<pair<int,int>> m)
{
    for(map<int,int,MyCom>::iterator it=m.begin();it!=m.end();it++)
    {
        cout << (*it).first<<it->second<<endl;
    }
}

void test()
{
    map<int,int> m;
    map<int,int> m5;
//    set<pair<int,int>> s;
//    m.insert(pair<int,int>(1,10));
//    m.insert(pair<int,int>(3,30));
//    m.insert(pair<int,int>(2,20));
//    m5.insert(pair<int,int>(2,20));
//    s.insert(pair<int,int>(1,20));
//    s.insert(pair<int,int>(2,20));
////    Pring(m);
////    Pring(s);
//    //拷贝构造
//    map<int,int> m2(m);
//    map<int,int> m3=m;
////    Pring(m3);
//
//    //大小
////    cout<< m.size()<<endl;
////    cout<< m.empty()<<endl;
//    //交换
//    m.swap(m5);
////    Pring(m);
//
////    map<int,int>::iterator it=m.begin();
//    map<int,int>::iterator it=m5.begin();
////    it++;
////    it =it+1;//不支持随机访问
//    //插入
//    m5.insert(make_pair(6,60));
//    m5[7]=70;//不建议这样插入，但是可以利用key来访问value
//    //删除
////    m5.clear();
//    m5.erase(2);//按照key来删除
//    m5.erase(m5.begin());
//    Pring(m5);
//    //查找
//    it = m5.find(6);
//    if(it!=m5.end())
//    {
//        cout << it->first << it->second<<endl;
//    }
//    else
//    {
//        cout<<"没有找到"<<endl;
//    }
//    //统计
//    cout<<m5.count(3)<<endl;
    //排序
    map<int,int,MyCom> m3;
    m3.insert(make_pair(1,10));
    m3.insert(make_pair(2,20));
    m3.insert(make_pair(3,30));
    Pring(m3);

}

int main()
{
    test();
    return 0;
}