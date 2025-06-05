import tkinter as tk

def on_board(): # Условие для ввода данных от юзера
    user_input = entry.get()
    label.config(text=f' Hello, {user_input} ! ')

def exit_program(): # Условие для закрытия программы
    root.destroy() # Краш программы и закрытие окна

root = tk.Tk() # Формируем окно
root.title('Приветствие в окне') # Название окна

label = tk.Label(root, text=" Введи свое имя ") # Текст в окне
label.pack() # Сохранение текста в окне

entry = tk.Entry(root) # Поле для ввода данных
entry.pack() # Сохранение поля для ввода данных в окне

button = tk.Button(root, text=f'Жми для приветствия!', command=on_board) # Кнопка для отработки запроса
button.pack() # Сохранение кнопки в окне

exit_button = tk.Button(root, text="Выход", command=exit_program) # Кнопка выхода из программы
exit_button.pack() # Сохранение кнопки в окне




root.mainloop()
