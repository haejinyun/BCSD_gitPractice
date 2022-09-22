# 용량이 정해진 stack 구현
class fix_Stack:
    def __init__(self, size):
        self.size = size
        self.array = [None] * self.size  # 배열에 임의의 공간을 초기화 시킨다.
        self.top = -1  # 초기 상단의 인덱스 초기화

    def __str__(self):
        return str(self.array[::-1])  # 마지막에 들어가게끔 슬라이싱을 통해 거꾸로 출력

    def isEmpty(self):
        if self.top == -1:  # 초기 상단의 값이 변하지 않는 것. => 빈 상태에서 변하지 않았다.
            return True
        else:
            return False

    def isFull(self):
        return self.top == self.size - 1

    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = e
        else:
            print("stack overflow")
            #exit()
            pass #몇번의 오버플로우가 발생하고, 결과적으로 어느 수까지 담겼는지 확인하기 위해 exit가 아닌 pass를 사용했다

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top + 1]
        else:
            print("stack underflow")
            #exit()
            pass #몇번의 언더플로우가 발생하고, 결과적으로 어느 수까지 담겼는지 확인하기 위해 exit가 아닌 pass를 사용했다

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            pass

    def size(self):
        return self.top + 1