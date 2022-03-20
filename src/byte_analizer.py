import re

Variables = {}
Functions = {}

def analize(string):
  string_cmd = string.split(":", maxsplit = 1)[0]
  if string_cmd == "kZslMZYnvPBwgdCz":
    splitted = string.split(":", maxsplit = 1)
    print(splitted[1].replace("%n", "\n"))

  elif string_cmd == "xddBNpXeLBGnpQgYDy": # exit
    exec('exit(0)')

  elif string_cmd == "oGwDokoxZgoeViFcAF": # var
    splitted = string.split(":")
    splitted_tst = splitted[1].split("=")
    if splitted_tst[1] == "KezJKhCxGRZnfLCGT": # input
      Variables[splitted_tst[0]] = input(f'[{splitted_tst[0]}] >> ').replace("%n", "\n")
    else:
      Variables[splitted_tst[0]] = splitted_tst[1].replace("%n", "\n")

  elif string_cmd == "OuGFUKNGxNLeHOudCK": # if
    if_args = string.split(":", maxsplit = 4)
    opcode = if_args[3]
    if opcode == '0':
      if int(Variables[if_args[1]], 10) < int(if_args[2], 10):
        analize(if_args[4])
    elif opcode == '1':
      if int(Variables[if_args[1]], 10) > int(if_args[2], 10):
        analize(if_args[4])
    elif opcode == '2':
      if int(Variables[if_args[1]], 10) == int(if_args[2], 10):
        analize(if_args[4])
    elif opcode == '3':
      if int(Variables[if_args[1]], 10) != int(if_args[2], 10):
        analize(if_args[4])
    elif opcode == '4':
      if int(Variables[if_args[1]], 10) <= int(if_args[2], 10):
        analize(if_args[4])
    elif opcode == '5':
      if int(Variables[if_args[1]], 10) >= int(if_args[2], 10):
        analize(if_args[4])
      else:
        print("[!] Invalid if condition")

  elif string_cmd == "ZOAmcoLkGlAXXqf": # func
    splitted = string.split(":", maxsplit = 2)
    list_cmds = splitted[2]
    name_function = splitted[1]
    Functions[name_function] = list_cmds

  elif string_cmd == "RDDDZUiIKbxCubJEN": # call
    splitted = string.split(":")
    func_devs = Functions[splitted[1]]
    cmd_list = re.sub(r'[\'\[\]]', '', func_devs).split(',')
    for i in cmd_list:
      analize(i)
    
  elif string_cmd == 'todeVDuRkYSIITaT': # ascii to bin
    bin_args = string.split(":", maxsplit = 2)
    chara = chr(int(bin_args[1]))
    try:
      pos = Variables[bin_args[2]].index(chara)
      Variables[bin_args[2]] = Variables[bin_args[2]][:pos] + bin(ord(Variables[bin_args[2]][pos]))[2:].zfill(8) + Variables[bin_args[2]][pos + 1:]
    except ValueError:
      pass

  elif string_cmd == 'uPapnsSbmeJLjin': # bin to decimal
    btd_args = string.split(":")
    try:
      Variables[btd_args[1]] = str(int(Variables[btd_args[1]], 2))
    except ValueError:
      pass

  elif string_cmd == 'IEKMEDdrPpzpdKy':
    add_args = string.split(":", maxsplit = 2)
    Variables[add_args[1]] = str(int(Variables[add_args[1]], 10) + int(add_args[2], 10))

  elif string_cmd == 'FLNPsiCIvICFtzpUAR':
    sub_args = string.split(":", maxsplit = 2)
    Variables[sub_args[1]] = str(int(Variables[sub_args[1]], 10) - int(sub_args[2], 10))

  elif string_cmd == 'kuhisCvwaXWfqCs':
    not_args = string.split(":", maxsplit = 2)
    Variables[not_args[1]] = str(~int(Variables[not_args[1]], 10))

  elif string_cmd == 'OcKUQCYqhwHXfAgGZH':
    xor_args = string.split(":", maxsplit = 2)
    Variables[xor_args[1]] = str(int(Variables[xor_args[1]], 10) ^ int(xor_args[2], 10))