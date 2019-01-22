from label_image import celestial_object
import wikipedia

print celestial_object
ans = "neptune"

if(ans == "spiral"):
    print("------------------------------------------------------")
    print("Spiral Galaxy : ")
    print("------------------------------------------------------")
    print(wikipedia.summary("Spiral Galaxy", sentences=2))
    #print(wikipedia.WikipediaPage(title = 'Spiral galaxy').summary)
elif(ans == "elliptical"):
    print("------------------------------------------------------")
    print("Elliptical Galaxy : ")
    print("------------------------------------------------------")
    print(wikipedia.summary("Elliptical galaxy", sentences=2))
    #print(wikipedia.WikipediaPage(title = 'Elliptical galaxy').summary)
elif(ans == "mercury"):
    print("------------------------------------------------------")
    print("Mercury Planet : ")
    print("------------------------------------------------------")
    print(wikipedia.summary("Mercury (planet)", sentences=2))
    #print(wikipedia.WikipediaPage(title = 'Mercury (planet)').summary)
elif(ans == "venus"):
    print("------------------------------------------------------")
    print("Venus Planet : ")
    print("------------------------------------------------------")
    print(wikipedia.summary("Venus", sentences=2))
    #print(wikipedia.WikipediaPage(title = 'Venus').summary)
elif(ans == "earth"):
    print("------------------------------------------------------")
    print("Earth Planet : ")
    print("------------------------------------------------------")
    print(wikipedia.summary("Earth", sentences=2))
    #print(wikipedia.WikipediaPage(title = 'Earth').summary)
elif(ans == "mars"):
    print("------------------------------------------------------")
    print("Mars Planet : ")
    print("------------------------------------------------------")
    print(wikipedia.summary("Mars", sentences=2))
    #print(wikipedia.WikipediaPage(title = 'Mars').summary)
elif(ans == "jupiter"):
    print("------------------------------------------------------")
    print("Jupiter Planet : ")
    print("------------------------------------------------------")
    print(wikipedia.summary("Jupiter", sentences=2))
    #print(wikipedia.WikipediaPage(title = 'Jupiter').summary)
elif(ans == "saturn"):
    print("------------------------------------------------------")
    print("Saturn Planet : ")
    print("------------------------------------------------------")
    print(wikipedia.summary("Saturn", sentences=2))
    #print(wikipedia.WikipediaPage(title = 'Saturn').summary)
elif(ans == "uranus"):
    print("------------------------------------------------------")
    print("Uranus Planet : ")
    print("------------------------------------------------------")
    print(wikipedia.summary("Uranus", sentences=2))
    #print(wikipedia.WikipediaPage(title = 'Uranus').summary)
elif(ans == "neptune"):
    print("------------------------------------------------------")
    print("Neptune Planet : ")
    print("------------------------------------------------------")
   # print(wikipedia.summary("Neptune", sentences=2))
    print(wikipedia.WikipediaPage(title = 'Neptune').summary)
