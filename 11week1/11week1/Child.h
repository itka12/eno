#pragma once
#include "Parent.h"
using namespace std;

class Child :
    public Parent
{
public:
    Child() { cout << "child �Ҹ��� " << endl; }
    ~Child() { cout << " Child �Ҹ���" << endl; }
};

