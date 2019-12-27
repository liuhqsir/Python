def f():
	print('in f()',1)
	yield 1

	print('in f()',2)
	yield 2

	print('in f()',3)
	yield 3
g = f()
"""
print(next(g))         ##这个是第一次
print(next(g))         ##这个是第二次
print(next(g))         
print(next(g))         ##这个是第三次
"""
for x in g:
	print(x)       ##这个是第四次
