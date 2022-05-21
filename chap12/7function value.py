# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/21 11:52

#元素返回多个值时,结果为元组

def smidgen(num):
    odd=[]
    even=[]
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

print(smidgen([10,29,34,44,53,55]))