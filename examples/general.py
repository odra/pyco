import pyco


def fn(msg):
    return msg


#builds a function object from another function
fn1 = pyco.from_fn(fn)

#function object as dict
print(fn1.as_dict())

#function code object as dict
print(fn1.code.as_dict())

#calls fn from fn1
print(fn1('Hello World!'))


#builds a function object from  a code object
fn2 = pyco.from_code(fn.__code__)

#calls fn from fn2
print(fn2('Hello World!'))


#builds a code object from a function
co1 = pyco.Code.from_fn(fn)

#code as dict
print(co1.as_dict())

#code object
print(co1.as_code())


#builds code object from native code
co2 = pyco.Code.from_code(fn.__code__)

#show co2 as dict
print(co2.as_dict())
