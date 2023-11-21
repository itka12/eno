#include <iostream>
#include "Box2.h"
using namespace std;
//template<typename T>
//void copy(T1 a1[], T2 a2[], int n) {
//	for (int i = 0; i < n; ++i)
//		a1[i] = a2[i];
//}
//template<typename T1, typename T2>
//void copy(T1 a1[], T2 a2[], int n) {
//	for (int i = 0; i < n; ++i)
//		a1[i] = a2[i];
//}
//int main() {
//	int a[100];
//	double b[100];
//	copy(a, b, 100);
//}

//template <typename T>
//class Box {
//	T data;
//public:
//	Box() {     }
//	void set(T value) {
//		data = value;
//	}
//	T get() {
//		return data;
//	}
//};
//
//int main() {
//	Box<int> box;
//	box.set(100);
//	cout << box.get() << endl;
//
//	Box<double> box1;
//	box1.set(3.141592);
//	cout << box.get() << endl;
//	return 0;
//}

//int main() {
//	Box2 <int, string>b2;
//	b2.set_first(100);
//	b2.set_second("idig");
//
//	cout << b2.get_first() << endl;
//	cout << b2.get_second() << endl;
//	return 0;
//}
#include "DynamicArray.h"
#include <iostream>
#include "MyExc.h"
//#include <string>

using namespace std;

int main()
{
	DynamicArray arr1(10);
	DynamicArray arr2(8);

	//for (int i = 0 ; i < 10; ++i)
	//	arr.SetAt(i, (i + 1) * 10);
	//cout << "Size of arr = " << arr.GetSize() << endl;

	//for (int i = 9; i > 0; --i)
	//	cout << "arr[" << i << "] = " << arr.GetAt(i) << endl;

	//if (!arr.SetAt(15, 100))
	//	cout << "실패" << endl;
	try {
		arr1.SetAt(5, 100);
		arr2.SetAt(5, 100);
		/*	cout << arr.GetAt(5) << endl;*/
			//arr.SetAt(8, 100);
		arr1.SetAt(8, 100);
		arr2.SetAt(8, 100);
		arr1.SetAt(10, 100);
		arr2.SetAt(10, 100);
	}
	catch (MyExc& ex) {
		cout << "&arr1 = " << &arr1 << "\n&arr2= " << &arr2 << endl;

		cout << "예의를 던진 객체의 주소 = " << ex.sender << endl;
		cout << "예의의 대한 설명= " << ex.description << endl;
		cout << "부가 정보= " << ex.info << endl;
	}
	cout << "Try - catch 종료  " << endl;
	return 0;
}

// 프로그램 실행: <Ctrl+F5> 또는 [디버그] > [디버깅하지 않고 시작] 메뉴
// 프로그램 디버그: <F5> 키 또는 [디버그] > [디버깅 시작] 메뉴

// 시작을 위한 팁: 
//   1. [솔루션 탐색기] 창을 사용하여 파일을 추가/관리합니다.
//   2. [팀 탐색기] 창을 사용하여 소스 제어에 연결합니다.
//   3. [출력] 창을 사용하여 빌드 출력 및 기타 메시지를 확인합니다.
//   4. [오류 목록] 창을 사용하여 오류를 봅니다.
//   5. [프로젝트] > [새 항목 추가]로 이동하여 새 코드 파일을 만들거나, [프로젝트] > [기존 항목 추가]로 이동하여 기존 코드 파일을 프로젝트에 추가합니다.
//   6. 나중에 이 프로젝트를 다시 열려면 [파일] > [열기] > [프로젝트]로 이동하고 .sln 파일을 선택합니다.