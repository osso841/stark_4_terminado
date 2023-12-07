from typing import Union
import re
#-------------------------------------------------------------------------
#PUNTO 1.1 
def extraer_iniciales(nombre_heroe:str) -> Union[str, bool]:
    ''' funcion que toma el nombre de un heroe y devuelve sus iniciales.
        param:
            nombre_heroe (str): el nombre del heroe
        return:
            str: iniciales del heroe
    '''
    try:
        nombre_heroe = re.sub('-', ' ', nombre_heroe)
        nombre_heroe = re.sub('the', '', nombre_heroe)

        lista_iniciales = re.findall("([A-Za-z])[A-Za-z]+" ,nombre_heroe)
        iniciales = '.'.join(lista_iniciales) + '.'
        iniciales = iniciales.upper()

        if len(nombre_heroe) == 0:
            iniciales = 'N/A'

    except TypeError as e:
        print(f'tipo de dato invalido. verificar: {e}')
        iniciales = None
    except Exception as e:
        print(f'error: {e}')
        iniciales = None
        
    return iniciales


#PUNTO 1.2
def obtener_dato_formato(dato:str) -> Union[str, bool]:
    ''' formatea un dato eliminando parentesis y convirtiendo a minusculas
        param:
            -dato (str): el dato a formatear

        Return:
            str: El dato formateado en formato snake_case.
            bool: False si el tipo de dato no es String
    '''
    if type(dato) == str:
        dato = dato.lower()
        dato = re.sub('\(.*?\)', '', dato)
        lista_dato = re.findall('[a-z]+', dato)
        dato_formateado = '_'.join(lista_dato)
    else:
        dato_formateado = False

    return dato_formateado


#PUNTO 1.3
def stark_imprimir_nombre_con_iniciales(nombre_heroe:str) -> bool:
    ''' imprime el nombre del heroe con iniciales y formato especifico
        param:
            nombre_heroe (str): el nombre del héroe.

        Return:
            bool: True si la operacion fue exitosa, Fase si el tipo de dato de entrada no es valido.

    '''

    if type(nombre_heroe) == str:
        dato_nombre =f'*{obtener_dato_formato(nombre_heroe)} ({extraer_iniciales(nombre_heroe)})'
        print(dato_nombre)
        retorno = True
    else:
        print('dato incorrecto, se espera un valor de tipo str.')
        retorno = False

    return retorno


#PUNTO 1.4
def stark_imprimir_nombres_con_iniciales(lista_heroes:list[dict]) -> bool:
    ''' Imprime los nombres de los héroes con iniciales y formato específico.

        Parámetros:
            - lista_heroes (list[dict]): Una lista de diccionarios que contienen información sobre los héroes.

        Retorna:
            - bool: True si la operación fue exitosa, False si la lista de héroes no es válida o está vacía.
    '''
    estado = False

    if lista_heroes and type(lista_heroes) == list:
        for personaje in lista_heroes:
            stark_imprimir_nombre_con_iniciales(personaje['nombre'])
        estado = True

    return estado  


#-------------------------------------------------------------------------

#PUNTO 2.1
def generar_codigo_heroe(diccionario_heroe:dict, id:int) -> Union[str, bool]:
    """Genera un código único para un héroe basado en su género y número de identificación.

        Param:
        - diccionario_heroe (dict): Un diccionario que contiene información sobre el héroe, incluido el género.
        - id (int): El número de identificación único del héroe.

        Retorna:
        - str: El código único del héroe, o "N/A" si no se puede generar un código válido.
        - bool: False si se ingresa un dato invalido
    """
    lista_generos = ['NB', 'M', 'F']
    if diccionario_heroe['genero'] and diccionario_heroe['genero'] in lista_generos:
        genero = diccionario_heroe['genero']
        match genero:
            case "M":
                codigo = "1"
            case "F":
                codigo = "2"
            case _:
                codigo = "0"
        id_str = str(id)
        
        codigo_heroe = f"{genero}-{codigo}{id_str.zfill(10-len(genero)-len(codigo)-1)}"
    else:
        codigo_heroe = "N/A"

    return codigo_heroe

