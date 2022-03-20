import random, string

def gen_func_name(registered = []):
  name = "".join(random.choices(string.ascii_letters, k = random.randint(5, 10)))
  while True:
    if name not in registered:
      registered.append(name)
      yield name

def write_func(path, code):
  with open(path, 'wb') as fo:
    fo.write(code.encode())

def gen_calc(operatord : dict):
  code = ""
  for _ in range(0xffff):
    c = random.choice(list(operatord.keys()))
    match c:
      case 0:
        code += f"'IEKMEDdrPpzpdKy:flag:{random.randint(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff, 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)}',"
      case 1:
        code += f"'FLNPsiCIvICFtzpUAR:flag:{random.randint(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff, 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)}',"
      case 4:
        code += f"'OcKUQCYqhwHXfAgGZH:flag:{random.randint(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff, 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff)}',"
      case 5:
        code += f"'kuhisCvwaXWfqCs:flag',"

  return code

def TEA():
  pass

if __name__ == '__main__':
  code = ""
  operatord = {
    0 : 'IEKMEDdrPpzpdKy', # add
    1 : 'FLNPsiCIvICFtzpUAR', # sub
    4 : 'OcKUQCYqhwHXfAgGZH', # xor
    5 : 'kuhisCvwaXWfqCs' # not
  }
  # start
  pre = next(gen_func_name())
  code += "ZOAmcoLkGlAXXqf:start:['kZslMZYnvPBwgdCz:<<- Welcome to 2022 AntCTF & D^3CTF! ->>%nHave fun with L-VM XD','oGwDokoxZgoeViFcAF:flag=KezJKhCxGRZnfLCGT','oGwDokoxZgoeViFcAF:cnt1=16','oGwDokoxZgoeViFcAF:cnt2=0','RDDDZUiIKbxCubJEN:']\n"
  code += f"ZOAmcoLkGlAXXqf:{pre}:['todeVDuRkYSIITaT:50:flag','FLNPsiCIvICFtzpUAR:cnt1:1','OuGFUKNGxNLeHOudCK:cnt1:0:1:RDDDZUiIKbxCubJEN:']\n"

  for i in range(51, 58):
    nxt = next(gen_func_name())
    code += f"ZOAmcoLkGlAXXqf:{nxt}:['todeVDuRkYSIITaT:{i}:flag','RDDDZUiIKbxCubJEN:{pre}']\n"
    pre = nxt

  for i in range(97, 123):
    nxt = next(gen_func_name())
    code += f"ZOAmcoLkGlAXXqf:{nxt}:['todeVDuRkYSIITaT:{i}:flag','RDDDZUiIKbxCubJEN:{pre}']\n"
    pre = nxt

  code += f"ZOAmcoLkGlAXXqf:okokok:['uPapnsSbmeJLjin:flag']\n"
  code += f"ZOAmcoLkGlAXXqf:okokokok:[{gen_calc(operatord)}]\n"

  # TODO: Tiny Encryption Algorithm
  code += f""

  # check
  code += "ZOAmcoLkGlAXXqf:check:['OuGFUKNGxNLeHOudCK:flag:1968605792116184018690864657909874691979680322976147490926185964162434022663332096:2:RDDDZUiIKbxCubJEN:correct','OuGFUKNGxNLeHOudCK:flag:1968605792116184018690864657909874691979680322976147490926185964162434022663332096:3:RDDDZUiIKbxCubJEN:wrong']\n"

  # info
  code += "ZOAmcoLkGlAXXqf:correct:['kZslMZYnvPBwgdCz:<<- Congratulations! ->>%n','xddBNpXeLBGnpQgYDy']\n"
  code += "ZOAmcoLkGlAXXqf:wrong:['kZslMZYnvPBwgdCz:<<- Wrong! ->>%n','xddBNpXeLBGnpQgYDy']\n"

  # run
  code += "RDDDZUiIKbxCubJEN:start\nRDDDZUiIKbxCubJEN:okokok\nRDDDZUiIKbxCubJEN:okokokok\nRDDDZUiIKbxCubJEN:check\n"
  write_func('release/bcode.lbc', code)