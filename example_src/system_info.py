"""
위 코드에서 psutil.cpu_percent() 함수는 현재 CPU 사용률을 반환하며,
psutil.cpu_count() 함수는 시스템에 있는 CPU 코어 수를 반환합니다.
psutil.virtual_memory() 함수는 메모리 사용량 정보를 반환하며,
psutil.disk_usage('/') 함수는 루트 디렉토리의 디스크 사용량 정보를 반환합니다.
반환된 정보들을 활용하여 필요한 처리를 수행할 수 있습니다.
"""
import psutil

# CPU 정보 얻기
cpu_percent = psutil.cpu_percent()
cpu_count = psutil.cpu_count()

print(f"CPU 사용률: {cpu_percent}%")
print(f"CPU 코어 수: {cpu_count}")

# 메모리 정보 얻기
virtual_memory = psutil.virtual_memory()

total_memory = virtual_memory.total // (1024*1024)
available_memory = virtual_memory.available // (1024*1024)
used_memory = total_memory - available_memory

print(f"전체 메모리: {total_memory}MB")
print(f"사용 가능한 메모리: {available_memory}MB")
print(f"사용 중인 메모리: {used_memory}MB")

# 디스크 정보 얻기
disk_usage = psutil.disk_usage('/')

total_disk_space = disk_usage.total // (1024*1024*1024)
used_disk_space = disk_usage.used // (1024*1024*1024)
free_disk_space = disk_usage.free // (1024*1024*1024)

print(f"전체 디스크 용량: {total_disk_space}GB")
print(f"사용 중인 디스크 용량: {used_disk_space}GB")
print(f"여유 있는 디스크 용량: {free_disk_space}GB")
