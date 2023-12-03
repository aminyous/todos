import json

with open("file/questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

answers = []
score = 0

for item in data:
    alternatives = [f"{i + 1} - {el}" for i, el in enumerate(item["Alternatives"])]
    alternatives = ", ".join(alternatives)

    user_answer = int(input(f"{item['Question_text']} : {alternatives} :"))

    item["user answer"] = user_answer


for index, item in enumerate(data):
    if item["Answer"] == item["user answer"]:
        score = score + 1
        print(f"{index + 1} - Correct answer :) User answer: {item['user answer']}, Correct Answer : {item['Answer']}")
    else:
        print(f"{index + 1} - Incorrect answer :( User answer: {item['user answer']}, Correct Answer : {item['Answer']}")

print(f"Score = {score} / {len(data)}")


