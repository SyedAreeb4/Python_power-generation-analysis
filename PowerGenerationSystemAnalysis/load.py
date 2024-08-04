import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class LoadScreen(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Load Duration Curve")
        self.geometry("800x600")  # Set initial geometry
        self.configure(bg='lightgreen')
        
        self.load_vars = [tk.StringVar() for _ in range(24)]
        self.load_data = []
        self.create_widgets()

    def create_widgets(self):
        # Create a canvas and a scrollbar
        canvas = tk.Canvas(self, borderwidth=0, background="lightgreen")
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        # Configure scrollbar and canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # Bind the canvas resize event to adjust the scroll region
        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        scrollable_frame.bind("<Configure>", on_frame_configure)

        # Create input fields for each hour
        for i in range(24):
            ttk.Label(scrollable_frame, text=f"Hour {i + 1} Load").grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
            ttk.Entry(scrollable_frame, textvariable=self.load_vars[i]).grid(row=i, column=1, padx=10, pady=5, sticky=tk.EW)

        # Button to generate the graph
        ttk.Button(scrollable_frame, text="Generate Load Profile Graph and Duration Curve", command=self.generate_load_duration_curve).grid(row=24, column=0, columnspan=2, pady=20)

        # Matplotlib plot
        self.figure, self.ax = plt.subplots(figsize=(8, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, master=scrollable_frame)
        self.canvas.get_tk_widget().grid(row=25, column=0, columnspan=2, pady=20, sticky=tk.NSEW)
        
        # Text area for results
        self.results_text = tk.Text(scrollable_frame, height=10, width=80)
        self.results_text.grid(row=26, column=0, columnspan=2, pady=20)

        # Ensure the grid layout adjusts
        scrollable_frame.columnconfigure(0, weight=1)
        scrollable_frame.columnconfigure(1, weight=3)
        scrollable_frame.rowconfigure(24, weight=0)  # Add this line to ensure the button row doesn't expand

    def generate_load_duration_curve(self):
        try:
            self.load_data = [float(var.get()) for var in self.load_vars]
            sorted_load_data = sorted(self.load_data, reverse=True)
            hours = np.arange(1, 25)

            # Plot bar chart
            self.ax.clear()
            self.ax.bar(hours, sorted_load_data, color='blue')
            self.ax.set_xlabel('Hour')
            self.ax.set_ylabel('Load (kW)')
            self.ax.set_title('Load Duration Curve')
            self.canvas.draw()

            # Calculate metrics
            total_load = sum(self.load_data)
            peak_load = max(self.load_data)
            average_load = total_load / 24
            load_factor = average_load / peak_load
            plant_capacity = peak_load * 1.15
            plant_capacity_factor = total_load / (plant_capacity * 24)
            annual_energy = total_load * 365

            results = (f"Load Factor: {load_factor:.2f}\n"
                       f"Total KWH: {total_load:.2f}\n"
                       f"Peak Demand: {peak_load:.2f} kW\n"
                       f"Average Load: {average_load:.2f} kW\n"
                       f"Plant Capacity: {plant_capacity:.2f} kW\n"
                       f"Plant Capacity Factor: {plant_capacity_factor:.2f}\n"
                       f"Annual Energy KWh: {annual_energy:.2f} KWh")
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, results)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")

    def destroy(self):
        super().destroy()  # Ensure to call the parent class's destroy method
