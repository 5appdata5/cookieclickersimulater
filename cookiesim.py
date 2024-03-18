from decimal import Decimal
import matplotlib.pyplot as plt

baseClicks = 1
clicks = 1
cookies = 0
seconds = 0
cps = 0
buildings = [
    [0, Decimal('0.1'), 15,0],  # Cursor
    [0, Decimal('1'), 100,1],   # Grandma
    [0, Decimal('8'), 1100,2],  # Farm
    [0, Decimal('47'), 12000,3],  # Mine
    [0, Decimal('260'), 130000,4],  # Factory
    [0, Decimal('1400'), 1400000,5],  # Bank
    [0, Decimal('7800'), 20000000,6],  # Temple
    [0, Decimal('44000'), 330000000,7],  # Wizard Tower
    [0, Decimal('260000'), 5100000000,8],  # Shipment
    [0, Decimal('1600000'), 75000000000,9],  # Alchemy Lab
    [0, Decimal('10000000'), 1000000000000,10],  # Portal
    [0, Decimal('65000000'), 14000000000000,11], # Time Machine
    [0, Decimal('430000000'), 170000000000000,12]  # Antimatter Condenser
]

upgrades = [[
    100, 500, 10000, 100000, 10000000, 100000000, 1000000000,
    10000000000, 10000000000000, 10000000000000000, 10000000000000000000,
    10000000000000000000000, 10000000000000000000000000,
    10000000000000000000000000000, 10000000000000000000000000000000
],
[
    1000, 5000, 50000, 5000000, 500000000, 50000000000,
    5000000000000, 500000000000000, 50000000000000000,
    5000000000000000000, 500000000000000000000,
    50000000000000000000000, 5000000000000000000000000,
    500000000000000000000000000, 50000000000000000000000000000,
    5000000000000000000000000000000
],
[
    11000, 55000, 550000, 55000000, 5500000000, 550000000000,
    55000000000000, 5500000000000000, 550000000000000000,
    55000000000000000000, 5500000000000000000000,
    550000000000000000000000, 55000000000000000000000000,
    5500000000000000000000000000, 550000000000000000000000000000
],
[
    120000, 600000, 6000000, 600000000, 60000000000, 6000000000000,
    6000000000000000, 6000000000000000000, 6000000000000000000000,
    6000000000000000000000000, 6000000000000000000000000000,
    6000000000000000000000000000000, 6000000000000000000000000000000000,
    6000000000000000000000000000000000000, 6000000000000000000000000000000000000000
],
[
    1300000, 6500000, 65000000, 6500000000, 650000000000,
    65000000000000, 65000000000000000, 65000000000000000000,
    65000000000000000000000, 65000000000000000000000000,
    65000000000000000000000000000, 65000000000000000000000000000000,
    65000000000000000000000000000000000, 65000000000000000000000000000000000000,
    65000000000000000000000000000000000000000
],
[
    14000000, 70000000, 700000000, 70000000000, 7000000000000,
    700000000000000, 700000000000000000, 700000000000000000000,
    700000000000000000000000, 700000000000000000000000000,
    700000000000000000000000000000, 70000000000000000000000000000000,
    70000000000000000000000000000000000000, 70000000000000000000000000000000000000000000,
    70000000000000000000000000000000000000000000000
],
[
    200000000, 1000000000, 10000000000, 1000000000000, 100000000000000,
    10000000000000000, 10000000000000000000, 10000000000000000000000,
    10000000000000000000000000, 10000000000000000000000000000,
    10000000000000000000000000000000, 10000000000000000000000000000000000,
    10000000000000000000000000000000000000, 10000000000000000000000000000000000000000,
    10000000000000000000000000000000000000000000
],
[
    3300000000, 16500000000, 165000000000, 16500000000000, 1650000000000000,
    1650000000000000000, 1650000000000000000000, 1650000000000000000000000,
    1650000000000000000000000000, 1650000000000000000000000000000,
    1650000000000000000000000000000000, 1650000000000000000000000000000000000,
    1650000000000000000000000000000000000000, 1650000000000000000000000000000000000000000,
    1650000000000000000000000000000000000000000000
],
[
    51000000000, 255000000000, 255000000000000, 255000000000000000, 255000000000000000000,
    2550000000000000000000000, 2550000000000000000000000000, 2550000000000000000000000000000,
    2550000000000000000000000000000000, 2550000000000000000000000000000000000000,
    2550000000000000000000000000000000000000, 2550000000000000000000000000000000000000000000,
    2550000000000000000000000000000000000000000000000, 255000000000000000
],
[
    750e9,          # Antimony
    3.75e12,        # Essence of dough
    37.5e12,        # True chocolate
    3.75e15,        # Ambrosia
    375e15,         # Aqua crustulae
    37.5e18,        # Origin crucible
    37.5e21,        # Theory of atomic fluidity
    37.5e24,        # Beige goo
    37.5e27,        # The advent of chemistry
    37.5e30,        # On second thought
    375e33,         # Public betterment
    3.75e36,        # Hermetic reconciliation
    37.5e39,        # Chromatic cycling
    375e42,         # Arcanized glassware
    3.75e48         # The dose makes the poison
],
[
    10e12,          # Ancient tablet
    50e12,          # Insane oatling workers
    500e12,         # Soul bond
    50e15,          # Sanity dance
    5e18,           # Brane transplant
    500e18,         # Deity-sized portals
    500e21,         # End of times back-up plan
    500e24,         # Maddening chants
    500e27,         # The real world
    500e30,         # Dimensional garbage gulper
    5e33,           # Embedded microportals
    50e33,          # His advent
    500e36,         # Domestic rifts
    5e48,           # Portal guns
    50e48           # A way home
],
[
    140e12,         # Flux capacitors
    700e12,         # Time paradox resolver
    7e15,           # Quantum conundrum
    700e15,         # Causality enforcer
    70e18,          # Yestermorrow comparators
    7e21,           # Far future enactment
    7e24,           # Great loop hypothesis
    7e27,           # Cookietopian moments of maybe
    7e30,           # Second seconds
    7e33,           # Additional clock hands
    70e36,          # Nostalgia
    700e36,         # Split seconds
    7e48,           # Patience abolished
    70e48,          # Timeproof upholstery
    700e48          # Rectifying a mistake
],
[
    1.7e15,          # Sugar bosons
    8.5e15,          # String theory
    85e15,           # Large macaron collider
    8.5e18,          # Big bang bake
    850e18,          # Reverse cyclotrons
    85e21,           # Nanocosmics
    85e24,           # The Pulse
    85e27,           # Some other super-tiny fundamental particle? Probably?
    85e30,           # Quantum comb
    85e33,           # Baking Nobel prize
    850e33,          # The definite molecule
    8.5e36,          # Flavor itself
    85e39,           # Delicious pull
    850e39,          # Employee minification
    8.5e45           # Candied atoms
]
]
upgradepower = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
goal = 10**15
cookiesgraph =[0]
time = [0]


