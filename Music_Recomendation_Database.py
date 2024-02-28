from collections import deque

class Album:
    def __init__(self, name, artist = None, year = None, length = None, genre = None, next_node = None):
        self.name = name
        self.artist = artist
        self.year = year
        self.length = length
        self.genre = genre
        self.children = []
    
    def display_info(self):
        print(
            f"""
            Album Name: {self.name}
            Artist: {self.artist}
            Year: {self.year}
            Length: {self.length} minutes
            """
        )
    
def bfs(root_node, goal_value):
    path_queue = deque()

    initial_path = [root_node]
    path_queue.appendleft(initial_path)

    while path_queue:
        current_path = path_queue.pop()
        current_node = current_path[-1]
    
        if root_node.name == goal_value:
            return root_node.children
    
        for child in root_node.children:
            node_found = bfs(child, goal_value)
        
            if node_found:
                return node_found
    return None
parent = Album("Parent")

rock = Album("rock")
Abbey_Road = Album("Abbey Road", "The Beatles", 1969, 47, "rock")
Nevermind = Album("Nevermind", "Nirvana", 1991, 42, "rock")
Roumors = Album("Rumours", "Fleetwood Mac", 1977, 39, "rock")

rap = Album("rap")
Illmatic = Album("Illmatic", "Nas", 1994, 39, "rap")
Straight_Outta_Compton = Album("Straight Outta Compton", "N.W.A.", 1988, 60, "rap")
Madvillainy = Album("Madvillainy", "Madvillain", 2004, 46, "rap")

country = Album("country")
Coat_of_Many_Colors = Album("Coat of Many Colors", "Dolly Parton", 1971, 27, "country")
Dreaming_My_Dreams = Album("Dreaming My Dreams", "Waylon Jennings", 1975, 31, "country")
Red_Headed_Stranger = Album("Red Headed Stranger", "Willie Nelson", 1975, 33, "country")

jazz = Album("jazz")
Kind_of_Blue = Album("Kind of Blue", "Miles Davis", 1959, 55, "jazz")
Mingus_Ah_Um = Album("Mingus Ah Um", "Charles Mingus", 1959, 72, "jazz")
A_Love_Supreme = Album("A Love Supreme", "John Coltrane", 1965, 32, "jazz")

rnb = Album("r&b")
The_Miseducation_of_Lauryn_Hill = Album("The Miseducation of Lauryn Hill", "Lauryn Hill", 1998, 77, "r&b")
Voodoo = Album("Voodoo", "D'Angelo", 2000, 78, "r&b")
Whats_Going_On = Album("What's Going On", "Marvin Gaye", 1971, 35, "r&b")

electronic = Album("electronic")
Homogenic = Album("Homogenic", "Bjork", 1997, 43, "electronic")
Dummy = Album("Dummy", "Portishead", 1994, 48, "electronic")
Discovery = Album("Discorvery", "Daft Punk", 2001, 60, "electronic")

folk = Album("folk")
Blue = Album("Blue", "Joni Mitchell", 1971, 35, "folk")
Pink_Moon = Album("Pink Moon", "Nick Drake", 1972, 26, "folk")
Bookends = Album("Bookends", "Simon and Garfunkel", 1968, 29, "folk")

funk = Album("funk")
Mothership_Connection = Album("Mothership Connection", "Parliament", 1975, 41, "funk")
Head_Hunters = Album("Head Hunters", "Herbie Hancock", 1973, 41, "funk")
Super_Fly = Album("Super Fly", "Curtis Mayfield", 1972, 43, "funk")

metal = Album("metal")
Paranoid = Album("Paranoid", "Black Sabbath", 1970, 41, "metal")
Master_of_Puppets = Album("Master of Puppets", "Metallica", 1986, 54, "metal")
Lateralus = Album("Lateralus", "Tool", 2001, 78, "metal")

parent.children = [rock, rap, country, jazz, rnb, electronic, folk, funk, metal]
rock.children = [Abbey_Road, Nevermind, Roumors]
rap.children = [Illmatic, Straight_Outta_Compton, Madvillainy]
country.children = [Coat_of_Many_Colors, Dreaming_My_Dreams, Red_Headed_Stranger]
jazz.children = [Kind_of_Blue, Mingus_Ah_Um, A_Love_Supreme]
rnb.children = [The_Miseducation_of_Lauryn_Hill, Voodoo, Whats_Going_On]
electronic.children = [Homogenic, Dummy, Discovery]
folk.children = [Blue, Pink_Moon, Bookends]
funk.children = [Mothership_Connection, Head_Hunters, Super_Fly]
metal.children = [Paranoid, Master_of_Puppets, Lateralus]

genre_list = ["rock", "rap", "country", "jazz", "r&b", "electronic", "folk", "funk", "metal"]

print("Welcome to Adam's album recomendation software: powered by AllMusic")
print("The genres we have available are: ")
for genre in genre_list:
    print(genre)

genre_rec = input("What genre are you interested in? ")
genre_rec_lower = genre_rec.lower()

if genre_rec_lower in genre_list:
    rec_list = bfs(parent, genre_rec_lower)
    for rec in rec_list:
        rec.display_info()
else:
    print("Sorry we don't have recommendations for that genre.")

search_again = input("Would you like another recommendation? y/n ")
while search_again == "y":
    genre_rec = input("What genre are you interested in? ")
    genre_rec_lower = genre_rec.lower()

    if genre_rec_lower in genre_list:
        rec_list = bfs(parent, genre_rec_lower)
        for rec in rec_list:
            rec.display_info()
    else:
        print("Sorry we don't have recommendations for that genre.")

    search_again = input("Would you like another recommendation? y/n ")

print("Thank you for using my album recommendation software. Please come again!")