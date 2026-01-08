class A:
    def make_sound(self):
        return "A sound"
class AA(A):
    def make_sound(self):
        return "AA sound"

class AAA(AA):
    def make_sound(self):
        return "AAA sound"

class B:
    def make_sound(self):
        return "B sound"

class BB(B):
    def make_sound(self):
        return "BB sound"

class BBB(BB):
    def make_sound(self):
        return "BBB sound"

class C:
    def make_sound(self):
        return "C sound"
class CC(C):
    def make_sound(self):
        return "CC sound"
class CCC(CC):
    def make_sound(self):
        return "CCC sound"

class D(AAA, BBB, CCC):
    pass

obj = D()
print(obj.make_sound())
print(D.mro())
