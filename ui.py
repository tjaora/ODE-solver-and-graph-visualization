# ui.py
import tkinter as tk
from tkinter import ttk
from ode_solver import solve_ode
from visualization import plot_solution, plot_influence
from result_presentation import display_solutions, compare_methods_accuracy

class OdeSolverUI:
    def __init__(self, master):
        self.master = master
        self.master.title("ODE Solver Tool")

        # UI components
        self.method_label = ttk.Label(self.master, text="Select ODE solver method:")
        self.method_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        self.method_var = tk.StringVar()
        self.method_combobox = ttk.Combobox(self.master, textvariable=self.method_var, values=['euler', 'heun', 'runge_kutta'])
        self.method_combobox.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
        self.method_combobox.set('euler')

        self.initial_value_label = ttk.Label(self.master, text="Enter initial value:")
        self.initial_value_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        self.initial_value_entry = ttk.Entry(self.master)
        self.initial_value_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        self.step_size_label = ttk.Label(self.master, text="Enter step size:")
        self.step_size_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

        self.step_size_entry = ttk.Entry(self.master)
        self.step_size_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

        self.start_time_label = ttk.Label(self.master, text="Enter start time:")
        self.start_time_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

        self.start_time_entry = ttk.Entry(self.master)
        self.start_time_entry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

        self.end_time_label = ttk.Label(self.master, text="Enter end time:")
        self.end_time_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

        self.end_time_entry = ttk.Entry(self.master)
        self.end_time_entry.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)

        self.equation_label = ttk.Label(self.master, text="Enter ODE in terms of t and y:")
        self.equation_label.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)

        self.equation_entry = ttk.Entry(self.master)
        self.equation_entry.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)

        self.solve_button = ttk.Button(self.master, text="Solve", command=self.solve_ode)
        self.solve_button.grid(row=6, column=0, columnspan=2, pady=10)

    def solve_ode(self):
        method = self.method_var.get()
        initial_value = float(self.initial_value_entry.get())
        step_size = float(self.step_size_entry.get())
        start_time = float(self.start_time_entry.get())
        end_time = float(self.end_time_entry.get())
        equation = self.equation_entry.get()

        t_values, y_values = solve_ode(method, initial_value, (start_time, end_time), step_size, equation)

        plot_solution(t_values, y_values, method.capitalize())

        # Example: Visualizing the influence of time on the solution
        plot_influence(t_values, y_values, "Time")

        # Example: Displaying numerical solutions
        display_solutions({method: (t_values, y_values)})

        # Example: Comparing methods accuracy
        errors = compare_methods_accuracy({'euler': 0.01, 'heun': 0.005, 'runge_kutta': 0.001})
        print("Errors:", errors)


def run_ui():
    root = tk.Tk()
    app = OdeSolverUI(root)
    root.mainloop()
