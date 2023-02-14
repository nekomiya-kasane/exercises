days_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days_offset_leap = [sum(days_leap[0:i]) for i in range(len(days_leap))]
days_offset = [sum(days[0:i]) for i in range(len(days))]

def is_leap_year(year):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return True
    return False

def normalize(year, month, week, day):
    start = 6 # 2000年第1天周6，需要算的是后面给定日期和这一天的差，加上6模7即可
    cnt_leap = int((year - 2001) / 4) - int((year - 2001) / 100) + int((year - 2001) / 400) \
        + (1 if year != 2000 else 0) 
        # 容斥原理，给定年份之前（不含），2001年后 能除尽4的 - 能除尽100的 + 能除尽400的 即 不含2000的所有闰年 的总数
        # 2000 起始，从2001开始算，所以给定年份大于2000时要把2000这1个加回来
        # 得到2000（含）~给定年份（不含） 的所有闰年 的总数
    incre_1 = (((year - 2000) - cnt_leap) * (365 % 7)) % 7
    # 给定年份之前（不含）非闰年总天数， %7得到贡献的星期的offset
    incre_2 = (cnt_leap * (366 % 7)) % 7
    # 给定年份之前（不含）闰年总天数， %7得到贡献的星期的offset
    start = ((incre_1 + incre_2) % 7 + start) % 7
    # 合计，得到给定年份之前（不含）所有年份贡献的星期的offset，如此可知给定年份1月1日的星期
    if not start:
        start = 7
    # 星期零重置为星期日

    is_leap = is_leap_year(year)
    month_start = (start + (days_offset_leap if is_leap else days_offset)[month - 1] % 7) % 7 
    # 同样地，计算给定年份内给定月份（不含）之前所有月份的天数，%7得到这前几月贡献的星期的offset，如此可知给定年份给定月份的1日的星期
    if not month_start:
        month_start = 7
    # 星期零重置为星期日
    if (week == 1) and (day < month_start): # 给定周目为第1周，但给定星期小于该月1日星期，判定非法
        return 0
    if (month_start == 1) and (not is_leap) and (month == 2) and (week > 4): # 给定2月>4周，但该非闰年2月起始周有周一，因此只能有4周，判定非法
        return 0
    
    day_num = (week - 1) * 7 + (day - month_start) + 1 # 计算给定周和星期对应的日数
    if day_num > (days_leap if is_leap else days)[month - 1]: # 若上面求的日数大于该月总天数，判定非法
        return 0

    return "{:0>4d}-{:0>2d}-{:0>2d}".format(year, month, day_num) # 合法的话上面的日数即为所求


if __name__ == "__main__":
    #while True:
        #year, month, week, day = list(map(int, input().strip().split()))
        #if not year:
            #break
        year, month, week, day = 9500, 12, 1, 7
        if (year < 200) or (month < 1) or (month > 12) or (day < 1) or (day > 7) or (week > 5) or (week < 1):
            # 此处有笔误，year < 2000，一个月最多6周，所以改为week > 6
            print(0)
        else:
            print(normalize(year, month, week, day))
        