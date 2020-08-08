# change the name of the 5th planet in planets
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'X', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
# planets[4] = 'Jupiter'
for planet in planets:
    if planet=='X':
        planets[planets.index('X')] = 'Jupiter'
        print("We believe it's",planets[4])