#PUNTO 2.2
def stark_generar_codigos_heroes(lista_heroes:list[dict]) -> Union[str, bool]:
    """
        Genera códigos únicos para una lista de héroes.

        Parámetros:
            lista_heroes (list): Una lista que contiene diccionarios con información sobre cada héroe.

        Retorna:
            str: Un mensaje con los códigos generados y la información de los héroes, o "False" si hay un error.
    """
    validacion = True
    if lista_heroes:
        for personaje in lista_heroes:
            if type(personaje) != dict:
                validacion = False
    else:
        validacion = False

    if validacion:
        mensaje = ''
        for posicion in range(len(lista_heroes)):
            codigo_heroe = generar_codigo_heroe(lista_heroes[posicion], posicion+1)
            formato_heroe = obtener_dato_formato(lista_heroes[posicion]['nombre'])
            iniciales_heroes = extraer_iniciales(lista_heroes[posicion]['nombre'])
            mensaje += f"*{formato_heroe} ({iniciales_heroes}) | {codigo_heroe} \n"

        mensaje += f"se asignaron {len(lista_heroes)} codigos"
    else:
        mensaje = False

    return mensaje

#-------------------------------------------------------------------------

#PUNTO 3.1
def sanitizar_entero(numero_str:str) -> int:
    """
    Convierte una cadena a un entero después de realizar la sanitización.

    Parámetros:
    - numero_str (str): Cadena que se intentará convertir a un entero.

    Retorna:
    - int: El entero resultante después de la sanitización.
           -3 si el parámetro no es una cadena.
           -2 si el parámetro es una cadena que representa un número entero negativo.
           -1 si el parámetro no es una cadena que representa un número entero válido.
    """

    if type(numero_str) != str:
        numero_retorno = -3
    else:    
        numero_str = numero_str.strip()
        if numero_str.isdigit():
            numero_retorno = int(numero_str)

        elif numero_str[0] == "-" and numero_str[1:len(numero_str)].isdigit():
            numero_retorno = -2

        else:
            numero_retorno = -1

    return numero_retorno


#PUNTO 3.2
def sanitizar_flotante(numero_str:str) -> float:
    """
        Convierte una cadena a un número de punto flotante después de realizar la sanitización.

        Parámetros:
            - numero_str (str): Cadena que se intentará convertir a un número de punto flotante.

        Retorna:
            - float: El número de punto flotante resultante después de la sanitización.
                -3 si el parámetro no es una cadena.
                -2 si el parámetro es una cadena que representa un número de punto flotante negativo.
                -1 si el parámetro no es una cadena que representa un número de punto flotante válido.
    """

    if type(numero_str) != str:
        numero_retorno = -3
    else:
        numero_str = numero_str.strip()
        patron_decimal = "^-?\d+(\.\d+)?$"
        if re.match(patron_decimal, numero_str):
            if numero_str[0] == "-":
                numero_retorno = -2
            else:
                numero_retorno = float(numero_str)
        else:
            numero_retorno = -1
    
    return  numero_retorno


#PUNTO 3.3
def sanitizar_string(valor_str:str, valor_por_defecto='-'):
    """
        Realiza la sanitización de una cadena de texto según ciertas reglas.

        Param:
        - valor_str (str): Cadena de texto que se va a sanitizar.
        - valor_por_defecto (str):  Valor por defecto a utilizar si la cadena está vacía.
                                    (opcional, por defecto es '-')

        Retorna:
        - str: La cadena de texto resultante después de la sanitización.
            Si la cadena contiene dígitos, retorna "N/A".
            Si la cadena está vacía y se proporciona un valor por defecto, retorna el valor por defecto en minúsculas.
            Si la cadena contiene "/", reemplaza "/" con un espacio.
            Si la cadena contiene solo letras, retorna la cadena en minúsculas.
    """
    valor_retorno = valor_str.strip()

    if any(letra.isdigit() for letra in valor_retorno):
        valor_retorno = "N/A"
    else:
        if not valor_retorno:
            valor_retorno = valor_por_defecto.strip()
            valor_retorno = valor_retorno.lower()
        else:
            if any(letra == '/' for letra in valor_retorno):
                valor_retorno = re.sub('/', ' ', valor_retorno)

            patron_texto = "^[A-Za-z]+$"
            if re.match(patron_texto, valor_retorno):
                valor_retorno = valor_retorno.lower()

    return valor_retorno


