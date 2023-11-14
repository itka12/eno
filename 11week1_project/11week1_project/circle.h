#include <iostream>
using namespace std;
class circle :
    public Shape
{
public:
    void Draw() const;
    void SetRadius(double radius);

    circle();
    circle(double x, double u, double radius);
protected:
    double _radius;
};