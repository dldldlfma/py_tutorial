import sys

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from PyQt5 import uic

from pprint import pprint

import cv2 as cv

Calui ='./ui.ui'

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(Calui,self)
        
        self.finder_Btn.clicked.connect(self.file_loader)
        self.save_Btn.clicked.connect(self.file_save)
        self.model = QStandardItemModel()
        self.file_list = []

        self.Binary_Btn.stateChanged.connect(self.check_state)
        self.Median_Btn.stateChanged.connect(self.check_state)

        self.median = 0
        self.binary = 0

    def check_state(self):
        if(self.Binary_Btn.checkState()):
            self.binary=1
        else:
            self.binary=0

        if(self.Median_Btn.checkState()):
            self.median=1
        else:
            self.median=0


    def file_loader(self):
        fname = QFileDialog.getOpenFileName(self)
        self.file_position.setText(fname[0])
        pixmap=QPixmap(fname[0])
        self.label.setPixmap(QPixmap(pixmap))
        self.model.appendRow(QStandardItem(fname[0]))
        self.listView.setModel(self.model)
        self.file_list.append(fname[0])
    
    def file_save(self):
        save_position = QFileDialog.getExistingDirectory(self)  #select save folder
        self.save_position.setText(save_position)


        for i,value in enumerate(self.file_list):
            if(self.binary):
                img = cv.imread(value,0)
            else:
                img = cv.imread(value,cv.IMREAD_COLOR)
            if(self.median):
                img = cv.medianBlur(img,5)
            if(self.binary):
                img = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 5)
            save_path = save_position + '_fix_'+ str(i) + value[value.find('.'):]
            cv.imwrite(save_path,img)
            cv.imshow('binary_img',img)
            cv.waitKey(0)

if __name__ =='__main__':
    app = QApplication(sys.argv)
    main_dialog=MainDialog()
    main_dialog.show()
    app.exec_() #event loop 진입
