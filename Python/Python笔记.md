# Python笔记
## 1. 字符串输出
1. 拼串
```python
print('Welcome ' + name + ' !')
```
2. 多个参数
```python
print('Welcome', name, '!')
```
3. 占位符
```python
print('Welcome %s !' % name)
```
4. 格式化字符串
```python
print(f'Welcome {name} !')
```

## 2. 对象
### 2.1. 对象的结构
1. ID（标识）：内存地址，通过 `id()` 来查看，变量中存储的对象的id
2. TYPE（类型）：通过 `type()` 来查看
3. VALUE（值）：可变、不可变

### 2.2. 对象比较
is比较两者是否是同一对象，同一对象返回true，不同返回false，is not相反

## 3. 逻辑运算
1. 非布尔值的逻辑运算
当我们对非布尔值进行与或运算时，Python会将其当做布尔值运算，最终会返回原值：
- **与运算是找false**：如果第一个值是false，则直接返回第一个值，就不看第二个值；如果第一个值是true，第二个也是true的话，找不到false，则返回第二个值；第二个是false的话，则返回该false的值，也就是返回第二个值
- **或运算是找true**：如果第一个值是true，就不看第二个值了，直接返回第一个值；如果第一个值是false，则判断第二个值，第二个值为true，即返回，若第二个值为false，找不到true，则返回最后一个值，即第二个值

## 4. 三元运算
- 语句1 if 条件表达式 else 语句2 

