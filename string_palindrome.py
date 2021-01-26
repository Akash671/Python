def solve(s):
   if s==s[::-1]:
      return 1
   else:
      return 0

s=str(input())
print(solve(s))
