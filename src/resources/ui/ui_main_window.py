# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowwFuZeE.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)
import src.resources.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(449, 634)
        MainWindow.setMinimumSize(QSize(449, 634))
        MainWindow.setMaximumSize(QSize(449, 734))
        icon = QIcon()
        icon.addFile(u":/icons/icons/logo2-transparent.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"/* QToolTip */\n"
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
"    padding: 6px 6px;             /* Padding for menu items */\n"
"    color: #ffffff;                /* White text */\n"
"}\n"
"\n"
"QMenuBar::item:selected {          /* Hovered menu item "
                        "*/\n"
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
"QMenu::item:selected {             /* Hovered menu item */\n"
"    background-color: #4a90e2;     /* Light blue background on hover */\n"
"    color: #ffffff;                /* Ensure text remains white */\n"
"}\n"
"\n"
"QMe"
                        "nu::item:pressed {              /* Pressed menu item */\n"
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
"    border-color: #3d78b2;         /* Darker blue border when checked */\n"
"}\n"
"\n"
"QMenu::indicator:unchecked {\n"
"    background-color: #2e2e2e;     /* Keep the dark gray when unchecked */\n"
"    border-co"
                        "lor: #5b5e60;         /* Light gray border when unchecked */\n"
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
"    height: 24px;                   /* Height of the separator */\n"
"    margin: 6px;                    /* Space around the separator */\n"
"}\n"
"\n"
"QToolBar::item {\n"
""
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
"    background-color: transparent; /* Ensure QLabel in status bar matches the bar's background */\n"
"}\n"
"\n"
"QStatusBar::indicator {\n"
"    background-color: #4a90e2;   /* Optional indicator styling, e.g., for i"
                        "cons or status signals */\n"
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
"    background-color: transparent;    /* Transparent background for the title */\n"
"    padding: 0 5px;                   /* Padding around the title */\n"
"    color: #ffffff;                   /* White text for the ti"
                        "tle */\n"
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
"    background-color: #333333;  /* Slightly lighter gray background on focus */\n"
"}\n"
"\n"
"QGraphicsView:disabled {\n"
"    background-color: #2e2e2e;  /* Dark gray background when disabled */\n"
"    border-color: #5b5e60;      /* L"
                        "ight gray border for disabled state */\n"
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
"    background-color: #2e2e2e;          /* Ensures all content within is black */\n"
"}\n"
"\n"
"/* QScrollArea Viewport\n"
"This covers above/below the scrollbar */\n"
"QScrollArea > QWidget {\n"
"    background-color: #2e2e2e;         "
                        " /* Background of the viewport widget */\n"
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
"    min-height: 15px;\n"
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
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"/* QLabel */\n"
"QLabel {\n"
"    color: #ffffff;             /* White text */\n"
"}\n"
"\n"
"/* QFrame */\n"
""
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
"    padding: 4px;                   /* Padding around the list */\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    background-color: transparent;  /* Transparent background for items */\n"
"    color: #ffffff;                 /* White text"
                        " for list items */\n"
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
"    border: 1px solid #5b5e60;  /* Light gray border */\n"
"    border-radius: 0px;         /* No rounded corners */\n"
"    padding: 10px;              /* Comfortable padding for text input */\n"
"    font-size: 13px;     "
                        "       /* Slightly smaller font */\n"
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
"    border-left: 1px solid #5b5e60;      /* Light gray border around tabs */\n"
"    border-top: 1px solid #5b5e60;\n"
"    border-right: 1px solid #5b5e60;\n"
""
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
"    background-color: #2e2e2e;      /* Dark gray for disabled tab */\n"
"    color: #777777;                 /* Light gray text for disabled tabs */\n"
"}\n"
"\n"
"/* Focused tab */\n"
""
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
"    padding-left: 2px;                    /* Padding inside the combo box */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #3a3a3a;       /* Slightly lighter gray on hover */\n"
""
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
"    height: 12px;                        /* Height of the arrow */\n"
"}\n"
"\n"
"QComboBox::down-arrow:hover {\n"
"    image: url(:/888EAC-20px/ICONS/888EAC-20px/arrow-down.s"
                        "vg); /* Optional: different icon on hover */\n"
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
"    color: #ffffff;                   /* White text for selected item */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #3d78b2;      "
                        "  /* Darker blue on hover */\n"
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
"    background-color: #3d78b2;  /* Darker blue on press */\n"
"    border-color: #2a5f92;      /* Even darker border when pressed */\n"
"}\n"
""
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
"    border-color: #0dce1d;          /* Darker blue border on hover */\n"
"}\n"
"\n"
"/*\n"
"red: ff050d\n"
"green: 0dce1d\n"
"*/\n"
"\n"
"/* Checked checkbox */\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #4a90e2;      /* Light blue when checked */\n"
"    border-color: #3d78b2;          /* Darker blue border whe"
                        "n checked */\n"
"/*    image: url(:/checked-icon.png);  Replace with your checkmark icon if needed */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border-color: #ff050d;\n"
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
"    border-color: #5b5e60;          /* Light gray border */\n"
"    color: #777777;                 /* Light gray label wh"
                        "en disabled */\n"
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
"    border-color: #3d78b2;       /* Darker blue border when checked */\n"
"}\n"
"\n"
"QRadioButton::indicator:pressed {\n"
"    background-color: #3d78b2;   /* Darker blue on press */"
                        "\n"
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
"    background-color: #3d78b2;    /* Darker blue background on press */\n"
"    border-color: #2a5f92;        /* Even darker bord"
                        "er when pressed */\n"
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
"    border-color: #3d78b2;          /* Darker blue border on hover */\n"
"}\n"
"\n"
"QToolButton::menu-button:pressed {"
                        "\n"
"    background-color: #3d78b2;      /* Darker blue on press */\n"
"    border-color: #2a5f92;          /* Even darker border on press */\n"
"}")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"/* Central Widget */\n"
"#centralwidget {\n"
"    background-color: #1e1e1e;  /* Dark gray background */\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet(u"QFrame {margin: 6px;}")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setStyleSheet(u"QFrame {margin: 0px;}")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mod_name_input = QLineEdit(self.frame_5)
        self.mod_name_input.setObjectName(u"mod_name_input")
        self.mod_name_input.setMinimumSize(QSize(0, 28))
        self.mod_name_input.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.mod_name_input.setStyleSheet(u"QLineEdit {padding: 3px;}")
        self.mod_name_input.setMaxLength(35)

        self.horizontalLayout_2.addWidget(self.mod_name_input)

        self.submit_btn = QPushButton(self.frame_5)
        self.submit_btn.setObjectName(u"submit_btn")
        self.submit_btn.setStyleSheet(u"QPushButton {padding: 5px;}")

        self.horizontalLayout_2.addWidget(self.submit_btn)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"QLabel {color: #888eac; padding-left: 3px;}")

        self.verticalLayout_2.addWidget(self.label_3)

        self.shortcut_cbox = QCheckBox(self.frame)
        self.shortcut_cbox.setObjectName(u"shortcut_cbox")
        self.shortcut_cbox.setStyleSheet(u"QCheckBox {padding-left: 5px;}")

        self.verticalLayout_2.addWidget(self.shortcut_cbox)

        self.insert_ingame_print_msg_cbox = QCheckBox(self.frame)
        self.insert_ingame_print_msg_cbox.setObjectName(u"insert_ingame_print_msg_cbox")
        self.insert_ingame_print_msg_cbox.setStyleSheet(u"QCheckBox {padding-left: 5px;}")

        self.verticalLayout_2.addWidget(self.insert_ingame_print_msg_cbox)

        self.build_mod_cbox = QCheckBox(self.frame)
        self.build_mod_cbox.setObjectName(u"build_mod_cbox")
        self.build_mod_cbox.setStyleSheet(u"QCheckBox {padding-left: 5px;}")

        self.verticalLayout_2.addWidget(self.build_mod_cbox)

        self.run_map_cbox = QCheckBox(self.frame)
        self.run_map_cbox.setObjectName(u"run_map_cbox")
        self.run_map_cbox.setStyleSheet(u"QCheckBox {padding-left: 5px;}")

        self.verticalLayout_2.addWidget(self.run_map_cbox)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.groupBox.setMinimumSize(QSize(0, 158))
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.groupBox)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 397, 330))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(3, 3, 3, 3)
        self.sp_ber1_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_ber1_cbox.setObjectName(u"sp_ber1_cbox")

        self.verticalLayout_9.addWidget(self.sp_ber1_cbox)

        self.sp_ber2_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_ber2_cbox.setObjectName(u"sp_ber2_cbox")

        self.verticalLayout_9.addWidget(self.sp_ber2_cbox)

        self.sp_ber3_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_ber3_cbox.setObjectName(u"sp_ber3_cbox")

        self.verticalLayout_9.addWidget(self.sp_ber3_cbox)

        self.sp_ber3b_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_ber3b_cbox.setObjectName(u"sp_ber3b_cbox")

        self.verticalLayout_9.addWidget(self.sp_ber3b_cbox)

        self.sp_mak_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_mak_cbox.setObjectName(u"sp_mak_cbox")

        self.verticalLayout_9.addWidget(self.sp_mak_cbox)

        self.sp_oki2_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_oki2_cbox.setObjectName(u"sp_oki2_cbox")

        self.verticalLayout_9.addWidget(self.sp_oki2_cbox)

        self.sp_oki3_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_oki3_cbox.setObjectName(u"sp_oki3_cbox")

        self.verticalLayout_9.addWidget(self.sp_oki3_cbox)

        self.sp_pby_fly_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_pby_fly_cbox.setObjectName(u"sp_pby_fly_cbox")

        self.verticalLayout_9.addWidget(self.sp_pby_fly_cbox)

        self.sp_pel1_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_pel1_cbox.setObjectName(u"sp_pel1_cbox")

        self.verticalLayout_9.addWidget(self.sp_pel1_cbox)

        self.sp_pel1a_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_pel1a_cbox.setObjectName(u"sp_pel1a_cbox")

        self.verticalLayout_9.addWidget(self.sp_pel1a_cbox)

        self.sp_pel1b_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_pel1b_cbox.setObjectName(u"sp_pel1b_cbox")

        self.verticalLayout_9.addWidget(self.sp_pel1b_cbox)

        self.sp_pel2_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_pel2_cbox.setObjectName(u"sp_pel2_cbox")

        self.verticalLayout_9.addWidget(self.sp_pel2_cbox)

        self.sp_see1_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_see1_cbox.setObjectName(u"sp_see1_cbox")

        self.verticalLayout_9.addWidget(self.sp_see1_cbox)

        self.sp_see2_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_see2_cbox.setObjectName(u"sp_see2_cbox")

        self.verticalLayout_9.addWidget(self.sp_see2_cbox)

        self.sp_sniper_cbox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.sp_sniper_cbox.setObjectName(u"sp_sniper_cbox")

        self.verticalLayout_9.addWidget(self.sp_sniper_cbox)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_3.addWidget(self.scrollArea_2)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_4 = QGroupBox(self.frame)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy2.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy2)
        self.groupBox_4.setMinimumSize(QSize(0, 158))
        self.groupBox_4.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_4.setStyleSheet(u"QGroupBox {border: none;}")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.groupBox_4)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setStyleSheet(u"QScrollBar::handle:vertical {\n"
"    min-height: 40px;\n"
"}")
        self.scrollArea_3.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_3.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 397, 506))
        self.scrollAreaWidgetContents_3.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(3, 3, 3, 3)
        self.mp_airfield_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_airfield_cbox.setObjectName(u"mp_airfield_cbox")

        self.verticalLayout_11.addWidget(self.mp_airfield_cbox)

        self.mp_asylum_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_asylum_cbox.setObjectName(u"mp_asylum_cbox")

        self.verticalLayout_11.addWidget(self.mp_asylum_cbox)

        self.mp_kwai_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_kwai_cbox.setObjectName(u"mp_kwai_cbox")

        self.verticalLayout_11.addWidget(self.mp_kwai_cbox)

        self.mp_drum_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_drum_cbox.setObjectName(u"mp_drum_cbox")

        self.verticalLayout_11.addWidget(self.mp_drum_cbox)

        self.mp_bgate_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_bgate_cbox.setObjectName(u"mp_bgate_cbox")

        self.verticalLayout_11.addWidget(self.mp_bgate_cbox)

        self.mp_castle_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_castle_cbox.setObjectName(u"mp_castle_cbox")

        self.verticalLayout_11.addWidget(self.mp_castle_cbox)

        self.mp_shrine_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_shrine_cbox.setObjectName(u"mp_shrine_cbox")

        self.verticalLayout_11.addWidget(self.mp_shrine_cbox)

        self.mp_stalingrad_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_stalingrad_cbox.setObjectName(u"mp_stalingrad_cbox")

        self.verticalLayout_11.addWidget(self.mp_stalingrad_cbox)

        self.mp_courtyard_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_courtyard_cbox.setObjectName(u"mp_courtyard_cbox")

        self.verticalLayout_11.addWidget(self.mp_courtyard_cbox)

        self.mp_dome_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_dome_cbox.setObjectName(u"mp_dome_cbox")

        self.verticalLayout_11.addWidget(self.mp_dome_cbox)

        self.mp_downfall_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_downfall_cbox.setObjectName(u"mp_downfall_cbox")

        self.verticalLayout_11.addWidget(self.mp_downfall_cbox)

        self.mp_hangar_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_hangar_cbox.setObjectName(u"mp_hangar_cbox")

        self.verticalLayout_11.addWidget(self.mp_hangar_cbox)

        self.mp_kneedeep_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_kneedeep_cbox.setObjectName(u"mp_kneedeep_cbox")

        self.verticalLayout_11.addWidget(self.mp_kneedeep_cbox)

        self.mp_makin_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_makin_cbox.setObjectName(u"mp_makin_cbox")

        self.verticalLayout_11.addWidget(self.mp_makin_cbox)

        self.mp_makin_day_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_makin_day_cbox.setObjectName(u"mp_makin_day_cbox")

        self.verticalLayout_11.addWidget(self.mp_makin_day_cbox)

        self.mp_nachtfeuer_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_nachtfeuer_cbox.setObjectName(u"mp_nachtfeuer_cbox")

        self.verticalLayout_11.addWidget(self.mp_nachtfeuer_cbox)

        self.mp_outskirts_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_outskirts_cbox.setObjectName(u"mp_outskirts_cbox")

        self.verticalLayout_11.addWidget(self.mp_outskirts_cbox)

        self.mp_vodka_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_vodka_cbox.setObjectName(u"mp_vodka_cbox")

        self.verticalLayout_11.addWidget(self.mp_vodka_cbox)

        self.mp_roundhouse_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_roundhouse_cbox.setObjectName(u"mp_roundhouse_cbox")

        self.verticalLayout_11.addWidget(self.mp_roundhouse_cbox)

        self.mp_seelow_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_seelow_cbox.setObjectName(u"mp_seelow_cbox")

        self.verticalLayout_11.addWidget(self.mp_seelow_cbox)

        self.mp_subway_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_subway_cbox.setObjectName(u"mp_subway_cbox")

        self.verticalLayout_11.addWidget(self.mp_subway_cbox)

        self.mp_docks_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_docks_cbox.setObjectName(u"mp_docks_cbox")

        self.verticalLayout_11.addWidget(self.mp_docks_cbox)

        self.mp_suburban_cbox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.mp_suburban_cbox.setObjectName(u"mp_suburban_cbox")

        self.verticalLayout_11.addWidget(self.mp_suburban_cbox)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_10.addWidget(self.scrollArea_3)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 111))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.zm_prototype_cbox = QCheckBox(self.groupBox_2)
        self.zm_prototype_cbox.setObjectName(u"zm_prototype_cbox")

        self.verticalLayout_4.addWidget(self.zm_prototype_cbox)

        self.zm_asylum_cbox = QCheckBox(self.groupBox_2)
        self.zm_asylum_cbox.setObjectName(u"zm_asylum_cbox")

        self.verticalLayout_4.addWidget(self.zm_asylum_cbox)

        self.zm_sumpf_cbox = QCheckBox(self.groupBox_2)
        self.zm_sumpf_cbox.setObjectName(u"zm_sumpf_cbox")

        self.verticalLayout_4.addWidget(self.zm_sumpf_cbox)

        self.zm_factory_cbox = QCheckBox(self.groupBox_2)
        self.zm_factory_cbox.setObjectName(u"zm_factory_cbox")

        self.verticalLayout_4.addWidget(self.zm_factory_cbox)


        self.verticalLayout_2.addWidget(self.groupBox_2)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ModOps HQ - WaW-Stock-Map-Script-Placer", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
