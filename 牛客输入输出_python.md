当输入是单个整数
```python
n = int(input)
```

当输入的一行有多个整数，使用split函数将不同的整数分开
将其转化为整型，再转为list列表
```python
a = list(map(int, input().split()))
```

输入多行,不知道多少行
```python
while True:
    try:
        a = list(map(int, input().split()))
        print(sum(a))
    except:
        break
```

输入多行，确定多少行
```python
n = int(input())
for i in range(n):
    a = list(map(int, input().split()))
    print(sum(a))
```

```python
#'多行输入'
res = []
n = int(input())#行数
for _ in range(n):
    s = input()
    if s!='':
        temp = [j for j in s.split()] #str输入
        # temp = [int(j) for j in s.split()] #int输入
        res.append(temp[0])
    else:
        break
print(res)
```

参考：
[牛客输入输出练习](https://ac.nowcoder.com/acm/contest/5652)
[牛客网OJ系统的常见输入输出(Python语言)](https://blog.csdn.net/weixin_43593330/article/details/108299217?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-1&spm=1001.2101.3001.4242)
[牛客网 多行输入输出问题 Python3 模板样例](https://blog.csdn.net/qq_39938666/article/details/101004633)