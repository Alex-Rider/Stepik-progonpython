# sleep_len_minutes, start_hour, start_min, = int(input()), int(input()), int(input())
# sleep_start_minutes = start_min + start_hour * 60
# print("sleep starts", sleep_start_minutes)
# sleep_start_minutes //= (60 * 24)
# print(sleep_start_minutes)

time_to_wake_up = int(input()) + int(input()) * 60 + int(input())
print(time_to_wake_up // 60, time_to_wake_up % 60, sep="\n")

