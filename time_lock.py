import sys
import datetime as dt
from decimal import *
from hashlib import md5

# To test with custom current time and epoch modify the current_time_dt and since_time_dt variables respectively
# To refactor, just delete leading zeros and relace spaces with commas, and make it individual integers, not a single string.
# e.g.: "2017 03 23 18 02 06" dt.datetime(2017,3,23,18,2,6)

if __name__ == '__main__':
    # get base time
    since_time = sys.stdin.readlines()[0].replace('\n','')
    print(f"epoch.txt:            {since_time}")

    # get current time
    # current_time_dt = dt.datetime.now()
    # change to set custom
    current_time_dt = dt.datetime(2017,4,23,18,2,30)
    current_time_dt_str = str(current_time_dt)
    current_time = f"{current_time_dt_str[0:4]} {current_time_dt_str[5:7]} {current_time_dt_str[8:10]} {current_time_dt_str[11:13]} {current_time_dt_str[14:16]} {str(round(Decimal(current_time_dt_str[17:])))}"
    print(f"current system time:  {current_time}")

    # get date diff
    since_time_dt = dt.datetime(int(since_time[0:4]), int(since_time[5:7]), int(since_time[8:10]), int(since_time[11:13]), int(since_time[14:16]), int(since_time[17:]))

    # compensating with -3600 for off-hour
    # get elapsed time
    time_elapsed_temp1 = int((current_time_dt-since_time_dt).total_seconds())
    tzone = dt.timezone.utc
    current_time_dt, since_time_dt = current_time_dt.replace(tzinfo=tzone), since_time_dt.replace(tzinfo=tzone)
    timedelta = current_time_dt - since_time_dt
    time_elapsed1 = int(timedelta.total_seconds() - 3600)
    time_elapsed1 -= (time_elapsed1 % 60)
    time_elapsed2 = int(timedelta.total_seconds())
    time_elapsed2 -= (time_elapsed2 % 60)

    # get hash
    hash1 = md5(str(time_elapsed1).encode()).hexdigest()
    fullhash1 = md5(hash1.encode()).hexdigest()
    hash2 = md5(str(time_elapsed2).encode()).hexdigest()
    fullhash2 = md5(hash2.encode()).hexdigest()
    print(f"complete hash:        {fullhash1}")

    # get truncated code
    code = ""
    j = 0
    for i in fullhash1:
        if j >= 2:
            break
        if i.isalpha():
            code += i
            j += 1
    j = 0
    for i in reversed(fullhash1):
        if j >= 2:
            break
        if i.isnumeric():
            code += i
            j += 1

    print(f"truncated hash:       {code}")

    print(f"\nIn case of daylight savings:")
    print(f"complete hash:        {fullhash2}")
    code = ""
    j = 0
    for i in fullhash2:
        if j >= 2:
            break
        if i.isalpha():
            code += i
            j += 1
    j = 0
    for i in reversed(fullhash2):
        if j >= 2:
            break
        if i.isnumeric():
            code += i
            j += 1
    print(f"truncated hash:       {code}")