# PUNTO 3.4
def sanitizar_dato(heroe:dict, clave:str, tipo_dato:str):
    """
    Realiza la sanitización de un dato específico en el diccionario de un héroe.

    Parámetros:
        heroe (dict): Diccionario que representa al héroe.
        clave (str): Clave del diccionario que se va a sanitizar.
        tipo_dato (str): Tipo de dato al que se quiere convertir ('string', 'entero' o 'flotante').

    Retorna:
        bool: True si la sanitización fue exitosa, False en caso contrario.
    """
    valores_esperado = ['string', 'entero', 'flotante']
    valor_retorno = False

    if tipo_dato.lower() in valores_esperado:
        if clave in heroe.keys():
            if tipo_dato == valores_esperado[0]:
                heroe[clave] = sanitizar_string(heroe[clave])
                valor_retorno = True
            elif tipo_dato == valores_esperado[1] and type(heroe[clave]) != int:
                heroe[clave] = sanitizar_entero(heroe[clave])
                valor_retorno = True
            elif tipo_dato == valores_esperado[2] and type(heroe[clave]) != float:
                heroe[clave] = sanitizar_flotante(heroe[clave])
                valor_retorno = True
        else:
            print('la clave especificada no existe en el heroe')
    else:
        print('Tipo de dato no reconococido')

    return valor_retorno


# PUNTO 3.5
def stark_normalizar_datos(lista_heroes:list):
    """
        Normaliza los datos de una lista de héroes según ciertas claves y tipos de datos predefinidos.

        Parámetros:
        - lista_heroes (list): Lista de diccionarios que representan a los héroes.

        Retorna:
        - list: Lista de héroes con datos normalizados.
    """
    claves_normalizar = {'altura':'flotante',
                         'peso':'flotante',
                         'color_ojos':'string',
                         'color_pelo':'string',
                         'fuerza':'entero',
                         'inteligencia':'string'}
    if lista_heroes:
        for personaje in lista_heroes:
            for clave, tipo_dato in claves_normalizar.items():
                sanitizar_dato(personaje, clave, tipo_dato)
        print("datos_normalizados")
    else:
        print("error: Lista de heroes vacia")

        

#-------------------------------------------------------------------------

# PUNTO 4.1
def stark_imprimir_indice_nombre(lista_heroes:list):
    """
        Imprime un índice formado por los nombres de los héroes en una lista.

        param:
            - lista_heroes (list): Lista de diccionarios que representan a los héroes.

        return:
            - str: Índice formado por los nombres de los héroes.
    """
    lista_nombres = []
    mensaje_aux = ''
    patron_exclusion = ' (the) '

    for personaje in lista_heroes:
        mensaje_aux = personaje['nombre']
        mensaje_aux = re.sub(patron_exclusion, ' ', mensaje_aux)
        mensaje_aux = re.sub(' ', '-', mensaje_aux)
        lista_nombres.append(mensaje_aux)

    mensaje_salida = '-'.join(lista_nombres)
    print(mensaje_salida)

#-------------------------------------------------------------------------

#PUNTO 5.1
def generar_separador(patron:str, largo:int, imprimir=True):
    """
        Genera un patrón repetitivo y opcionalmente lo imprime.

        Param:
        - patron (str): Carácter o patrón a repetir.
        - largo (int): Número de veces que se repetirá el patrón.
        - imprimir (bool): Indica si se imprimirá el patrón generado (predeterminado: True).

        Return:
        - str: Patrón generado.
    """
    if len(patron) <=2 and len(patron) >= 1 and largo > 0 and largo <= 235:
        patron_generado = patron*largo
    else:
        patron_generado = "N/A"

    if imprimir:
            print(patron_generado)

    return patron_generado

#PUNTO 5.2
def generar_encabezado(titulo:str):
    """
    Genera un encabezado con un título centrado y rodeado por un patrón de separación.

    Parámetros:
    - titulo (str): Título del encabezado.

    Retorna:
    - str: Encabezado generado.
    """
    encabezado = generar_separador('*',70, False) + '\n'
    encabezado += '\t\t' + titulo.upper() + '\n'
    encabezado += generar_separador('*', 70, False) + '\n'

    return encabezado


