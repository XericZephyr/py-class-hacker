import sys
import types

from py_class_hacker import register_class_hook, register_module_hook

__author__ = 'zhengxu'


class Target(object):
    pass


class Target2(object):
    pass


class Hacker(Target, Target2, object):

    @classmethod
    def class_add(cls, a, b):
        return a + b

    def add(self, a, b):
        return a + b

    @staticmethod
    def static_add(a, b):
        return a + b

    @property
    def num(self):
        return 1


def ut_test_module_hack():
    t = Target()
    register_module_hook()   # hook all classes
    print t.add(1, 2)
    print Target.class_add(1, 2)
    print t.static_add(1, 2)
    print t.num


if __name__ == '__main__':
    ut_test_module_hack()
