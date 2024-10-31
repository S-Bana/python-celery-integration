from two import add


result = add.delay(5,8)

# get result without time out , unlimited loop, not good !
# print(result.get())

# get result with time out ,but have timeout error exception, ok.
# print(result.get(timeout=3))

if result.ready():
    print(result.get(timeout=3))
