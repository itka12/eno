/********************************************************************************
** Form generated from reading UI file 'QtWidgets_14week.ui'
**
** Created by: Qt User Interface Compiler version 5.12.12
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_QTWIDGETS_14WEEK_H
#define UI_QTWIDGETS_14WEEK_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPlainTextEdit>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_QtWidgets_14weekClass
{
public:
    QAction *action_new;
    QAction *action_2;
    QAction *action_open;
    QAction *action_save;
    QAction *action_exit;
    QWidget *centralWidget;
    QPlainTextEdit *plainTextEdit;
    QMenuBar *menuBar;
    QMenu *menu_file;
    QMenu *menu_edit;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *QtWidgets_14weekClass)
    {
        if (QtWidgets_14weekClass->objectName().isEmpty())
            QtWidgets_14weekClass->setObjectName(QString::fromUtf8("QtWidgets_14weekClass"));
        QtWidgets_14weekClass->resize(711, 394);
        action_new = new QAction(QtWidgets_14weekClass);
        action_new->setObjectName(QString::fromUtf8("action_new"));
        action_2 = new QAction(QtWidgets_14weekClass);
        action_2->setObjectName(QString::fromUtf8("action_2"));
        action_open = new QAction(QtWidgets_14weekClass);
        action_open->setObjectName(QString::fromUtf8("action_open"));
        action_save = new QAction(QtWidgets_14weekClass);
        action_save->setObjectName(QString::fromUtf8("action_save"));
        action_exit = new QAction(QtWidgets_14weekClass);
        action_exit->setObjectName(QString::fromUtf8("action_exit"));
        centralWidget = new QWidget(QtWidgets_14weekClass);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        centralWidget->setEnabled(true);
        plainTextEdit = new QPlainTextEdit(centralWidget);
        plainTextEdit->setObjectName(QString::fromUtf8("plainTextEdit"));
        plainTextEdit->setGeometry(QRect(0, 0, 241, 281));
        QtWidgets_14weekClass->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(QtWidgets_14weekClass);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 711, 18));
        menu_file = new QMenu(menuBar);
        menu_file->setObjectName(QString::fromUtf8("menu_file"));
        menu_edit = new QMenu(menuBar);
        menu_edit->setObjectName(QString::fromUtf8("menu_edit"));
        QtWidgets_14weekClass->setMenuBar(menuBar);
        mainToolBar = new QToolBar(QtWidgets_14weekClass);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        QtWidgets_14weekClass->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(QtWidgets_14weekClass);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        QtWidgets_14weekClass->setStatusBar(statusBar);

        menuBar->addAction(menu_file->menuAction());
        menuBar->addAction(menu_edit->menuAction());
        menu_file->addAction(action_new);
        menu_file->addAction(action_open);
        menu_file->addAction(action_save);
        menu_file->addSeparator();
        menu_file->addAction(action_exit);

        retranslateUi(QtWidgets_14weekClass);

        QMetaObject::connectSlotsByName(QtWidgets_14weekClass);
    } // setupUi

    void retranslateUi(QMainWindow *QtWidgets_14weekClass)
    {
        QtWidgets_14weekClass->setWindowTitle(QApplication::translate("QtWidgets_14weekClass", "\353\251\224\353\252\250\354\236\245", nullptr));
        action_new->setText(QApplication::translate("QtWidgets_14weekClass", "\354\203\210\353\241\234 \353\247\214\353\223\244\352\270\260", nullptr));
        action_2->setText(QApplication::translate("QtWidgets_14weekClass", "\354\203\210 \354\260\275", nullptr));
        action_open->setText(QApplication::translate("QtWidgets_14weekClass", "\354\227\264\352\270\260", nullptr));
        action_save->setText(QApplication::translate("QtWidgets_14weekClass", "\354\240\200\354\236\245", nullptr));
        action_exit->setText(QApplication::translate("QtWidgets_14weekClass", "\353\201\235\353\202\264\352\270\260", nullptr));
        menu_file->setTitle(QApplication::translate("QtWidgets_14weekClass", "\355\214\214\354\235\274", nullptr));
        menu_edit->setTitle(QApplication::translate("QtWidgets_14weekClass", "\355\216\270\354\247\221", nullptr));
    } // retranslateUi

};

namespace Ui {
    class QtWidgets_14weekClass: public Ui_QtWidgets_14weekClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_QTWIDGETS_14WEEK_H
