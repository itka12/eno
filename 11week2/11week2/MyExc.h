#pragma once
class MyExc
{
public:
	const void* sender;
	const char* description;
	int info;

	MyExc(const void* sender, const char* description, int info) {
		this->sender = sender;
		this->description = description;
		this->info = info;
	}
};

