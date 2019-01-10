planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")

outer_planet_list = ["Neptune", "Uranus"]
planet_list.extend(outer_planet_list)

planet_list.append("pluto")

planet_list.insert(1, "Earth")
planet_list.insert(1, "Venus")

rocky_planets = planet_list[0:4]

del(planet_list[8])


expeditions = [
    ("Cassini", "Saturn"),
    ("Voyager 1", "Neptune" ),
    ("New Horizons", "Pluto"),
    ("Juno", "Jupiter")
]

for planet in planet_list:
    visitors = []
    for expedition in expeditions:
        if expedition[1] == planet:
            visitors.append(expedition[0])
    print("{0} has been visited by {1}".format(planet, (', ').join(visitors)))
