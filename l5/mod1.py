import mod3


def mod1():
    print('Func from mod1.py')


def go():
    print('Go from mod1.py')

# go() will not be imported in lesson.py

__all__ = ['mod1']

print('This is mod1.py')
print(__name__)
mod3.mod3()