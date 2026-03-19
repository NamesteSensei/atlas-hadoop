#!/usr/bin/env python3
import sys

current_company = None
current_total = 0

for line in sys.stdin:
    line = line.strip()

    try:
        _, value = line.split("\t")
        company, salary = value.split(",")

        salary = int(salary)

        if current_company == company:
            current_total += salary
        else:
            if current_company:
                print(f"{current_company}\t{current_total}")

            current_company = company
            current_total = salary

    except:
        continue

# print last company
if current_company:
    print(f"{current_company}\t{current_total}")