#if QT_CONFIG(tooltip)
        self.mod_name_input.setToolTip(QCoreApplication.translate("MainWindow", u"35 char limit", None))
#endif // QT_CONFIG(tooltip)
        self.mod_name_input.setText("")
        self.mod_name_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter ModName", None))
        self.submit_btn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ModName Example: nazi_zombie_prototype | nacht | myTestMap1", None))
#if QT_CONFIG(tooltip)
        self.shortcut_cbox.setToolTip(QCoreApplication.translate("MainWindow", u"e.g.\n"
"'+set fs_game mods/{self.modName} +devmap {self.mapName} +set r_fullscreen 0'", None))
#endif // QT_CONFIG(tooltip)
        self.shortcut_cbox.setText(QCoreApplication.translate("MainWindow", u"Add shortcut to desktop (w/ args) ..for quick map loading ?", None))
#if QT_CONFIG(tooltip)
        self.insert_ingame_print_msg_cbox.setToolTip(QCoreApplication.translate("MainWindow", u"Example of in-game print message:\n"
"'zm_test1 built successfully!'\n"
"\n"
"Currently only available for mode: zm", None))
#endif // QT_CONFIG(tooltip)
        self.insert_ingame_print_msg_cbox.setText(QCoreApplication.translate("MainWindow", u"Insert an in-game print message to confirm build ?", None))
        self.build_mod_cbox.setText(QCoreApplication.translate("MainWindow", u"Build Mod ?", None))
        self.run_map_cbox.setText(QCoreApplication.translate("MainWindow", u"Run Map ?", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"SP", None))
        self.sp_ber1_cbox.setText(QCoreApplication.translate("MainWindow", u"Ring of Steel (ber1)", None))
        self.sp_ber2_cbox.setText(QCoreApplication.translate("MainWindow", u"Eviction (ber2)", None))
        self.sp_ber3_cbox.setText(QCoreApplication.translate("MainWindow", u"Heart of the Reich (ber3)", None))
        self.sp_ber3b_cbox.setText(QCoreApplication.translate("MainWindow", u"Downfall (ber3b)", None))
        self.sp_mak_cbox.setText(QCoreApplication.translate("MainWindow", u"Semper Fi (mak)", None))
        self.sp_oki2_cbox.setText(QCoreApplication.translate("MainWindow", u"Blowtorch & Corkscrew (oki2)", None))
        self.sp_oki3_cbox.setText(QCoreApplication.translate("MainWindow", u"Breaking Point (oki3)", None))
        self.sp_pby_fly_cbox.setText(QCoreApplication.translate("MainWindow", u"Black Cats (pby_fly)", None))
        self.sp_pel1_cbox.setText(QCoreApplication.translate("MainWindow", u"Little Resistance (pel1)", None))
        self.sp_pel1a_cbox.setText(QCoreApplication.translate("MainWindow", u"Burn 'Em Out (pel1a)", None))
        self.sp_pel1b_cbox.setText(QCoreApplication.translate("MainWindow", u"Relentless (pel1b)", None))
        self.sp_pel2_cbox.setText(QCoreApplication.translate("MainWindow", u"Hard Landing (pel2)", None))
        self.sp_see1_cbox.setText(QCoreApplication.translate("MainWindow", u"Their Land, Their Blood (see1)", None))
        self.sp_see2_cbox.setText(QCoreApplication.translate("MainWindow", u"Blood and Iron (see2)", None))
        self.sp_sniper_cbox.setText(QCoreApplication.translate("MainWindow", u"Vendetta (sniper)", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"MP", None))
        self.mp_airfield_cbox.setText(QCoreApplication.translate("MainWindow", u"Airfield (mp_airfield)", None))
        self.mp_asylum_cbox.setText(QCoreApplication.translate("MainWindow", u"Asylum (mp_asylum)", None))
        self.mp_kwai_cbox.setText(QCoreApplication.translate("MainWindow", u"Banzai (mp_kwai)", None))
        self.mp_drum_cbox.setText(QCoreApplication.translate("MainWindow", u"Battery (mp_drum)", None))
        self.mp_bgate_cbox.setText(QCoreApplication.translate("MainWindow", u"Breach (mp_bgate)", None))
        self.mp_castle_cbox.setText(QCoreApplication.translate("MainWindow", u"Castle (mp_castle)", None))
        self.mp_shrine_cbox.setText(QCoreApplication.translate("MainWindow", u"Cliffside (mp_shrine)", None))
        self.mp_stalingrad_cbox.setText(QCoreApplication.translate("MainWindow", u"Corrosion (mp_stalingrad)", None))
        self.mp_courtyard_cbox.setText(QCoreApplication.translate("MainWindow", u"Courtyard (mp_courtyard)", None))
        self.mp_dome_cbox.setText(QCoreApplication.translate("MainWindow", u"Dome (mp_dome)", None))
        self.mp_downfall_cbox.setText(QCoreApplication.translate("MainWindow", u"Downfall (mp_downfall)", None))
        self.mp_hangar_cbox.setText(QCoreApplication.translate("MainWindow", u"Hangar (mp_hangar)", None))
        self.mp_kneedeep_cbox.setText(QCoreApplication.translate("MainWindow", u"Knee Deep (mp_kneedeep)", None))
        self.mp_makin_cbox.setText(QCoreApplication.translate("MainWindow", u"Makin (mp_makin)", None))
        self.mp_makin_day_cbox.setText(QCoreApplication.translate("MainWindow", u"Makin Day (mp_makin_day)", None))
        self.mp_nachtfeuer_cbox.setText(QCoreApplication.translate("MainWindow", u"Nightfire (mp_nachtfeuer)", None))
        self.mp_outskirts_cbox.setText(QCoreApplication.translate("MainWindow", u"Outskirts (mp_outskirts)", None))
        self.mp_vodka_cbox.setText(QCoreApplication.translate("MainWindow", u"Revolution (mp_vodka)", None))
        self.mp_roundhouse_cbox.setText(QCoreApplication.translate("MainWindow", u"Roundhouse (mp_roundhouse)", None))
        self.mp_seelow_cbox.setText(QCoreApplication.translate("MainWindow", u"Seelow (mp_seelow)", None))
        self.mp_subway_cbox.setText(QCoreApplication.translate("MainWindow", u"Station (mp_subway)", None))
        self.mp_docks_cbox.setText(QCoreApplication.translate("MainWindow", u"Sub Pens (mp_docks)", None))
        self.mp_suburban_cbox.setText(QCoreApplication.translate("MainWindow", u"Upheaval (mp_suburban)", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"ZM", None))
        self.zm_prototype_cbox.setText(QCoreApplication.translate("MainWindow", u"Nacht der Untoten (nazi_zombie_prototype)", None))
        self.zm_asylum_cbox.setText(QCoreApplication.translate("MainWindow", u"Verr\u00fcckt (nazi_zombie_asylum)", None))
        self.zm_sumpf_cbox.setText(QCoreApplication.translate("MainWindow", u"Shi No Numa (nazi_zombie_sumpf)", None))
        self.zm_factory_cbox.setText(QCoreApplication.translate("MainWindow", u"Der Riese (nazi_zombie_factory)", None))
    # retranslateUi

