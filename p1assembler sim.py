mot = {
    "LDA": 1,
    "ADD": 2,
    "SUB": 3,
    "MULT": 4,
    "DIV": 5,
    "READ": 6,
    "OUT": 7,
    "STO": 8,
    "HLT": 9
}

# ================= Generating machine code ==================

def get_tokenized_src_prog(file_path):
    with open(file_path) as src_prog:
        tokenized_prog = [list(map(str.upper, line.split())) for line in src_prog]
    return tokenized_prog

def get_machine_code(tokenized_prog):
    target_mach_code, symb_tab, loc_cntr = [], {}, 1
    for instruc in tokenized_prog:
        machine_code = '0'
        if "DS" in instruc:
            symb_tab[instruc[0]] = loc_cntr
            target_mach_code.append(machine_code)
            loc_cntr += 1
        else:
            mnem = instruc[0]
            var_addr = '000' if mnem == "HLT" else str(symb_tab[instruc[1]]).zfill(3)
            machine_code = str(mot[mnem]) + var_addr
            target_mach_code.append(machine_code)
    return target_mach_code


path = r"D:\Jayesh\Msc CS\Sem 2\Compiler Design and Construction\Prac 1 - Assembly Simulator\sample_assembly_prog.txt"
tokenized_prog = get_tokenized_src_prog(path)
machine_code = get_machine_code(tokenized_prog)
print("\ntokenized instructions:", *tokenized_prog, sep = "\n")
print("\nMachine code: ")
print(*machine_code, sep = "\n")

# Saving machine code to file (might be optional)
with open(r"D:\Jayesh\Msc CS\Sem 2\Compiler Design and Construction\Prac 1 - Assembly Simulator\machine_code.txt", "w") as outfile:
    outfile.write("\n".join(machine_code))


# ============== Executing machine instructions ===============

acc = 0
memory = { i: None for i in range(1000) }
print("\nExecuting statements: ")
for instruc in [code for code in machine_code if code != '0']:
    op_code, addr = int(instruc[0]), int(instruc[1:])
    if op_code == 1:
        acc = memory[addr]
    elif op_code == 2:
        acc += memory[addr]
    elif op_code == 3:
        acc -= memory[addr]
    elif op_code == 4:
        acc *= memory[addr]
    elif op_code == 5:
        acc /= memory[addr]
    elif op_code == 6:
        val = float(input("Enter a value: "))
        memory[addr] = val
    elif op_code == 7:
        print("Output: ", memory[addr])
    elif op_code == 8:
        memory[addr] = acc
    elif op_code == 9:
        print("\nProcess complete")




