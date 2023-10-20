heading_len = int(input("Enter a len of heading: "))
heading_count = int(input("Enter a count of heading: "))
headings = []
for _ in range(heading_count):
    heading = input("Heading: ")
    if len(heading) > heading_len:
        heading = heading[:25] + "..."
        headings.append(heading)
    else:
        headings.append(heading)
for i in headings:
    print(i)