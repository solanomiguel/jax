from jax.interpreters import cse
import jax.linear_util as lu
from jax.core import pack
import jax.numpy as np
from jax import make_jaxpr, grad, jvp

###

# def f(x):
#   return np.sin(x) + np.sin(x)

# print f(3.)
# print cse.cse(lu.wrap_init(f)).call_wrapped(3.)
# print make_jaxpr(cse.cse(lu.wrap_init(f)).call_wrapped)(3.)

# print grad(f)(3.)
# print grad(cse.cse(lu.wrap_init(f)).call_wrapped)(3.)

# print grad(f)(3.)
# print cse.cse(lu.wrap_init(grad(f))).call_wrapped(3.)

# print
# print

###

# def f(x):
#   # return (np.sin(x) + np.cos(x)) + (np.cos(x) + np.sin(x))
#   return (np.sin(x) + np.cos(x)) + (np.sin(x) * np.cos(x))

# print f(3.)
# print cse.cse(lu.wrap_init(f)).call_wrapped(3.)
# print make_jaxpr(cse.cse(lu.wrap_init(f)).call_wrapped)(3.)

# print
# print

###

# def f(x):
#   y = x + x + x + x + x + x + x
#   return y + y

# print f(3.)
# print cse.cse(lu.wrap_init(f)).call_wrapped(3.)
# print make_jaxpr(cse.cse(lu.wrap_init(f)).call_wrapped)(3.)

###

# from collections import Counter

# def deriv(f):
#   return lambda x: jvp(f, (x,), (1.,))


# def f(x):
#   return np.sin(x) + np.cos(x) + np.tan(x)

# g = f
# for i in range(6):
#   jaxpr = make_jaxpr(g)(3.)
#   print(Counter(eqn.primitive for eqn in jaxpr.eqns).most_common())

#   g = deriv(g)