import random

numbera = random.randint(1, 9)
numberb = random.randint(1, 9)
symbol = random.randint(0, 1)
result = 0

print("请计算下面的公式：")
print()

if (symbol):
	result = numbera + numberb
	print("  ", numbera, " + ", numberb, " = ？")
elif (numbera > numberb):
	result = numbera - numberb
	print("  ", numbera, " - ", numberb, " = ？")
else:
	result = numbera + numberb
	print("  ", numbera, " + ", numberb, " = ？")

print()

answer = input("请输入你的答案：")
print()
if (result == int(answer)):
	print("恭喜你，回答正确！")
else:
	print("Ooops，回答错误！")