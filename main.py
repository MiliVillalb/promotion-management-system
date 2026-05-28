# ...................................................
# TRABAJO PRACTICO NRO 3
# EQUIPO DE TRABAJO
# 1ER ANO - SISTEMAS - UTN
# GIAN LUCA VIANI
# ....................................................

# Importa las librerías a utilizar
import os
import pickle
import getpass
import io
import os.path
from datetime import datetime

# Define el tipo de registro USUARIO
class usuario:
    def __init__(self):
        self.codUsuario = 0
        self.nombreUsuario = ""
        self.claveUsuario = ""
        self.tipoUsuario = ""


# Define el tipo de registro LOCAL
class local:
    def __init__(self):
        self.codLocal = 0
        self.nombreLocal = ""
        self.ubicacionLocal = ""
        self.rubroLocal = ""
        self.codUsuario = 0
        self.estado = ""


# Define el tipo de registro PROMOCIONES
class promociones:
    def __init__(self):
        self.codPromo = 0
        self.textoPromo = ""
        self.fechaDesdePromo = datetime.now()
        self.fechaHastaPromo = datetime.now()
        self.diasSemana = []
        self.estado = ""
        self.codLocal = 0


# Define el tipo de registro USO_PROMOCIONES
class uso_promociones:
    def __init__(self):
        self.codCliente = 0
        self.codPromo = 0
        self.fechaUsoPromo = datetime.now()


# Define el tipo de registro NOVEDADES
class novedades:
    def __init__(self):
        self.codNovedad = 0
        self.textoNovedad = ""
        self.fechaDesdeNovedad = datetime.now()
        self.fechaHastaNovedad = datetime.now()
        self.tipoUsuario = ""
        self.estado = ""


# Verifica existencia de carpeta de trabajo
def verifica_carpeta_trabajo():
    ruta = "C:\\tp3\\"
    if not os.path.exists(ruta):
        os.makedirs(ruta)


# Crear/Abrir usuarios.dat
def existe_abre_usuario():
    archfis_usuario = 'C:\\tp3\\usuarios.dat'
    if os.path.exists(archfis_usuario):
        global archlog_usuario
        archlog_usuario = open(archfis_usuario, "r+b")
    else:
        archlog_usuario = open(archfis_usuario, "w+b")
        crea_usuario_admin()
    return archlog_usuario


# Crear/Abrir locales.dat
def existe_abre_local():
    archfis_local = 'C:\\tp3\\locales.dat'
    if os.path.exists(archfis_local):
        global archlog_local
        archlog_local = open(archfis_local, "r+b")
    else:
        archlog_local = open(archfis_local, "w+b")
    return archlog_local


# Crear/Abrir promociones.dat
def existe_abre_prom():
    archfis_promociones = 'C:\\tp3\\promociones.dat'
    if os.path.exists(archfis_promociones):
        global archlog_promociones
        archlog_promociones = open(archfis_promociones, "r+b")
    else:
        archlog_promociones = open(archfis_promociones, "w+b")
    return archlog_promociones


# Crear/Abrir prom_uso.dat
def existe_abre_prom_uso():
    archfis_prom_uso = 'C:\\tp3\\uso_promociones.dat'
    if os.path.exists(archfis_prom_uso):
        global archlog_prom_uso
        archlog_prom_uso = open(archfis_prom_uso, "r+b")
    else:
        archlog_prom_uso = open(archfis_prom_uso, "w+b")
    return archlog_prom_uso


# Crear/Abrir novedades.dat
def existe_abre_novedades():
    archfis_novedades = 'C:\\tp3\\novedades.dat'
    if os.path.exists(archfis_novedades):
        global archlog_novedades
        archlog_novedades = open(archfis_novedades, "r+b")
    else:
        archlog_novedades = open(archfis_novedades, "w+b")
    return archlog_novedades


# Formateo de registros de usuarios
def formateo_usuario(reg_usuario):
    reg_usuario.nombreUsuario = str(reg_usuario.nombreUsuario)
    reg_usuario.nombreUsuario = reg_usuario.nombreUsuario.ljust(100, ' ')
    reg_usuario.claveUsuario = reg_usuario.claveUsuario.ljust(8, ' ')
    reg_usuario.tipoUsuario = str(reg_usuario.tipoUsuario)
    reg_usuario.tipoUsuario = reg_usuario.tipoUsuario.ljust(20, ' ')


# Formateo de registros de locales
def formateo_local(reg_local):
    reg_local.nombreLocal = str(reg_local.nombreLocal)
    reg_local.nombreLocal = reg_local.nombreLocal.ljust(50, ' ')
    reg_local.ubicacionLocal = str(reg_local.ubicacionLocal)
    reg_local.ubicacionLocal = reg_local.ubicacionLocal.ljust(50, ' ')
    reg_local.rubroLocal = str(reg_local.rubroLocal)
    reg_local.rubroLocal = reg_local.rubroLocal.ljust(50, ' ')


# Formateo de registros de promociones
def formateo_promocion(reg_promocion):
    reg_promocion.textoPromo = str(reg_promocion.textoPromo)
    reg_promocion.textoPromo = reg_promocion.textoPromo.ljust(200, ' ')
    reg_promocion.fechaDesdePromo = reg_promocion.fechaDesdePromo
    reg_promocion.fechaHastaPromo = reg_promocion.fechaHastaPromo
    for i in range(0, 6):
        reg_promocion.diasSemana[i] = str(reg_promocion.diasSemana[i])
        reg_promocion.diasSemana[i] = reg_promocion.diasSemana[i].ljust(1, ' ')
    reg_promocion.estado = str(reg_promocion.estado)
    reg_promocion.estado = reg_promocion.estado.ljust(10, ' ')


