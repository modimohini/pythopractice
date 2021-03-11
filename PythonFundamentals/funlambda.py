def my_function(tools, bk="EXPRESS"):
  print("frontend tools: " + tools + "backend: " + bk)

my_function("HTML ", "React")
my_function("CSS ", "MERN")
my_function("JS " )

# lambda

x = lambda a, b, c : a + b * c
print(x(1,2,3))

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


# py --> obj, class ==> obj constructor/blueprint 
class myclass:
    m = 1
m1 = myclass()
print(m1.m)

