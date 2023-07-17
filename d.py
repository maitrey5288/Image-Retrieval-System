'''
this file is for testing

'''




from fuzzywuzzy import fuzz
from fuzzywuzzy import process
  
s1 = '''The Solar System[c] is the gravitationally bound system of the Sun and the objects that orbit the star. The largest of such objects are the eight planets, in order from the Sun: four terrestrial planets named Mercury, Venus, Earth and Mars, two gas giants named Jupiter and Saturn, and two ice giants named Uranus and Neptune. The terrestrial planets have a definite surface and are mostly made of rock and metal. The gas giants are mostly made of hydrogen and helium, while the ice giants are mostly made of 'volatile' substances such as water, ammonia, and methane. In some texts, these terrestrial and giant planets are called the inner Solar System and outer Solar System planets respectively.

The Solar System was formed 4.6 billion years ago from the gravitational collapse of a giant interstellar molecular cloud. Over time, the cloud formed the Sun and a protoplanetary disk that gradually coalesced to form planets and other objects. That is the reason why all eight planets have an orbit that lies near the same plane. In the present day, 99.86% of the Solar System's mass is in the Sun and most of the remaining mass is contained in the planet Jupiter. Six planets, six largest possible dwarf planets and many other bodies have natural satellites or moons orbiting around them. All giant planets and a few smaller bodies are encircled by planetary rings, composed of ice, dust and sometimes moonlets.

There are an unknown number of smaller dwarf planets and innumerable small bodies orbiting the Sun.[d] These objects are distributed in the asteroid belt that lies between the orbits of Mars and Jupiter, the Kuiper belt, the scattered disc that both lies beyond Neptune's orbit and at even further reaches of the Solar System which they would be classified as an extreme trans-Neptunian object. There is consensus among astronomers to these nine objects as dwarf planets: the asteroid Ceres, the Kuiper-belt objects Pluto, Orcus, Haumea, Quaoar, and Makemake, and the scattered-disc objects Gonggong, Eris, and Sedna.[d] Many small-body populations, including comets, centaurs and interplanetary dust clouds, freely travel between the regions of the Solar System.

The solar wind, a stream of charged particles flowing outwards from the Sun, creates a bubble-like region of the interplanetary medium in the interstellar medium known as the heliosphere. The heliopause is the point at which pressure from the solar wind is equal to the opposing pressure of the interstellar medium; it extends out to the edge of the scattered disc. The Oort cloud, which is thought to be the source for long-period comets, may also exist at a distance roughly a thousand times further than the heliosphere. The nearest stars to the Solar System are within the Local Bubble; the closest star is named Proxima Centauri and is at a distance of 4.2441 light-years away.'''
# s1.split()
# s1= s1.split()
# print(s1)
# for i in range(len(s1)):
#     l= []
#     l.append(s1[i])
#     s1[i] = l
print(s1)    
# s1= s1.split()
s2 = "sun"
# s1= ['acteis']
print( "FuzzyWuzzy Ratio: ", fuzz.ratio(s1, s2))
print( "FuzzyWuzzy PartialRatio: ", fuzz.partial_ratio(s1, s2))
print( "FuzzyWuzzy TokenSortRatio: ", fuzz.token_sort_ratio(s1, s2))
print( "FuzzyWuzzy TokenSetRatio: ", fuzz.token_set_ratio(s1, s2))
print( "FuzzyWuzzy paartial TokenSetRatio: ", fuzz.partial_token_set_ratio(s1, s2))
print( "FuzzyWuzzy WRatio: ", fuzz.WRatio(s1, s2),'\n\n')
print(process.extractOne(s2,s1)[1])
print('klk')
# for process library,
query = 'book'
choices = ['geek for geek', 'geek geek', 'g. for bookshelves'] 
print( "List of ratios: ")
print( process.extract(s2, s1), "hi",'\n')
print ("Best among the above list: ",process.extractOne(s2, s1,scorer=fuzz.partial_token_set_ratio))

abc =process.extractOne(s2, s1)
print(abc[1])
a = process.extract(s2,s1,scorer=fuzz.partial_token_sort_ratio)

print(a)

print("new")

a = "District,"

b = 'afp utilities'

print(fuzz.WRatio(a, b))