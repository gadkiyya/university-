import sys
import math
import random
from PyQt5.QtWidgets import (QMainWindow, QWidget, QApplication, QPushButton,
                             QLineEdit, QLabel, QTextEdit, QFrame, QVBoxLayout,
                             QInputDialog, QColorDialog, QFontDialog, QFileDialog,
                             QAction, QMessageBox, QMenuBar, QToolBar, QStatusBar)
from PyQt5.QtGui import QColor, QIcon, QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Основной layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Виджеты для демонстрации работы
        self.label = QLabel("Результаты будут отображаться здесь")
        self.label.setAlignment(Qt.AlignCenter)
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)

        # Виджет для демонстрации цвета
        self.color_frame = QFrame()
        self.color_frame.setStyleSheet("background-color: black")
        self.color_frame.setFixedHeight(50)

        # Добавление виджетов в layout
        layout.addWidget(self.label)
        layout.addWidget(self.text_edit)
        layout.addWidget(self.color_frame)

        # Создание меню
        self.createMenus()

        # Создание панели инструментов
        self.createToolBar()

        # Строка состояния
        self.statusBar().showMessage('Готово')

        # Настройки окна
        self.setGeometry(300, 300, 600, 500)
        self.setWindowTitle('Лабораторные работы PyQt5')
        self.show()

    def createMenus(self):
        # Меню Файл
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Файл')

        # Действия для меню Файл
        openFile = QAction(QIcon.fromTheme('document-open'), 'Открыть', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Открыть файл')
        openFile.triggered.connect(self.showFileDialog)
        fileMenu.addAction(openFile)

        exitAction = QAction(QIcon.fromTheme('application-exit'), 'Выход', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Выйти из приложения')
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

        # Меню Диалоги
        dialogMenu = menubar.addMenu('&Диалоги')

        # Действия для меню Диалоги
        inputDialogAction = QAction('Ввод текста', self)
        inputDialogAction.triggered.connect(self.showInputDialog)
        dialogMenu.addAction(inputDialogAction)

        colorDialogAction = QAction('Выбор цвета', self)
        colorDialogAction.triggered.connect(self.showColorDialog)
        dialogMenu.addAction(colorDialogAction)

        fontDialogAction = QAction('Выбор шрифта', self)
        fontDialogAction.triggered.connect(self.showFontDialog)
        dialogMenu.addAction(fontDialogAction)

        # Меню Лабораторные работы
        labMenu = menubar.addMenu('&Лабораторные')

        # Действия для меню Лабораторные
        lab1Action = QAction('Калькулятор', self)
        lab1Action.triggered.connect(self.runLab1)
        labMenu.addAction(lab1Action)

        lab2Action = QAction('Генератор случайных чисел', self)
        lab2Action.triggered.connect(self.runLab2)
        labMenu.addAction(lab2Action)

        lab3Action = QAction('Решение квадратного уравнения', self)
        lab3Action.triggered.connect(self.runLab3)
        labMenu.addAction(lab3Action)

        lab4Action = QAction('Конвертер температур', self)
        lab4Action.triggered.connect(self.runLab4)
        labMenu.addAction(lab4Action)

        # Меню Справка
        helpMenu = menubar.addMenu('&Справка')

        aboutAction = QAction('О программе', self)
        aboutAction.triggered.connect(self.showAboutDialog)
        helpMenu.addAction(aboutAction)

    def createToolBar(self):
        toolbar = self.addToolBar('Инструменты')

        # Кнопки для диалогов
        inputBtn = QPushButton('Ввод текста')
        inputBtn.clicked.connect(self.showInputDialog)
        toolbar.addWidget(inputBtn)

        colorBtn = QPushButton('Выбор цвета')
        colorBtn.clicked.connect(self.showColorDialog)
        toolbar.addWidget(colorBtn)

        fontBtn = QPushButton('Выбор шрифта')
        fontBtn.clicked.connect(self.showFontDialog)
        toolbar.addWidget(fontBtn)

        # Разделитель
        toolbar.addSeparator()

        # Кнопки для лабораторных
        lab1Btn = QPushButton('Калькулятор')
        lab1Btn.clicked.connect(self.runLab1)
        toolbar.addWidget(lab1Btn)

        lab2Btn = QPushButton('Случайные числа')
        lab2Btn.clicked.connect(self.runLab2)
        toolbar.addWidget(lab2Btn)

    def showInputDialog(self):
        text, ok = QInputDialog.getText(self, 'Ввод текста',
                                        'Введите ваш текст:')
        if ok:
            self.label.setText(f"Вы ввели: {text}")
            self.text_edit.append(f"Пользователь ввел текст: {text}")

    def showColorDialog(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.color_frame.setStyleSheet(f"background-color: {col.name()}")
            self.text_edit.append(f"Выбран цвет: {col.name()}")

    def showFontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.text_edit.setFont(font)
            self.text_edit.append(f"Установлен шрифт: {font.family()}, размер: {font.pointSize()}")

    def showFileDialog(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Открыть файл',
                                               '/home', 'Текстовые файлы (*.txt);;Все файлы (*)')
        if fname:
            try:
                with open(fname, 'r', encoding='utf-8') as f:
                    data = f.read()
                    self.text_edit.setText(data)
                    self.statusBar().showMessage(f'Открыт файл: {fname}')
            except Exception as e:
                QMessageBox.critical(self, 'Ошибка', f'Не удалось открыть файл: {str(e)}')

    def showAboutDialog(self):
        QMessageBox.about(self, "О программе",
                          "Это крутое приложение:)))\n")


    # Реализация лабораторных работ
    def runLab1(self):
        """Калькулятор"""
        num1, ok1 = QInputDialog.getDouble(self, 'Калькулятор', 'Введите первое число:')
        if not ok1: return

        num2, ok2 = QInputDialog.getDouble(self, 'Калькулятор', 'Введите второе число:')
        if not ok2: return

        operations = ["+", "-", "*", "/"]
        operation, ok = QInputDialog.getItem(self, 'Калькулятор',
                                             'Выберите операцию:', operations, 0, False)
        if not ok: return

        result = None
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                QMessageBox.warning(self, 'Ошибка', 'Деление на ноль!')
                return
            result = num1 / num2

        self.text_edit.append(f"Калькулятор: {num1} {operation} {num2} = {result}")
        self.label.setText(f"Результат: {result}")

    def runLab2(self):
        """Генератор случайных чисел"""
        min_val, ok1 = QInputDialog.getInt(self, 'Генератор случайных чисел',
                                           'Минимальное значение:', 0, -10000, 10000, 1)
        if not ok1: return

        max_val, ok2 = QInputDialog.getInt(self, 'Генератор случайных чисел',
                                           'Максимальное значение:', 100, -10000, 10000, 1)
        if not ok2: return

        if min_val > max_val:
            QMessageBox.warning(self, 'Ошибка', 'Минимальное значение больше максимального!')
            return

        count, ok3 = QInputDialog.getInt(self, 'Генератор случайных чисел',
                                         'Количество чисел:', 1, 1, 100, 1)
        if not ok3: return

        numbers = [random.randint(min_val, max_val) for _ in range(count)]
        result = ", ".join(map(str, numbers))

        self.text_edit.append(f"Случайные числа ({min_val}-{max_val}): {result}")
        self.label.setText(f"Сгенерировано: {result}")

    def runLab3(self):
        """Решение квадратного уравнения"""
        a, ok1 = QInputDialog.getDouble(self, 'Квадратное уравнение',
                                        'Коэффициент a:', 1, -1000, 1000, 2)
        if not ok1 or a == 0: return

        b, ok2 = QInputDialog.getDouble(self, 'Квадратное уравнение',
                                        'Коэффициент b:', 0, -1000, 1000, 2)
        if not ok2: return

        c, ok3 = QInputDialog.getDouble(self, 'Квадратное уравнение',
                                        'Коэффициент c:', 0, -1000, 1000, 2)
        if not ok3: return

        D = b ** 2 - 4 * a * c
        result = ""

        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            result = f"Два корня: x₁ = {x1:.2f}, x₂ = {x2:.2f}"
        elif D == 0:
            x = -b / (2 * a)
            result = f"Один корень: x = {x:.2f}"
        else:
            result = "Действительных корней нет"

        self.text_edit.append(f"Уравнение: {a}x² + {b}x + {c} = 0\nДискриминант: {D:.2f}\n{result}")
        self.label.setText(result)

    def runLab4(self):
        """Конвертер температур"""
        temp, ok = QInputDialog.getDouble(self, 'Конвертер температур',
                                          'Введите температуру:', 0, -273.15, 10000, 2)
        if not ok: return

        options = ["Цельсий → Фаренгейт", "Фаренгейт → Цельсий",
                   "Цельсий → Кельвин", "Кельвин → Цельсий"]
        choice, ok = QInputDialog.getItem(self, 'Конвертер температур',
                                          'Выберите преобразование:', options, 0, False)
        if not ok: return

        result = 0
        if choice == options[0]:
            result = temp * 9 / 5 + 32
            self.text_edit.append(f"{temp}°C = {result:.2f}°F")
        elif choice == options[1]:
            result = (temp - 32) * 5 / 9
            self.text_edit.append(f"{temp}°F = {result:.2f}°C")
        elif choice == options[2]:
            result = temp + 273.15
            self.text_edit.append(f"{temp}°C = {result:.2f}K")
        elif choice == options[3]:
            result = temp - 273.15
            self.text_edit.append(f"{temp}K = {result:.2f}°C")

        self.label.setText(f"Результат: {result:.2f}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
