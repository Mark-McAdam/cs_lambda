# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon 
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name 
    def __str__(self):
        return(f"Waypoint is equal to: {self.name} lat: {self.lat} lon: {self.lon} ")

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, lat, lon, difficulty, size):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return (super().__str__()) + (f"Difficulty: {self.difficulty} Size: {self.size}") 
        # (f"Geocache is equal to: {self.name} lat: {self.lat} lon: {self.lon} ")


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
new_wpt = Waypoint("Catacombs", 41.70505, -121.51521)
print(new_wpt)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# print(waypoint)
new_wpt_str = new_wpt.__str__()
print(new_wpt_str)


# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
# self, name, lat, lon, difficulty, size
new_geo = Geocache("Newberry Views", 44.052137, -121.41556, 1.5, 2)
new_geo_str = new_geo.__str__()
print(new_geo_str)

# Print it--also make this print more nicely
# print(geocache)