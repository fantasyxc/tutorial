print('Hello, python!!')
print('11111')

a = 'bbbb'
print(a)

b = 123_4888888888888888888888888888888888_88888999999999999999999999999999999
print(b)

c = 1234567890, 00000, 00000
print(type(c))

name = 'XiaChang'
# 使用四种方式来输出字符串
# 1. 拼串
print('Welcome ' + name + ' !')
# 2. 多个参数
print('Welcome', name, '!')
# 3. 占位符
print('Welcome %s !' % name)
# 4. 格式化字符串
print(f'Welcome {name} !')

num_a = 100 ** 2
num_b = 100 ** 0.5
print('num_a=', num_a, ', num_b=', num_b)

print(1 == 1)

print(not(1))

print(1 and 0 and 3)
print(1 and 2 and 3)
print(1 and 2 and 0)
print(0 and 1 and 3)

a = 20
b = 30
print("a 大于 b") if (a > b) else print("b 大于 a")

aa = 1 or 2 and 3
print('aa =', aa)