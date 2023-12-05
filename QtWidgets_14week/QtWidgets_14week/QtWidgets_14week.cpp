#include "QtWidgets_14week.h"
#include <qmessagebox.h>
QtWidgets_14week::QtWidgets_14week(QWidget *parent)
    : QMainWindow(parent)
{
    ui.setupUi(this);
    connect(ui.action_new, SIGNAL(triggered()), this, SLOT(NewFile()));
    connect(ui.action_open, SIGNAL(triggered()), this, SLOT(NewFile()));
    connect(ui.action_save, SIGNAL(triggered()), this, SLOT(NewFile()));
}
void QtWidgets_14week::init() {
    bSaved = true;
    blsSetFileName = false;

    strFileName = QString::fromLocal8Bit("���� ����");
    strShowFileName = QString::fromLocal8Bit("���� ����");

    this->setWindowTitle(strFileName + QString::fromLocal8Bit("- Qt �޸���"));
}
void QtWidgets_14week::textChange() {
    if (bSaved) {
        bSaved = false;
        this->setWindowTitle("*" + this->windowTitle());
    }
}

QtWidgets_14week::~QtWidgets_14week()
{}
void QtWidgets_14week::OpenFile() {
    QMessageBox msgBox;
    msgBox.setText("Action Open File");
    msgBox.setStandardButtons(QMessageBox::Ok | QMessageBox::Cancel);
    msgBox.setDefaultButton(QMessageBox::Ok);
    if (msgBox.exec() == QMessageBox::Ok) {
        msgBox.close();
    }
}
void QtWidgets_14week::NewFile() {
    ui.plainTextEdit->clear();
    init();

    QMessageBox msgBox;
    msgBox.setText("Action Open File");
    msgBox.setStandardButtons(QMessageBox::Ok | QMessageBox::Cancel);
    msgBox.setDefaultButton(QMessageBox::Ok);
    if (msgBox.exec() == QMessageBox::Ok) {
        msgBox.close();
    }
}
void QtWidgets_14week::SaveFile() {
    QMessageBox msgBox;
    msgBox.setText("Action Open File");
    msgBox.setStandardButtons(QMessageBox::Ok | QMessageBox::Cancel);
    msgBox.setDefaultButton(QMessageBox::Ok);
    if (msgBox.exec() == QMessageBox::Ok) {
        msgBox.close();
    }
}
bool QtWidgets_14week::setFileName() {
    if (!blsSetFileName) {
        strFileName = QFileDialog::setSaveFileName(This, 
            QString::fromLocal8Bit("����"), QDir)
    }
}

