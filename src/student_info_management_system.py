# 学生信息管理系统

# 初始化学生信息字典
students = {}

def add_student():
    """添加学生信息"""
    name = input("请输入学生姓名: ")
    age = input("请输入学生年龄: ")
    grade = input("请输入学生年级: ")
    students[name] = {"年龄": age, "年级": grade}
    print(f"学生 {name} 的信息已添加成功！")

def find_student():
    """查找学生信息"""
    name = input("请输入要查找的学生姓名: ")
    if name in students:
        print(f"学生姓名: {name}")
        print(f"学生年龄: {students[name]['年龄']}")
        print(f"学生年级: {students[name]['年级']}")
    else:
        print(f"找不到学生 {name} 的信息！")

def delete_student():
    """删除学生信息"""
    name = input("请输入要删除的学生姓名: ")
    if name in students:
        del students[name]
        print(f"学生 {name} 的信息已删除成功！")
    else:
        print(f"找不到学生 {name} 的信息！")

def display_students():
    """显示所有学生信息"""
    if not students:
        print("暂无学生信息！")
    else:
        print("学生信息列表:")
        for name, info in students.items():
            print(f"学生姓名: {name}")
            print(f"学生年龄: {info['年龄']}")
            print(f"学生年级: {info['年级']}")
            print()

def main():
    while True:
        print("\n欢迎使用学生信息管理系统")
        print("1. 添加学生信息")
        print("2. 查找学生信息")
        print("3. 删除学生信息")
        print("4. 显示所有学生信息")
        print("5. 退出系统")

        choice = input("请输入选项(1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            find_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("感谢使用学生信息管理系统，再见！")
            break
        else:
            print("无效选项，请重新输入！")

if __name__ == "__main__":
    main()
