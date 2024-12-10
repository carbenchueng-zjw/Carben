//
// Created by kabun  on 10/4/21.
//
#include <iostream>
using namespace std;


//指针和函数
void swap(int *num_1,int *num_2)
{
    cout<< "交换前："<< *num_1<<"\t"<<*num_2 <<endl;
    int temp = * num_1;
    *num_1 = *num_2;
    *num_2=temp;

    cout<< "交换后："<< *num_1<<"\t"<<*num_2 <<endl;
}

void BUBBLESTORE(int *arr,int len)
{
    cout <<"排序前"<<":"<<endl;
    for (int i =0;i<len;i++)
    {
        cout<<arr[i]<<"\t";
    }
    cout<<endl;
//开始冒泡排序：外层：总共排序轮数为  元素个数-1
    for (int c =0;c<len-1;c++)
    {
//        内层循环对比
        for (int j =0;j<len-c-1;j++)
        {
            if (arr[j]>arr[j+1])
            {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1]=temp;
            }
        }
    }
    cout <<"排序后"<<":"<<endl;
    for (int i =0;i<len;i++)
    {
        cout<<arr[i]<<"\t";
    }
    cout<<endl;

}

//指针
int main()
{
//    int a = 10;
//    //    定义一个指针：数据类型 * 变量名
//    int * p;
////    让指针记录变量a的地址
//    p =&a;
//    cout << &a <<endl;
//    cout << p <<endl;
//
//    //使用指针，解引用
//    *p = 1000;
//    cout<< *p
//    <<a<< endl
//    <<sizeof(p)<<endl;
//    //空指针：不能访问，初始化指针变量
//    int *u = NULL;

////1：const修饰指针--叫做常量指针(指向可以修改，指向的值不能改)
//    int a = 10;
//    int b = 20;
//    const int *p = &a;//常量指针
//    p = &b;
//
////2：const修饰指针--叫做指针常量(指向不可以修改，指向的值能改)
//    int * const u = &a;//指针常量
//    *u = 30;
//
////3：const修饰指针--叫做指针常量(指向,值都不可以修改)
//    const int * const c = &a;

//指针和数组
//    int arr[] = {1,2,3,11,22,33};
//    int*p = arr;
////    cout << *p++ <<endl;
//    for (int i=0;i<6;i++)
//    {
//        cout << *p++ <<endl;
//    }

//    int a = 10;
//    int b = 20;
//    //地址传递
//    swap(&a,&b);
//    cout << a <<"\t"<< b <<endl;

    int arr[] = {66,55,33,22,11,55,88};
    int len = sizeof(arr)/ sizeof(arr[0]);
    int*p = arr;
    BUBBLESTORE(arr,len);
    cout << p[0]<<endl;

    return 0;
}

