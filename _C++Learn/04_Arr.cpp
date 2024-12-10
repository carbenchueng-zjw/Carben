//
// Created by kabun  on 10/3/21.
//

#include <iostream>
#include <string>
using namespace std;

int main()
{
//    //第一种：
//    int arr_1[5];
//    arr_1[0] = 10;
////    cout << arr_1[0] <<endl;
//    //第二种：如果还有元素没被定义，会用0补齐
    int arr_2[5] = {1,2,3};
//    cout << arr_2[1] <<endl;
//    //第三种
//    int arr_3[]={11,22,33,44,55,66};
//
//    cout << sizeof(arr_1)/sizeof(arr_1[0]) <<endl;//获取数组的个数
//    cout << &arr_3[2] <<endl;//查看每个元素的首地址
////    cout << int(arr_3) <<endl;

//  找最大值
//    int arr[]={11,22,77,44,55,66};
//    int max = 0;
//    int len = sizeof(arr)/ sizeof(arr[0]);
//    int index = sizeof(arr)/ sizeof(arr[0])-1;
//    int end_index = sizeof(arr)/ sizeof(arr[0])-1;
//    for (int i =0; i<=index ;i++)
//    {
//        cout <<"逆置前："<< arr[i]<<"::";
//    }
//    cout << endl;
//    for (int i=0; i<len; i++)//找出最大值
//    {
//        if(arr[i]>max)
//        {
//            max = arr[i];
//        }
////
//    }
//    cout << max<< endl;
//    倒序排列：要按下标位置，不能按元素个数
//    for (int a = index; a >=0;a--)
//    {
//        cout << arr[a] << "\t";
//    }
//    元素首尾置换，不是简单的倒序输出
//    int start = 0;
//    while (start<index)
//    {
//        int temp = arr[start];
//        arr[start] = arr[index];
//        arr[index]=temp;
//
//        start++;
//        index--;
//    }
//    cout<<index<<endl;
//    for (int s =0; s<=end_index ;s++)
//    {
//        cout <<"逆置后："<< arr[s]<<"::";
//    }

////    冒泡排序
//    int arr[] = {3,5,1,7,4,6,9,11,23,16};
//    cout <<"排序前"<<":"<<endl;
//    for (int i =0;i<9;i++)
//    {
//        cout<<arr[i]<<"\t";
//    }
//    cout<<endl;
////开始冒泡排序：外层：总共排序轮数为  元素个数-1
//    for (int c =0;c<9-1;c++)
//    {
////        内层循环对比
//        for (int j =0;j<9-c-1;j++)
//        {
//            if (arr[j]>arr[j+1])
//            {
//                int temp = arr[j];
//                arr[j] = arr[j+1];
//                arr[j+1]=temp;
//            }
//        }
//    }
//    cout <<"排序后"<<":"<<endl;
//    for (int i =0;i<9;i++)
//    {
//        cout<<arr[i]<<"\t";
//    }
//    cout<<endl;

//二维数组
//    第一种命名(推荐)
//    int arr[2][3]= {
//            {1,2,3},
//            {4,5,6}
//    };
////    第二种
//    int arr_1[2][3]= {1,2,3,4,5,6};
////    第三种
//    int arr_2[][3]= {1,2,3,4,5};
//    for (auto & i : arr_2)
//    {
//        for (int j : i)
//        {
//            cout<<j<<"\t";
//        }
//        cout<<endl;
//    }

//    考试成绩的统计，输出三名同学的总成绩
//            语文      数学      英语
//    张三    100       100      100
//    李四    90        50       100
//    王五    60        70       80
//    int scores[3][3] =
//        {
//            {100,100,100},
//            {90,50,100},
//            {60,70,80},
//        };
//    string names[3] = {"张三","李四","王五"};
//    for (int c =0;c<3;c++)
//    {
//        int summ = 0;
//        for (int j =0;j<3;j++)
//        {
//            summ+=scores[c][j];
////            cout << scores[c][j]<<"\t";
//        }
//        cout<<names[c]<<"个人的总分是："<<summ<<endl;
//    }

    return 0;
}