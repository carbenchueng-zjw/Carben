//
// Created by kabun  on 11/3/21.
//

#ifndef INC_3_CPP_P06_ARRAY_H
#define INC_3_CPP_P06_ARRAY_H

#endif //INC_3_CPP_P06_ARRAY_H
#include <iostream>
#pragma once
using namespace std;


template <class T>
class MyArray
{
public:
    MyArray(int capacity)
    {
//        cout << "有参构造的调用" <<endl;
        this->m_capacity = capacity;
        this->m_size=0;
        this->p_address= new T[this->m_capacity];
    }

    //拷贝构造
    MyArray(const MyArray& array)
    {
//        cout << "拷贝构造的调用" <<endl;
        this->m_capacity = array.m_capacity;
        this->m_size=array.m_size;
//        this->p_address= array.p_address;
        this->p_address=new T[array.m_capacity];//深拷贝

//        如果已经有数据，将数组的数据拷贝过来
        for(int i =0;i<this->m_size;i++)
        {
            this->p_address[i] = array.p_address[i];
        }
    }
//    重载等于（"="）号，防止前拷贝问题
    MyArray& operator=(const MyArray& array)
    {
//        cout << "operator的调用" <<endl;
        //如果有数据，要先释放
        if(this->p_address!=NULL)
        {
            delete[] this->p_address;
            this->p_address = NULL;
            this->m_capacity = 0;
            this->m_size=0;
        }
        //深拷贝
        this->m_capacity = array.m_capacity;
        this->m_size=array.m_size;
//        this->p_address= array.p_address;
        this->p_address=new T[array.m_capacity];//深拷贝
        for(int i =0;i<this->m_size;i++)
        {
            this->p_address[i] = array.p_address[i];
        }
        return *this;
    }

    //尾插法
    void PushBack(const T &value)
    {
//        先判断容量是否等于大小
        if(this->m_capacity==this->m_size)
        {
            return;
        }
        this->p_address[this->m_size] = value;//尾插入
        this->m_size++;//更新数组大小
    }
    //尾删法
    void DelBack()
    {
        //逻辑删除：让用户不能访问最后一个元素
        if(this->m_size==0)
        {
            return;
        }
        this->m_size--;
    }

    //通过下标方式访问数据中的元素
    T& operator[](int index)
    {
        return this->p_address[index];
    }

    //返回数组的容量
    int GetCapacity()
    {
        return this->m_capacity;
    }
    //返回数组的大小
    int GetSize()
    {
        return this->m_size;
    }

    ~MyArray()
    {
//        cout << "myarray的析构函数调用" <<endl;
        if(this->p_address!=NULL)
        {
            delete[] this->p_address;
            this->p_address = NULL;
        }
    }

private:
    T *p_address;//指向堆区开辟的数组
    int m_capacity;//数组容量
    int m_size;//数组大小
};