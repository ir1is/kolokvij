import projectile_drop as pd

objekt1 = pd.ProjectileDrop()
objekt2 = pd.ProjectileDrop()

objekt1.init(2000,200)
# print(objekt1.visina(15))
# print(objekt1.akceleracija(2))

objekt2.init(10,5)
# print(objekt2.visina(3))
# print(objekt2.akceleracija(3))

objekt1.fall()
