import sys
from datetime import datetime

import mysql.connector
import pandas as pd
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox, QFileDialog, QLabel, QPushButton, QWidget, QVBoxLayout, QTableWidget
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap

from CNC_Data import Ui_MainWindow

class ConnectToMySQL():
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = '123456'
        self.port = '3306'
        self.database = 'cnc_data'
        self.con = None

    def connect(self):
        """
        create connect with database
        """
        self.con = mysql.connector.connect(
            host=self.host,
            user=self.user,
            passwd=self.password,
            port=self.port,
            database=self.database
        )

    def get_all_data_from_db(self):
        try:
            self.connect()
            cursor = self.con.cursor(dictionary=True)
            sql = "SELECT * FROM spindle;"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

        except Exception as e:
            print("get data fail")
            print(e)

        finally:
            if self.con:
                self.con.close()

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 200, 800, 550)
        self.setWindowTitle('Descriptions')
        self.label = QLabel(self)

        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(['Message', 'Description'])

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        self.setLayout(layout)

        self.update_data()


    def update_data(self):
        ## another connect to db
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456',
            database='cnc_data'
        )
        cursor = db.cursor()
        cursor.execute('SELECT Message, Description FROM Descriptions;')
        results = cursor.fetchall()
        db.close()

        ## clearing table
        self.table_widget.clearContents()
        self.table_widget.setRowCount(0)

        ## filling the table with data from the database
        for row_number, row_data in enumerate(results):
            self.table_widget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.table_widget.setItem(row_number, column_number, item)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.get_data_btn = self.ui.get_data_btn
        self.select_save_path_btn = self.ui.get_path_btn
        self.save_btn = self.ui.save_btn
        self.file_path = self.ui.lineEdit
        self.result_table = self.ui.tableWidget
        self.plot = self.ui.graphicsView

        self.button = QPushButton('Descriptions', self)
        self.button.move(750, 110)
        self.button.clicked.connect(self.open_second_window)


        label = QLabel(self)
        pixmap = QPixmap("icons/graph.XAcqp.png")
        label.setPixmap(pixmap)
        label.setGeometry(18, 380, 961, 261)
        self.layout().addWidget(label)
        self.show()

    def open_second_window(self):

        self.second_window = SecondWindow()
        self.second_window.show()

    @pyqtSlot(bool)
    def on_get_data_btn_clicked(self):
        result = ConnectToMySQL().get_all_data_from_db()

        if result:
            self.result_table.setRowCount(len(result))

            for row, item in enumerate(result):
                column_1_item = QTableWidgetItem(str(item['Spindle_ID']))
                column_2_item = QTableWidgetItem(str(item['Speed']))
                column_3_item = QTableWidgetItem(str(item['Gear']))
                column_4_item = QTableWidgetItem(str(item['Power']))
                column_5_item = QTableWidgetItem(str(item['Position']))
                column_6_item = QTableWidgetItem(str(item['Torque']))

                self.result_table.setItem(row, 0, column_1_item)
                self.result_table.setItem(row, 1, column_2_item)
                self.result_table.setItem(row, 2, column_3_item)
                self.result_table.setItem(row, 3, column_4_item)
                self.result_table.setItem(row, 4, column_5_item)
                self.result_table.setItem(row, 5, column_6_item)

        else:
            ## show some message if no data got from db
            QMessageBox.information(self, 'Warning', 'No data got from database, please try again')
            return

    @pyqtSlot(bool)
    def on_get_path_btn_clicked(self):
        """
        get save file path
        """
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            self.file_path.setText(folder_path)


    @pyqtSlot(bool)
    def on_save_btn_clicked(self):
        """
        save data to excel
        """
        ## get the save path from window
        file_path = self.file_path.text().strip()
        if not file_path:
            QMessageBox.information(self, 'Warning', 'Please select path for save data..........')
            return

        ## create save file name
        now = datetime.now().strftime("%Y-%m-%d")
        file_name = f"Save Data {now}.xlsx"

        ## get data from window table
        data_table = self.result_table

        try:
            writer = pd.ExcelWriter(f"{file_path}/{file_name}")

            info_headers = [data_table.horizontalHeaderItem(x).text() for x in range(data_table.columnCount())]
            info_df = pd.DataFrame(columns=info_headers)

            for row in range(data_table.rowCount()):
                for col in range(data_table.columnCount()):
                    info_df.at[row, info_headers[col]] = data_table.item(row, col).text()

            ## save data to excel
            info_df.to_excel(writer, index=False)
            writer._save()


            ## show some note after save successfully
            QMessageBox.information(self, 'note', 'Data saved successfully.')
        except Exception as e:

            ## show some note when save fail
            QMessageBox.information(self, 'note', f'Fail to save data: {e}')

if __name__ == '__main__':
    print("start")
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())