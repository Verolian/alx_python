for i in range(99):
    print(f"{i} = 0x{hex(i)[2:]}" if i < 16 else f"{i} = 0x{hex(i)[2:].format()}")