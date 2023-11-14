//#include "main.h"
#include <iostream>
#include <string>
#include "circle.h"
#include "Rectangle.h"
#include "Shape.h"
using namespace std;
int main() {
	//Shape s;
	//s.Move(100, 100);
	//s.Draw();

	//Rectangle r;
	//r.Move(200, 100);
	//r.Resize(50, 50);
	//r.Draw();

	//circle c;
	//c.Move(300, 100);
	//c.SetRadius(30);
	//c.Draw();

	//return 0;

	Shape* shapes[5] = { NULL };

	shapes[0] = new circle(100, 100, 5);
	shapes[1] = new Rectangle(300, 300, 100, 100);
	shapes[2] = new Rectangle(200, 100, 50, 150);
	shapes[3] = new circle(100, 300, 150);
	shapes[4] = new Rectangle(200, 200, 200, 200);

	for (int i = 0; i < 5 : ++i) {
		shapes[i]->Draw();
	}
	for (i = 0; i < 5; ++i)
	{
		delete shapes[i];
		shapes[i] = NULL;
	}
	return 0;
}