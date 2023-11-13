coord_dict = {}
count = 0
count_coord_dict = {"1":0,"2":0,"3":0,"4":0,'5':0,"6":0,"7":0,'8':0,'9':0}
for _ in range(int(input("Count coord: "))):
    coord_x = input("X: ")
    coord_y = input("Y: ")
    coord_dict[coord_x] = coord_y
new_coord_dict = {}
for i in coord_dict:
    if i[0] == coord_dict[i][0]:
        new_coord_dict[i] = coord_dict[i]

for i in new_coord_dict:
    for j in new_coord_dict:
        if i[0] == j[0]:
            if new_coord_dict[i][0] == new_coord_dict[j][0]:
                point = True
            else:
                point = False
    if point == True:
        count += 1
        count_coord_dict[i[0]] += 1

max_count_cord_list = [count_coord_dict[i]for i in count_coord_dict]
print(max(max_count_cord_list))