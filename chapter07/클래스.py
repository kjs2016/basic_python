class Super :

        def __init__(self, name) :
            self.name = name

        def show(self):
            print('name -->', self.name)

class Sub(Super) :
    def __init__(self, name, job):
        super().__init__(name)
        self.job = job
    def show(self):
        super().show(); # super 키워드를 이용해서 부모 클래스의 멤버 메소드 호출
        print('job -->', self.job);
        print(self.name+"님의 직업은 "+self.job+"입니다.");

if __name__=='__main__':

   person = Sub("홍길동", "도둑")#자식 클래스로 객체를 생성
   person.show()