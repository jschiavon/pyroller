# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyroller.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from src import roller

def _sanitize_input(string, default=0):
    if string == '':
        return default
    return int(string)

def _obtain_reroll_data(reroll_idx):
    if reroll_idx <= 3:
        return reroll_idx
    elif reroll_idx == 4:
        return 'lowest'
    elif reroll_idx == 5:
        return '2lowest'
    else:
        raise ValueError('Should not have arrived here!')

def _obtain_stats_data(stat_idx):
    if stat_idx == 0:
        return None
    elif stat_idx == 1:
        return 'min'
    elif stat_idx == 2:
        return 'max'
    elif stat_idx == 3:
        return 'mean'


class PyRollerMainWindow(object):

    def setup_fonts(self):
        self.titlefont = QtGui.QFont()
        self.titlefont.setPointSize(14)
        self.titlefont.setBold(True)
        self.titlefont.setWeight(75)
        self.resultfont = QtGui.QFont()
        self.resultfont.setItalic(True)

    def add_icon(self):
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("ui/imgs/dice.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)

    def setup_roller_input(self):
        self.dice_roller_input = QtWidgets.QVBoxLayout()
        self.dice_roller_input.setObjectName("dice_roller_input")

        self.dice_number = QtWidgets.QLineEdit(self.widget)
        self.dice_number.setMinimumSize(QtCore.QSize(150, 0))
        self.dice_number.setObjectName("dice_number")
        self.dice_roller_input.addWidget(self.dice_number)

        self.dice_size = QtWidgets.QLineEdit(self.widget)
        self.dice_size.setMinimumSize(QtCore.QSize(150, 0))
        self.dice_size.setObjectName("dice_size")
        self.dice_roller_input.addWidget(self.dice_size)

        self.modifier = QtWidgets.QLineEdit(self.widget)
        self.modifier.setMinimumSize(QtCore.QSize(150, 0))
        self.modifier.setObjectName("modifier")
        self.dice_roller_input.addWidget(self.modifier)

        self.advantage_box = QtWidgets.QHBoxLayout()
        self.advantage_label = QtWidgets.QLabel(self.widget)
        self.advantage_box.addWidget(self.advantage_label)
        self.advantage = QtWidgets.QCheckBox(self.widget)
        self.advantage_box.addWidget(self.advantage)
        self.dice_roller_input.addLayout(self.advantage_box)

        self.summary_box = QtWidgets.QComboBox(self.widget)
        self.summary_box.setObjectName("summary_box")
        self.summary_box.addItem("")
        self.summary_box.addItem("")
        self.summary_box.addItem("")
        self.summary_box.addItem("")
        self.dice_roller_input.addWidget(self.summary_box)

        self.reroll = QtWidgets.QComboBox(self.widget)
        self.reroll.setObjectName("reroll")
        self.reroll.addItem("")
        self.reroll.addItem("")
        self.reroll.addItem("")
        self.reroll.addItem("")
        self.reroll.addItem("")
        self.reroll.addItem("")
        self.dice_roller_input.addWidget(self.reroll)

    def setup_stats_input(self):
        self.stat_gen_input = QtWidgets.QFormLayout()
        self.stat_gen_input.setObjectName("stat_gen_input")

        self.method_label = QtWidgets.QLabel(self.widget)
        self.method_label.setObjectName("method_label")
        self.stat_gen_input.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.method_label)

        self.stats_label = QtWidgets.QLabel(self.widget)
        self.stats_label.setObjectName("stats_label")
        self.stat_gen_input.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.stats_label)

        self.stats_box = QtWidgets.QComboBox(self.widget)
        self.stats_box.setMinimumSize(QtCore.QSize(190, 0))
        self.stats_box.setObjectName("stats_box")
        self.stats_box.addItem("")
        self.stats_box.addItem("")
        self.stats_box.addItem("")
        self.stats_box.addItem("")
        self.stat_gen_input.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.stats_box)

        self.method_box = QtWidgets.QComboBox(self.widget)
        self.method_box.setMinimumSize(QtCore.QSize(190, 0))
        self.method_box.setObjectName("method_box")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.method_box.addItem("")
        self.stat_gen_input.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.method_box)

    def setup_physical_stat_output(self):
        self.physical_stats = QtWidgets.QFormLayout()
        self.physical_stats.setObjectName("physical_stats")

        self.strength_label = QtWidgets.QLabel(self.widget)
        self.strength_label.setFont(self.resultfont)
        self.strength_label.setObjectName("strength_label")
        self.physical_stats.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.strength_label)

        self.strength = QtWidgets.QLineEdit(self.widget)
        self.strength.setMinimumSize(QtCore.QSize(50, 0))
        self.strength.setAlignment(QtCore.Qt.AlignCenter)
        self.strength.setReadOnly(True)
        self.strength.setPlaceholderText("8")
        self.strength.setObjectName("strength")
        self.physical_stats.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.strength)

        self.dexterity_label = QtWidgets.QLabel(self.widget)
        self.dexterity_label.setFont(self.resultfont)
        self.dexterity_label.setObjectName("dexterity_label")
        self.physical_stats.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.dexterity_label)

        self.dexterity = QtWidgets.QLineEdit(self.widget)
        self.dexterity.setMinimumSize(QtCore.QSize(50, 0))
        self.dexterity.setAlignment(QtCore.Qt.AlignCenter)
        self.dexterity.setReadOnly(True)
        self.dexterity.setPlaceholderText("8")
        self.dexterity.setObjectName("dexterity")
        self.physical_stats.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dexterity)

        self.constitution_label = QtWidgets.QLabel(self.widget)
        self.constitution_label.setFont(self.resultfont)
        self.constitution_label.setObjectName("constitution_label")
        self.physical_stats.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.constitution_label)

        self.constitution = QtWidgets.QLineEdit(self.widget)
        self.constitution.setMinimumSize(QtCore.QSize(50, 0))
        self.constitution.setAlignment(QtCore.Qt.AlignCenter)
        self.constitution.setReadOnly(True)
        self.constitution.setPlaceholderText("8")
        self.constitution.setObjectName("constitution")
        self.physical_stats.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.constitution)

    def setup_mental_stat_output(self):
        self.mental_stats = QtWidgets.QFormLayout()
        self.mental_stats.setObjectName("mental_stats")
        self.intelligence_label = QtWidgets.QLabel(self.widget)

        self.intelligence_label.setFont(self.resultfont)
        self.intelligence_label.setObjectName("intelligence_label")
        self.mental_stats.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.intelligence_label)

        self.intelligence = QtWidgets.QLineEdit(self.widget)
        self.intelligence.setMinimumSize(QtCore.QSize(50, 0))
        self.intelligence.setAlignment(QtCore.Qt.AlignCenter)
        self.intelligence.setReadOnly(True)
        self.intelligence.setPlaceholderText("8")
        self.intelligence.setObjectName("intelligence")
        self.mental_stats.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.intelligence)

        self.wisdom_label = QtWidgets.QLabel(self.widget)
        self.wisdom_label.setFont(self.resultfont)
        self.wisdom_label.setObjectName("wisdom_label")
        self.mental_stats.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.wisdom_label)

        self.wisdom = QtWidgets.QLineEdit(self.widget)
        self.wisdom.setMinimumSize(QtCore.QSize(50, 0))
        self.wisdom.setAlignment(QtCore.Qt.AlignCenter)
        self.wisdom.setReadOnly(True)
        self.wisdom.setPlaceholderText("8")
        self.wisdom.setObjectName("wisdom")
        self.mental_stats.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.wisdom)

        self.charisma_label = QtWidgets.QLabel(self.widget)
        self.charisma_label.setFont(self.resultfont)
        self.charisma_label.setObjectName("charisma_label")
        self.mental_stats.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.charisma_label)

        self.charisma = QtWidgets.QLineEdit(self.widget)
        self.charisma.setMinimumSize(QtCore.QSize(50, 0))
        self.charisma.setAlignment(QtCore.Qt.AlignCenter)
        self.charisma.setReadOnly(True)
        self.charisma.setPlaceholderText("8")
        self.charisma.setObjectName("charisma")
        self.mental_stats.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.charisma)

    def setup_stats_output(self):
        self.stat_gen_output = QtWidgets.QHBoxLayout()
        self.stat_gen_output.setObjectName("stat_gen_output")
        self.setup_physical_stat_output()
        self.stat_gen_output.addLayout(self.physical_stats)
        self.setup_mental_stat_output()
        self.stat_gen_output.addLayout(self.mental_stats)

    def setup_roller_output(self):
        self.dice_roller_output = QtWidgets.QFormLayout()
        self.dice_roller_output.setObjectName("dice_roller_output")

        self.dice_roller_results = QtWidgets.QLineEdit(self.widget)
        self.dice_roller_results.setAlignment(QtCore.Qt.AlignCenter)
        self.dice_roller_results.setReadOnly(True)
        self.dice_roller_results.setObjectName("dice_roller_results")
        self.dice_roller_output.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dice_roller_results)

        self.dice_roller_results_label = QtWidgets.QLabel(self.widget)
        self.dice_roller_results_label.setFont(self.resultfont)
        self.dice_roller_results_label.setObjectName("dice_roller_results_label")
        self.dice_roller_output.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.dice_roller_results_label)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 478)
        MainWindow.setMinimumSize(QtCore.QSize(180, 0))

        self.setup_fonts()
        self.add_icon()

        # MAIN LAYOUTS
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 651, 421))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(40)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")

        # TITLES
        self.dice_roller_label = QtWidgets.QLabel(self.widget)
        self.dice_roller_label.setFont(self.titlefont)
        self.dice_roller_label.setAlignment(QtCore.Qt.AlignCenter)
        self.dice_roller_label.setObjectName("dice_roller_label")
        self.gridLayout.addWidget(self.dice_roller_label, 0, 0, 1, 1)
        self.stat_gen_label = QtWidgets.QLabel(self.widget)
        self.stat_gen_label.setFont(self.titlefont)
        self.stat_gen_label.setAlignment(QtCore.Qt.AlignCenter)
        self.stat_gen_label.setObjectName("stat_gen_label")
        self.gridLayout.addWidget(self.stat_gen_label, 0, 1, 1, 1)

        # INPUTS
        self.setup_roller_input()
        self.gridLayout.addLayout(self.dice_roller_input, 1, 0, 3, 1)

        self.setup_stats_input()
        self.gridLayout.addLayout(self.stat_gen_input, 1, 1, 1, 1)

        # BUTTONS
        self.stat_gen_button = QtWidgets.QPushButton(self.widget)
        self.stat_gen_button.setFont(self.titlefont)
        self.stat_gen_button.setIcon(self.icon)
        self.stat_gen_button.setIconSize(QtCore.QSize(20, 20))
        self.stat_gen_button.setObjectName("stat_gen_button")
        self.stat_gen_button.clicked.connect(self.roll_stats)
        self.gridLayout.addWidget(self.stat_gen_button, 2, 1, 1, 1)

        self.dice_roller_button = QtWidgets.QPushButton(self.widget)
        self.dice_roller_button.setFont(self.titlefont)
        self.dice_roller_button.setIcon(self.icon)
        self.dice_roller_button.setIconSize(QtCore.QSize(20, 20))
        self.dice_roller_button.setObjectName("dice_roller_button")
        self.dice_roller_button.clicked.connect(self.roll_dice)
        self.gridLayout.addWidget(self.dice_roller_button, 4, 0, 1, 1)

        # OUTPUTS
        self.setup_stats_output()
        self.gridLayout.addLayout(self.stat_gen_output, 3, 1, 3, 1)

        self.setup_roller_output()
        self.gridLayout.addLayout(self.dice_roller_output, 5, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dice_roller_label.setText(_translate("MainWindow", "Dice roller"))
        self.stat_gen_label.setText(_translate("MainWindow", "Stat generator"))
        self.advantage_label.setText(_translate("MainWindow", "Advantage"))
        self.summary_box.setItemText(0, _translate("MainWindow", "Normal roll"))
        self.summary_box.setItemText(1, _translate("MainWindow", "Minimum"))
        self.summary_box.setItemText(2, _translate("MainWindow", "Maximum"))
        self.summary_box.setItemText(3, _translate("MainWindow", "Mean"))
        self.reroll.setItemText(0, _translate("MainWindow", "No reroll"))
        self.reroll.setItemText(1, _translate("MainWindow", "Reroll 1s"))
        self.reroll.setItemText(2, _translate("MainWindow", "Reroll 1s-2s"))
        self.reroll.setItemText(3, _translate("MainWindow", "Reroll 1s-2s-3s"))
        self.reroll.setItemText(4, _translate("MainWindow", "Reroll lowest"))
        self.reroll.setItemText(5, _translate("MainWindow", "Reroll two lowest"))
        self.dice_number.setPlaceholderText(_translate("MainWindow", "Input dices number (1)"))
        self.modifier.setPlaceholderText(_translate("MainWindow", "Input roll modifier (+0)"))
        self.dice_size.setPlaceholderText(_translate("MainWindow", "Input dice size (6)"))
        self.method_label.setText(_translate("MainWindow", "Method"))
        self.stats_label.setText(_translate("MainWindow", "Statistics"))
        self.stats_box.setItemText(0, _translate("MainWindow", "Normal roll"))
        self.stats_box.setItemText(1, _translate("MainWindow", "Minimum"))
        self.stats_box.setItemText(2, _translate("MainWindow", "Maximum"))
        self.stats_box.setItemText(3, _translate("MainWindow", "Mean"))
        self.method_box.setItemText(0, _translate("MainWindow", "3d6"))
        self.method_box.setItemText(1, _translate("MainWindow", "3d6 (reroll lowest)"))
        self.method_box.setItemText(2, _translate("MainWindow", "4d6 (exclude lowest)"))
        self.method_box.setItemText(3, _translate("MainWindow", "5d6 (exclude 2 lowest)"))
        self.stat_gen_button.setText(_translate("MainWindow", "ROLL!"))
        self.strength_label.setText(_translate("MainWindow", "Strength"))
        self.dexterity_label.setText(_translate("MainWindow", "Dexterity"))
        self.constitution_label.setText(_translate("MainWindow", "Constitution"))
        self.intelligence_label.setText(_translate("MainWindow", "Intelligence"))
        self.wisdom_label.setText(_translate("MainWindow", "Wisdom"))
        self.charisma_label.setText(_translate("MainWindow", "Charisma"))
        self.dice_roller_button.setText(_translate("MainWindow", "ROLL!"))
        self.dice_roller_results.setPlaceholderText(_translate("MainWindow", "0"))
        self.dice_roller_results_label.setText(_translate("MainWindow", "Results"))

    def roll_stats(self):
        pass

    def roll_dice(self):
        s = _sanitize_input(self.dice_size.text(), 6)
        n = _sanitize_input(self.dice_number.text(), 1)
        m = _sanitize_input(self.modifier.text(), 0)

        r = _obtain_reroll_data(self.reroll.currentIndex())
        stats = _obtain_stats_data(self.summary_box.currentIndex())

        if stats is None:
            rolled = roller.roll_dice(s, n, m, r)
        else:
            rolled = roller.roll_stats(s, n, m, r, stats)
        self.dice_roller_results.setText(str(rolled))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = PyRollerMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())