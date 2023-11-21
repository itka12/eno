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
	//	cout << "����" << endl;
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

		cout << "���Ǹ� ���� ��ü�� �ּ� = " << ex.sender << endl;
		cout << "������ ���� ����= " << ex.description << endl;
		cout << "�ΰ� ����= " << ex.info << endl;
	}
	cout << "Try - catch ����  " << endl;
	return 0;
}

// ���α׷� ����: <Ctrl+F5> �Ǵ� [�����] > [��������� �ʰ� ����] �޴�
// ���α׷� �����: <F5> Ű �Ǵ� [�����] > [����� ����] �޴�

// ������ ���� ��: 
//   1. [�ַ�� Ž����] â�� ����Ͽ� ������ �߰�/�����մϴ�.
//   2. [�� Ž����] â�� ����Ͽ� �ҽ� ��� �����մϴ�.
//   3. [���] â�� ����Ͽ� ���� ��� �� ��Ÿ �޽����� Ȯ���մϴ�.
//   4. [���� ���] â�� ����Ͽ� ������ ���ϴ�.
//   5. [������Ʈ] > [�� �׸� �߰�]�� �̵��Ͽ� �� �ڵ� ������ ����ų�, [������Ʈ] > [���� �׸� �߰�]�� �̵��Ͽ� ���� �ڵ� ������ ������Ʈ�� �߰��մϴ�.
//   6. ���߿� �� ������Ʈ�� �ٽ� ������ [����] > [����] > [������Ʈ]�� �̵��ϰ� .sln ������ �����մϴ�.