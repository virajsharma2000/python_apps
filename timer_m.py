import time
seconds=int(input("enter time"))
for i in range(seconds+1):
 print(str(seconds-i)+"seconds")
 time.sleep(1)
print("time's up")
