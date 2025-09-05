import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPlainTextEdit, 
                            QFileDialog, QMessageBox, QMenuBar, QStatusBar)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QAction, QKeySequence, QFont, QIcon

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.current_file = None
        self.is_modified = False
        
        self.init_ui()
        self.init_menus()
        self.init_statusbar()
        
        self.connect_signals()
        
        self.update_title()
        
    def init_ui(self):
        self.setWindowTitle("Текстовый редактор")
        self.setGeometry(100, 100, 800, 600)

        self.text_edit = QPlainTextEdit()
        self.text_edit.setFont(QFont("Consolas", 11))
        self.setCentralWidget(self.text_edit)
        
    def init_menus(self):
        menubar = self.menuBar()
        
        file_menu = menubar.addMenu('&Файл')
        
        open_action = QAction('&Открыть', self)
        open_action.setShortcut(QKeySequence.StandardKey.Open)
        open_action.setStatusTip('Открыть существующий файл')
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        
        save_action = QAction('&Сохранить', self)
        save_action.setShortcut(QKeySequence.StandardKey.Save)
        save_action.setStatusTip('Сохранить текущий файл')
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)
        
        save_as_action = QAction('Сохранить &как...', self)
        save_as_action.setShortcut(QKeySequence.StandardKey.SaveAs)
        save_as_action.setStatusTip('Сохранить файл с новым именем')
        save_as_action.triggered.connect(self.save_file_as)
        file_menu.addAction(save_as_action)
        
        file_menu.addSeparator()
        
        new_action = QAction('&Новый', self)
        new_action.setShortcut(QKeySequence.StandardKey.New)
        new_action.setStatusTip('Создать новый документ')
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)
        
        file_menu.addSeparator()
        
        close_action = QAction('&Закрыть', self)
        close_action.setShortcut(QKeySequence.StandardKey.Quit)
        close_action.setStatusTip('Закрыть приложение')
        close_action.triggered.connect(self.close_application)
        file_menu.addAction(close_action)
        
        edit_menu = menubar.addMenu('&Правка')
        
        undo_action = QAction('&Отменить', self)
        undo_action.setShortcut(QKeySequence.StandardKey.Undo)
        undo_action.setStatusTip('Отменить последнее действие')
        undo_action.triggered.connect(self.text_edit.undo)
        edit_menu.addAction(undo_action)
        
        redo_action = QAction('&Повторить', self)
        redo_action.setShortcut(QKeySequence.StandardKey.Redo)
        redo_action.setStatusTip('Повторить отмененное действие')
        redo_action.triggered.connect(self.text_edit.redo)
        edit_menu.addAction(redo_action)
        
        edit_menu.addSeparator()
        
        cut_action = QAction('&Вырезать', self)
        cut_action.setShortcut(QKeySequence.StandardKey.Cut)
        cut_action.setStatusTip('Вырезать выделенный текст')
        cut_action.triggered.connect(self.text_edit.cut)
        edit_menu.addAction(cut_action)
        
        copy_action = QAction('&Копировать', self)
        copy_action.setShortcut(QKeySequence.StandardKey.Copy)
        copy_action.setStatusTip('Копировать выделенный текст')
        copy_action.triggered.connect(self.text_edit.copy)
        edit_menu.addAction(copy_action)
        
        paste_action = QAction('&Вставить', self)
        paste_action.setShortcut(QKeySequence.StandardKey.Paste)
        paste_action.setStatusTip('Вставить текст из буфера обмена')
        paste_action.triggered.connect(self.text_edit.paste)
        edit_menu.addAction(paste_action)
        
        help_menu = menubar.addMenu('&Справка')
        
        about_action = QAction('&О программе', self)
        about_action.setStatusTip('Информация о программе')
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
        
    def init_statusbar(self):
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage('Готов')
        
    def connect_signals(self):
        self.text_edit.textChanged.connect(self.on_text_changed)
        
    def on_text_changed(self):
        if not self.is_modified:
            self.is_modified = True
            self.update_title()
            
    def update_title(self):
        if self.current_file:
            filename = os.path.basename(self.current_file)
        else:
            filename = "Новый документ"
            
        modified_indicator = " *" if self.is_modified else ""
        self.setWindowTitle(f"{filename}{modified_indicator} - Текстовый редактор")
        
    def new_file(self):
        if self.check_unsaved_changes():
            self.text_edit.clear()
            self.current_file = None
            self.is_modified = False
            self.update_title()
            self.status_bar.showMessage('Создан новый документ')
            
    def open_file(self):
        if not self.check_unsaved_changes():
            return
            
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            'Открыть файл',
            '',
            'Текстовые файлы (*.txt);;Все файлы (*.*)'
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.text_edit.setPlainText(content)
                    
                self.current_file = file_path
                self.is_modified = False
                self.update_title()
                self.status_bar.showMessage(f'Файл открыт: {os.path.basename(file_path)}')
                
            except Exception as e:
                QMessageBox.critical(
                    self,
                    'Ошибка',
                    f'Не удалось открыть файл:\n{str(e)}'
                )
                
    def save_file(self):
        if self.current_file:
            return self.save_to_file(self.current_file)
        else:
            return self.save_file_as()
            
    def save_file_as(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            'Сохранить файл как',
            '',
            'Текстовые файлы (*.txt);;Все файлы (*.*)'
        )
        
        if file_path:
            return self.save_to_file(file_path)
        return False
        
    def save_to_file(self, file_path):
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(self.text_edit.toPlainText())
                
            self.current_file = file_path
            self.is_modified = False
            self.update_title()
            self.status_bar.showMessage(f'Файл сохранен: {os.path.basename(file_path)}')
            return True
            
        except Exception as e:
            QMessageBox.critical(
                self,
                'Ошибка',
                f'Не удалось сохранить файл:\n{str(e)}'
            )
            return False
            
    def check_unsaved_changes(self):
        if not self.is_modified:
            return True
            
        reply = QMessageBox.question(
            self,
            'Несохраненные изменения',
            'Документ был изменен.\nСохранить изменения?',
            QMessageBox.StandardButton.Save | 
            QMessageBox.StandardButton.Discard | 
            QMessageBox.StandardButton.Cancel,
            QMessageBox.StandardButton.Save
        )
        
        if reply == QMessageBox.StandardButton.Save:
            return self.save_file()
        elif reply == QMessageBox.StandardButton.Discard:
            return True
        else:
            return False
            
    def close_application(self):
        if self.check_unsaved_changes():
            self.close()
            
    def closeEvent(self, event):
        if self.check_unsaved_changes():
            event.accept()
        else:
            event.ignore()
            
    def show_about(self):
        QMessageBox.about(
            self,
            'О программе',
            '''<h3>Текстовый редактор</h3>
            <p>Версия: 1.0</p>
            <p>Простой текстовый редактор на PyQt6</p>
            <p><b>Возможности:</b></p>
            <ul>
            <li>Создание, открытие и сохранение файлов</li>
            <li>Базовые операции редактирования</li>
            <li>Проверка несохраненных изменений</li>
            </ul>
            <p>© 2025 Текстовый редактор</p>'''
        )

def main():
    app = QApplication(sys.argv)
    
    app.setStyle('Fusion')
    
    editor = TextEditor()
    editor.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()