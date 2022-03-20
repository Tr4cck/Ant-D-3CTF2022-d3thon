import random
import string

def gen_func_name(registered = []):
  name = "".join(random.choices(string.ascii_letters, k = random.randint(15, 18)))
  while True:
    if name not in registered:
      registered.append(name)
      yield name

if __name__ == '__main__':
  for _ in range(100):
    print(next(gen_func_name()))