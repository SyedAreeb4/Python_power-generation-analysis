import tkinter as tk
from tkinter import ttk
from hydro import HydroScreen
from geothermal import GeothermalScreen
from nuclear import NuclearScreen
from solar import SolarScreen
from steam import SteamScreen
from wind import WindScreen
from load import LoadScreen

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Power Plant Cost Calculator")
        self.geometry("600x400")  # Adjusted size
        self.original_bg_color = 'lightgreen'  # Store original background color
        # self.configure(bg=self.original_bg_color)  # Set background color

        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self, padding="16", style='TFrame')
        frame.pack(fill=tk.BOTH, expand=True)

        # Style configuration for the frame
        style = ttk.Style()
        style.configure('TFrame', background=self.original_bg_color)

        # Increase button font size
        button_style = ttk.Style()
        button_style.configure('TButton', font=('Arial', 14))  # Button text size

        ttk.Button(frame, text="Hydro Power Plant", command=self.open_hydro).pack(pady=10)
        ttk.Button(frame, text="Geothermal Power Plant", command=self.open_geothermal).pack(pady=10)
        ttk.Button(frame, text="Nuclear Power Plant", command=self.open_nuclear).pack(pady=10)
        ttk.Button(frame, text="Solar Power Plant", command=self.open_solar).pack(pady=10)
        ttk.Button(frame, text="Steam Power Plant", command=self.open_steam).pack(pady=10)
        ttk.Button(frame, text="Wind Power Plant", command=self.open_wind).pack(pady=10)
        ttk.Button(frame, text="Load Analysis", command=self.open_load).pack(pady=10)

    def open_hydro(self):
        self.open_screen(HydroScreen)

    def open_geothermal(self):
        self.open_screen(GeothermalScreen)

    def open_nuclear(self):
        self.open_screen(NuclearScreen)

    def open_solar(self):
        self.open_screen(SolarScreen)

    def open_steam(self):
        self.open_screen(SteamScreen)

    def open_wind(self):
        self.open_screen(WindScreen)

    def open_load(self):
        self.open_screen(LoadScreen)

    def open_screen(self, screen_class):
        screen = screen_class(self)
        screen.top.protocol("WM_DELETE_WINDOW", screen.destroy)  # Properly destroy the Toplevel window
        screen.top.mainloop()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
