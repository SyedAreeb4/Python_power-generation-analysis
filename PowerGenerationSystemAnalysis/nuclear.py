import tkinter as tk
from tkinter import ttk, messagebox

class NuclearScreen:
    def __init__(self, parent):
        self.parent = parent
        self.top = tk.Toplevel(parent)
        self.top.title("Nuclear Power Plant")
        self.top.geometry("600x800")
        self.top.configure(bg='lightgreen')

        # Define variables
        self.construction_cost_var = tk.StringVar()
        self.interest_dep_var = tk.StringVar()
        self.operating_cost_var = tk.StringVar()
        self.maintenance_cost_var = tk.StringVar()
        self.annual_energy_var = tk.StringVar()

        # Results
        self.fixed_cost = 0
        self.variable_cost = 0
        self.cost_per_unit = 0
        self.cost_pkr = 0

        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.top, padding="16", style='TFrame')
        frame.pack(fill=tk.BOTH, expand=True)

        style = ttk.Style()
        style.configure('TFrame', background='lightgreen')

        input_font = ('Arial', 12)
        label_font = ('Arial', 14)

        self.create_input(frame, "Construction Cost ($)", self.construction_cost_var, label_font, input_font)
        self.create_input(frame, "Interest and Depreciation (%)", self.interest_dep_var, label_font, input_font)
        self.create_input(frame, "Operating Cost ($)", self.operating_cost_var, label_font, input_font)
        self.create_input(frame, "Maintenance Cost ($)", self.maintenance_cost_var, label_font, input_font)
        self.create_input(frame, "Annual Energy (KWh)", self.annual_energy_var, label_font, input_font)

        button_style = ttk.Style()
        button_style.configure('TButton', font=('Arial', 14))

        ttk.Button(frame, text="Calculate", command=self.calculate_nuclear_cost, style='TButton').pack(pady=20)

        self.results_label = ttk.Label(frame, text="GENERATION COST", font=("Arial", 24))
        self.results_label.pack(pady=20)

        self.fixed_cost_label = ttk.Label(frame, text="", font=label_font)
        self.fixed_cost_label.pack()
        
        self.variable_cost_label = ttk.Label(frame, text="", font=label_font)
        self.variable_cost_label.pack()
        
        self.cost_per_unit_label = ttk.Label(frame, text="", font=label_font)
        self.cost_per_unit_label.pack()
        
        self.cost_pkr_label = ttk.Label(frame, text="", font=label_font)
        self.cost_pkr_label.pack()

    def create_input(self, parent, label_text, variable, label_font, input_font):
        ttk.Label(parent, text=label_text, font=label_font).pack(anchor=tk.W, pady=5)
        ttk.Entry(parent, textvariable=variable, font=input_font).pack(fill=tk.X, pady=5)

    def calculate_nuclear_cost(self):
        try:
            construction_cost = float(self.construction_cost_var.get())
            interest_dep = float(self.interest_dep_var.get())
            operating_cost = float(self.operating_cost_var.get())
            maintenance_cost = float(self.maintenance_cost_var.get())
            annual_energy = float(self.annual_energy_var.get())

            self.fixed_cost = construction_cost * (interest_dep / 100)
            self.variable_cost = maintenance_cost + operating_cost
            self.cost_per_unit = (self.fixed_cost + self.variable_cost) / annual_energy
            self.cost_pkr = self.cost_per_unit * 285

            self.update_results()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")

    def update_results(self):
        self.fixed_cost_label.config(text=f'Fixed Cost $ : {self.fixed_cost:.2f} per kWh')
        self.variable_cost_label.config(text=f'Variable Cost $ : {self.variable_cost:.2f} per kWh')
        self.cost_per_unit_label.config(text=f'Cost per Unit $/KWh : {self.cost_per_unit:.2f} per kWh')
        self.cost_pkr_label.config(text=f'Cost per Unit pkr/KWh : {self.cost_pkr:.2f} per kWh')

    def destroy(self):
        self.top.destroy()
