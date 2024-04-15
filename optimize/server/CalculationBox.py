import random
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def calculateFunction(T1, T2):
  a = 1
  b = 1
  y = 1
  A1 = 2
  A2 = 2
  V1 = 9
  V2 = 10
  t = 8
  return (a * (T2 - T1)**A1 + b * 1 / V1 * (T1 + T2 - y - V2)**A2) * t

class PointOpt:
  def __init__(self, x1, x2):
    self.T1 = x1
    self.T2 = x2
    self.F = calculateFunction(x1, x2)
    self.IsCorrect = self.secondKindCheck(x1, x2)

  # Функция проверки условий 2 рода
  def secondKindCheck(self, T1, T2):
    T1T2 = 12.00
    return (T2 + T1) <= T1T2

  # Функция смещения незафиксированных вершин к центру фиксированных точек комплекса
  def changePointToCorrect(correctPoints, changePoints):  
    x1 = changePoints.T1
    x2 = changePoints.T2

    sumX1 = 0
    sumX2 = 0

    for i in range(len(correctPoints)):
      sumX1 += correctPoints[i].T1
      # print(sumX1)
      sumX2 += correctPoints[i].T2

    while not(x1 + x2 <= 12):
      x1 = 0.5 * (x1 + (sumX1 / len(correctPoints)))
      x2 = 0.5 * (x2 + (sumX2 / len(correctPoints)))

    return PointOpt(x1, x2)

  # Функция смещения точки к центру, смещение на половину расстояния
  def changePointToCorrectByHalf(Cx1, Cx2, newPoint):
    x1 = newPoint.T1
    x2 = newPoint.T2

    while not(x1 + x2 <= 12):
      x1 = 0.5 * (x1 + Cx1)
      x2 = 0.5 * (x2 + Cx2)

    return PointOpt(x1, x2)

  # Функция смещения точки к наилучшей, на половину расстояния
  def moveToBestPoint(correctPoint, goodPoint, badValue):
    x1 = correctPoint.T1
    x2 = correctPoint.T2
    value = correctPoint.F

    while value <= badValue:
      x1 = 0.5 * (x1 + goodPoint.T1)
      x2 = 0.5 * (x2 + goodPoint.T2)
      value = calculateFunction(x1, x2)

    return PointOpt(x1, x2)

start_time = datetime.now()

n = 8 # Число независимых пременных
EPS = 0.01 # заданная точность вычисления
N_POINTS = 1 + n # Размер комплекса
# Условия 1 рода
LOW = -3.00
UP = 14.00

box = list() # список 

# Функция формирования стартового комплекса
def doStartComplex(g, h):    
  points = []
  # Формирование исходного комплекса
  for i in range(1, N_POINTS+1):
    x1 = g + random.random() * (h - g)
    x2 = g + random.random() * (h - g)
    points.append(PointOpt(x1, x2))

  # Создание массивов фиксированных и нефиксированных точек
  GoodPoints = []
  BadPoints = []

  # Фиксация точек удовлетворяющих всем условиям
  for i in range(len(points)):
    point = points[i]
    if point.IsCorrect == True:
      GoodPoints.append(point)
    else: BadPoints.append(point)

  # Смещение незафиксированных точек к центру
  if len(BadPoints) != 0:
    for point in BadPoints:
      newPoint = PointOpt.changePointToCorrect(GoodPoints, point)
      GoodPoints.append(newPoint)
  return GoodPoints

# Основная функция алгоритма
def solveBox():
  box = []
  # Получение точек стартового комплекса
  points = doStartComplex(LOW, UP)
  count = 0

  while count < 10000:
    # Сортировка точек
    points = sorted(points, key=lambda pointOpt: pointOpt.F) 
    for point in points:
      if point.T1 + point.T2 <= 12:
        box.append(point) 

    # Поиск координат центра с отброшенной наихудшей вершиной
    sum1 = sum(i.T1 for i in points) - points[0].T1
    sum2 = sum(i.T2 for i in points) - points[0].T2
    Ct1 = sum1 / (N_POINTS - 1)
    Ct2 = sum2 / (N_POINTS - 1)

    # Расчет расстояния от наихудшей и наилучшей вершин до центра комплекса
    B = ((abs(Ct1 - points[-1].T1) + abs(Ct1 - points[0].T1)) + (abs(Ct2 - points[-1].T2) + abs(Ct2 - points[0].T2))) / (2 * n)

    # Проверка условий остановки, если среднее расстояние 
    # от наихудшей и наилучшей вершин от центра комплекса
    # меньше заданного числа, то поиск останавливается
    if EPS > B:
      return points[-1]

    count += 1

    # Вычисление координат новой точки взамен наихудшей
    newT1 = 2.3 * Ct1 - 1.3 * points[0].T1
    newT2 = 2.3 * Ct2 - 1.3 * points[0].T2

    # Проверка условий 1 рода для новой точки,
    # если они нарушаются то новая точка принмает значение
    # х+е/х-е и у+е/у-е соответственно
    if newT1 > UP: newT1 = UP - EPS
    if newT1 < LOW: newT1 = LOW + EPS
    if newT2 > UP: newT2 = UP - EPS
    if newT2 < LOW: newT2 = LOW + EPS

    # Проверка условий 2 рода для новой точки
    newPoint = PointOpt(newT1, newT2)
    if not(newPoint.IsCorrect == True):
      newPoint = PointOpt.changePointToCorrectByHalf(Ct1, Ct2, newPoint)

    # Если новая точка хуже наихудшей, то смещаеем ее на половину расстояния к лучшей из вершин
    if newPoint.F <= points[0].F:
      newPoint = PointOpt.moveToBestPoint(newPoint, points[-1], points[0].F);
    points[0] = newPoint;

def main():
  calculationResult = solveBox()
  maxFunction_Box = round(calculationResult.F, 2)
  T1_Box = round(calculationResult.T1, 2)
  T2_Box = round(calculationResult.T2, 2)

  calculationTime = datetime.now() - start_time
  microseconds_Box = calculationTime.microseconds

  fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize =(8, 10))
  X = np.linspace(LOW, UP, 60)
  Y = np.linspace(LOW, UP, 60)
  x, y = np.meshgrid(X, Y)
  z = ((y - x)**2 + 1 / 9 * (x + y - 10)**2) * 8
  
  ax.plot_surface(x, y, z, cmap='PRGn', cstride=1, rstride=1, edgecolor = 'mediumpurple', linewidth = 0.1, alpha=0.8)
  
  ax.scatter(T1_Box, T2_Box, maxFunction_Box, color = 'crimson', marker='o', zorder=1)
  ax.view_init(20, 80)
  fig.savefig('Box.png', dpi=fig.dpi)
  open('Box.png','rb+')

  return [T1_Box, T2_Box, maxFunction_Box, microseconds_Box]


