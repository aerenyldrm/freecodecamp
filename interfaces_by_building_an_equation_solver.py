from abc import ABC, abstractmethod # abstract base class
import re
class Equation(ABC):
    degree: int
    type: str
    def __init__(self, *arguments):
        if self.degree + 1 != len(arguments):
            raise TypeError(f"'Equation' object gets {self.degree + 1} positional arguments but {len(arguments)} were provided.")
        if any(not isinstance(argument, (int, float)) for argument in arguments):
            raise TypeError("It is necessary to select coefficients as type of 'int' or 'float'.")
        if arguments[0] == 0:
            raise ValueError("It is necessary that highest degree coefficient is different from 0.")
        self.coefficients = {len(arguments) - n - 1: argument for n, argument in enumerate(arguments)}
    def __init_subclass__(cls):
        if not hasattr(cls, "degree"):
            raise AttributeError(f"Not able to create '{cls.__name__}' class: missing required attribute 'degree'.")
        if not hasattr(cls, "type"):
            raise AttributeError(f"Not able to create '{cls.__name__}' class: missing required attribute type'.")
    def __str__(self):
        terms = []
        for n, coefficient in self.coefficients.items():
            if not coefficient:
                continue
            if n == 0:
                terms.append(f"{coefficient:+}")
            elif n == 1:
                terms.append(f"{coefficient:+}x")
            else:
                terms.append(f"{coefficient:+}x**{n}")
        equation_string = " ".join(terms) + " = 0"
        return re.sub(r"(?<!\d)1(?=x)", "", equation_string.strip("+"))
    @abstractmethod
    def solve(self):
        pass
    @abstractmethod
    def analyze(self):
        pass
class LinearEquation(Equation):
    degree = 1
    type = "LNEAR EQUATION"
    def solve(self):
        a, b = self.coefficients.values()
        x = - b / a
        return [x]
    def analyze(self):
        slope, intercept = self.coefficients.values()
        return {"slope": slope, "intercept": intercept}
class QuadraticEquation(Equation):
    degree = 2
    type = "QUADRATIC EQUATION"
    def __init__(self, *arguments):
        super().__init__(*arguments)
        a, b, c = self.coefficients.values()
        self.delta = b ** 2 - 4 * a * c
    def solve(self):
        if self.delta < 0:
            return []
        a, b, _ = self.coefficients.values()
        x1 = (- b + (self.delta) ** 0.5) / (2 * a)
        x2 = (- b - (self.delta) ** 0.5) / (2 * a)
        if self.delta == 0:
            return [x1]
        return [x1, x2]
    def analyze(self):
        a, b, c = self.coefficients.values()
        x = - b / (2 * a)
        y = a * x ** 2 + b * x + c
        if a > 0:
            concavity = 'upwards'
            min_max = 'min'
        else:
            concavity = 'downwards'
            min_max = 'max'
        return {'x': x, 'y': y, 'min_max': min_max, 'concavity': concavity}
def solver(equation):
    if not isinstance(equation, Equation):
        raise TypeError("It is neccessary that argument is an Equation object.")
    output_string = f"\n{equation.type:-^24}"
    output_string += f"\n\n{equation!s:^24}\n\n"
    output_string += f"{'SOLUTION':-^24}\n\n"
    results = equation.solve()
    match results:
        case []:
            results_list = ["No real roots exist."]
        case [x]:
            results_list = [f"x = {x:+.3f}"]
        case [x1, x2]:
            results_list = [f"x1 = {x1:+.3f}", f"x2 = {x2:+.3f}"]
    for result in results_list:
        output_string += f"{result:^24}\n"
    output_string += f"\n{'DETAIL':-^24}\n\n"
    details = equation.analyze()
    match details:
        case {'slope': slope, 'intercept': intercept}:
            details_list = [f'slope = {slope:>16.3f}', f'y - intercept = {intercept:>8.3f}']
        case {'x': x, 'y': y, 'min_max': min_max, 'concavity': concavity}:
            coordinates = f'({x:.3f}, {y:.3f})'
            details_list = [f'concavity = {concavity:>12}', f'{min_max} = {coordinates:>18}']
    for detail in details_list:
        output_string += f'{detail}\n'
    return output_string
linear_equation = LinearEquation(2, 3)
quadratic_equation = QuadraticEquation(1, 2, 1)
print(solver(linear_equation))
print(solver(quadratic_equation))