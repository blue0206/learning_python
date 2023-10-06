names = ['Rudeus', 'Sylphiette', 'Subaru', 'Emily']
count = 0
while(count < 4):
    print(f"\nDear {names[count]}," + "\nI'll be turning 25 years old coming " + 
          "Thursday and I would be really happy to be" + 
          "\nable to celebrate it with you! I'll be waiting." +
          "\nYour best friend and teammate,\nBLUE")
    count = count + 1
print("\n\n")
print(f"Unfortunately, {names[1]} can't make it.")

del names[1]
names.insert(1, 'Arianna')

print("\n\n")
print("I've found a bigger dinner table! I'll invite more of my cherished " + 
      "friends now!")
names.insert(0, 'Kazuma')
names.insert(3, 'Naofumi')
names.append('Megumin')
count = 0
while(count < 7):
    print(f"\nDear {names[count]}," + "\nI'll be turning 25 years old coming " + 
          "Thursday and I would be really happy to be" + 
          "\nable to celebrate it with you! I'll be waiting." +
          "\nYour best friend and teammate,\nBLUE")
    count = count + 1

print("\n\n")
print("It looks like my new dinner table won't arrive in time. " + 
      "I'll have to shrink my guest list now.")

count = 0
while(count < 5):
    cancel_invite = names.pop()
    print(f"\n\nDear {cancel_invite}," + 
          "\nIt is my deep regret to let you know that the invitation I sent" + 
          "\nyou for my birthday part now stands cancelled." + 
          "\nThere's not much space and the new dinner table won't make it " + 
          "in time.\nI hope you'll forgive me for this." + 
          "\n\nYour best friend and teammate," + 
          "\nBLUE")
    count = count + 1

print("\n\n")
count = 0
while(count < 2):
    print(f"\nDear {names[count]}," + 
          "\nI'd like you to know that you're still invited!" + 
          "\n\nBLUE")
    count = count + 1

count = 0
while(count < 2):
    del names[0]
    count = count + 1

print("\n\n")
print(names)