#PUNTO 5.3
def imprimir_ficha_heroes(heroe:dict, id:int):
    """
        Imprime la ficha de un héroe con información específica.

        Param:
        - heroe (dict): Diccionario con la información del héroe.
        - id (int): Identificador del héroe.
    """

    id += 1
    ficha_heroes = generar_encabezado("principal")
    ficha_heroes += f'NOMBRE DEL HEROE:\t{obtener_dato_formato(heroe["nombre"])} ({extraer_iniciales(heroe["nombre"])})\n'
    ficha_heroes += f'IDENTIDAD SECRETA:\t{obtener_dato_formato(heroe["identidad"])}\n'
    ficha_heroes += f'CONSULTORA:\t{obtener_dato_formato(heroe["empresa"])}\n'
    ficha_heroes += f'CODIGO DE HEROE:\t{generar_codigo_heroe(heroe, id)}\n'
    ficha_heroes += generar_encabezado("fisico")
    ficha_heroes += f'ALTURA: \t{heroe["altura"]} CM\n'
    ficha_heroes += f'PESO: \t{heroe["peso"]} kg.\n'
    ficha_heroes += f'FUERZA: \t{heroe["fuerza"]} N.\n'
    ficha_heroes += generar_encabezado("SEÑAS PARTICULARES")
    ficha_heroes += f'COLOR DE OJOS: \t{heroe["color_ojos"]}\n'
    ficha_heroes += f'COLOR DE PELO: \t{heroe["color_pelo"]}\n'
    print(ficha_heroes)


#PUNTO 5.5
def stark_navegar_fichas(lista_heroes:list):
    """
        Navega por las fichas de héroes en una lista.

        Parámetros:
        - lista_heroes (list): Lista de héroes.
    """
    posicion = 0
    while True:
        imprimir_ficha_heroes(lista_heroes[posicion], posicion)
        print('[1] IR A LA IZQUIERDA', '[2] IR A LA DERECHA', '[3] SALIR\n')
        opcion = input('ingrese una opcion: ')

        if opcion.isdigit():
            opcion = int(opcion)

        match opcion:
            case 1:
                posicion -= 1
                if posicion < 0:
                    posicion = len(lista_heroes) - 1
            case 2:
                posicion += 1
                if posicion > len(lista_heroes) - 1:
                    posicion = 0
            case 3:
                break

#-------------------------------------------------------------------------

#PUNTO 6.0
def imprimir_menu_principal():
    '''
    Imprime el menú principal del programa.

    El menú incluye opciones para realizar diversas acciones en el sistema.
    '''
    menu_principal = generar_encabezado('MI MENU PRINCIPAL')
    menu_principal +='1- imprimir la lista de nombres junto con sus iniciales\n'
    menu_principal +='2- imprimir la lista de nombres y el codigo del mismo\n'
    menu_principal +='3- Normalizar datos\n'
    menu_principal +='4- imprimir indice de nombres\n'
    menu_principal +='5- Navergar fichas\n'
    menu_principal +='6- Salir\n'

    print(menu_principal)


def stark_app_4(lista_heroes:list):
    """
    Aplicación principal del programa para gestionar datos de héroes.

    La función utiliza un menú principal para ofrecer diversas opciones de interacción
    con la lista de héroes proporcionada.

    Opciones:
    1. Imprimir la lista de nombres junto con sus iniciales.
    2. Imprimir la lista de nombres y el código del héroe.
    3. Normalizar datos.
    4. Imprimir índice de nombres.
    5. Navegar fichas.
    6. Salir.

    Parámetros:
    - lista_heroes (list): Lista de diccionarios que representan a los héroes.

    """

    while True:
        imprimir_menu_principal()

        opcion = input('elija una opcion: ')
        if opcion.isdigit():
            opcion = int(opcion)

        match opcion:
            case 1:
                cadena_nombre_iniciales = stark_imprimir_nombres_con_iniciales(lista_heroes)
                if cadena_nombre_iniciales:
                    print('datos cargados correctamente')
                else:
                    print('hubo un error en la carga. revisar!!!')
            case 2:
                nombre_codigos_personajes = stark_generar_codigos_heroes(lista_heroes)
                if nombre_codigos_personajes:
                    print(nombre_codigos_personajes)
                else:
                    print('error en asignacion de codigos')
            case 3:
                stark_normalizar_datos(lista_heroes)
            case 4:
                stark_imprimir_indice_nombre(lista_heroes)
            case 5:
                stark_navegar_fichas(lista_heroes)
            case 6: 
                break