#pragma once
class Shape
{
public:
	void Move(double x, double y);
	void Draw() const;
	virtual void Draw() const;

	Shape();
	Shape(double x, double y);
protected:
	double _x, _y;
};