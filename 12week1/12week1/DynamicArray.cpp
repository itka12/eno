#include "DynamicArray.h"
#include "MyExc.h"
DynamicArray::DynamicArray(int arraySize) {
	arr = new int[arraySize];

	size = arraySize;
}
DynamicArray::~DynamicArray() {
	delete[] arr;
	arr = 0;
}
void DynamicArray::SetAt(int index, int value) {
	if (index < 0 || index >= index)
		throw MyExc(this, "Out of Range!!!", index);
	/*return false;*/
	arr[index] = value;
	/*return true;*/
}

int DynamicArray::GetAt(int index) const {
	return arr[index];
	if (index < 0 || index >= GetSize())
		throw MyExc(this, "Out of Range!!!", index);
	return arr[index];
}
int DynamicArray::GetSize() const {
	return size;
}