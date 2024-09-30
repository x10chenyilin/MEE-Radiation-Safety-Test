Count = [214, 290, 358, 412]
Part = ["电离辐射安全与防护基础", "核技术利用辐射安全法律法规"]
Type = ["单选题", "多选题"]
Point = [2, 4, 1] 

class Problem:
    def __init__(self, part, type, id, content, answer):
        self.part = part
        self.type = type
        self.id = id
        self.content = content
        self.answer = answer

    def point(self, input):
        if self.type == 0:
            return Point[0] if input == self.answer[0] else 0
        else:
            input = re.findall(r"[A-E]", input)
            set_input = set(input)
            set_answer = set(self.answer)
            if not set_input:
                return 0
            elif set_input == set_answer:
                return Point[1]
            elif set_input.issubset(set_answer):
                return Point[2]
            else:
                return 0
            
    def get_answer(self):
        ans = ""
        for i in self.answer:
            ans += i
        return ans


problems, answers = "", ""
with open("problems.txt", 'r') as problem:
    for line in problem:
        problems += line
with open("answers.txt", 'r', encoding='utf-8') as answer:
    for line in answer:
        answers += line

import re
problems = problems.split("\n\n")
answers = re.findall(r"\d+.[A-E,]+", answers)
for i in range(len(answers)):
    answers[i] = answers[i].split(".")[1]
    answers[i] = re.findall(r"[A-E]", answers[i])

Problem_list = [Problem(int(i >= Count[1]),
                        int(Count[0] <= i < Count[1] or Count[2] <= i < Count[3]),
                        i + 1,
                        problems[i].split("、", 1)[1],
                        answers[i]) for i in range(len(problems))]