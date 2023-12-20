# ode_solver.py
import numpy as np

def euler_method(y0, t_span, h, equation):
    t_values = np.arange(t_span[0], t_span[1] + h, h)
    y_values = [y0]

    for t in t_values[:-1]:
        y_next = y_values[-1] + h * eval(equation, {'t': t, 'y': y_values[-1]})
        y_values.append(y_next)

    return t_values, y_values

def heun_method(y0, t_span, h, equation):
    t_values = np.arange(t_span[0], t_span[1] + h, h)
    y_values = [y0]

    for t in t_values[:-1]:
        k1 = eval(equation, {'t': t, 'y': y_values[-1]})
        k2 = eval(equation, {'t': t + h, 'y': y_values[-1] + h * k1})
        y_next = y_values[-1] + 0.5 * h * (k1 + k2)
        y_values.append(y_next)

    return t_values, y_values

def runge_kutta_method(y0, t_span, h, equation):
    t_values = np.arange(t_span[0], t_span[1] + h, h)
    y_values = [y0]

    for t in t_values[:-1]:
        k1 = eval(equation, {'t': t, 'y': y_values[-1]})
        k2 = eval(equation, {'t': t + 0.5 * h, 'y': y_values[-1] + 0.5 * h * k1})
        k3 = eval(equation, {'t': t + 0.5 * h, 'y': y_values[-1] + 0.5 * h * k2})
        k4 = eval(equation, {'t': t + h, 'y': y_values[-1] + h * k3})

        y_next = y_values[-1] + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
        y_values.append(y_next)

    return t_values, y_values

def solve_ode(method, initial_value, t_span, h, equation):
    if method == 'euler':
        return euler_method(initial_value, t_span, h, equation)
    elif method == 'heun':
        return heun_method(initial_value, t_span, h, equation)
    elif method == 'runge_kutta':
        return runge_kutta_method(initial_value, t_span, h, equation)
    else:
        raise ValueError(f"Unsupported method: {method}")
