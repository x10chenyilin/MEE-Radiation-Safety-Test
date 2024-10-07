from problem import Problem, Problem_list, Part, Type, Count

SINGLE_CHOICE = 40
MULTIPLE_CHOICE = 10
PASS_POINT = 90

if __name__ == '__main__':
    print("============================================")
    print("============欢迎进入辐射安全考核============")
    print("============================================")
    print("")
    print(f"请选择模式（1：顺序做题；2：模拟考试）")
    mode = int(input())

    if mode == 1:
        print(f"请选择题库范围（1：{Part[0]}；2：{Part[1]}；3：全部）")
        part = int(input()) - 1
        print(f"请选择题目类型（1：{Type[0]}；2：{Type[1]}；3：全部）")
        type = int(input()) - 1
        
        print("============================================")
        print("================顺序做题开始================")
        print("============================================")
        print("提示：输入Exit退出做题并保存错题")
        print("提示：输入答案时只输入字母组合")
        print("")

        wrong = []
        total_correct = 0
        total_problem = 0
        total_point = 0
        total_fullpoint = 0
        for problem in Problem_list:
            if (type == 2 or problem.type == type) and (part == 2 or problem.part == part):
                print(f"（{Type[problem.type]}）{problem.id}、{problem.content}")
                input_ = input().upper()
                point = problem.point(input_)
                if input_ == "EXIT":
                    break
                total_problem += 1
                total_point += point
                total_fullpoint += 4 if problem.type == 1 else 2
                if point == 0:
                    wrong.append(problem.id)
                    print(f"错误！正确答案：{problem.get_answer()}")
                elif problem.point(input_) == 1:
                    wrong.append(problem.id)
                    print(f"部分正确！正确答案：{problem.get_answer()}")
                else: 
                    total_correct += 1
                    print("正确！")

        print("============================================")
        print("================顺序做题结束================")
        print("============================================")
        print(f"正确题数：{total_correct}/{total_problem}")
        print(f"得分：{total_point}/{total_fullpoint}")

        print("")

        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        with open(f"错题_{timestamp}.txt", "w") as f:
            for i in wrong:
                f.write(f"{Problem_list[i - 1].id}、{Problem_list[i - 1].content}" + f"\n答案：{Problem_list[i - 1].get_answer()}" + "\n\n")
            
    if mode == 2:
        print("============================================")
        print("================模拟考试开始================")
        print("============================================")
        print("提示：输入Exit退出做题并保存错题")
        print("提示：输入答案时只输入字母组合")
        print(f"提示：共{SINGLE_CHOICE}道单选题，{MULTIPLE_CHOICE}道多选题，总分{PASS_POINT}分以上为合格")
        print("")

        wrong = []
        total_correct = 0
        total_problem = 0
        total_point = 0
        total_fullpoint = 0

        import random
        random_id = random.sample(list(range(0, Count[0])) + list(range(Count[1], Count[2])), SINGLE_CHOICE) + \
                    random.sample(list(range(Count[0], Count[1])) + list(range(Count[2], Count[3])), MULTIPLE_CHOICE)

        for id in random_id:
            problem = Problem_list[id]
            print(f"（{Type[problem.type]}）{total_problem+1}、{problem.content}")
            input_ = input().upper()
            point = problem.point(input_)
            if input_ == "EXIT":
                break
            total_problem += 1
            total_point += point
            total_fullpoint += 4 if problem.type == 1 else 2
            if point == 0:
                wrong.append(problem.id)
                print(f"错误！正确答案：{problem.get_answer()}")
            elif problem.point(input_) == 1:
                wrong.append(problem.id)
                print(f"部分正确！正确答案：{problem.get_answer()}")
            else: 
                total_correct += 1
                print("正确！")
        else:
            print("============================================")
            print("================模拟考试结束================")
            print("============================================")
            print(f"正确题数：{total_correct}/{total_problem}")
            print(f"得分：{total_point}/{total_fullpoint}")
            if total_point >= PASS_POINT:
                print("恭喜你通过了考试！")
            else:
                print("很遗憾，你没有通过考试。")
            exit()
        print("============================================")
        print("================模拟考试中断================")
        print("============================================")
        print(f"正确题数：{total_correct}/{total_problem}")
        print(f"得分：{total_point}/{total_fullpoint}")