from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

class IDButton(QPushButton):
	idSignal = pyqtSignal(int)

	def __init__(self, _id, icon_path, parent):
		super(IDButton, self).__init__(parent)
		self._id = _id
		self.clicked.connect(self.idClicked)

	@pyqtSlot()
	def idClicked(self):
		self.idSignal.emit(self._id)