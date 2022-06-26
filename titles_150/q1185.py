#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author RenMeng
@since 2022/1/3
'''

class Solution:
    def run_nian(self, year):
        if year % 100 == 0:
            year = year // 100
        if year % 4 == 0:
            return True
        return False

    def month_days(self, year, month):
        if month == 2:
            if self.run_nian(year):
                return 29
            else:
                return 28

        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        return 30


    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        now_year = 2022
        now_month = 1
        now_day = 3
        now_week = 1
        flag = True

        if year > now_year:
            now_year, year = year, now_year
            now_month, month = month, now_month
            now_day, day = day,now_day
            flag = False

        total_days = 0
        # 左闭右开
        m = now_month - 1
        while m >= 1:
            total_days += self.month_days(now_year, m)
            m -= 1
        total_days += now_day - 1

        total_days += self.month_days(year, month) - day + 1
        m = month + 1
        while m <= 12:
            total_days += self.month_days(year, m)
            m += 1

        for y in range(year+1, now_year):
            if self.run_nian(y):
                total_days += 366
            else:
                total_days += 365

        if flag:
            now_week += 7 - total_days % 7
        else:
            now_week += total_days % 7
        now_week %= 7
        week_dict = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday"}
        return week_dict[now_week]
