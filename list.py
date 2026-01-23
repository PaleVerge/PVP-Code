phone=['xiaomi','huawei','oppo','vivo','samsung','apple']
phone.insert(0,"meizu")
delphone=phone.pop()

print(f"恭喜你获得了{phone}手机")
print(f"很遗憾你未获得{delphone}手机")
delphone=phone.pop()

print(f"恭喜你获得了{phone}手机")
print(f"很遗憾你未获得{delphone}手机")
delphone=phone.pop()

print(f"恭喜你获得了{phone}手机")
print(f"很遗憾你未获得{delphone}手机")
delphone=phone.pop()

print(f"恭喜你获得了{phone}手机")
print(f"很遗憾你未获得{delphone}手机")
delphone=phone.pop()

print(f"恭喜你获得了{phone}手机")
print(f"很遗憾你未获得{delphone}手机")

del phone[0-1]
print(phone)