def dreamBuilding():
    global buildings
    currentdreamcps = 0
    currentdream = None
    for b in buildings:
        buildingprice = Decimal(b[2]) * Decimal('1.15') ** b[0]
        if b[1]/buildingprice > currentdreamcps:
            currentdreamcps = b[1] / b[2]
            currentdream = b
    return currentdream

def buyBuilding(building):
    global cookies
    if cookies >= building[2]:
        building[0] += 1
        cookies -= building[2]

def dreamUpgrade():
    global upgrades
    global buildings
    currentdreamcps = 0
    currentdream = None
    for u in range(0,len(upgrades)):
        upgradePrice = upgrades[u][0]
        newdream = (buildings[u][0]*buildings[u][2])*upgradepower[u]/upgradePrice
        if newdream > currentdreamcps:
            currentdreamcps = newdream
            currentdream = u
        if newdream != 0:
            return u

def buyUpgrade(u):
    global cookies
    if u != None:
        if cookies >= upgrades[u][0]:
            upgradepower[u] += 1
            cookies -= upgrades[u][0]
            del upgrades[u][0]

while cookies < goal:
    for b in buildings:
        cps += b[0] * b[2]
    cookies += clicks * 125
    cookies += cps
    seconds += 1
    cps = 0
    buyUpgrade(dreamUpgrade())
    buyBuilding(dreamBuilding())
    
    cookiesgraph.append(int(cookies))
    time.append(seconds)
cookiesgraph.append(int(cookies))
time.append(seconds)
print(seconds/60)


plt.plot(time, cookiesgraph)
plt.xlabel('Time (seconds)')
plt.ylabel('Cookies')
plt.title('Cookies Over Time')
plt.show()
