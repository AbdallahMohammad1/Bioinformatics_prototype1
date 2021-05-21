from PyQt5.QtWidgets import QFileDialog


class Text():
    def read_data(self):
        path_image = QFileDialog.getOpenFileName(None, 'Open TEXT ', '/home', "TEXT (*.txt)")[0]
        return path_image

    def data(self):
        path = self.read_data()
        f = open(path, "r")
        return f.read()
