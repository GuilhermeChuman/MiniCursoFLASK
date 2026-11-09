import pandas as pd

df = pd.read_csv("alunos_100.csv")

def loadData():
    global df 
    df = pd.read_csv("alunos_100.csv")

def loadAlunos():
    loadData()
    return df["nome"].to_dict()

def addAluno(data):
    loadData()
    novo_aluno = pd.DataFrame([data])
    dfNovo = pd.concat([df, novo_aluno], ignore_index=True)
    dfNovo.to_csv("alunos_100.csv", index=False)
    return True

def deleteAluno(idAluno):
    loadData()
    global df
    df = df.drop(df[df['id'] == idAluno].index)
    df.to_csv("alunos_100.csv", index=False)
    return True

def updateAluno(idAluno, data):
    loadData()
    global df
    df = df.drop(df[df['id'] == idAluno].index)
    novo_aluno = pd.DataFrame([data])
    dfNovo = pd.concat([df, novo_aluno], ignore_index=True)
    dfNovo.to_csv("alunos_100.csv", index=False)
    return True

def searchAlunoByName(term):
    loadData()
    search = df[df["nome"].str.contains(term, case=False)]
    return search.to_dict()
