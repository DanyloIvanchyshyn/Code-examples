import urllib.request
urllib.request.urlretrieve("https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt", "D:\elements1_20.txt")

def get_names():
  ls = []
  i = 0
  while i < 5:
    flag = 0
    tmp = input("Enter the name of an element: ")
    if ls:
          for p in ls:
            if p.lower() == tmp.lower():
              print("{} was already entered <-- no duplicates allowed".format(tmp))
              flag = 1
              break
    if len(tmp.strip()) == 0:
      flag = 1
    if flag == 0:
      ls.append(tmp)
      i += 1
  return ls

f = open("D:\elements1_20.txt","r")
lst = []
corr = []
incorr = []
for x in f:
  lst.append(x.rstrip())
f.close()
for k in get_names():
  flg = 0
  for m in lst:
    if k.lower() == m.lower():
      corr.append(k)
      flg = 1
      break
  if flg == 0:
    incorr.append(k)

print("\n", 20*len(corr), "% score\n")
print("Found: ", corr)
print("\nNot found: ", incorr)

