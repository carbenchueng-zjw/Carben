//
// Created by kabun  on 11/10/21.
//

#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <deque>
#include <time.h>

using namespace std;

class Player
{
public:
    int m_score;
    string m_name;
    Player(int score,string name)
    {
        this->m_name = name;
        this->m_score = score;
    }
};


void CreatPlater(vector<Player> &o)
{
    string name_seed = "ABCDE";
    for(int i =0;i<5;i++)
    {
        string name="选手";
        name+=name_seed[i];

        int score=0;
        Player P(score,name);
        o.push_back(P);
    }
}

void SetScore(vector<Player> &v)
{
    for(vector<Player>::iterator it=v.begin();it!=v.end();it++)
    {
        deque<int> d;
        for (int i =0;i<10;i++)
        {
            int score =rand()%41+60;  //60~100
            d.push_back(score);
        }

        //排序
        sort(d.begin(),d.end());
        d.pop_front();
        d.pop_back();
//        cout << d.size();

        //取平均分
        int sum=0;
        for(deque<int>::iterator dit=d.begin();dit!=d.end();dit++)
        {
            sum += *dit;
//            cout << *dit<<"  ";
        }
//        cout << endl;
        int avg = sum/d.size();
//        cout << avg <<endl;
        //将平均分赋值给选手
        it->m_score = avg;

//        cout << "选手" << it->m_name << "的评分：：" << it->m_score <<endl;
//        cout << "选手" << it->m_name << "的评分：：";
//        for(deque<int>::iterator dit=d.begin();dit!=d.end();dit++)
//        {
//            cout << *dit << "  ";
//        }
//        cout << endl;
    }
}

void ShowScore(vector<Player> &v)
{
    for(vector<Player>::iterator it=v.begin();it!=v.end();it++)
    {
        cout << "选手" << it->m_name << "的评分：：" << it->m_score <<endl;
    }
}

//int main()
//{
//    //随机数种子
//    srand((unsigned int)time(NULL));
//    //创建5名选手
//    vector<Player> v;
//    CreatPlater(v);
//    //测试
////    for(vector<Player>::iterator it=v.begin();it!=v.end();it++)
////    {
////        cout << (*it).m_name<<(*it).m_score <<endl;
////    }
//
//    //打分
//    SetScore(v);
//    //显示
//    ShowScore(v);
//
//}



