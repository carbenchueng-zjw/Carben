//
// Created by kabun  on 10/20/21.
//

#include <iostream>
#include <string>
using namespace std;

class CPU
{
public:
    virtual void calculater()=0;
};
class GPU
{
public:
    virtual void display()=0;
};
class Memory
{
public:
    virtual void storage()=0;
};
//电脑
class Computer
{
public:
    Computer(CPU *cpu,GPU *gpu,Memory *memory)
    {
        m_cpu=cpu;
        m_gpu=gpu;
        m_memory=memory;
    }
    void work()
    {
        m_cpu->calculater();
        m_gpu->display();
        m_memory->storage();
    };
    ~Computer()
    {
        if (m_cpu!=NULL)
        {
            delete m_cpu;
            m_cpu = NULL;//防止出现野指针
        }
        else if (m_gpu!=NULL)
        {
            delete m_gpu;
            m_gpu = NULL;
        }
        else if (m_memory!=NULL)
        {
            delete m_memory;
            m_memory = NULL;
        }
    }

private:
    CPU *m_cpu;
    GPU *m_gpu;
    Memory *m_memory;
};
//英特尔厂商
class InterCPU:public CPU
{
public:
    void calculater()
    {
        cout<< "英特尔开始计算了"<<endl;
    }
};
class InterGPU:public GPU
{
public:
    void display()
    {
        cout<< "英特尔开始显示了"<<endl;
    }
};
class InterMemory:public Memory
{
public:
    void storage()
    {
        cout<< "英特尔开始存储了"<<endl;
    }
};

//lenovo厂商
class lenovoCPU:public CPU
{
public:
    void calculater()
    {
        cout<< "lenovo开始计算了"<<endl;
    }
};
class lenovoGPU:public GPU
{
public:
    void display()
    {
        cout<< "lenovo开始显示了"<<endl;
    }
};
class lenovoMemory:public Memory
{
public:
    void storage()
    {
        cout<< "lenovo开始存储了"<<endl;
    }
};
void test()
{

    //创建第一台电脑
    Computer *c1 = new Computer(new InterCPU,new InterGPU,new InterMemory);
    c1->work();
    delete c1;

    //创建第二台电脑
    Computer *c2 = new Computer(new lenovoCPU,new lenovoGPU,new lenovoMemory);
    c2->work();
    delete c2;
}

int main()
{
    test();
    return 0;
}











