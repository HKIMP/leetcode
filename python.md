242. 有效的字母异位词 
     学习 Counter, sorted, Unicode, 字典 values() 获取字典键对应的值 组成的列表
        
243. 字母异位词分组 
    ''.join(sorted(s)), ord(), [0]*26 和 [0 for _ in range(26)]谁快, 
    d.setdefault(tuple(count), []) 用tuple是因为 list不能做键
    如果存在tuple(count)的键，就返回对应的值，不存在就添加键，值对应[]

144. 二叉树的前序遍历
     ```python
     nonlocal global
     这里的规则是针对不可变元素：字符串，数字等
     对列表等可变元素无效。
     因为对可变元素的修改并不是针对元素本身。

     res.append(cur.val) #注意是cur.val
     ```
102. 二叉树的层序遍历
     for 和 while的问题
     ```python
     ll = [1, 2, 3]
     for _ in range(len(l)):
          print(2)
          ll.pop()
     while len(l)>1:
          print(2)
          ll.pop()
     ```
     while循环每次会刷新len(layer), for循环不会。
     统一建议
     ```python
     n = len(ll)
     for i in range(n):
          pass
     ```
300. 最长递增子序列 
     bisect.bisect_left





