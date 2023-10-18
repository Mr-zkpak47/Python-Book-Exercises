from ast import Num


guestList: list[str] = ["harry", "hamad", "moiz"]
print(f"Hello,{guestList[0]}.You are invited to dinner.")
print(f"Hello,{guestList[1]}.You are invited to dinner.")
print(f"Hello,{guestList[2]}.You are invited to dinner.\n")

print(f"Sorry,{guestList[1]}.You can't make it to the dinner.\n")

del guestList[1]
guestList.insert(1, "sulman")

print("Second set of invitations:\n")

print(f"Hello,{guestList[0]}.You are still invited to dinner.")
print(f"Hello,{guestList[1]}.You are still invited to dinner.")
print(f"Hello,{guestList[2]}.You are still invited to dinner.")

print("\nHurrah!We just found a bigger dinner table.\n")

guestList.insert(0, "ammad")
guestList.insert(1, "ayaan")
guestList.append("bilal")

print(f"Hello,{guestList[0]}.You are still also invited to dinner.")
print(f"Hello,{guestList[1]}.You are still also invited to dinner.")
print(f"Hello,{guestList[2]}.You are still also invited to dinner.")
print(f"Hello,{guestList[3]}.You are still also invited to dinner.")
print(f"Hello,{guestList[4]}.You are still also invited to dinner.")
print(f"Hello,{guestList[5]}.You are still also invited to dinner.")