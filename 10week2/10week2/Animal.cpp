//#include "Animal.h"
#include <iostream>
using namespace std;

class animal {

public:
	void speak() { 
		cout << "Animal speak()" << endl;
	}
};
class Dog : public animal
{
public:
	int age;
	void speak()
	{
		cout << "港港" << endl;
	}
};
class Cat : public animal 
{
public:
	void speak() {
		cout << "具克" << endl;
	}
};

//int main() {
//	animal* a1 = new Dog();
//	a1->speak();
//
//	animal* a2 = new Cat();
//	a2->speak();
//	//a1 -> age =10;
//	return 0; 
//}