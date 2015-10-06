import sys
import types

__author__ = 'zhengxu'



"""
    TODO: Add multi-base class support
"""


class Target(object):
    pass


class Target2(object):
    pass


class Hacker(Target, Target2, object):
    @classmethod
    def __evil_xz_hack_base__(cls, strategy='safe'):
        """
        :param strategy: 'safe' or 'override'
        :return:
        """
        base_classes = cls.__bases__
        for base_class in base_classes:
            print base_class
        base_class = cls.__base__
        for x in cls.__dict__:
            if not (x in base_class.__dict__) or not (strategy == 'safe'):
                # instance method
                if isinstance(cls.__dict__[x], (types.FunctionType, classmethod, staticmethod, property)):
                    setattr(base_class, x, cls.__dict__[x])
                else:
                    print "Warning: Unsupported Wrap Type: [%s:%s] %s" % \
                          (str(x), type(cls.__dict__[x]), str(cls.__dict__[x]))

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


def ut_test_hack():
    Hacker.__evil_xz_hack_base__()
    # test instance method
    t = Target()
    print t.add(1, 2)
    print Target.class_add(1, 2)
    print t.static_add(1, 2)
    print t.num

    # for register all classes in current function
    current_module = sys.modules[__name__].__dict__
    for k, v in current_module.iteritems():
        if isinstance(v, (type, types.ClassType)):
            print k, v



if __name__ == '__main__':
    ut_test_hack()
