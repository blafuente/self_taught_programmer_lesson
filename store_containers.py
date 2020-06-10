#Example of storing a container within a containger
locations = []

la = (34.0522, 1888.2437)
chicago = (41.8781, 87.6298)

locations.append(la)
locations.append(chicago)

print(locations)

eights = ["Edgar Allen Poe", "Charles Dickens"]

nines = [
    "Hemingway",
    "Fitzgerald",
    "Orwell",
    "Sinclair"
]
authors = (eights,nines)
print(authors[0])
print(authors[1])
print(authors[1][3])

# Although a tuble can be only used as a key in a dictionary
# Any container can be a value in a dictionary
# A dictionary with a tuple, list, and dictionary
ny = {
    "location" : (40.7128, 74.0059), # tuple

    "celebs" : [ "W. Allen", "Jay Z","K. Bacon"], # list

    # dictionary
    "facts" : { 
        "state" : "NY",
        "country" : "America"
    }
}
