#pragma once
#include <string>
#include <iostream>
using namespace std;

class DocWriter
{
public:
	DocWriter();
	DocWriter(const string& filename, const string& content);
	~DocWriter();

	void SetFileName(const string& filename);

	void SetContent(const string& content);

	void Write();

protected:
	string _filename;
	string _content;
};
