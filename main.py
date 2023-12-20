# main.py
from ui import run_ui
from ode_solver import euler_method
from visualization import plot_solution, plot_influence
from result_presentation import display_solutions, compare_methods_accuracy

def main():
    run_ui()

    # Example input
    method = 'euler'
    initial_value = 1.0
    step_size = 0.1
    start_time = 0.0
    end_time = 2.0
    equation = 't - y'

    # Solve the ODE
    t_values, y_values = euler_method(initial_value, (start_time, end_time), step_size, equation)

    # Display the solution plot
    plot_solution(t_values, y_values, method.capitalize())

    # Visualize the influence of step size on solutions
    t_values_list = []
    y_values_list = []

    # Example: Influence of step size on solutions for step sizes 0.1, 0.5
    for step in [0.1, 0.5]:
        t, y = euler_method(initial_value, (start_time, end_time), step, equation)
        t_values_list.append(t)
        y_values_list.append(y)

    # Plotting the influence of step size on solutions
    plot_influence(t_values_list, y_values_list, 'Step Size')

    # Display numerical solutions
    display_solutions({method: (t_values, y_values)})

    # Compare methods accuracy (placeholder error values)
    errors = compare_methods_accuracy({'euler': 0.01, 'heun': 0.005, 'runge_kutta': 0.001})
    print("Errors:", errors)

if __name__ == "__main__":
    main()
