class perfectnumber:
  def solution(self,n):
    if n<=0:
      return  False
    sum = 0
    for i in range(1,n):
      if n%i == 0:
        sum += i
    return sum == n
obj = perfectnumber()
if obj.solution(6}:
  print(True)
else:
  print(False)
