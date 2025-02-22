# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'console.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPlainTextEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_ConsoleWidget(object):
    def setupUi(self, ConsoleWidget):
        if not ConsoleWidget.objectName():
            ConsoleWidget.setObjectName(u"ConsoleWidget")
        ConsoleWidget.resize(915, 394)
        ConsoleWidget.setStyleSheet(u"/* Console QWidget */\n"
"#ConsoleWidget {\n"
"	background-color: #1e1e1e;  /* Dark gray background */\n"
"    border-radius: 4px;          /* Rounded corners */\n"
"}\n"
"\n"
"/* QToolTip */\n"
"QToolTip {\n"
"    background-color: #2e2e2e;   /* Dark gray background */\n"
"    color: #ffffff;              /* White text */\n"
"    border: 1px solid #5b5e60;   /* Light gray border */\n"
"    padding: 4px;                /* Padding for the tooltip */\n"
"    border-radius: 4px;          /* Rounded corners */\n"
"    opacity: 200;                /* Slight transparency */\n"
"    font-size: 12px;             /* Slightly smaller font size for readability */\n"
"}\n"
"\n"
"/* QMenuBar */\n"
"QMenuBar {\n"
"    background-color: #2e2e2e;    /* Dark gray background */\n"
"    color: #ffffff;               /* White text */\n"
"    border-bottom: 1px solid #5b5e60;  /* Light gray border for separation */\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background-color: transparent; /* Transparent background */\n"
"    padding: "
                        "6px 6px;             /* Padding for menu items */\n"
"    color: #ffffff;                /* White text */\n"
"}\n"
"\n"
"QMenuBar::item:selected {          /* Hovered menu item */\n"
"    background-color: #4a90e2;     /* Light blue on hover */\n"
"    color: #ffffff;                /* Ensure text remains white */\n"
"}\n"
"\n"
"QMenuBar::item:pressed {           /* Pressed menu item */\n"
"    background-color: #3d78b2;     /* Darker blue on press */\n"
"    color: #ffffff;                /* Ensure text remains white */\n"
"}\n"
"\n"
"/* QMenu */\n"
"QMenu {\n"
"    background-color: #2e2e2e;     /* Dark gray background for menus */\n"
"    border: 1px solid #5b5e60;     /* Light gray border */\n"
"}\n"
"\n"
"QMenu::item {\n"
"    background-color: transparent; /* Transparent background for menu items */\n"
"    color: #ffffff;                /* White text */\n"
"	padding: 6px;\n"
"    margin-left: 6px;             /* Padding for each menu item */\n"
"}\n"
"\n"
"QMenu::item:selected {             /* Hovered m"
                        "enu item */\n"
"    background-color: #4a90e2;     /* Light blue background on hover */\n"
"    color: #ffffff;                /* Ensure text remains white */\n"
"}\n"
"\n"
"QMenu::item:pressed {              /* Pressed menu item */\n"
"    background-color: #3d78b2;     /* Darker blue background on press */\n"
"    color: #ffffff;                /* Ensure text remains white */\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    background-color: #5b5e60;     /* Light gray separator between items */\n"
"}\n"
"\n"
"/* QMenu::indicator (checkboxes and radio buttons in menus) */\n"
"QMenu::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    background-color: #2e2e2e;     /* Dark gray background for indicators */\n"
"    border: 1px solid #5b5e60;     /* Light gray border */\n"
"    border-radius: 2px;            /* Slightly rounded corners */\n"
"}\n"
"\n"
"QMenu::indicator:checked {\n"
"    background-color: #4a90e2;     /* Light blue when checked */\n"
"    border-color: #3d78b2;         /"
                        "* Darker blue border when checked */\n"
"}\n"
"\n"
"QMenu::indicator:unchecked {\n"
"    background-color: #2e2e2e;     /* Keep the dark gray when unchecked */\n"
"    border-color: #5b5e60;         /* Light gray border when unchecked */\n"
"}\n"
"\n"
"/* QToolBar */\n"
"QToolBar {\n"
"    background-color: #2e2e2e;      /* Dark gray background */\n"
"    border: 1px solid #5b5e60;      /* Light gray border */\n"
"    padding: 4px;                   /* Padding inside the toolbar */\n"
"    spacing: 4px;                   /* Spacing between toolbar buttons */\n"
"}\n"
"\n"
"QToolBar::handle {\n"
"    background-color: #5b5e60;      /* Light gray handle for draggable toolbars */\n"
"    width: 10px;                    /* Width of the handle */\n"
"	height: 10px;\n"
"    margin: 4px;                    /* Margin around the handle */\n"
"}\n"
"\n"
"QToolBar::separator {\n"
"    background-color: #5b5e60;      /* Light gray for separators */\n"
"    width: 1px;                     /* Thickness of the separator */\n"
""
                        "    height: 24px;                   /* Height of the separator */\n"
"    margin: 6px;                    /* Space around the separator */\n"
"}\n"
"\n"
"QToolBar::item {\n"
"    padding: 4px;                   /* Padding for individual toolbar items */\n"
"}\n"
"\n"
"/* QStatusBar */\n"
"QStatusBar {\n"
"    background-color: #2e2e2e;   /* Dark gray background */\n"
"    border-top: 1px solid #5b5e60; /* Light gray top border for separation */\n"
"    color: #ffffff;              /* White text */\n"
"    font-size: 13px;             /* Slightly smaller font for the status bar */\n"
"    padding: 6px;                /* Padding inside the status bar */\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    border: none;                /* No border around individual status items */\n"
"    padding: 0px 5px;            /* Padding between status bar items */\n"
"}\n"
"\n"
"QStatusBar QLabel {\n"
"    color: #ffffff;              /* White text for any QLabel inside the status bar */\n"
"    background-color: transparent; /* Ens"
                        "ure QLabel in status bar matches the bar's background */\n"
"}\n"
"\n"
"QStatusBar::indicator {\n"
"    background-color: #4a90e2;   /* Optional indicator styling, e.g., for icons or status signals */\n"
"    border-radius: 4px;          /* Rounded corners for any indicator elements */\n"
"}\n"
"\n"
"/* QGroupBox */\n"
"QGroupBox {\n"
"    background-color: #2e2e2e;        /* Dark gray background */\n"
"    border: 1px solid #5b5e60;        /* Light gray border */\n"
"    border-radius: 4px;               /* Rounded corners */\n"
"    margin-top: 15px;                 /* Space above the group box */\n"
"    padding-top: 0px;                    /* Padding inside the group box */\n"
"    color: #ffffff;                   /* White text for the title */\n"
"    font-weight: bold;                /* Bold title text */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;    /* Position the title at the top left */\n"
"    background-color: transparent;    /* Tran"
                        "sparent background for the title */\n"
"    padding: 0 5px;                   /* Padding around the title */\n"
"    color: #ffffff;                   /* White text for the title */\n"
"}\n"
"\n"
"QGroupBox::title:hover {\n"
"    color: #4a90e2;                   /* Light blue title on hover */\n"
"}\n"
"\n"
"QGroupBox:flat {\n"
"    border: none;                     /* No border when the group box is flat */\n"
"}\n"
"\n"
"QGroupBox:disabled {\n"
"    color: #777777;                   /* Lighter gray text for disabled group box */\n"
"    border-color: #5b5e60;            /* Keep the light gray border */\n"
"}\n"
"\n"
"/* QGraphicsView */\n"
"QGraphicsView {\n"
"    background-color: #2e2e2e;  /* Dark gray background */\n"
"    border: 1px solid #5b5e60;  /* Light gray border */\n"
"    border-radius: 4px;         /* Rounded corners */\n"
"}\n"
"\n"
"QGraphicsView:focus {\n"
"    border-color: #4a90e2;      /* Light blue border when focused */\n"
"    background-color: #333333;  /* Slightly lighter gray backg"
                        "round on focus */\n"
"}\n"
"\n"
"QGraphicsView:disabled {\n"
"    background-color: #2e2e2e;  /* Dark gray background when disabled */\n"
"    border-color: #5b5e60;      /* Light gray border for disabled state */\n"
"    color: #777777;             /* Lighter gray for disabled text or content */\n"
"}\n"
"\n"
"QGraphicsView::viewport {\n"
"    background-color: #2e2e2e;  /* Dark gray background for the viewport */\n"
"}\n"
"\n"
"/* QScrollArea\n"
"This covers around the outter edge, like 2-3px maybe */\n"
"QScrollArea {\n"
"    background-color: #2e2e2e;  /* Dark gray background */\n"
"    border: 1px solid #5b5e60;  /* Light gray border */\n"
"    border-radius: 4px;         /* Rounded corners */\n"
"    padding: 5px;               /* Padding inside the scroll area */\n"
"}\n"
"\n"
"/* Alternatively, this may also target the viewport more directly\n"
"This covers the whole area, including above/below the scrollbar */\n"
"QScrollArea QWidget {\n"
"    background-color: #2e2e2e;          /* Ensures all content"
                        " within is black */\n"
"}\n"
"\n"
"/* QScrollArea Viewport\n"
"This covers above/below the scrollbar */\n"
"QScrollArea > QWidget {\n"
"    background-color: #2e2e2e;          /* Background of the viewport widget */\n"
"}\n"
"\n"
"/* Scroll Corner (the area between horizontal and vertical scroll bars) */\n"
"QScrollArea::corner {\n"
"    background-color: #2e2e2e;  /* Dark gray to match the overall scroll area */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: #111;\n"
"    width: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #61657B;\n"
"    min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #ff6b27;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    border: none;\n"
"    width: 0;\n"
"    height: 0;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScroll"
                        "Bar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"/* QLabel */\n"
"QLabel {\n"
"    color: #ffffff;             /* White text */\n"
"}\n"
"\n"
"/* QFrame */\n"
"QFrame {\n"
"    background-color: #2e2e2e;  /* Dark gray for frames */\n"
"}\n"
"\n"
"/* QLineEdit */\n"
"QLineEdit {\n"
"    background-color: #2e2e2e;  /* Dark gray background for input fields */\n"
"    color: #ffffff;             /* White text */\n"
"    border: 1px solid #5b5e60;  /* Light gray border */\n"
"    border-radius: 4px;         /* Rounded corners */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #4a90e2;      /* Light blue border when focused */\n"
"    background-color: #333333;  /* Slightly lighter gray on focus */\n"
"}\n"
"\n"
"/* QListWidget */\n"
"QListWidget {\n"
"    background-color: #2e2e2e;      /* Dark gray background */\n"
"    color: #ffffff;                 /* White text */\n"
"    border: 1px solid #5b5e60;      /* Light gray border */\n"
"    padding: 4px;                   /* Padding around th"
                        "e list */\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    background-color: transparent;  /* Transparent background for items */\n"
"    color: #ffffff;                 /* White text for list items */\n"
"    border: none;                   /* No border for list items */\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #4a90e2;      /* Light blue background when selected */\n"
"    color: #ffffff;                 /* Ensure text remains white when selected */\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #3d78b2;      /* Darker blue on hover */\n"
"    color: #ffffff;                 /* Ensure text remains white when hovered */\n"
"}\n"
"\n"
"QListWidget::item:focus {\n"
"    border: 1px solid #4a90e2;      /* Light blue border on focus */\n"
"}\n"
"\n"
"/* QPlainTextEdit */\n"
"QPlainTextEdit {\n"
"    background-color: #2b2b2b;  /* Darker gray background for text area */\n"
"    color: #ffffff;             /* White text */\n"
"    border: 1px solid #5b5e60;  /* Light gray "
                        "border */\n"
"    border-radius: 0px;         /* No rounded corners */\n"
"    padding: 10px;              /* Comfortable padding for text input */\n"
"    line-height: 1.4;           /* Adjust line spacing for readability */\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border-color: #4a90e2;      /* Light blue border on focus */\n"
"    background-color: #3a3a3a;  /* Slightly lighter gray on focus */\n"
"}\n"
"\n"
"/* QTabWidget */\n"
"QTabWidget::pane {\n"
"    background-color: #2e2e2e;      /* Dark gray background */\n"
"    border: 1px solid #5b5e60;      /* Light gray border around the pane */\n"
"    padding: 4px;                   /* Padding inside the pane */\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0px;                      /* Space from the left */\n"
"}\n"
"\n"
"/* QTabBar::tab */\n"
"QTabBar::tab {\n"
"    background-color: #3c3f41;      /* Dark gray background for tabs */\n"
"    color: #ffffff;                 /* White text for tabs */\n"
"    border-left: 1px solid #5b5e60;      /* L"
                        "ight gray border around tabs */\n"
"    border-top: 1px solid #5b5e60;\n"
"    border-right: 1px solid #5b5e60;\n"
"    padding: 4px 8px;              /* Padding for each tab */\n"
"    margin-left: 2px;                    /* Slight margin between tabs */\n"
"    margin-right: 2px;\n"
"    border-top-left-radius: 4px;    /* Rounded top corners */\n"
"    border-top-right-radius: 4px;   /* Rounded top corners */\n"
"}\n"
"\n"
"/* Selected tab */\n"
"QTabBar::tab:selected {\n"
"    background-color: #4a90e2;      /* Light blue background for selected tab */\n"
"    color: #ffffff;                 /* White text for selected tab */\n"
"    border-color: #4a90e2;          /* Blue border for selected tab */\n"
"}\n"
"\n"
"/* Hovered tab */\n"
"QTabBar::tab:hover {\n"
"    background-color: #3d78b2;      /* Darker blue on hover */\n"
"    color: #ffffff;                 /* White text */\n"
"}\n"
"\n"
"/* Disabled tab */\n"
"QTabBar::tab:disabled {\n"
"    background-color: #2e2e2e;      /* Dark gray for disabled tab "
                        "*/\n"
"    color: #777777;                 /* Light gray text for disabled tabs */\n"
"}\n"
"\n"
"/* Focused tab */\n"
"QTabBar::tab:focus {\n"
"    border: 1px solid #4a90e2;      /* Blue border when tab is focused */\n"
"}\n"
"\n"
"/* Tab close button (optional) */\n"
"QTabBar::close-button {\n"
"    /* image: url(close-icon.png);     Replace with your close icon path */\n"
"    subcontrol-position: right;     /* Position the close button on the right */\n"
"    margin: 0 8px 0 0;              /* Spacing for the close button */\n"
"}\n"
"/*\n"
"QTabBar::close-button:hover {\n"
"    image: url(close-icon-hover.png);   Change icon on hover \n"
"}*/\n"
"\n"
"/* QComboBox */\n"
"QComboBox {\n"
"    background-color: #2e2e2e;       /* Dark gray background */\n"
"    color: #ffffff;                  /* White text */\n"
"    border: 1px solid #5b5e60;       /* Light gray border */\n"
"    border-radius: 4px;              /* Rounded corners */\n"
"    padding-left: 2px;                    /* Padding inside the combo"
                        " box */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #3a3a3a;       /* Slightly lighter gray on hover */\n"
"    border-color: #4a90e2;           /* Light blue border on hover */\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    background-color: #333333;       /* Lighter gray on focus */\n"
"    border-color: #4a90e2;           /* Light blue border on focus */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;                      /* Width of the drop-down button */\n"
"    background-color: #2e2e2e;        /* Dark gray background for drop-down */\n"
"    border-left: 1px solid #5b5e60;   /* Light gray separator between drop-down button and combo box */\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/888EAC-20px/ICONS/888EAC-20px/arrow-down.svg);  /*Replace with your down arrow icon */\n"
"    width: 12px;                         /* Width of the arrow */\n"
"    height: 12px;                        /* Height o"
                        "f the arrow */\n"
"}\n"
"\n"
"QComboBox::down-arrow:hover {\n"
"    image: url(:/888EAC-20px/ICONS/888EAC-20px/arrow-down.svg); /* Optional: different icon on hover */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #2e2e2e;        /* Dark gray background for drop-down list */\n"
"    color: #ffffff;                   /* White text */\n"
"    border: 1px solid #5b5e60;        /* Light gray border around the list */\n"
"    selection-background-color: #4a90e2;  /* Light blue background for selected item */\n"
"    selection-color: #ffffff;         /* White text for selected item */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    background-color: transparent;    /* Transparent background for list items */\n"
"    padding: 6px;                     /* Padding for each item in the list */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: #4a90e2;        /* Light blue when an item is selected */\n"
"    color: #ffffff;                   /* White "
                        "text for selected item */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #3d78b2;        /* Darker blue on hover */\n"
"    color: #ffffff;                   /* White text when hovered */\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color: #2e2e2e;        /* Dark gray background when disabled */\n"
"    color: #777777;                   /* Lighter gray text when disabled */\n"
"    border-color: #5b5e60;            /* Keep the light gray border */\n"
"}\n"
"\n"
"/* QPushButton */\n"
"QPushButton {\n"
"    background-color: #3c3f41;  /* Dark gray background */\n"
"    color: #ffffff;             /* White text */\n"
"    border: 1px solid #5b5e60;  /* Light gray border */\n"
"    border-radius: 4px;         /* Rounded corners */\n"
"	padding: 0px 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4a90e2;  /* Light blue on hover */\n"
"    border-color: #3d78b2;      /* Darker blue border */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color"
                        ": #3d78b2;  /* Darker blue on press */\n"
"    border-color: #2a5f92;      /* Even darker border when pressed */\n"
"}\n"
"\n"
"/* QCheckBox */\n"
"QCheckBox {\n"
"    color: #ffffff;                 /* White text for checkbox label */\n"
"    spacing: 6px;                   /* Space between checkbox and label */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 14px;                    /* Set the size of the checkbox */\n"
"    height: 14px;\n"
"    background-color: #2e2e2e;      /* Dark gray background for the checkbox */\n"
"    border: 1px solid #5b5e60;      /* Light gray border */\n"
"    border-radius: 2px;             /* Slight rounding for modern look */\n"
"}\n"
"\n"
"/* Hovered checkbox */\n"
"QCheckBox::indicator:hover {\n"
"    background-color: #3b73b4;      /* Light blue on hover */\n"
"    border-color: #ff050d;          /* Darker blue border on hover */\n"
"}\n"
"\n"
"/*\n"
"red: ff050d\n"
"green: 0dce1d\n"
"*/\n"
"\n"
"/* Checked checkbox */\n"
"QCheckBox::indicator:checked {\n"
"    back"
                        "ground-color: #4a90e2;      /* Light blue when checked */\n"
"    border-color: #3d78b2;          /* Darker blue border when checked */\n"
"/*    image: url(:/checked-icon.png);  Replace with your checkmark icon if needed */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border-color: #0dce1d;\n"
"}\n"
"\n"
"/* Indeterminate checkbox (for tri-state checkboxes) */\n"
"QCheckBox::indicator:indeterminate {\n"
"    background-color: #4a90e2;      /* Light blue when in indeterminate state */\n"
"    border-color: #3d78b2;          /* Darker blue border */\n"
"/*    image: url(:/indeterminate-icon.png);  Replace with your indeterminate icon */\n"
"}\n"
"\n"
"/* Pressed checkbox */\n"
"QCheckBox::indicator:pressed {\n"
"    background-color: #3d78b2;      /* Darker blue on press */\n"
"    border-color: #2a5f92;          /* Even darker border when pressed */\n"
"}\n"
"\n"
"/* Disabled checkbox */\n"
"QCheckBox::indicator:disabled {\n"
"    background-color: #2e2e2e;      /* Dark gray when disabled */\n"
""
                        "    border-color: #5b5e60;          /* Light gray border */\n"
"    color: #777777;                 /* Light gray label when disabled */\n"
"}\n"
"\n"
"/* QRadioButton */\n"
"QRadioButton {\n"
"    color: #ffffff;              /* White text */\n"
"    spacing: 5px;                /* Space between radio button and label */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 14px;                 /* Size of the radio button */\n"
"    height: 14px;\n"
"    background-color: #2e2e2e;   /* Dark gray background for the indicator */\n"
"    border: 1px solid #5b5e60;   /* Light gray border */\n"
"    border-radius: 8px;          /* Circular radio button */\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    background-color: #4a90e2;   /* Light blue on hover */\n"
"    border-color: #3d78b2;       /* Darker blue border on hover */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #4a90e2;   /* Light blue when checked */\n"
"    border-color: #3d78b2;       /* Darker blue border when c"
                        "hecked */\n"
"}\n"
"\n"
"QRadioButton::indicator:pressed {\n"
"    background-color: #3d78b2;   /* Darker blue on press */\n"
"    border-color: #2a5f92;       /* Even darker border on press */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:pressed {\n"
"    background-color: #3d78b2;   /* Darker blue when checked and pressed */\n"
"    border-color: #2a5f92;       /* Even darker border when checked and pressed */\n"
"}\n"
"\n"
"/* QToolButton */\n"
"QToolButton {\n"
"    background-color: #3c3f41;    /* Dark gray background */\n"
"    color: #ffffff;               /* White text/icon */\n"
"    border: 1px solid #5b5e60;    /* Light gray border */\n"
"    border-radius: 4px;           /* Rounded corners */\n"
"    padding: 0px 0px;            /* Padding for comfortable button size */\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #4a90e2;    /* Light blue background on hover */\n"
"    border-color: #3d78b2;        /* Darker blue border on hover */\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    bac"
                        "kground-color: #3d78b2;    /* Darker blue background on press */\n"
"    border-color: #2a5f92;        /* Even darker border when pressed */\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"    background-color: #3d78b2;    /* Darker blue when checked */\n"
"    border-color: #2a5f92;        /* Border color when checked */\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color: #2e2e2e;    /* Dark gray when disabled */\n"
"    color: #777777;               /* Lighter gray text/icon for disabled state */\n"
"    border-color: #5b5e60;        /* Keep the border color same as normal state */\n"
"}\n"
"\n"
"/* QToolButton::menu-button */\n"
"QToolButton::menu-button {\n"
"    background-color: #3c3f41;      /* Dark gray background for menu button */\n"
"    border: 1px solid #5b5e60;      /* Light gray border for menu button */\n"
"    padding: 4px;                   /* Padding for the menu button */\n"
"}\n"
"\n"
"QToolButton::menu-button:hover {\n"
"    background-color: #4a90e2;      /* Light blue on hover */\n"
""
                        "    border-color: #3d78b2;          /* Darker blue border on hover */\n"
"}\n"
"\n"
"QToolButton::menu-button:pressed {\n"
"    background-color: #3d78b2;      /* Darker blue on press */\n"
"    border-color: #2a5f92;          /* Even darker border on press */\n"
"}")
        self.verticalLayout = QVBoxLayout(ConsoleWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(ConsoleWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {background: transparent;}")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.console = QPlainTextEdit(self.frame)
        self.console.setObjectName(u"console")
        font = QFont()
        font.setPointSize(9)
        self.console.setFont(font)
        self.console.setFrameShape(QFrame.Shape.NoFrame)
        self.console.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.console.setReadOnly(True)
        self.console.setTabStopDistance(16.000000000000000)

        self.horizontalLayout_2.addWidget(self.console)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(ConsoleWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame {\n"
"    border: 1px solid #555;\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.close_console_btn = QPushButton(self.frame_2)
        self.close_console_btn.setObjectName(u"close_console_btn")

        self.horizontalLayout.addWidget(self.close_console_btn)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(ConsoleWidget)

        QMetaObject.connectSlotsByName(ConsoleWidget)
    # setupUi

    def retranslateUi(self, ConsoleWidget):
        ConsoleWidget.setWindowTitle(QCoreApplication.translate("ConsoleWidget", u"ConsoleWidget", None))
        self.console.setPlaceholderText(QCoreApplication.translate("ConsoleWidget", u"Build Mod Console...", None))
        self.close_console_btn.setText(QCoreApplication.translate("ConsoleWidget", u"Close Console", None))
    # retranslateUi

