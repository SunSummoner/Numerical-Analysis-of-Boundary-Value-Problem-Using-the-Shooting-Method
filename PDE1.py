#Please check references for source code credit

import sympy as sym
sym.init_printing()
x, y, u, v = sym.symbols('x y u v')

# Streamfunction
psi = sym.Function(r'psi')(x,y)

# Define u and v based on the streamfunction
u = psi.diff(y)
v = -psi.diff(x)

# Check the continuity equation:
print(u.diff(x) + v.diff(y) == 0)
