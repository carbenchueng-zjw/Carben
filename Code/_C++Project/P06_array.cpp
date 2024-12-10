//
// Created by kabun  on 11/3/21.
//

#include "P06_array.hpp"

void PrintArr(MyArray <int>&arr)
{
    for(int i =0;i<5;i++)
    {
        cout << arr[i]<<endl;
    }
}

//测试自定义数据类型的数组
class Person
{
public:
    string m_name;
    int m_age;

    Person()
    {

    };

    Person(string name,int age)
    {
        this->m_name = name;
        this->m_age = age;
    }
};
void PrintPersonArr(MyArray <Person>&arr)
{
    for(int i =0;i<arr.GetSize();i++)
    {
        cout <<"姓名：\t"<< arr[i].m_name
        <<"年龄：\t"<<arr[i].m_age<<endl;
    }
}

void test()
{
    MyArray<Person> arr(10);
    Person p1("孙悟空",999);
    Person p2("可口可乐",111);
    Person p3("书本",2323);
    Person p4("赵云",55);
    Person p5("策士统领",666);

    arr.PushBack(p1);
    arr.PushBack(p2);
    arr.PushBack(p3);
    arr.PushBack(p4);
    arr.PushBack(p5);
    PrintPersonArr(arr);
}

int main()
{
//    MyArray<int> array1(5);
//    MyArray<int> array2(array1);
//    MyArray<int> array3(100);
//    array3 = array1;
    //尾加
//    MyArray<int> array1(5);
//    for(int i =0;i<5;i++)
//    {
//        array1.PushBack(i);
////        cout << array1[i]<<endl;
//    }
//    PrintArr(array1);
//    cout<<"容量：\t"<< array1.GetCapacity() <<endl;
//    cout<<"大小：\t"<< array1.GetSize() <<endl;
//
//    //尾删
//    MyArray<int> array2(array1);
//    array2.DelBack();
//    cout<<"容量：\t"<< array2.GetCapacity() <<endl;
//    cout<<"大小：\t"<< array2.GetSize() <<endl;
//    cout<<"arr1 of id：\t"<< &array1 <<endl;
//    cout<<"arr2 of id：\t"<< &array2 <<endl;

    test();

    return 0;
}
