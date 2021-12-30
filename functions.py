from os import listdir, mkdir

folders = ['kkp']

def saveText(filename, text, folder):
    if folder not in listdir(path = "texts/"):
        mkdir("texts/"+folder)
        mkdir("texts/"+folder+"/qa")

    with open("texts/"+folder+"/"+filename+".txt", "w") as tfile:
        tfile.write(text)

def exportQuestions(content):
    question, questions = [], []
    flag = False
    flag2 = False

    for piece in content: # FILTERING
        if flag == False:
            if piece in [str(i) for i in range(1, 11)]:
                flag = True
                continue
        else:
            if flag2 == False:
                if piece == ')':
                    flag2 = True
                    question.append(piece)
                    continue
            else:
                if piece != "şıkkıdır.":
                    question.append(piece)
                else:
                    # "şıkkıdır." kelimesi alınmaz
                    flag = False
                    question.remove(')')
                    question.insert(0, '*')
                    questions.append(question)
                    question = []
    # FILTERING END

    ans = []
    for question in questions:
        ans.append(question[len(question)-1])
        while question.pop() != "Çözüm":
            pass
    # TAKING ANSWER
    return (questions, ans)
