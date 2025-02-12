# Enter your code here. Read input from STDIN. Print output to STDOUT
# in_data = []
# try:
#     in_tmp = input()
#     while in_tmp:
#         in_data.append(in_tmp.split(" "))
#         in_tmp = input()
# except Exception as e:
#     pass

in_data = [[1, 2],[3, 4]]

out_data = []
out_tmp = []
count = 0

for list_ in in_data:
    for i in range(count, len(in_data)):
        count += 1
        if count > len(in_data) - 1:
            break

        for j in list_:
            second_list = in_data[count]
            for number in second_list:
                out_tmp = (int(j), int(number))
                out_data.append(out_tmp)

out_data_str = ""
for elm in out_data:
    out_data_str += str(elm) + " "

out_data = out_data_str.rstrip(" ")

print(out_data)