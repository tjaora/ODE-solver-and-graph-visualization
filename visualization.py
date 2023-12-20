# visualization.py
import matplotlib.pyplot as plt

def plot_solution(t_values, y_values, method_name):
    plt.plot(t_values, y_values, label=method_name)
    plt.xlabel('Time')
    plt.ylabel('Solution')
    plt.legend()

def plot_influence(t_values_list, y_values_list, parameter_name):
    plt.figure(figsize=(8, 6))

    for i in range(len(t_values_list)):
        plt.plot(t_values_list[i], y_values_list[i], label=f'{parameter_name}={i + 1}')

    plt.xlabel('Time')
    plt.ylabel('Solution')
    plt.title(f'Influence of {parameter_name} on Solutions')
    plt.legend()
    plt.show()

# Example usage:
# Assuming t_values and y_values for different step sizes are available
t_values_1, y_values_1 = [0, 1, 2, 3], [0, 1, 4, 9]  # Example data for step size 1
t_values_2, y_values_2 = [0, 0.5, 1, 1.5, 2, 2.5, 3], [0, 0.25, 1, 2.25, 4, 6.25, 9]  # Example data for step size 0.5

# Plotting the influence of step size on solutions
plot_influence([t_values_1, t_values_2], [y_values_1, y_values_2], 'Step Size')
