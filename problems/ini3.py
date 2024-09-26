def string_slice(s, a, b, c, d):
  return s[a:b+1], s[c:d+1]

if __name__ == "__main__":
  with open("../inputs/rosalind_ini3_4_dataset.txt", "r") as f:
    s = f.readline().strip()
    a, b, c, d = map(int, f.readline().strip().split())
  s1, s2 = string_slice(s, a, b, c, d)
  print("Rosalind Strings and Lists (INI3): ", s1, s2)