# in_int = int(input())

in_int = 5
for i in range(1, in_int + 1):
    out_data_center = str(i)
    out_data_left = ""
    out_data_right = ""
    for j in range(1, i):
        out_data_left = out_data_left + str(j)
        out_data_right = str(j) + out_data_right

    out_data_final = out_data_left + out_data_center + out_data_right
    print(out_data_final)