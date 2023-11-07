#include "DocWriter.h"
#include <fstream>
using namespace std;
DocWriter::DocWriter()
{
	_filename = "NoName.txt";
	_content = "There is no content.";

}
DocWriter::DocWriter(const string& filename, const string& content)
{
	_filename = filename;
	_content = content;
}
DocWriter::	~DocWriter() 
{
}

void DocWriter::SetFileName(const string& filename) {
	_filename = filename;
}

void DocWriter::SetContent(const string& content) {
	_content = content;
}
void DocWriter::Write() {
	ofstream of(_filename.c_str());

	of << "# Content #\n\n";

	of << _content;
}
//
//int main() {
//	DocWriter dw;
//	dw.SetFileName("test.txt");
//	dw.SetContent("You must be a good programmer~!!");
//	dw.Write();
//
//	return 0;
//}