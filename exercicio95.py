curso01 = int(input("Digite quantas avaliações o curso01 teve:"))
curso02 = int(input("Digite quantas avaliações o curso02 teve:"))

if curso01 == curso02:
    print("Empate")
elif curso01 > curso02:
    print("Curso01 é maior")
else:
    print("Curso02 é maior")
