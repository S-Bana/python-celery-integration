from two import add


result = add.delay(5,8)

# get result without time out , unlimited loop, not good !
print(result.get())