# Formateo de registros de uso de promociones
#   def formateo_prom_uso(reg_prom_uso):
#    reg_prom_uso.codCliente = reg_prom_uso.codCliente.ljust(8, ' ')
#    reg_prom_uso.codPromo = reg_prom_uso.codPromo.ljust(8, ' ')


# Formateo de registros de uso de novedades
def formateo_novedades(reg_novedades):
    reg_novedades.textoNovedad = str(reg_novedades)
    reg_novedades.textoNovedad = reg_novedades.textoNovedad.ljust(200, ' ')
    reg_novedades.tipoUsuario = str(tipoUsuario)
    reg_novedades.tipoUsuario = reg_novedades.tipoUsuario.ljust(20, ' ')


def busca_usuario(usuario_mail):
    os.system('cls')
    global archfis_usuario
    global archlog_usuario
    archfis_usuario = 'C:\\tp3\\usuarios.dat'
    global reg_usuario
    pos = -1
    codUsuario = ''
    tam = os.path.getsize(archfis_usuario)
    if tam == 0:
        pos = -1
    else:
        reg_usuario = usuario()
        archlog_usuario.seek(0, 0)
        while archlog_usuario.tell() < tam:
            p = archlog_usuario.tell()
            reg_usuario = pickle.load(archlog_usuario)
            if reg_usuario.nombreUsuario.replace(" ", "") == str(usuario_mail.replace(" ", "")):
                pos = p
                codUsuario = reg_usuario.codUsuario
    return pos, codUsuario


def busca_local(nombreLocal):
    os.system('cls')
    global archfis_local
    global archlog_local
    archfis_local = 'C:\\tp3\\locales.dat'
    global reg_local
    pos = -1
    tam = os.path.getsize(archfis_local)
    if tam == 0:
        pos = -1
    else:
        reg_local = local()
        archlog_local.seek(0, 0)
        while archlog_local.tell() < tam:
            p = archlog_local.tell()
            reg_local = pickle.load(archlog_local)
            if reg_local.nombreLocal.replace(" ", "") == str(nombreLocal.replace(" ", "")):
                pos = p
    return pos


def busca_local_cod(codLocal):
    os.system('cls')
    global archfis_local
    global archlog_local
    archfis_local = 'C:\\tp3\\locales.dat'
    global reg_local
    pos = -1
    tam = os.path.getsize(archfis_local)
    if tam == 0:
        pos = -1
    else:
        reg_local = local()
        archlog_local.seek(0, 0)
        while archlog_local.tell() < tam:
            p = archlog_local.tell()
            reg_local = pickle.load(archlog_local)
            if reg_local.codLocal == codLocal:
                pos = p
    return pos


def busca_nombre_local(codLocal):
    os.system('cls')
    #print('Me pasaron el cod de local :  ', codLocal)
    global archfis_local
    global archlog_local
    archfis_local = 'C:\\tp3\\locales.dat'
    nombre = ''
    tam = os.path.getsize(archfis_local)
    if tam == 0:
        print('No hay locales en el archivo')
    else:
        reg_local = local()
        archlog_local.seek(0, 0)
        encontro = False
        while archlog_local.tell() < tam:
            p = archlog_local.tell()
            reg_local = pickle.load(archlog_local)
            if str(reg_local.codLocal) == str(codLocal):
                #print('los codigos son IGUALES!!!!')
                #print('codlocal', codLocal,'codlocalregisto', reg_local.codLocal,'///')
                #print('El nombre del local es ', reg_local.nombreLocal)
                nombre = reg_local.nombreLocal
                encontro = True
    if not encontro:
            nombre = 'desconocido'
    return nombre


def busca_promo(codPromo):
    os.system('cls')
    global archfis_promociones
    global archlog_promociones
    archfis_promociones = 'C:\\tp3\\promociones.dat'
    global reg_promociones
    pos = -1
    estado = ' '
    fechaDesde = ''
    fechaHasta = ''
    tam = os.path.getsize(archfis_promociones)
    if tam == 0:
        pos = -1
    else:
        reg_promociones = promociones()
        archlog_promociones.seek(0, 0)
        while archlog_promociones.tell() < tam:
            p = archlog_promociones.tell()
            reg_promociones = pickle.load(archlog_promociones)
            if reg_promociones.codPromo == codPromo:
                estado = reg_promociones.estado
                fechaDesde = reg_promociones.fechaDesdePromo
                fechaHasta = reg_promociones.fechaHastaPromo
                pos = p
    return pos, estado, fechaDesde, fechaHasta


def crea_usuario_admin():
    os.system('cls')
    global archfis_usuario
    global archlog_usuario
    archlog_usuario.seek(0, 2)
    reg_usuario = usuario()
    reg_usuario.codUsuario = 1
    reg_usuario.nombreUsuario = "admin"
    reg_usuario.claveUsuario = "12345"
    reg_usuario.tipoUsuario = "administrador"
    formateo_usuario(reg_usuario)
    pickle.dump(reg_usuario, archlog_usuario)
    archlog_usuario.flush()
    acum = 0


