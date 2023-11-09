////#include "UnderGrSt.h"
//#include <string>
//#include <iostream>
//
//using namespace std;
//
//class UnderGrSt {
//public:
//	string name;
//	string department;
//	void out() {
//		cout << "이름: " << name << endl;
//		cout << "대파:  " << department << endl;
//	}
//};
//class DormStudent {
//public:
//	string building;
//	int roomnumber;
//	void out() {
//		cout << "기숙사: " << building << endl;
//		cout << "호:  " << roomnumber << endl;
//	}
//};
//
//class UnderGrSt_DormStudent :
//	public UnderGrSt,
//	public DormStudent
//{
//public:
//	void out() {
//		UnderGrSt::out();
//		DormStudent::out();
//	}
//};
//
//int main() {
//	UnderGrSt_DormStudent std;
//	std.name = "Hyun C L";
//	std.department = "info & Com";
//	std.building = "NamJ";
//	std.roomnumber = 1555;
//	std.UnderGrSt::out();
//	std.DormStudent::out();
//	return 0;
//}