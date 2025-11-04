import math
Graus = float(input('Digite o ângulo agudo: '))
Radianos = math.radians(Graus)
sen = math.sin(Radianos)
cos = math.cos(Radianos)
tan = math.tan(Radianos)
print('Seno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}'.format(sen, cos, tan))