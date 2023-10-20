rec_count = int(input("Count of recommendations: "))
recs = []
for _ in range(rec_count):
    rec = input("Recommendation: ")
    if rec[:2] == "не" or rec[:2] == "Не":
        recs.append(rec[3:])
    else:
        recs.append(rec)

for elem in recs:
    print(elem)