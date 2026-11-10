"""
RECORD CHECK  -  my version
===========================

Name  : Divy Patel
Lane  : IT
Date  :30-09-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
over_limit_count = 0   
while True:
    label = input("hostname, gb used, gb total ")
    if label == "quit":
        print(" quite successfully")
        break
    value = float(input("65 "))
    limit = float(input("100"))

    while limit == 0:
        print("Limit cannot be zero. Please enter a valid limit.")
        limit = float(input("Enter a limit "))

    difference = limit - value
    percent = (value / limit) * 100

    status = ""
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    if status == "OVER LIMIT":
     over_limit_count += 1

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f"Value: {value:>10.2f}")
    print(f"Limit: {limit:>10.2f}")
    print(f"Difference: {difference:>10.2f}")
    print(f"Percent: {percent:>10.2f}%")
    print(f"Status: {status:>10}")
    print("=" * 34)