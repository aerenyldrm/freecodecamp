class Vector2D:
    def __init__(self, *, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return str(tuple(getattr(self, component) for component in vars(self)))
    def __repr__(self):
        argument_list = [f"{key} = {value}" for key, value in vars(self).items()]
        argument_to_join = ", ".join(argument_list)
        return f"{self.__class__.__name__}({argument_to_join})"
    def __add__(self, other):
        if type(self) != type(other):
            NotImplemented
        else:
            kwargument = {component: getattr(self, component) + getattr(other, component) for component in vars(self)}
            return self.__class__(**kwargument)
    def __sub__(self, other):
        if type(self) != type(other):
            NotImplemented
        else:
            kwargument = {component: getattr(self, component) - getattr(other, component) for component in vars(self)}
            return self.__class__(**kwargument)
    def __mul__(self, other):
        if type(other) in (int, float):
            kwargument = {component: getattr(self, component) * other for component in vars(self)}
            return self.__class__(**kwargument)
        elif type(self) == type(other):
            return sum(getattr(self, component) * getattr(other, component) for component in vars(self))
        else:
            return NotImplemented
    def __eq__(self, other):
        if type(self) != type(other):
            return NotImplemented
        else:
            return all(getattr(self, component) == getattr(other, component) for component in vars(self))
    def __ne__(self, other):
        return not self == other
    def __lt__(self, other):
        if type(self) != type(other):
            NotImplemented
        else:
            return self.norm() < other.norm()
    def __gt__(self, other):
        if type(self) != type(other):
            NotImplemented
        else:
            return self.norm() > other.norm()
    def __le__(self, other):
        return not self > other
    def __ge__(self, other):
        return not self < other
    def norm(self):
        return sum(value**2 for value in vars(self).values())**0.5
class Vector3D(Vector2D):
    def __init__(self, *, x, y, z):
        super().__init__(x=x, y=y)
        self.z = z
    def cross(self, other):
        if type(self) != type(other):
            NotImplemented
        else:
            kwargument = {
                'x': self.y * other.z - self.z * other.y,
                'y': self.z * other.x - self.x * other.z,
                'z': self.x * other.y - self.y * other.x
            }
            return self.__class__(**kwargument)
a_vector = Vector3D(x = 3, y = 4, z = 12)
other_vector = Vector3D(x = 2, y = 3, z=1)
print(a_vector.norm())
print(a_vector)
print(a_vector.__repr__())
print(a_vector + other_vector)
print(a_vector - other_vector)
print(a_vector * 2)
print(a_vector * other_vector)
print(a_vector == other_vector)
print(a_vector.__ne__(other_vector))
print(a_vector < other_vector)
print(a_vector.cross(other_vector))