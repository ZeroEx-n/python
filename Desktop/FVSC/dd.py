import tkinter as tk
from tkinter import messagebox

# Функция для создания дополнительных окон, как окно ошибки
def create_additional_windows():
    # Создаем 3 дополнительных окна, как окно ошибки
    for _ in range(3):
        messagebox.showerror("Ошибка", "Это окно ошибки!")  # Это стандартное окно ошибки

# Основное окно
root = tk.Tk()
root.title("Главное окно")
root.geometry("300x150")

# Кнопка для создания дополнительных окон
button = tk.Button(root, text="Создать 3 окна ошибок", command=create_additional_windows)
button.pack(pady=50)

# Запуск основного цикла обработки событий
root.mainloop()
