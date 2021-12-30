import re
import pandas
import os
from functions import exportQuestions
from functions import folders

def start_regx():
    for folder in folders:
        fs = os.listdir(path = "texts/"+folder+"/")
        fs.remove('qa')
        for txtfile in fs:
            with open("texts/"+folder+"/"+txtfile, "r") as file:
                content_list = file.read().split()
                qs, ans = exportQuestions(content_list)
                ansx = ' '.join(ans)

                for i in range(len(qs)):
                    qs[i].append("(("+ans[i]+"))")

                qsS = []
                for question in qs:
                    qsS.append([' '.join(question)])

                qsdf = pandas.DataFrame(qsS, columns = ['QA'])
                qsdf.to_csv("texts/"+folder+"/qa/"+txtfile+".csv", index=False)
