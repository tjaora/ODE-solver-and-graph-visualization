# result_presentation.py

def display_solutions(method_results):
    for method, (t_values, y_values) in method_results.items():
        print(f"Numerical solution for {method}:")
        for t, y in zip(t_values, y_values):
            print(f"t={t:.2f}, y={y:.4f}")

def compare_methods_accuracy(errors):
    for method, error in errors.items():
        print(f"Error for {method}: {error}")
    return errors
