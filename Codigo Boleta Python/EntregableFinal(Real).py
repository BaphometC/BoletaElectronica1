import os
'''
Login
-----------------------
¿Estas Registrado 1 = SI / 2 = NO?
Si elegiste NO
    Registro
    -----------------
    Ingresa tu nombre completo: xxx
    Ingresa tu nombre de usuario: xxx
    Ingresa tu contraseña: xxx
si elegiste SI
Ingresar Usuario: xxxx
Ingresar Contraseña: xxxxx
Bienvenido: Juan Perez Castro
Ingresar producto a comprar: 1
Elegiste el producto: Pintura tecno azul
Ingresa cantidada a comprar: 20
¿Desea Continuar si/no? si
Ingresar producto a comprar: 1
Elegiste el producto: Pintura tecno azul
Ingresa cantidada a comprar: 20
¿Desea Continuar si/no? no
**
Comprobante de pago QService v1.1
**
Nombre del Cliente: Juan Perez
Producto   Precio     Cantidad   Importe
xx1        10         20         200
-------------------------------------------------------
SubTotal       :169.49
IGV            :30.50
Total a Pagar  :200.00
'''

Id = ['PRO-01', 'PRO-02', 'PRO-03', 'PRO-04', 'PRO-05', 'PRO-06', 'PRO-07', 'PRO-08', 'PRO-09', 'PRO-10']
NamesPro = ['Xiaomi Redmi 9', 'Amazon Echo Dot with Alexa', 'Xiaomi Mi Range extender pro R03', 'TV Xiaomi Mi Box S 4K', 'True Wireless JBL Tune 115', 'Micro Premium Maono AU-902 Usb', 'Samsung Galaxy A22 64GB', 'Hyperx Quad Cast Standalone Usb', 'Mouse Inalámbrico Vertical Logitech MX', 'Monitor Curvo Gamer 23.6" MSI OptixG24C FHD 1ms 144 Hz']
Prices = [1230.2, 650, 560, 210.4, 360.9, 400.9, 1250.9, 380.9, 120.9, 1200.9]
users = ['admin','jperez','mscott','dschrute','rswanson','lknope','aludgate','tbarnes','bperry','aedison']
pwds = ['root','jperez123','mscott456','dschrute789','rswanson123','lknope456','aludgate789','tbarnes123','bperry456','aedison789']
namesUsers = ['Administrador','Julio Perez','Michael Scott','Dwight Schrute','Ron Swanson','Leslie Knope','April Ludgate','Troy Barnes','Britta Perry','Annie Edison']



