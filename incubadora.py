import pandas as pd

nome_aluno = input("Qual o seu nome?");
email_aluno = input("Digite seu email:");
horario_incubadora = input("Qual horário deseja usar?");
autorizacao = input("Pode sair sozinho? (S/N)").lower();

while autorizacao not in ['s', 'n']:
    print('Por favor responda com "S" ou "N".');
    autorizacao = input("Pode sair sozinho? (S/N)").lower();

data = {'Nome': [nome_aluno], 'Email': [email_aluno], 'Horario Incubadora': [horario_incubadora], 'Autorização': [autorizacao]}
df = pd.DataFrame(data)

excel_file = 'incubadora.xlsx'
df.to_excel(excel_file, index=False)

print("Seu horário foi marcaso com sucesso", excel_file)
    