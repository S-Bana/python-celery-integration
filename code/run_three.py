from three import add


result = add.delay(5,8)
print(result.get(timeout=10))