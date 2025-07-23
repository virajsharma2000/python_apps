import ctypes

gpu_driver = ctypes.CDLL('libcuda.so')

gpu_driver.cuInit(0)

devices_count = ctypes.c_int()
status = gpu_driver.cuDeviceGetCount(ctypes.byref(devices_count))

for i in range(devices_count.value):
 name = ctypes.create_string_buffer(100)
 gpu_driver.cuDeviceGetName(name, 100, i)

 ctx = ctypes.c_void_p()
 gpu_driver.cuCtxCreate(ctypes.byref(ctx), i, i)

 free_memory = ctypes.c_size_t()
 total_memory = ctypes.c_size_t()
 clock_rate = ctypes.c_int()

 gpu_driver.cuMemGetInfo(ctypes.byref(free_memory), ctypes.byref(total_memory))
 gpu_driver.cuDeviceGetAttribute(ctypes.byref(clock_rate), 13, i)

 print('device name:', name.value.decode())
 print('total memory:', round(total_memory.value / (1024 ** 3), 2), 'GB')
 print('free memory:', round(free_memory.value / (1024 ** 3), 2), 'GB')
 print('used memory:', round(total_memory.value / (1024 ** 3) - free_memory.value / (1024 ** 3), 2), 'GB')
 print('clock rate:', clock_rate.value / 1_000_000, 'GHZ')
 
 print()

# I love nvidia + python
# first nvidia was hardware only, software did not at all knew about it
# now they are the best ever friends ever in the world
# viraj sharma