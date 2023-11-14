#pragma once
#include <iostream>
using namespace std;
class Parent
{
public:
	Parent() { cout << "parent 持失切" << endl; }
	virtual ~Parent() { cout << "Parent 持識切" << endl; }
};

