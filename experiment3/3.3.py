# 定义⼀个三维向量类，并定义相应的特殊⽅法实现两个该类对象之间的加、减运算(要求⽀持运算符+、-)，
# 实现该类对象与标量的乘、除运算(要求⽀持运算符*、/)，以及向量长度的计算(要求使⽤属性实现)。

import math


class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.length = math.sqrt(x ** 2 + y ** 2 + z ** 2)

    def add(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def sub(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def mul(self, other):
        return Vector3D(self.x * other, self.y * other, self.z * other)

    def div(self, other):
        return Vector3D(self.x / other, self.y / other, self.z / other)

    def __add__(self, other):
        return self.add(other)


# v1 = Vector3D(1, 2, 3)
# v2 = Vector3D(4, 5, 6)
# v3 = 3


v1 = Vector3D(3, 4, 5)
v2 = Vector3D(1, 2, 3)
v3 = 2


print("v1 + v2 = " + "(" + str(v1.add(v2).x) + ", " + str(v1.add(v2).y) + ", " + str(v1.add(v2).z) + ")")
print("v1 - v2 = " + "(" + str(v1.sub(v2).x) + ", " + str(v1.sub(v2).y) + ", " + str(v1.sub(v2).z) + ")")
print("v1 * v3 = " + "(" + str(v1.mul(v3).x) + ", " + str(v1.mul(v3).y) + ", " + str(v1.mul(v3).z) + ")")
print("v1 / v3 = " + "(" + str(v1.div(v3).x) + ", " + str(v1.div(v3).y) + ", " + str(v1.div(v3).z) + ")")
print("v1的长度为：" + str(v1.length))
print("v2的长度为：" + str(v2.length))