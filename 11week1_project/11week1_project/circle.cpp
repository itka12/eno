#include "circle.h"
circle::circle() {
    _radius = 100.0f;
}
circle::circle(double x, double y, double radius)
    :Shape(x, y)
{
    SetRadius(radius);
}
void circle::Draw() const {
    cout << "[Circle] position = (" << _x << "," << _y << ") "
        "radius = " << _radius << ")\n";
}
void circle::SetRadius(double radius)
{
    _radius = radius;
}