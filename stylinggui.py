import tkinter as tk
from tkinter import ttk

class ClickerGUI:
    def __init__(self, root, click_thread):
        self.root = root
        self.click_thread = click_thread
        self.root.title("Python Auto-Clicker")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        # Frame principal
        main_frame = ttk.Frame(root, style="Main.TFrame")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        # Label de título
        self.title_label = ttk.Label(main_frame, text="Auto-Clicker by Augusto V", font=("Helvetica", 18), background="#000000", foreground="#FFFFFF")
        self.title_label.pack(pady=10)

        # Estilo dos botões
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), padding=6, background="#000000", foreground="#FFFFFF")
        style.map("TButton", background=[('active', '#333333'), ('!active', '#000000')],
                  foreground=[('active', '#FFFFFF'), ('!active', '#FFFFFF')])

        # Cores personalizadas do frame principal
        style.configure("Main.TFrame", background="#000000")

        # Botões estilizados
        self.button_start = ttk.Button(main_frame, text="Iniciar", command=self.start_clicking, style="TButton")
        self.button_stop = ttk.Button(main_frame, text="Parar", command=self.stop_clicking, style="TButton")
        self.button_exit = ttk.Button(main_frame, text="Sair", command=self.exit_program, style="TButton")

        self.button_start.pack(pady=5)
        self.button_stop.pack(pady=5)
        self.button_exit.pack(pady=5)

        # Cor de fundo da janela principal
        self.root.configure(bg="#000000")

    def start_clicking(self):
        self.click_thread.start_clicking()

    def stop_clicking(self):
        self.click_thread.stop_clicking()

    def exit_program(self):
        self.click_thread.exit()
        self.root.quit()
