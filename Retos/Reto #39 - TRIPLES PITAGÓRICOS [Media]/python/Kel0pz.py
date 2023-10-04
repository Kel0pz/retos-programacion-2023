print("Programa que obtiene las diferentes Ternas Pitagóricas de cualquier número")
while True:
    num=int(input("Ingresa valor: "))
    print("(Cateto#1 , Cateto#2 , Hipotenusa)")
    col=0
    fil=0
    hip=float()
    while col < num:
        col+=1
        while fil < num:
            fil+=1
            hip=((col**2)+(fil**2))**0.5
            hip_2=hip//1
            if ((hip%hip_2)== 0)and(hip < num):
                print("(",col,",",fil,",",int(hip),")")
            else:
                continue
        fil=col #Comentario_1
    print("")

"""Comentario_1:
    Se reasigna el valor de la variable "fil", porque el segundo bucle while no podria continuar
    y al igularlo con la variable "col" no se duplican los resultados, ya que es una matriz simetrica de (num x num)
    ejemplo: (6,8,10) son simetricos a (8,6,10)"""
