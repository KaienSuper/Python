scoring_ex = {1:2, 2:4, 3:6, 4:8, 5:10, 6:12, 7:14, 8:16, 9:18, 10:20, 11:22,
              12:24, 13:26, 14:28, 15:30, 16:32, 17:34, 18:36, 19:38, 20:40}
scoring_in = {1:3, 2:6, 3:9, 4:12, 5:15, 6:18, 7:21, 8:24, 9:27, 10:30, 11:33, 
              12:36, 13:39, 14:42, 15:45, 16:48, 17:51, 18:54, 19:57, 20:60}
def score(sector, num_sector=None):
    if num_sector == None:
        if sector == "Яблочко":
            return 50
        elif sector == "Зеленое кольцо":
            return 25
    else:
        if sector == "Внешнее кольцо":
            return scoring_ex[num_sector]
        else:
            return scoring_in[num_sector]

print(score("Яблочко"))
print(score("Внешнее кольцо",1))