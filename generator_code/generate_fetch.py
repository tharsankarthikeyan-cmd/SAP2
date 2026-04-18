pos_opcode = []
for i in range(0, 256):
    pos_opcode.append(f"{i:02x}")
t_state = []
for j in range(0, 3):
    t_state.append(f"{j:01x}")
flag = []
for k in range(0, 8):
    flag.append(f"{k:01x}")

f = open("rom.txt", "a")
for i in pos_opcode:
    for k in flag:
        for j in t_state:
            f.write(i + j + k + ":" + " ")
            if int(j) == 0:
                f.write("000000009" + "\n")
            elif int(j) == 1:
                f.write("000000d4" + "\n")
            elif int(j) == 2:
                f.write("10000100" + "\n")
