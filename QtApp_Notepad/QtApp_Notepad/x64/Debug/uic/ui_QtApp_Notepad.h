/********************************************************************************
** Form generated from reading UI file 'QtApp_Notepad.ui'
**
** Created by: Qt User Interface Compiler version 5.12.12
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_QTAPP_NOTEPAD_H
#define UI_QTAPP_NOTEPAD_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPlainTextEdit>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_QtApp_NotepadClass
{
public:
    QWidget *centralWidget;
    QGridLayout *gridLayout;
    QGridLayout *gridLayout_2;
    QPlainTextEdit *plainTextEdit;
    QMenuBar *menuBar;
    QMenu *menufile;
    QMenu *menuedit;
    QMenu *menuform;
    QMenu *menuview;
    QMenu *menuhelp;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *QtApp_NotepadClass)
    {
        if (QtApp_NotepadClass->objectName().isEmpty())
            QtApp_NotepadClass->setObjectName(QString::fromUtf8("QtApp_NotepadClass"));
        QtApp_NotepadClass->resize(594, 397);
        centralWidget = new QWidget(QtApp_NotepadClass);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        gridLayout = new QGridLayout(centralWidget);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        gridLayout->setContentsMargins(0, 0, 0, 0);
        gridLayout_2 = new QGridLayout();
        gridLayout_2->setSpacing(6);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        plainTextEdit = new QPlainTextEdit(centralWidget);
        plainTextEdit->setObjectName(QString::fromUtf8("plainTextEdit"));

        gridLayout_2->addWidget(plainTextEdit, 0, 0, 1, 1);


        gridLayout->addLayout(gridLayout_2, 0, 0, 1, 1);

        QtApp_NotepadClass->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(QtApp_NotepadClass);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 594, 26));
        menufile = new QMenu(menuBar);
        menufile->setObjectName(QString::fromUtf8("menufile"));
        menuedit = new QMenu(menuBar);
        menuedit->setObjectName(QString::fromUtf8("menuedit"));
        menuform = new QMenu(menuBar);
        menuform->setObjectName(QString::fromUtf8("menuform"));
        menuview = new QMenu(menuBar);
        menuview->setObjectName(QString::fromUtf8("menuview"));
        menuhelp = new QMenu(menuBar);
        menuhelp->setObjectName(QString::fromUtf8("menuhelp"));
        QtApp_NotepadClass->setMenuBar(menuBar);
        mainToolBar = new QToolBar(QtApp_NotepadClass);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        QtApp_NotepadClass->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(QtApp_NotepadClass);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        QtApp_NotepadClass->setStatusBar(statusBar);

        menuBar->addAction(menufile->menuAction());
        menuBar->addAction(menuedit->menuAction());
        menuBar->addAction(menuform->menuAction());
        menuBar->addAction(menuview->menuAction());
        menuBar->addAction(menuhelp->menuAction());

        retranslateUi(QtApp_NotepadClass);

        QMetaObject::connectSlotsByName(QtApp_NotepadClass);
    } // setupUi

    void retranslateUi(QMainWindow *QtApp_NotepadClass)
    {
        QtApp_NotepadClass->setWindowTitle(QApplication::translate("QtApp_NotepadClass", "QtApp_Notepad", nullptr));
        menufile->setTitle(QApplication::translate("QtApp_NotepadClass", "\355\214\214\354\235\274", nullptr));
        menuedit->setTitle(QApplication::translate("QtApp_NotepadClass", "\355\216\270\354\247\221", nullptr));
        menuform->setTitle(QApplication::translate("QtApp_NotepadClass", "\354\204\234\354\213\235", nullptr));
        menuview->setTitle(QApplication::translate("QtApp_NotepadClass", "\353\263\264\352\270\260", nullptr));
        menuhelp->setTitle(QApplication::translate("QtApp_NotepadClass", "\353\217\204\354\233\200\353\247\220", nullptr));
    } // retranslateUi

};

namespace Ui {
    class QtApp_NotepadClass: public Ui_QtApp_NotepadClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_QTAPP_NOTEPAD_H
