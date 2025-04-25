from datetime import date

import time


startTime = time.perf_counter()


ldates = []
d1 = date(2024, 4, 13)
d2 = date(2022, 5, 16)
d3 = date(2023, 8, 30)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)

ldates.sort()
time.sleep(4)

for d in ldates:
    print(d)
    
    
endTime  = time.perf_counter()

print("Execution Time is : ")
