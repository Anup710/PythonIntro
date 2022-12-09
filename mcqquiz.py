class Question:
    def __init__(self, prompt, answer_key):
        self.prompt = prompt
        self.answer_key = answer_key


question_statements = [
    "What is the Anup was born?\n(a)Saturday (b)Monday (c) Thursday\n",
    "What is the name of the rogue brasilian president candidate?\n(a) Seth Rogan (b) José Bolsanaro (c) Joe Biden\n",
    "Why is eDc such a failure: \n(a) Poor leadership (b) nepotism (c) high funding\n",
]

questions = [
    Question(question_statements[0], "a"),
    Question(question_statements[1], "b"),
    Question(question_statements[2], "a"),
]


def run_test(questions):
    score = 0
    for q in questions:
        response = input(q.prompt + "\nYour answer: ")
        if response == q.answer_key:
            score += 1
    print("Your final score is", score, "/", len(questions))


run_test(questions)
