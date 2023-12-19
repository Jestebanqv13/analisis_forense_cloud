def generar_informe(resultados_analisis):
   # Acá debemos de implementar una biblioteca que nos ayude con el reporte
    informe = "Informe Forense:\n"

    for categoria, resultado in resultados_analisis.items():

        informe += f"\nCategoría: {categoria}\n"
        informe += f"Resultado: {resultado}\n"

    return informe
