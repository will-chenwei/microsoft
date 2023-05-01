#-*-coding:utf-8-*-

class Student(object):

    """

    自定义Student类

    """

    def __init__(self, name, score):

    # 初始化Student，参数name,score

        self.name = name

        self.score = score

    def __cmp__(self, other):

    # 重写比较方法，根据Student类属性score进行比较

        return cmp(self.score, other.score)

    def show(self):

        return 'name:'+self.name+'; score:'+str(self.score)

 

def get_input():

    name = raw_input('input name  ')

    if not name: # 当姓名输入为空时，返回None

        return (None,None)

    score = raw_input('input %s\'s score  ' % name)

    if name and score:

        return (name,int(score)) # 为方便比较，将score强制转换为int型

    else:

        return (None,None)

 

def main():

    s_list = []

    while True: # 一直循环输入姓名及成绩

        name,score = get_input()

        if name and score:

            s = Student(name, score)

            s_list.append(s)

        else: # 当输入姓名或成绩为空时跳出循环

            break

    s_list.sort() # 对Student实体进行排序

    for i,s in enumerate(s_list): # 遍历已经排序的实体列表，并进行显示

        print ' '.join([str(i+1), s.name, str(s.score)])

 

if __name__ == '__main__':

    main()

输入及输出如下

input name  a

input a's score  97

input name  b

input b's score  95

input name  c

input c's score  96

input name  

1 b 95

2 c 96

3 a 97