def Delivery():
    PRObuy = []
    PREbuy = []
    CANTbuy = []
    IMPORTbuy = []

    ST = 0   
    IGV = 0         
    TOTAL = 0

    os.system('cls')
    print('+++++++++++++ ҎeruḎelivery© +++++++++++++')
    print('*****************************************')
    print('++++++ Bienvenido(a)  '+ namesUsers[usu] + ' ++++++')
    print('*****************************************')
    resp = input('Desea realizar alguna compra? Escriba si/no: ')
    if resp == 'si':

        limite = 0
        while resp == 'si' and limite < 10:
            cod = input('Codigo del Producto: ')
            for item in Id:
                if cod == item:
                    i = Id.index(cod)
                    print('Producto: ' + NamesPro[i])
                    CANT = int(input('Cantidad: '))
                    limite +=1
                    IMP = float(CANT) * Prices[i]
                    PRObuy.append(NamesPro[i])
                    PREbuy.append(Prices[i])
                    CANTbuy.append(CANT)
                    IMPORTbuy.append(IMP) 
                    TOTAL = TOTAL + IMP
                    ST = TOTAL / 1.18
                    IGV = TOTAL - ST
                    resp = input('¿Desea agregar otro Producto? si/no: ')
                    break
            else:
                print('CODIGO DE PRODUCTO INEXISTENTE')                
        else:
            if  limite == 10:
                os.system('cls')
                print('++ LLEGASTE AL LIMITE DISPONIBLE DE COMPRA ++')
                print('++++ Comprobante:')
                print('++++++++++++++++++++++++++++++++++++++++ BOLETA ELECTRONICA ++++++++++++++++++++++++++++++++++++++')
                print('**************************************************************************************************')
                print('     Cliente:       ' + namesUsers[usu])
                print('')
                print('{:<60} {:<12} {:<15} {:<15}'.format('     Producto:', '     Precio:', '     Cantidad:', '     Importe:'))

                for item in PRObuy:
                    i = PRObuy.index(item)
                    print('     {:<60} {:<12} {:<15} {:<15}'.format(item, PREbuy[i], CANTbuy[i], IMPORTbuy[i]))

                print('\n')
                
                print('                                                                               Subtotal:      ' + str(round(ST,2)))
                print('                                                                               IGV:           ' + str(round(IGV,2)))
                print('                                                                               Total a pagar: ' + str(TOTAL))
                print('\n')
                print('         ++++++++++++++ GRACIAS POR SU ELECCION ' + namesUsers[usu] + ' ESPERAMOS VOLVER A VERTE PRONTO ++++++++++++++')
                print('    +++++++++++++++++++++++++++++++++++++++++++++ ҎeruḎelivery© +++++++++++++++++++++++++++++++++++++++++')
                print('                                  PERUDELIVERY © 2021 Todos Los derechos Reservados                           ')

            else:
                os.system('cls')
                print('\n++++ Comprobante:')
                print('\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                print('++++++++++++++++++++++++++++++++++++++++ BOLETA ELECTRONICA ++++++++++++++++++++++++++++++++++++++')
                print('**************************************************************************************************')
                print('     Cliente:       ' + namesUsers[usu])
                print('')
                print('{:<60} {:<12} {:<15} {:<15}'.format('     Producto:', '     Precio:', '     Cantidad:', '     Importe:'))

                for item in PRObuy:
                    i = PRObuy.index(item)
                    print('     {:<60} {:<12} {:<15} {:<15}'.format(item, PREbuy[i], CANTbuy[i], IMPORTbuy[i]))

                print('\n')
                
                print('                                                                               Subtotal:      ' + str(round(ST,2)))
                print('                                                                               IGV:           ' + str(round(IGV,2)))
                print('                                                                               Total a pagar: ' + str(TOTAL))
                print('\n')
                print('++++++++++++++ GRACIAS POR SU ELECCION ' + namesUsers[usu] + ' ESPERAMOS VOLVER A VERTE PRONTO ++++++++++++++')
                print('+++++++++++++++++++++++++++++++++++++++++++++++++ ҎeruḎelivery© +++++++++++++++++++++++++++++++++++++++++++++')
                print('**************************************************************************************************************')
                print('                                  PERUDELIVERY © 2021 Todos Los derechos Reservados                           ')
    else:
        os.system('cls')
        print('****************************************************')
        print('** Gracias por su preferencia, tenga un Buen dia **')
        print('+++++++++++++++++++ ҎeruḎelivery© ++++++++++++++++++')
        print('...................................................')
        print(' PERUDELIVERY © 2021 Todos Los derechos Reservados ')
'''
def SignUp():
    newname = input('Nombre Completo: ')
    namesUsers.insert(10,newname)
    newuser = input('Nuevo Usuario: ')
    users.insert(10,newuser)
    newpwd = input('Nuevo Password: ')
    pwds.insert(10,newpwd)
    print('*** Usuario Registrado Correctamente ***')
    anws = input('++++ Desea Logearse? Escriba si/no: \n')
    if anws == 'si'or anws == 'SI':
        usuario = input('Usuario: ')
        usu = users.index(usuario)
        if users[usu] == usuario:
            pwd = input('Password: ')
            if pwd == pwds[usu]:
                Delivery()
            else:
                print('+++++ BLOCKED USER +++++')
        else:
            print('+++++ Usuario Inexistente +++++')
    elif anws == 'no'or anws == 'NO':
        print('** Gracias por su preferencia, tenga un Buen dia **')
        print('+++++++++++++++++++ PERUDELIVERY ++++++++++++++++++')
        print('...................................................')
    else:
        print('++ ERROR 890 ++')
        print('++ OPCION NO VALIDA ++')
        print('Saliendo del Programa....')
'''
'''
def SignIn():
    print('*****************************************')
    print('++++++++++++++ PERUDELIVERY +++++++++++++')
    anws = input('++++ Esta registrado? Escriba si/no: \n')
    if anws == 'si':
        usuario = input('Usuario: ')
        usu = users.index(usuario)
        if users[usu] == usuario:
            pwd = input('Password: ')
            if pwd == pwds[usu]:
                Delivery()
            else:
                print('+++++ BLOCKED USER +++++')
        else:
            print('+++++ Usuario Inexistente +++++')
    elif anws == 'no':
        SignUp()
    else:
        print('++ ERROR 450 ++')
        print('++ OPCION NO VALIDA ++')
        print('Saliendo del Programa....')  
'''
os.system('cls')
print('******************************************')
print('++++++++++++++ PERUDELIVERY ++++++++++++++')
print('************** BIENVENIDO(A) *************')
anws = input('++++ Esta registrado? Escriba si/no: ')
if anws == 'si' or anws == 'SI':
    os.system('cls')
    print('*******************************')
    print('++++++++ PERUDELIVERY +++++++++')
    print('************ LOGIN ************')
    usuario = input('Usuario: ')
    usu = users.index(usuario)
    if users[usu] == usuario:
        x = 1
        while x <= 4:
            pwd = input('Password: ')
            if pwd == pwds[usu]:
                Delivery()
                break
            else:
                print(f'Intento {x} de 3')
                x+=1
                        
        else:
            os.system('cls')
            print('+++++ SE SUPERO EL NUMERO DE INTENTOS +++++')
            print('++++++++++++++ BLOCKED USER +++++++++++++++')
            print('Ha alcanzado el numero maximo de intentos')
            print(' ҎeruḎelivery© 2021 Todos Los derechos Reservados ')
            print('Saliendo del Programa....')
       
    else:
        print('+++++ Usuario Inexistente +++++')
elif anws == 'no' or anws == 'NO':
    os.system('cls')
    print('*******************************')
    print('++++++++ PERUDELIVERY +++++++++')
    print('*********** SIGN UP **********')
    print('* Por Favor Siga los pasos para ')
    print(' Crearle una nueva cuenta *')
    print('*******************************')
    newname = input('Nombre Completo: ')
    namesUsers.insert(10,newname)
    newuser = input('Nuevo Usuario: ')
    users.insert(10,newuser)
    newpwd = input('Nuevo Password: ')
    pwds.insert(10,newpwd)
    os.system('cls')
    print('*** Usuario Registrado Correctamente ***')
    anws = input('++++ Desea Logearse? Escriba si/no: \n')
    if anws == 'si'or anws == 'SI':
        os.system('cls')
        print('*******************************')
        print('++++++++ PERUDELIVERY +++++++++')
        print('************ LOGIN ************')
        usuario = input('Usuario: ')
        usu = users.index(usuario)
        if users[usu] == usuario:
            x = 1
            while x <= 4:
                pwd = input('Password: ')
                if pwd == pwds[usu]:
                    Delivery()
                    break
                else:
                    print(f'Intento {x} de 3')
                    x+=1
                            
            else:
                os.system('cls')
                print('+++++ SE SUPERO EL NUMERO DE INTENTOS +++++')
                print('++++++++++++++ BLOCKED USER +++++++++++++++')
                print('Ha alcanzado el numero maximo de intentos')
                print(' ҎeruḎelivery© 2021 Todos Los derechos Reservados ')
                print('Saliendo del Programa....')
        else:
            print('+++++ Usuario Inexistente +++++')
    elif anws == 'no'or anws == 'NO':
        
        print('** Gracias por su preferencia, tenga un Buen dia **')
        print('+++++++++++++++++++ PERUDELIVERY ++++++++++++++++++')
        print('...................................................')
        print(' ҎeruḎelivery© 2021 Todos Los derechos Reservados ')
    else:
        
        print('++ ERROR 890 ++')
        print('++ OPCION NO VALIDA ++')
        print(' ҎeruḎelivery© 2021 Todos Los derechos Reservados ')
        print('Saliendo del Programa....')
        
else:
    
    print('++ ERROR 450 ++')
    print('++ OPCION NO VALIDA ++')
    print(' ҎeruḎelivery© 2021 Todos Los derechos Reservados ')
    print('Saliendo del Programa....')