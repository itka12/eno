#pragma once
#include "DocWriter.h"
class HTMLWriter :
    public DocWriter
{
public:
    HTMLWriter(void);
    HTMLWriter(const string& filename, const string& content);
    ~HTMLWriter(void);

    HTMLWriter();
    ~HTMLWriter();

    void Write();

    void SetFont(const string& fontname, int fontsize, const string& fontcolor);

protected:
    string _fontname;
    int _fontsize;
    string _fontcolor;
};

