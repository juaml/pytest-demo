"""Provide model API."""


def add(a, b):
    """Add two values."""
    if isinstance(a, str) or isinstance(b, str):
        raise ValueError("Adding of strings not allowed!")

    return a + b


def mul(a, b):
    """Multiply two values."""
    return a * b


def predict(x):
    """Predict y for new observation x."""
    intercept = 5
    coef = 0.7
    return add(mul(coef, x), intercept)


def main():
    for x in range(10):
        y = predict(x)
        print(f"f({x}) = {y}")


if __name__ == "__main__":
    main()
