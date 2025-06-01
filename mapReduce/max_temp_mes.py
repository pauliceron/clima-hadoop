from mrjob.job import MRJob
from mrjob.step import MRStep
import csv
from datetime import datetime

class MaxTempPorMes(MRJob):

    def mapper(self, _, line):
        try:
            row = next(csv.reader([line]))
            if row[0] == "date":
                return
            fecha = datetime.strptime(row[0], "%Y-%m-%d")
            mes = fecha.strftime("%Y-%m")
            maxtemp = float(row[1])
            yield mes, (maxtemp, 1)
        except:
            pass

    def reducer(self, mes, valores):
        total_temp = 0
        count = 0
        for temp, c in valores:
            total_temp += temp
            count += c
        yield mes, round(total_temp / count, 2)

if __name__ == '__main__':
    MaxTempPorMes.run()
