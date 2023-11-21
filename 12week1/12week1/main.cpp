#include <iostream>
#include <string>

using namespace std;

//int <typename int>
//int get_max(int x, int y) {
//	if (x > y) return x;
//	else return y;
//}
//double <typename double>
//double ge_max(double x, double y) {
//	if (x > y) return x;
//	else return y;
//}
//int main() {
//	cout << get_max(1, 3) << endl;
//	cout << get_max(1.2, 3.9) << endl;
//	return 0;
//}

//template <typename int>
//void swap_values(int& x, int& y) {
//	int temp;
//	temp = x;
//	x = y;
//	y = temp;
//}
//
//template <typename char>
//void swap_values(char* s1, char* s2) {
//	int len;
//	len = (strlen(s1) > = strlen(s2)) ? strlen(s1) : strlen(s2);
//	char* tmp = new char[len + 1];
//
//	strcpy(tmp, s1);
//	strcpy(s1, s2);
//	strcpy(s2, tmp);
//	delete[] tmp;
//}
//int main() {
//	int x = 100, y = 200;
//	swap_values(x, y);
//	cout << x << " " << y << endl;
//	char s1[100] = " This is a first string";
//	char s2[100] = " This is a first string";
//	swap_values(s1, s2);
//
//	cout << s1 << " " << s2 << endl;
//	return 0;
// }