import csv
from max_temp_mes import MaxTempPorMes  # importa tu clase MRJob

def guardar_resultados(input_path, output_csv):
    job = MaxTempPorMes(args=[input_path])
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Mes', 'MaxTemp'])  # cabecera del CSV

        with job.make_runner() as runner:
            runner.run()
            for key, value in job.parse_output(runner.cat_output()):
                writer.writerow([key, value])

if __name__ == '__main__':
    entrada = '../datos/entrada/datos_clima_medellin_2024.csv'  # ruta a tu archivo de entrada
    salida = '../datos/salida/max_temp_mes.csv'  # ruta donde guardarás el CSV con resultados
    guardar_resultados(entrada, salida)
    print(f'Resultados guardados en {salida}')
