import math as m


class MullerMethod:

    def __init__(self, f, x0, x1, x2, tolerance=1e-6, max_iterations=10):
        self.f = f
        self.x0 = x0
        self.x1 = x1
        self.x2 = x2
        self.tolerance = tolerance
        self.max_iterations = max_iterations

    def UpdateRoote(self):
        d1 = self.f(self.x0) - self.f(self.x2)
        d2 = self.f(self.x1) - self.f(self.x2)
        h1_2 = self.x0 - self.x1
        h2_3 = self.x1 - self.x2
        c = self.f(self.x1)

        a = ((h1_2 * d2) - (h2_3 * d1)) / ((h1_2 * h2_3) * (self.x1 - self.x0))
        b = ((h1_2 ** 2) * d2 - (h2_3 ** 2) * d1) / ((self.x0 - self.x1) * (h2_3 * h1_2))

        if abs(b) < 1e-10:
            print("Warning: Division by zero encountered. Exiting.")
            return None

        discriminant = b ** 2 - 4 * a * c

        if discriminant < 0:
            print("Negative discriminant encountered. Root finding might not converge.")
            return None

        updated_root = self.x1 - (2 * c) / (b + m.sqrt(discriminant))

        return updated_root

    def find_root(self):

        for iteration in range(self.max_iterations):
            # Calculate updated root estimate
            updated_root = self.UpdateRoote()
            if updated_root is None:
                return

            # Check for convergence
            if abs((updated_root - self.x1) / updated_root) < self.tolerance:
                print(f"Number of iterations: {iteration + 1}")
                print(f"Root: {updated_root}")
                print(f"Tolerance: {self.tolerance}")
                break

            # Update guesses for the next iteration
            self.x0, self.x1, self.x2 = (self.x1, updated_root, self.x2 if updated_root > self.x1 else self.x0)


if __name__ == "__main__":
    f = lambda x: m.cos(x) - 1.3 * x  # If I do 'm.tan(x) -1.3*x' then a root will be found
    x0 = 0
    x1 = 0.5
    x2 = 1
    tolerance = 0.01
    max_iterations = 20
    mullerM = MullerMethod(f, x0, x1, x2, tolerance, max_iterations)
    mullerM.find_root()
