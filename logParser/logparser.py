#!/usr/bin/env python3

from collections import defaultdict


class logParse:
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.lines = []

    def parse(self):
        for line in self.file:
            self.lines.append(line.strip().split())
        return self.lines

    def getTopIps(self):
        ipList = defaultdict(int)
        for line in self.parse():
            ipList[line[0]] += 1
        return sorted(ipList.items(), key=lambda line: line[1], reverse=True)


    def getAvgPageSize(self):
        sizeList = []
        for line in self.parse():
            sizeList.append(int(line[6]))
        return round(sum(sizeList) / len(sizeList), 2)


    def getErrorRate(self):
        returnCodes = []
        numberrs = 0
        for line in self.parse():
            returnCodes.append(int(line[5]))
            if int(line[5]) != 200:
                numberrs += 1
        return (round(float(numberrs / len(returnCodes) * 100), 2))



if __name__ == "__main__":
  r = logParse('./input1.txt')
  print(f'Top 3 IPs:')
  for x, y in enumerate(r.getTopIps()):
      if x < 3:
        print(f'Count: {y[1]}, IP: {y[0]}')

  print(f'Average Page Size: {r.getAvgPageSize()}')
  print(f'Error Rate: {r.getErrorRate()}%')