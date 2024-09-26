def calc_hypotenuse(a, b):
  return a**2 + b**2

if __name__ == "__main__":
  with open("../inputs/rosalind_ini2_2_dataset.txt", "r") as f:
    ins = f.readline().strip().split()
    a, b = int(ins[0]), int(ins[1])
  print("Rosalind: Variables and Some Arithmatic (INI2):  ", calc_hypotenuse(a, b))