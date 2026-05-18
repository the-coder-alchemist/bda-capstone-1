import time

start = time.perf_counter()

# code to time goes here

end = time.perf_counter()
elapsed = end - start
#Use round() to show the time with 2 decimal points:

serial_time = round(elapsed, 2)
print(f"Serial execution: {serial_time}")