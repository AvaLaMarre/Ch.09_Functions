import random
import math


def volume_sphere(radius):
    pie = math.pi
    vol = 4/3 * pie * radius**3
    return vol
    #print(f"The Volume Is {vol:.2f} ")


def volume_cylinder(r,h):
    '''this function determines the volume of an cylinder'''
    pie = math.pi
    vol = pie * r**2 *h
    return vol
    #print(f"The Volume Is {vol:.2f}")


def main():
    print(volume_cylinder(1,5))
    print(volume_sphere(3))
    print(__name__)


if __name__ == "__main__":
    main()

volume = volume_cylinder(5,12)
print(volume)
volume = volume_sphere(5)

print(help(volume_cylinder))

num = 10
print("hello world", + num)