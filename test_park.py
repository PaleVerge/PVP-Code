import random
from datetime import datetime, timedelta


def generate_test_data(filename="test_input.txt"):
    with open(filename, "w") as f:
        # 1. 模拟存入 50 辆车
        for i in range(50):
            car_type = random.randint(1, 3)  # 1:大, 2:中, 3:小
            car_id = f"粤B{10000 + i}"
            # 随机入场时间 (2026年1月1日)
            hour = random.randint(0, 12)
            minute = random.randint(0, 59)

            f.write(f"1\n{car_type}\n2026.1.1 {hour}:{minute}\n{car_id}\n")

        # 2. 模拟 30 辆车陆续离开
        for i in range(30):
            car_type = random.randint(1, 3)
            car_id = f"粤B{10000 + i}"
            # 随机离场时间 (入场时间后 1-10 小时)
            leave_hour = random.randint(13, 23)
            leave_min = random.randint(0, 59)

            f.write(f"2\n{car_type}\n{car_id}\n2026.1.1 {leave_hour}:{leave_min}\n")

        # 3. 统计操作
        f.write("4\n1\n")  # 统计停车数量
        f.write("4\n3\n2026.1\n")  # 统计月收入

        # 4. 退出程序
        f.write("q\n")


generate_test_data()
print("测试数据 'test_input.txt' 已生成！")