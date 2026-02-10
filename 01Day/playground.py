# print("hello, world!")

# a = 500
# b = 500
# print(id(a))
# print(id(b))
# print(a is b)

import dis

code = "print('Hello')"
compiled_code = compile(code, '<string>', 'exec')
dis.dis(compiled_code)

print(dir(list()))
