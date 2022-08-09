class A:

    def __init__(self, zmienna):
        self.zmienna = zmienna

    def api(self):
        return f"Wartość = {self.zmienna}"


class B(A):

    def __init__(self, zmienna):
        self.zmienna = zmienna

    def api(self):
        return f"Inna wartość = {self.zmienna}"


x1 = A("Linux OS")
x2 = B(["Linux", 5, "Kernel"])
x1_test = x1.api()
x2_test = x2.api()

print(x1_test)
print(x1_test=="Wartość = Linux OS")

print(x2_test)
print(x2_test=="Inna wartość = ['Linux', 5, 'Kernel']")

test_1 = A("Sharp MZ-731")
test_2 = B("CPU Motorola 6800")

print(test_1.api())
print(test_2.api())
# print(isinstance(x1, A))
# print(isinstance(x1, B))
# print(isinstance(x2, A))
# print(isinstance(x2, B))

# Wartość = Linux OS
# True
# Inna wartość = ['Linux', 5, 'Kernel']
# True
# True
# False
# True
# True
