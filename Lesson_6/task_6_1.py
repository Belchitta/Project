with open("nginx_logs.txt", 'r', encoding='utf-8') as file_x:
    line = file_x.readline()
    a = []
    for line in file_x:
        line_part_0 = line.split()
        final_line = [tuple([line_part_0[0]] + [line_part_0[5].strip('"')] + [line_part_0[6]])]
        a.append(final_line)
    s = list(zip(*a))
    print(s)



