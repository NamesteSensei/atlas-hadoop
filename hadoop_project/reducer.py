#!/usr/bin/env python3
import sys

top = []

for line in sys.stdin:
    line = line.strip()

    try:
        id, value = line.split("\t")
        company, salary = value.split(",")
        salary = float(salary)

        top.append((salary, id, company))

        # keep only top 10
        top = sorted(top, reverse=True)[:10]

    except:
        continue

# final output
print("id\tSalary\tcompany")
for salary, id, company in top:
    print(f"{id}\t{salary}\t{company}")
