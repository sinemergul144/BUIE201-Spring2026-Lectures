def fit(x, y):
    if len(x) != len(y):
        raise ValueError("x and y must have the same length")
    if len(x) < 2:
        raise ValueError("At least two data points are required")

    n = len(x)

    mean_x = sum(x) / n
    mean_y = sum(y) / n

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator += (x[i] - mean_x) * (y[i] - mean_y)
        denominator += (x[i] - mean_x) ** 2

    if denominator == 0:
        raise ValueError("Cannot compute slope (all x values may be identical)")

    m = numerator / denominator
    b = mean_y - m * mean_x

    return m, b


def predict(x_value, m, b):
    return m * x_value + b


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 5, 4, 5]

    m, b = fit(x, y)

    print(f"y = {m:.2f}x + {b:.2f}")
    print("Predicted value for x=6:", predict(6, m, b))