def cantidad_registrosUsuario():
    os.system('cls')
    global archfis_usuario
    global archlog_usuario
    archfis_usuario = 'C:\\tp3\\usuarios.dat'
    reg_usuario = usuario()
    archlog_usuario.seek(0, 0)
    reg_usuario = pickle.load(archlog_usuario)
    tamano_archivo_usuario = os.path.getsize(archfis_usuario)
    if tamano_archivo_usuario != 0:
        tamano_registro_usuario = archlog_usuario.tell()
        cantReg = int(tamano_archivo_usuario // tamano_registro_usuario)
    else:
        cantReg = 0
    return cantReg


def cantidad_registrosLocal():
    os.system('cls')
    global archfis_local
    global archlog_local
    archfis_local = 'C:\\tp3\\locales.dat'
    reg_local = local()
    archlog_local.seek(0, 0)
    tamano_archivo_local = os.path.getsize(archfis_local)
    if tamano_archivo_local != 0:
        reg_local = pickle.load(archlog_local)
        tamano_registro_local = archlog_local.tell()
        cantReg = int(tamano_archivo_local // tamano_registro_local)
    else:
        cantReg = 0
    return cantReg


def cantidad_registrosPromociones():
    os.system('cls')
    global archfis_promociones
    global archlog_promociones
    archfis_promociones = 'C:\\tp3\\promociones.dat'
    reg_promocion = promociones()
    archlog_promociones.seek(0, 0)
    tamano_archivo_promociones = os.path.getsize(archfis_promociones)
    if tamano_archivo_promociones != 0:
        reg_promocion = pickle.load(archlog_promociones)
        tamano_registro_promociones = archlog_promociones.tell()
        cantReg = int(tamano_archivo_promociones // tamano_registro_promociones)
    else:
        cantReg = 0
    return cantReg

def cantidad_registrosPromocionesUso():
    os.system('cls')
    global archfis_prom_uso
    global archlog_prom_uso
    archfis_prom_uso = 'C:\\tp3\\uso_promociones.dat'
    reg_prom_uso = uso_promociones()
    archlog_prom_uso.seek(0, 0)
    tamano_archivo_prom_uso = os.path.getsize(archfis_prom_uso)
    if tamano_archivo_prom_uso != 0:
        reg_prom_uso = pickle.load(archlog_prom_uso)
        tamano_registro_prom_uso = archlog_prom_uso.tell()
        cantReg = int(tamano_archivo_prom_uso // tamano_registro_prom_uso)
    else:
        cantReg = 0
    return cantReg

def crea_clientes():
    os.system('cls')
    global archfis_usuario
    global archlog_usuario
    reg_usuario = usuario()
    cantReg = int(cantidad_registrosUsuario())
    archlog_usuario.seek(0, 2)
    mail = input("Ingrese mail del cliente: ")
    posi, codUsuario = busca_usuario(mail)
    if posi != -1:
        print('El usuario/cliente ya existe!!')
    else:
        reg_usuario.nombreUsuario = mail
        reg_usuario.claveUsuario = input('Clave: ')
        while len(reg_usuario.claveUsuario) != 8:
            print('La clave debe tener 8 caracteres. Intente nuevamente...')
            reg_usuario.claveUsuario = input('Clave: ')
        reg_usuario.tipoUsuario = 'cliente'
        reg_usuario.codUsuario = cantReg + 1
        formateo_usuario(reg_usuario)
        pickle.dump(reg_usuario, archlog_usuario)
        archlog_usuario.flush()

def crea_duenosLocales():
    os.system('cls')
    global archfis_usuario
    global archlog_usuario
    reg_usuario = usuario()
    cantReg = int(cantidad_registrosUsuario())
    archlog_usuario.seek(0, 2)
    print('\nUsted esta a punto de crear una cuenta de DUENO....')
    mail = input("\nIngrese mail del dueño a crear(0 para salir): ")
    posi, codUsuario = busca_usuario(mail)
    if posi != -1:
        print('\nEl mail/dueño ya existe!!')
    else:
        reg_usuario.nombreUsuario = mail
        reg_usuario.claveUsuario = input('Clave: ')
        while len(reg_usuario.claveUsuario) != 8:
            print('La clave debe tener 8 caracteres. Intente nuevamente...')
            reg_usuario.claveUsuario = input('Clave: ')
        reg_usuario.tipoUsuario = 'dueño'
        reg_usuario.codUsuario = cantReg + 1
        formateo_usuario(reg_usuario)
        pickle.dump(reg_usuario, archlog_usuario)
        archlog_usuario.flush()


def crear_descuento(codUsuario):
    os.system('cls')
    global archfis_promociones
    global archlog_promociones
    reg_promociones = promociones()
    cantReg = int(cantidad_registrosPromociones())
    archlog_promociones.seek(0, 2)
    print('\nUsted esta a punto de crear una PROMOCION....')
    textoPromo = input("\nIngrese la descripcion de la promocion (0 para salir): ")
    reg_promociones.textoPromo = textoPromo
    diaDesde = int(input('dia desde : '))
    mesDesde = int(input('mes desde : '))
    anoDesde = int(input('ano desde : '))
    fechaDesde = datetime(anoDesde, mesDesde, diaDesde)
    reg_promociones.fechaDesdePromo = fechaDesde
    diaHasta = int(input('dia hasta : '))
    mesHasta = int(input('mes hasta : '))
    anoHasta = int(input('ano hasta : '))
    fechaHasta = datetime(anoHasta, mesHasta, diaHasta)
    reg_promociones.fechaHastaPromo = fechaHasta
    reg_promociones.diasSemana = []
    reg_promociones.codLocal = input('Ingrese el cod de Local a referenciar : ')
    for i in range(7):
        reg_promociones.diasSemana.append(float(input(f'Dia nro {i + 1}: ')))
    reg_promociones.estado = 'Pendiente'
    print('\nSe ha creado una nueva promocion. El estado asignado es :', reg_promociones.estado)
    reg_promociones.codUsuario = codUsuario
    reg_promociones.codPromo = cantReg + 1
    print('\nEl nuevo codigo de promocion asignado es : ', reg_promociones.codPromo)
    formateo_promocion(reg_promociones)
    pickle.dump(reg_promociones, archlog_promociones)
    archlog_promociones.flush()

def reporte_uso_descuentos(codUsuario):
    os.system('cls')
    global archfis_promociones
    global archlog_promociones
    reg_promociones = promociones()
    archfis_promociones = 'C:\\tp3\\promociones.dat'
    global archfis_prom_uso
    global archlog_prom_uso
    reg_prom_uso = uso_promociones()
    archfis_prom_uso = 'C:\\tp3\\uso_promociones.dat'
    codDueno = codUsuario
    print('\nUsted es el cod de dueno: ', codDueno)
    print('\nFavor ingresar el intervalo de fechas que requiere para el reporte')
    diaDesde = int(input('dia desde : '))
    mesDesde = int(input('mes desde : '))
    anoDesde = int(input('ano desde : '))
    fechaDesde = datetime(anoDesde, mesDesde, diaDesde)
    diaHasta = int(input('\ndia hasta : '))
    mesHasta = int(input('mes hasta : '))
    anoHasta = int(input('ano hasta : '))
    fechaHasta = datetime(anoHasta, mesHasta, diaHasta)
    tam = os.path.getsize(archfis_promociones)
    tamUso = os.path.getsize(archfis_prom_uso)
    contador = 0
    if tam == 0:
        print('No hay promociones disponibles')
    else:
        print('\nREPORTE DE USO DE DESCUENTOS')
        print('Fecha desde: ', fechaDesde, '    Fecha hasta: ', fechaHasta)
        archlog_promociones.seek(0, 0)
        while archlog_promociones.tell() < tam:
            reg_promociones = pickle.load(archlog_promociones)
            if reg_promociones.estado.replace(" ", "") == 'aprobada' and reg_promociones.fechaDesdePromo >= fechaDesde and reg_promociones.fechaHastaPromo <= fechaHasta:
                print('\n  Cod Promo', '      Texto', '                  Fecha desde', '                          Fecha hasta', '        ', 'Cod Local')
                print('        ', reg_promociones.codPromo,'            ', reg_promociones.textoPromo.replace(" ",""),'         ', reg_promociones.fechaDesdePromo,'          ', reg_promociones.fechaHastaPromo, '               ', reg_promociones.codLocal)
                archlog_prom_uso.seek(0, 0)
                while archlog_prom_uso.tell() < tamUso:
                    reg_prom_uso = pickle.load(archlog_prom_uso)
                    if str(reg_promociones.codPromo) == str(reg_prom_uso.codPromo):
                        contador += 1
                        print('Cantidad de Usos: ',contador)
                    else:
                        print('No hay promociones que cumplan los requisitos solicitados.')
            else:
                print('')


def listar_descuentos_pendientes():
    os.system('cls')
    global archfis_promociones
    global archlog_promociones
    reg_promociones = promociones()
    archfis_promociones = 'C:\\tp3\\promociones.dat'
    tam = os.path.getsize(archfis_promociones)
    if tam == 0:
        print('No hay promociones disponibles')
    else:
        archlog_promociones.seek(0, 0)
        cantPendiente = 0
        print('-----------------   LISTADO  PROMOCIONES PENDIENTE DE APROBACION ----------------')
        print('Cod Promocion', '    Texto Promo', '     Validez desde', '          Validez hasta', '                Estado', '   Codigo local','    Nombre Loc')
        while archlog_promociones.tell() < tam:
            reg_promociones = pickle.load(archlog_promociones)
            nombre_local = busca_nombre_local(reg_promociones.codLocal)
            if reg_promociones.estado.replace(" ","") == 'Pendiente':
                print('       ', reg_promociones.codPromo,'           ', reg_promociones.textoPromo.replace(" ", ""),'     ', reg_promociones.fechaDesdePromo,'      ', reg_promociones.fechaHastaPromo,'     ' ,reg_promociones.estado,'    ' ,reg_promociones.codLocal,'         ',nombre_local)
                cantPendiente = cantPendiente + 1
        if cantPendiente == 0:
            print('Ya no quedan Promociones pendientes de aprobacion!')
        else:
            aprobar_denegar_descuento()


def listar_descuentos_vigentes():
    os.system('cls')
    global archfis_promociones
    global archlog_promociones
    reg_promociones = promociones()
    archfis_promociones = 'C:\\tp3\\promociones.dat'
    tam = os.path.getsize(archfis_promociones)
    if tam == 0:
        print('No hay promociones disponibles')
    else:
        dia_hoy = datetime.now()
        print('\nEstas son las promociones disponibles al dia de hoy : ', dia_hoy)
        print(' ')
        archlog_promociones.seek(0, 0)
        print('\n-----------------   L I S T A D O  D E  P R O M O C I O N E S ----------------')
        print('Cod Promocion', '    Texto Promo', '     Validez desde', '           Validez hasta', '          Estado', '          Codigo local')
        while archlog_promociones.tell() < tam:
            reg_promociones = pickle.load(archlog_promociones)
            if reg_promociones.fechaDesdePromo < dia_hoy < reg_promociones.fechaHastaPromo and reg_promociones.estado.replace(" ","") == 'aprobada':
                print('       ', reg_promociones.codPromo,'           ', reg_promociones.textoPromo.replace(" ", ""),'     ', reg_promociones.fechaDesdePromo,'      ', reg_promociones.fechaHastaPromo,'     ' ,reg_promociones.estado,'    ' ,reg_promociones.codUsuario)


def aprobar_denegar_descuento():
    os.system('cls')
    global archfis_promociones
    global archlog_promociones
    reg_promociones = promociones()
    archfis_promociones = 'C:\\tp3\\promociones.dat'
    codPromo = int(input("\nIngrese el codigo del Descuento a Aprobar/Rechazar: "))
    posi, estado = busca_promo(codPromo)
    decision = ''
    if posi != -1 and estado.replace(" ","") == 'Pendiente':
        archlog_promociones.seek(posi, 0)
        reg_promociones = pickle.load(archlog_promociones)
        print('\nEl texto de la promocion seleccionada es: ', reg_promociones.textoPromo)
        print('Vigente desde : ', reg_promociones.fechaDesdePromo)
        print('Vigente hasta : ', reg_promociones.fechaHastaPromo)
        # for i in range(7):
        #    print(f'Dia nro {i + 1}: {reg_promociones["diasSemana"][i]}')
        print('Estado Actual : ', reg_promociones.estado)
        print('Codigo de Local asignado : ', reg_promociones.codLocal)
        while decision.lower() != 's' and decision.lower() != 'n':
            decision = input("\nAprueba Promocion Si/No ?: ")
            if decision.lower() == 's':
                reg_promociones.estado = 'aprobada'
                print('\nLa promocion ha sido APROBADA')
            elif decision.lower() == 'n':
                reg_promociones.estado = 'rechazada'
                print('La promocion ha sido RECHAZADA')
            else:
                print("\nUsted debe tomar una decision. Por favor intente nuevamente...")
        archlog_promociones.seek(posi, 0)
        formateo_promocion(reg_promociones)
        pickle.dump(reg_promociones, archlog_promociones)
        archlog_promociones.flush()
    else:
        print('\nEl codigo de descuento no existe o no esta pendiente')
    pass


def cerrar():
    archlog_usuario.close()
    archlog_local.close()
    archlog_promociones.close()
    archlog_prom_uso.close()


def listar_usuario():
    os.system('cls')
    global archfis_usuario
    global archlog_usuario
    reg_usuario = usuario()
    archfis_usuario = 'C:\\tp3\\usuarios.dat'
    tam = os.path.getsize(archfis_usuario)
    if tam == 0:
        print('No hay usuarios registrados')
    else:
        archlog_usuario.seek(0, 0)
        print('Cod Usuario', '   Usuario', '  Clave      ', 'Tipo de Usuario')
        while archlog_usuario.tell() < tam:
            reg_usuario = pickle.load(archlog_usuario)
            print(reg_usuario.codUsuario, "          ", reg_usuario.nombreUsuario.replace(" ", ""), "       ",
                  reg_usuario.claveUsuario, "   ", reg_usuario.tipoUsuario, )


def listar_locales():
    os.system('cls')
    global archfis_local
    global archlog_local
    reg_local = local()
    archfis_local = 'C:\\tp3\\locales.dat'
    tam = os.path.getsize(archfis_local)
    if tam == 0:
        print('No hay locales registrados')
    else:
        archlog_local.seek(0, 0)
        print('--------     L I S T A D O  D E  L O C A L E S       ---------')
        print('Codigo Local   ', 'Nombre Local', ' Rubro Local', '  Ubicacion  ', ' Cod Usuario')
        while archlog_local.tell() < tam:
            reg_local = pickle.load(archlog_local)
            if reg_local.estado == " ":
                print('   ', reg_local.codLocal,'       ', reg_local.nombreLocal.replace(" ", ""),'         ', reg_local.rubroLocal.replace(" ", ""),'       ', reg_local.ubicacionLocal.replace(" ", ""),'        ', reg_local.codUsuario)


def listar_UsoPromociones():
    os.system('cls')
    global archfis_prom_uso
    global archlog_prom_uso
    archfis_prom_uso = 'C:\\tp3\\uso_promociones.dat'
    reg_promoUso = uso_promociones()
    tam = os.path.getsize(archfis_prom_uso)
    if tam == 0:
        print('No hay Promociones Utilizadas')
    else:
        archlog_prom_uso.seek(0, 0)
        print('--------     LISTADO DE PROMOCIONES UTILIZADAS       ---------')
        print('Codigo Cliente     ', 'Codigo de Promocion      ', 'Fecha de uso de la promocion')
        while archlog_prom_uso.tell() < tam:
            reg_promoUso = pickle.load(archlog_prom_uso)
            miFormatoFecha = "%d de %B de %Y"
            fechaUso = str(reg_promoUso.fechaUsoPromo.strftime(miFormatoFecha))
            print('    ', reg_promoUso.codCliente, '                 ', reg_promoUso.codPromo,'            ', fechaUso)


def menu_administrador():
    os.system('cls')
    opcion = -1
    while opcion == -1:
        print("\nBienvenido al Menu Administrador\n")
        print("1. Gestión de locales")
        print("2. Crear cuentas de dueños de locales")
        print("3. Aprobar / Denegar solicitud de descuento")
        print("4. Gestión de novedades")
        print("5. Reporte de utilización de descuentos")
        print("0. Salir")
        opcion = int(input("\nSeleccione una opción: "))
        if 1 <= opcion < 5:
            if opcion == 1:
                submenu_gestionLocales()
                opcion = -1
            elif opcion == 2:
                # listar_locales()
                crea_duenosLocales()
                opcion = -1
            elif opcion == 3:
                print("Aprobar / Denegar solicitud de descuento")
                listar_descuentos_pendientes()
                opcion = -1
            elif opcion == 4:
                print("Gestión de novedades / esta parte se hace en Chapin!")
            elif opcion == 5:
                print("Reporte de utilización de descuentos")
            elif opcion == 0:
                print("Saliendo....")
            else:
                print("Opción no válida. Por favor, elija una opción válida.")


def menu_dueno_local(codUsuario):
    os.system('cls')
    opcion = -1
    while opcion == -1:
        print("\nBienvenido al Menu Dueño de Local\n")
        print("1. Crear Descuento")
        print("2. Reporte de uso de descuentos")
        print("3. Ver Novedades")
        print("0. Salir")
        opcion = int(input("\nSeleccione una opción: "))
        if 1 <= opcion < 4:
            if opcion == 1:
                print("Crear descuento")
                listar_descuentos_vigentes()
                crear_descuento(codUsuario)
                opcion = -1
            elif opcion == 2:
                print("Reporte de uso de descuentos")
                reporte_uso_descuentos(codUsuario)
                opcion = -1
            elif opcion == 3:
                print("Ver novedades (solo chapin")
                input()
                opcion = -1
            elif opcion == 0:
                print("Saliendo...")
            else:
                print("Opción no válida. Por favor, elija una opción válida.")


def submenu_gestionLocales():
    os.system('cls')
    opcion = 'z'
    while opcion == 'z':
        print("\n\nBienvenido al Sub-Menu de Gestion de Locales")
        print("a. Crear locales")
        print("b. Modificar local")
        print("c. Eliminar local")
        print("d. Mapa de Locales")
        print("e. Volver")
        opcion = input("\nSeleccione una opción: ")
        if opcion == 'a':
            listar_locales()
            crea_local()
            ordenarLocales()
        elif opcion == 'b':
            listar_locales()
            modificar_local()
            ordenarLocales()
        elif opcion == 'c':
            listar_locales()
            baja_logica_local()
        elif opcion == 'd':
            print("Mapa de Locales")
            mapaLocales()
        elif opcion == 'e':
            print("\nVolviendo al menu de Administrador")
        else:
            print("\nOpción no válida. Por favor, elija una opción válida.")


def crea_local():
    os.system('cls')
    global archfis_local
    global archlog_local
    reg_local = local()
    opcion = 's'
    while opcion == 's':
        cantReg = int(cantidad_registrosLocal())
        archlog_local.seek(0, 2)
        nombreLocal = input("\nIngrese Nombre del NUEVO local: ")
        posi = busca_local(nombreLocal)
        if posi != -1:
            print('\nEl Local ya existe!!')
        else:
            reg_local.nombreLocal = str(nombreLocal)
            reg_local.ubicacionLocal = input('Ubicacion del Local: ')
            reg_local.rubroLocal = str(input("Indique el Rubro: I-indumentaria  P-perfumeria  C-comida : "))
            while (reg_local.rubroLocal.lower() != 'i') and (reg_local.rubroLocal.lower() != 'p') and (reg_local.rubroLocal.lower() != 'c'):
                    reg_local.rubroLocal = str(input('El rubro no es correcto. Favor intente nuevamente :'))
            if reg_local.rubroLocal.lower() == 'i':
                reg_local.rubroLocal = 'indumentaria'
            elif reg_local.rubroLocal.lower() == 'p':
                reg_local.rubroLocal = 'perfumeria'
            elif reg_local.rubroLocal == 'c':
                reg_local.rubroLocal = 'comida'
            reg_local.codUsuario = int(input('Codigo de Usuario/Dueno: '))
            reg_local.estado = ' '
            reg_local.codLocal = cantReg + 1
            print('Codigo Local : ', reg_local.codLocal)
            formateo_local(reg_local)
            pickle.dump(reg_local, archlog_local)
            archlog_local.flush()
            opcion = input('Marque N para terminar la carga de locales: ')
            if opcion.lower() == 'n':
                print('\n Ha finalizado de cargar nuevos locales...')


def modificar_local():
    os.system('cls')
    codLocal = int(input("Ingrese el codigo del Local a modificar: "))
    posi = busca_local_cod(codLocal)
    if posi != -1:
        archlog_local.seek(posi, 0)
        reg_local = pickle.load(archlog_local)
        print('El nombre actual es: ', reg_local.nombreLocal)
        print('La ubicacion actual es: ', reg_local.ubicacionLocal)
        print('El rubro actual es: ', reg_local.rubroLocal)
        print('El cod del dueno actual es: ', reg_local.codUsuario)
        reg_local.nombreLocal = input('Ingrese nuevo Nombre: ')
        reg_local.ubicacionLocal = input('Ingrese nueva Ubicacion: ')
        reg_local.rubroLocal = str(input("Indique el Rubro: I-indumentaria  P-perfumeria  C-comida : "))
        while (reg_local.rubroLocal.lower() != 'i') and (reg_local.rubroLocal.lower() != 'p') and (
                reg_local.rubroLocal.lower() != 'c'):
            reg_local.rubroLocal = str(input('El rubro no es correcto. Favor intente nuevamente :'))
        reg_local.codUsuario = input('Ingrese nuevo Cod Dueno: ')
        archlog_local.seek(posi, 0)
        formateo_local(reg_local)
        pickle.dump(reg_local, archlog_local)
        archlog_local.flush()
        print('El registro se ha modificado con exito')
    else:
        print('El local no existe')
    pass


def baja_logica_local():
    os.system('cls')
    codLocal = int(input("Ingrese cod Local a borrar: "))
    pos = busca_local_cod(codLocal)
    if pos != -1:
        archlog_local.seek(pos, 0)
        reg_local = pickle.load(archlog_local)
        print('Usted esta a punto de borrar el Local: ', reg_local.nombreLocal)
        print('Ubicado en : ', reg_local.ubicacionLocal)
        print('Del Rubro : ', reg_local.rubroLocal)
        borrar = input('Si esta seguro marque -S-')
        if borrar.lower() == 's':
            reg_local.estado = 'X'
            print('El registro ha sido borrado.')
            archlog_local.seek(pos, 0)
            formateo_local(reg_local)
            pickle.dump(reg_local, archlog_local)
            archlog_local.flush()
        else:
            print('El registro NO ha sido borrado.')
    else:
        print("el cod de Local ingresado no existe")
    pass


def mapaLocales():
    os.system('cls')
    global archfis_local
    global archlog_local
    reg_local = local()
    archfis_local = 'C:\\tp3\\locales.dat'
    tam = os.path.getsize(archfis_local)
    localMax = cantidad_registrosLocal()
    cantLoc = 0
    if tam == 0:
        print('No hay locales registrados')
    else:
        archlog_local.seek(0, 0)
        elementos_por_fila = 0
        cantidad_filas = 0  # Contador de filas
        print('+-+-+-+-+-+-+-+-+-+-+')
        while cantidad_filas < 10:
            while elementos_por_fila < 5:
                cantLoc += 1
                if tam > archlog_local.tell():
                    reg_local = pickle.load(archlog_local)
                if cantLoc <= localMax:
                    print('|' + f'{reg_local.codLocal:2}', end=' ')
                else:
                    numero = " 0"
                    print('|' + f'{numero:2}', end=' ')
                elementos_por_fila += 1
            print('|')
            print('+-+-+-+-+-+-+-+-+-+-+')
            elementos_por_fila = 0
            cantidad_filas += 1


def menu_cliente(codUsuario):
    os.system('cls')
    opcion = -1
    while opcion == -1:
        print("\nBienvenido al Menu de Clientes\n")
        print("1. Buscar descuentos en Local")
        print("2. Solicitar descuento")
        print("3. Ver Novedades")
        print("0. Salir")
        opcion = int(input("\nSeleccione una opción: "))
        if 0 <= opcion < 4:
            if opcion == 1:
                print("Buscar descuentos en Local")
                busca_promo_local()
                input()
                opcion = -1
            elif opcion == 2:
                print("Solicitar descuento")
                solicitar_descuento(codUsuario)
                input()
                opcion = -1
            elif opcion == 3:
                print("\nVer novedades..(en chapin)")
                input()
                opcion = -1
            elif opcion == 0:
                print("Saliendo...")
            else:
                print("Opción no válida. Por favor, elija una opción válida.")


def busca_promo_local():
    os.system('cls')
    global archfis_promociones
    global archlog_promociones
    reg_promociones = promociones()
    archfis_promociones = 'C:\\tp3\\promociones.dat'
    tam = os.path.getsize(archfis_promociones)
    if tam == 0:
        print('\nNo hay promociones disponibles')
    else:
        hoy = datetime.now()
        #print('\nHoy es ',hoy)
        codLocal = int(input('Ingrese codigo de local: '))
        diaPromo = int(input("\nIngrese dia de la promo: "))
        mesPromo = int(input("Ingrese mes de la promo: "))
        anoPromo = int(input("Ingrese ano de la promo: "))
        fechaPromo = datetime(anoPromo, mesPromo, diaPromo)
        if fechaPromo >= hoy:
            # print('codigo local buscado : ',codLocal)
            # print('Fecha a considerar : ',fechaPromo)
            archlog_promociones.seek(0, 0)
            cantPendiente = 0
            print('\n-----------------   LISTADO  PROMOCIONES VIGENTES DEL LOCAL ----------------')
            print('Cod Promocion', '    Texto Promo', '     Validez desde', '   Validez hasta')
            while archlog_promociones.tell() < tam:
                reg_promociones = pickle.load(archlog_promociones)
                #print('El estado original es:', reg_promociones.estado.replace(" ", ""))
                #print('lo quiero comparar con -aprobada-')
                #print('El local solicitado es : ', codLocal)
                #print('El cod de local de la promo encontrada es : ', reg_promociones.codLocal)
                if reg_promociones.estado.replace(" ", "") == 'aprobada' and str(reg_promociones.codLocal) == str(codLocal):
                 #   print('si pasa por aca es que esta la promo aprobada!!!')
                # and reg_promociones.codLocal == codLocal:
                    print('   ', reg_promociones.codPromo, '           ', reg_promociones.textoPromo.replace(" ", ""),'     ', reg_promociones.fechaDesdePromo, '      ', reg_promociones.fechaHastaPromo)
                else:
                    print('\nNo hay mas promociones aprobadas para el local solicitado!')
        else:
            print('\nNo es posible buscar promociones / La fecha se encuentra en el pasado\n')

def solicitar_descuento(codUsuario):
    os.system('cls')
    global archfis_prom_uso
    global archlog_prom_uso
    reg_prom_uso = uso_promociones()
    cantReg = int(cantidad_registrosPromocionesUso())
    archlog_prom_uso.seek(0, 2)
    print('\nUsted esta a punto de SOLICITAR un DESCUENTO....')
    codPromo = int(input("\nIngrese el CODIGO de la PROMOCION: "))
    codigoPromocionCliente = codPromo
    fechaHoy = datetime.now()
    posi, estadoPromo, fechaDesde, fechaHasta = busca_promo(codPromo)
    #print('la pos es ', posi)
    #print('El estado de la promo es : ', estadoPromo)
    #print('Desde el ', fechaDesde,' hasta el ', fechaHasta)
    if posi == -1:
        print('\nNo hay promociones cargadas!!\n')
    else:
        if estadoPromo.replace(" ","") == 'aprobada' and fechaDesde < fechaHoy < fechaHasta:
            #print('\nla promo se puede usar')
            reg_prom_uso.codPromo = codigoPromocionCliente
            reg_prom_uso.codCliente = codUsuario
            print('Usted tiene el Codigo de Cliente: ', reg_prom_uso.codCliente)
            print('Ha solicitado la promocion nro : ', reg_prom_uso.codPromo)
            reg_prom_uso.fechaUsoPromo = fechaHoy
            print('Para el dia : ',reg_prom_uso.fechaUsoPromo)
            print('\nUsted ha finalizado el registro del uso de esta promocion en el sistema.')
            print('Presione cualquier techa para continuar...')
            input()
            #formateo_prom_uso(reg_prom_uso)
            pickle.dump(reg_prom_uso, archlog_prom_uso)
            archlog_prom_uso.flush()
        else:
            print('\nLa promo no esta activa actualmente.')


# Ordena el listado de locales en orden alfabetico
def ordenarLocales():
    os.system('cls')
    global archfis_local
    global archlog_local
    archfis_local = 'C:\\tp3\\locales.dat'
    archlog_local.seek(0, 0)
    auxi = local()
    auxj = local()
    auxi = pickle.load(archlog_local)
    tamreg = archlog_local.tell()
    tamarch = os.path.getsize(archfis_local)
    cantReg = int(tamarch/tamreg)
    for i in range(0, cantReg - 1):
        for j in range(i + 1, cantReg):
            archlog_local.seek(i*tamreg, 0)
            auxi = pickle.load(archlog_local)
            archlog_local.seek(j * tamreg, 0)
            auxj = pickle.load(archlog_local)
            if auxi.nombreLocal > auxj.nombreLocal:
                archlog_local.seek(i*tamreg, 0)
                pickle.dump(auxj, archlog_local)
                archlog_local.seek(j * tamreg, 0)
                pickle.dump(auxi, archlog_local)
                archlog_local.flush()

# Login de usuarios
def login():
    os.system('cls')
    intentos = 3
    while intentos > 0:
        usuario_mail = input(str("Ingrese su mail: "))
        clave = getpass.getpass("Ingrese su clave: ")
        pos, codUsuario = busca_usuario(usuario_mail)
        if pos == -1:
            print('El usuario y/o clave incorrectos. Intentos restantes ', intentos - 1)
            intentos -= 1
        else:
            archlog_usuario.seek(pos, 0)
            usuario = pickle.load(archlog_usuario)
            if usuario_mail.replace(" ", "") == usuario.nombreUsuario.replace(" ", "") and clave.replace(" ", "") == usuario.claveUsuario.replace(" ", ""):
                print('\n\nInicio de session exitoso. BIENVENIDO, ', usuario.nombreUsuario)
                print(' ')
                if usuario.tipoUsuario.replace(" ", "") == "administrador":
                    menu_administrador()
                    intentos = 0
                elif usuario.tipoUsuario.replace(" ", "") == "dueño":
                    menu_dueno_local(codUsuario)
                    intentos = 0
                elif usuario.tipoUsuario.replace(" ", "") == "cliente":
                    menu_cliente(codUsuario)
                    intentos = 0
                else:
                    print('El usuario y/o clave incorrectos. Intentos restantes ', intentos - 1)
                intentos -= 1
    if intentos == 0:
        print('Usted ha alcanzado la maxima cantidad de intentos. Volvera al menu principal')
        input()


# PROGRAMA PRINCIPAL
verifica_carpeta_trabajo()
archlog_usuario = existe_abre_usuario()
archlog_local = existe_abre_local()
archlog_promociones = existe_abre_prom()
archlog_prom_uso = existe_abre_prom_uso()
archlog_novedades = existe_abre_novedades()
os.system('cls')
opcion = -1
while opcion != 3:
    print("\n===  M E N U   P R I N C I P A L  ===\n")
    print("1- Ingresar con usuario registrado")
    print("2- Registrarse como cliente")
    print("3- Salir")
    #print("4- listado usuarios")
    #print("5- listado locales")
    #print("6- Listado Descuentos Vigentes")
    #print("7- Listado Uso de Promociones")
    opcion = int(input("\nSeleccione una opción: "))
    if 1 <= opcion < 4:
        if opcion == 1:
            print("\n\nIngresar como Usuario Registrado")
            login()
        elif opcion == 2:
            print("\n\nRegistrarse como Cliente")
            crea_clientes()
        elif opcion == 3:
            print("\n\nUsted esta abandonando el sistema. ¡Hasta luego!")
        #elif opcion == 4:
            #print("\n\nListado de usuario para chequeo general del sistema")
            #listar_usuario()
        #elif opcion == 5:
            #print("\n\nListado de locales para chequeo general del sistema")
            #reg_local = local()
            #archfis_local = 'C:\\tp3\\locales.dat'
            #tam = os.path.getsize(archfis_local)
            #if tam == 0:
            #    print('No hay locales registrados')
            #else:
            #     ordenarLocales()
            #listar_locales()
        #elif opcion == 6:
            #print("\n\nListado de Promociones para chequeo general del sistema")
            #listar_descuentos_vigentes()
        #elif opcion == 7:
            #print("\n\nListado de USO de Promociones")
            #listar_UsoPromociones()
    else:
        if opcion != 3:
            print("\nOpción no válida. Por favor, elija una opción válida.\n\n\n")
cerrar()