class Foo():
	
	foo=123
	_foo='zhangsan'
	__foo='lisi'
	'''print('running in modlue')
	def inner():
		print(3)
	return inner'''
a=Foo()
print(dir(a))
print(a.foo)