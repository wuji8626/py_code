# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/24 22:59

#print(10/0)

import traceback
try:
    print('-----------------------')
    print(10/0)
except:
    traceback.print_exc()