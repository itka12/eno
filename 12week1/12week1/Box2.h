#pragma once
template <typename T1, typename T2>
class Box2 {
	T1 first_data; // T1�� Ÿ��(type)�� ��Ÿ����.
	T2 second_data; // T2�� Ÿ��(type)�� ��Ÿ����.
public:
	Box2() { }
	T1 get_first();
	T2 get_second();
	void set_first(T1 value) {
		first_data = value;
	}
	void set_second(T2 value) {
		second_data = value;
	}
};
template <typename T1, typename T2>
T1 Box2<T1, T2>::get_first() {
	return first_data;
}
template <typename T1, typename T2>
T2 Box2<T1, T2>::get_second() {
	return second_data;
}

