#include "HTMLWriter.h"

int main() {
	//HTMLWriter hw("test.html", "youmust be a good programmer");
	//hw.SetFileName("test.html");
	//hw.SetContent("You must be a good programmer");
	//hw.SetFont("Arial", 16, "blue");
	//hw.Write();
	//return 0;

	HTMLWriter hw;
	DocWriter dw;
	dw.SetContent("hi");
	dw.SetFileName("new");

	dw = hw;
}
