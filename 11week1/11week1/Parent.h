#pragma once
#include <iostream>
using namespace std;
class Parent
{
public:
	Parent() { cout << "parent ������" << endl; }
	virtual ~Parent() { cout << "Parent ������" << endl; }
};

