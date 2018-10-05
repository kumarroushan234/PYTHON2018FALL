class emp:
  "this is example of employee class"
  empcnt=0
  sumsal=0
  def __init__(self,ename,sal,family,dept):
      self.ename=ename
      self.sal=sal
      self.family=family
      self.dept=dept
      emp.empcnt+=1
      emp.sumsal+=sal

  def display(self):
      print("name:",self.ename,"salary:",self.sal,"family:",self.family,"dept:",self.dept)

class fulltime(emp):
    def __init__(self,n,s,f,d):
        emp.__init__(self,n,s,f,d)

emplpoyee1=emp("navya",5000,"mother,father","development")
emplpoyee2=emp("ramya",4000,"sister","support")
emplpoyee3=emp("sirisha",2000,"brother","HR")
emplpoyee4=fulltime("sasleen",3000,"none","production")
emplpoyee4.display()
print("total employees", emp.empcnt)
avg = emp.sumsal/emp.empcnt
print("average sal", avg)
