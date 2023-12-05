#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_QtWidgets_14week.h"

class QtWidgets_14week : public QMainWindow
{
    Q_OBJECT

public:
    QtWidgets_14week(QWidget *parent = nullptr);
    ~QtWidgets_14week();

private:
    Ui::QtWidgets_14weekClass ui;

    bool bSaved;
    bool blsSetFileName;
    QString strFileName;
    QString strShowFileName;

    void init();
    bool setFileName();


public slots:
    void OpenFile();
    void NewFile();
    void SaveFile();
    void textChange();
};
