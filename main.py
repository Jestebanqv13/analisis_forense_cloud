
# main

from modulo_autenticacion import autenticador
from modulo_recopilar_datos import recolectar_datos
from modulo_analisis import analizar_actividad
from modulo_reporte import generar_reporte


def main():
    # Autenticación
    token_auth = autenticador()

    # Recopilacion de datos
    datos = recolectar_datos(token_auth)

    # Analisis de actividad
    resultado_analisis = analizar_actividad(datos)

    # Generacion de informes
    generar_reporte(resultado_analisis)


if __name__ == "__main__":

    main()
