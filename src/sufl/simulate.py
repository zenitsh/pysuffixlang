class Runnable:
    def __init__(self):
        self.dic = {}
        self.fdic = {}
        self.lis = []
        self.rs = []

    def load(self,text):
        lis_s = [self.lis]
        lis_c = self.lis
        string_list = text.split()
        for s in string_list:
            if s=="prog":
                lis_s.append(lis_c)
                lis_c = []
            elif s=="end":
                tmp_lis = lis_c
                lis_c = lis_s.pop()
                lis_c.append(tmp_lis)
            else:
                lis_c.append(s)
        return self.lis

    def run(self,lis=None):
        if lis==None:
            lis=self.lis
        lis_c = lis
        
        for s in lis_c:
            if isinstance(s, list):
                self.rs.append(s)
            elif s.isdigit():
                self.rs.append(int(s))
            elif len(s)>0 and s[0]=='\'':
                self.rs.append(s[1:])
            elif s in self.dic.keys():
                self.rs.append(self.dic[s])
            elif s in self.fdic.keys():
                self.run(self.fdic[s])
            elif s == '+':
                tmp = self.rs[-2]+self.rs[-1]
                self.rs.pop()
                self.rs[-1]=tmp
            elif s == '-':
                tmp = self.rs[-2]-self.rs[-1]
                self.rs.pop()
                self.rs[-1]=tmp
            elif s == '*':
                tmp = self.rs[-2]*self.rs[-1]
                self.rs.pop()
                self.rs[-1]=tmp
            elif s == '/':
                tmp = self.rs[-2]/self.rs[-1]
                self.rs.pop()
                self.rs[-1]=tmp
            elif s == 'sync':
                self.dic[self.rs[-1]] = self.rs[-2]
                self.rs.pop()
                self.rs.pop()
            elif s == 'func':
                self.fdic[self.rs[-1]] = self.rs[-2]
                self.rs.pop()
                self.rs.pop()
            elif s == 'cond':
                if self.rs[-3] == False:
                    self.run(self.rs[-1])
                else:
                    self.run(self.rs[-2])
            elif s == 'loop':
                s1 = self.rs[-2]
                s2 = self.rs[-1]
                self.run(s1)
                while self.rs[-3] == True:
                    self.run(s1)
                    self.run(s2)
            elif s == 'input':
                if self.rs[-1] == "int":
                    self.rs.pop()
                    self.rs.append(int(input()))
                elif self.rs[-1] == "string":
                    self.rs.pop()
                    self.rs.append(input())
            elif s == 'print':
                print(self.rs.pop())
            elif s == 'job':
                if self.rs[-1] == "sqrt":
                    self.rs[-2] = __import__("math").sqrt(self.rs[-2])
                self.rs.pop()
            print(self.dic)
            print(self.fdic)
            print(self.rs)
            print("\n")