import numpy as np

#! We can install the special library from the website. You can reach the website below the links;
# https://pypi.org/

#! Actually, if you use the visual studio code, you can reach the terminal the below side. Write "pip install numpy", and after installing, you can import inside your project.

grades = np.random.normal(80, 30, 100)
print(np.mean(grades))
