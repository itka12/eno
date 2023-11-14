#pragma once
#include "Parent.h"
using namespace std;

class Child :
    public Parent
{
public:
    Child() { cout << "child ¼Ò¸êÀÚ " << endl; }
    ~Child() { cout << " Child ¼Ò¸êÀÚ" << endl; }
};

