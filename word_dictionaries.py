'''
- Asher Wu, Cody Spitznas
- 12/9/24
- CptS 111, Fall 2024
- Hangman Marathon
- This project simulates the game of Hangman.
- Modules used: none
'''

'''
Themes are holidays, animals, geography, fantasy, and history. The word lengths go from 3 to 10 characters. I strongly recommend the theme being a variable
(one being 'all') selected at the start of the game, and then using the theme variable with the appropriate word length to pick the appropriate dictionary.
If the theme is 'all,' then a random dictionary that corresponds to that length.
'''

# Dictionary of words of length 3 with the theme holidays
holiday_words_3 = {
    "joy": "A feeling of great pleasure and happiness.",
    "elf": "A small, often mischievous creature from folklore.",
    "eve": "The day or period of time immediately before an event or occasion.",
    "pie": "A baked dish of fruit, or meat and vegetables, typically with a top and base of pastry.",
    "toy": "An object for a child to play with, typically a model or miniature replica of something.",
    "hat": "A shaped covering for the head worn for warmth, as a fashion item, or as part of a uniform.",
    "bow": "A knot tied with two loops and two loose ends, used especially for tying shoelaces and decorative ribbons.",
    "joy": "A feeling of great pleasure and happiness.",
    "nut": "A fruit consisting of a hard or tough shell around an edible kernel.",
    "log": "A part of the trunk or a large branch of a tree that has fallen or been cut off."
}
# Dictionary of words of length 4 with the theme holidays
holiday_words_4 = {
    "gift": "A thing given willingly to someone without payment; a present.",
    "snow": "Atmospheric water vapor frozen into ice crystals and falling in light white flakes.",
    "tree": "A woody perennial plant, typically having a single stem or trunk growing to a considerable height.",
    "bell": "A hollow object, typically made of metal, that sounds a clear musical note when struck.",
    "card": "A piece of thick, stiff paper or thin pasteboard, in particular one used for writing or printing on.",
    "cake": "An item of soft, sweet food made from a mixture of flour, shortening, eggs, sugar, and other ingredients, baked and often decorated.",
    "star": "A fixed luminous point in the night sky which is a large, remote incandescent body like the sun.",
    "wish": "A desire or hope for something to happen.",
    "yule": "An archaic term for Christmas, or the Christmas season.",
    "noel": "Another term for Christmas, especially in songs and carols."
}
# Dictionary of words of length 5 with the theme holidays
holiday_words_5 = {
    "feast": "A large meal, typically one in celebration of something.",
    "candy": "A sweet food made with sugar or syrup combined with fruit, chocolate, or nuts.",
    "angel": "A spiritual being believed to act as an attendant, agent, or messenger of God.",
    "santa": "A figure of a jolly old man in red, who brings gifts to children on Christmas Eve.",
    "wreath": "An arrangement of flowers, leaves, or stems fastened in a ring and used for decoration.",
    "stock": "A supply of goods kept on hand for sale to customers by a merchant, distributor, manufacturer, etc.",
    "party": "A social gathering of invited guests, typically involving eating, drinking, and entertainment.",
    "cheer": "A shout of encouragement, praise, or joy.",
    "holly": "A shrub or tree with prickly dark green leaves, small white flowers, and red berries.",
    "elves": "Plural of elf, small, often mischievous creatures from folklore."
}
# Dictionary of words of length 6 with the theme holidays
holiday_words_6 = {
    "turkey": "A large bird native to North America, traditionally eaten at Thanksgiving.",
    "candle": "A cylinder or block of wax or tallow with a central wick that is lit to produce light as it burns.",
    "sleigh": "A sled drawn by horses or reindeer, especially one used for passengers.",
    "ornament": "A thing used to make something look more attractive but usually having no practical purpose.",
    "ginger": "A hot, fragrant spice made from the rhizome of a plant, used in cooking and baking.",
    "spirit": "The non-physical part of a person which is the seat of emotions and character.",
    "reindeer": "A deer of the tundra and subarctic regions of Eurasia and North America, both sexes of which have large branching antlers.",
    "garland": "A wreath of flowers and leaves, worn on the head or hung as a decoration.",
    "jingle": "A light ringing sound such as that made by metal objects being shaken together.",
    "winter": "The coldest season of the year, in the northern hemisphere from December to February and in the southern hemisphere from June to August."
}
# Dictionary of words of length 7 with the theme holidays
holiday_words_7 = {
    "holiday": "A day of festivity or recreation when no work is done.",
    "chimney": "A vertical channel or pipe that conducts smoke and combustion gases up from a fire or furnace.",
    "cracker": "A thin, crisp wafer often eaten with cheese or other savory toppings.",
    "festive": "Relating to a festival, especially Christmas.",
    "gingham": "A lightweight plain-woven cotton cloth, typically checked in white and a bold color.",
    "kinfolk": "Relatives or family members.",
    "menorah": "A candelabrum with seven or nine lights that is used in Jewish worship.",
    "pumpkin": "A large rounded orange-yellow fruit with a thick rind, edible flesh, and many seeds.",
    "rejoice": "Feel or show great joy or delight.",
    "snowman": "A representation of a human figure created with compressed snow."
}
# Dictionary of words of length 8 with the theme holidays
holiday_words_8 = {
    "reindeer": "A deer of the tundra and subarctic regions of Eurasia and North America, both sexes of which have large branching antlers.",
    "snowfall": "An instance of snow falling.",
    "mistletoe": "A plant with white berries, traditionally used as a Christmas decoration.",
    "holidays": "A period of time during which you relax and enjoy yourself away from home.",
    "tradition": "The transmission of customs or beliefs from generation to generation.",
    "festival": "A day or period of celebration, typically for religious reasons.",
    "gathering": "An assembly or meeting, especially a social or festive one or one held for a specific purpose.",
    "celebrate": "Acknowledge (a significant or happy day or event) with a social gathering or enjoyable activity.",
    "firework": "A device containing gunpowder and other combustible chemicals which causes spectacular effects and explosions when ignited.",
    "snowflake": "A flake of snow, especially a feathery ice crystal, typically displaying delicate sixfold symmetry."
}
# Dictionary of words of length 9 with the theme holidays
holiday_words_9 = {
    "christmas": "The annual Christian festival celebrating Christ's birth, held on December 25.",
    "festivity": "The celebration of something in a joyful and exuberant way.",
    "decoration": "The process or art of decorating or adorning something.",
    "celebrate": "Acknowledge (a significant or happy day or event) with a social gathering or enjoyable activity.",
    "tradition": "The transmission of customs or beliefs from generation to generation.",
    "gathering": "An assembly or meeting, especially a social or festive one or one held for a specific purpose.",
    "snowflake": "A flake of snow, especially a feathery ice crystal, typically displaying delicate sixfold symmetry.",
    "fireworks": "A device containing gunpowder and other combustible chemicals which causes spectacular effects and explosions when ignited.",
    "snowstorm": "A heavy fall of snow, especially with a high wind."
}
# Dictionary of words of length 10 with the theme holidays
holiday_words_10 = {
    "celebration": "The action of marking one's pleasure at an important event or occasion by engaging in enjoyable, typically social, activity.",
    "decoration": "The process or art of decorating or adorning something.",
    "snowflakes": "A flake of snow, especially a feathery ice crystal, typically displaying delicate sixfold symmetry.",
    "fireplaces": "A place for a domestic fire, especially a grate or hearth at the base of a chimney.",
    "traditions": "The transmission of customs or beliefs from generation to generation.",
    "gatherings": "An assembly or meeting, especially a social or festive one or one held for a specific purpose.",
    "festivities": "The celebration of something in a joyful and exuberant way.",
    "snowstorms": "A heavy fall of snow, especially with a high wind.",
    "reindeer": "A deer of the tundra and subarctic regions of Eurasia and North America, both sexes of which have large branching antlers.",
    "hollyberry": "The small, typically red fruit of the holly plant, often used in Christmas decorations."
}

# Dictionary of words of length 3 with the theme animals
animal_words_3 = {
    "cat": "A small domesticated carnivorous mammal with soft fur, a short snout, and retractile claws.",
    "dog": "A domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, and a barking, howling, or whining voice.",
    "bat": "A nocturnal flying mammal that can navigate using echolocation.",
    "ant": "A small insect typically having a sting and living in a complex social colony.",
    "bee": "A flying insect known for its role in pollination and, in the case of the best-known bee species, the European honey bee, for producing honey.",
    "cow": "A fully grown female animal of a domesticated breed of ox, kept to produce milk or beef.",
    "fox": "A small to medium-sized, omnivorous mammal belonging to several genera of the family Canidae.",
    "owl": "A nocturnal bird of prey with large forward-facing eyes surrounded by facial disks, a hooked beak, and typically a loud call.",
    "rat": "A rodent that resembles a large mouse, typically having a pointed snout and a long, sparsely haired tail.",
    "pig": "A domesticated mammal with a stout body, short legs, and a snout used for digging."
}
# Dictionary of words of length 4 with the theme animals
animal_words_4 = {
    "lion": "A large tawny-colored cat that lives in prides, found in Africa and northwestern India.",
    "wolf": "A wild carnivorous mammal which is the largest member of the dog family.",
    "bear": "A large, heavy mammal with thick fur and a very short tail.",
    "frog": "A tailless amphibian with a short squat body, moist smooth skin, and very long hind legs for leaping.",
    "deer": "A hoofed grazing or browsing animal, with branched bony antlers that are shed annually and typically borne only by the male.",
    "crab": "A crustacean with a broad carapace, stalked eyes, and five pairs of legs, the first pair of which are modified as pincers.",
    "fish": "A limbless cold-blooded vertebrate animal with gills and fins living wholly in water.",
    "hawk": "A diurnal bird of prey with broad rounded wings and a long tail, typically taking prey by surprise with a short chase.",
    "mole": "A small burrowing mammal with dark velvety fur, a long muzzle, and very small eyes.",
    "goat": "A hardy domesticated ruminant animal that has backward curving horns and (in the male) a beard."
}
# Dictionary of words of length 5 with the theme animals
animal_words_5 = {
    "horse": "A large plant-eating domesticated mammal with solid hooves and a flowing mane and tail.",
    "sheep": "A domesticated ruminant animal with a thick woolly coat and (typically only in the male) curving horns.",
    "zebra": "An African wild horse with black-and-white stripes and an erect mane.",
    "whale": "A very large marine mammal with a streamlined hairless body, a horizontal tail fin, and a blowhole on top of the head for breathing.",
    "shark": "A long-bodied chiefly marine fish with a cartilaginous skeleton, a prominent dorsal fin, and toothlike scales.",
    "tiger": "A very large solitary cat with a yellow-brown coat striped with black, native to the forests of Asia but becoming increasingly rare.",
    "eagle": "A large bird of prey with a massive hooked bill and long broad wings, renowned for its keen sight and powerful soaring flight.",
    "koala": "A bearlike arboreal Australian marsupial that has thick gray fur and feeds on eucalyptus leaves.",
    "lemur": "An arboreal primate with a pointed snout and typically a long tail, found only in Madagascar.",
    "panda": "A large bearlike mammal with characteristic black-and-white markings, native to certain mountain forests in China."
}
# Dictionary of words of length 6 with the theme animals
animal_words_6 = {
    "monkey": "A small to medium-sized primate that typically has a long tail, most kinds of which live in trees in tropical countries.",
    "rabbit": "A burrowing, plant-eating mammal with long ears, long hind legs, and a short tail.",
    "giraffe": "A large African mammal with a very long neck and forelegs, having a coat patterned with brown patches separated by lighter lines.",
    "donkey": "A domesticated hoofed mammal of the horse family with long ears and a braying call.",
    "parrot": "A bird, often vividly colored, with a short down-curved hooked bill, grasping feet, and a raucous voice.",
    "beetle": "An insect of an order distinguished by having forewings typically modified into hard wing cases that cover and protect the hind wings and abdomen.",
    "falcon": "A bird of prey with long pointed wings and a notched beak, typically catching prey by diving on it from above.",
    "otter": "A semiaquatic fish-eating mammal of the weasel family, with an elongated body, dense fur, and webbed feet.",
    "badger": "A heavily built omnivorous nocturnal mammal of the weasel family, typically having a gray and black coat.",
    "weasel": "A small, slender, carnivorous mammal related to, but generally smaller than, the stoat."
}
# Dictionary of words of length 7 with the theme animals
animal_words_7 = {
    "giraffe": "A large African mammal with a very long neck and forelegs, having a coat patterned with brown patches separated by lighter lines.",
    "dolphin": "A small gregarious toothed whale that typically has a beaklike snout and a curved fin on the back.",
    "buffalo": "A heavily built wild ox with backswept horns, found mainly in the Old World tropics.",
    "penguin": "A large flightless seabird of the southern hemisphere, with black upper parts and white underparts and wings developed into flippers for swimming underwater.",
    "chicken": "A domestic fowl kept for its eggs or meat, especially a young one.",
    "leopard": "A large, solitary cat that has a yellowish-brown or tawny coat with black spots and usually hunts at night.",
    "octopus": "A cephalopod mollusk with eight sucker-bearing arms, a soft saclike body, and no internal shell."
}
# Dictionary of words of length 8 with the theme animals
animal_words_8 = {
    "elephant": "A large herbivorous mammal with a trunk, native to Africa and southern Asia.",
    "kangaroo": "A large plant-eating marsupial with powerful hind legs and a long tail, native to Australia.",
    "dinosaur": "A diverse group of reptiles of the clade Dinosauria that first appeared during the Triassic period.",
    "alligator": "A large semiaquatic reptile similar to a crocodile but with a broader and shorter head, native to the Americas.",
    "buffaloes": "Large, heavily built wild oxen with backswept horns, found mainly in the Old World tropics.",
    "chipmunk": "A small striped rodent of the squirrel family, found in North America and Asia.",
    "flamingo": "A tall wading bird with mainly pink or scarlet plumage and long legs and neck.",
    "porpoise": "A small toothed whale with a low triangular dorsal fin and a blunt rounded snout."
}
# Dictionary of words of length 9 with the theme animals
animal_words_9 = {
    "kangaroos": "Large plant-eating marsupials with powerful hind legs and a long tail, native to Australia.",
    "dolphins": "Small gregarious toothed whales that typically have a beaklike snout and a curved fin on the back.",
    "elephants": "Large herbivorous mammals with trunks, native to Africa and southern Asia.",
    "alligators": "Large semiaquatic reptiles similar to crocodiles but with broader and shorter heads, native to the Americas.",
    "chipmunks": "Small striped rodents of the squirrel family, found in North America and Asia.",
    "flamingos": "Tall wading birds with mainly pink or scarlet plumage and long legs and necks.",
    "porpoises": "Small toothed whales with low triangular dorsal fins and blunt rounded snouts.",
    "buffaloes": "Large, heavily built wild oxen with backswept horns, found mainly in the Old World tropics.",
    "penguins": "Large flightless seabirds of the southern hemisphere, with black upper parts and white underparts and wings developed into flippers for swimming underwater.",
    "leopards": "Large, solitary cats that have yellowish-brown or tawny coats with black spots and usually hunt at night."
}
# Dictionary of words of length 10 with the theme animals
animal_words_10 = {
    "chimpanzee": "A great ape with large ears, mainly black coloration, and lighter skin on the face, native to the forests of west and central Africa.",
    "crocodiles": "Large predatory semi-aquatic reptiles with long jaws, long tails, short legs, and a powerful bite.",
    "orangutans": "Large arboreal apes with long reddish-brown hair, long arms, and a large face, native to the rainforests of Borneo and Sumatra.",
    "rattlesnake": "A venomous American snake with a series of horny rings on the tail that produce a characteristic rattling sound when vibrated.",
    "woodpecker": "A bird with a strong bill and a stiff tail, which climbs tree trunks to find insects and drums on dead wood to mark territory.",
    "butterflies": "Insects with two pairs of large, typically brightly colored wings that are covered with microscopic scales.",
    "hippopotami": "Large, mostly herbivorous, semi-mammalian mammals, native to sub-Saharan Africa.",
    "grasshopper": "A plant-eating insect with long hind legs that are used for jumping and for producing a chirping sound.",
    "chameleons": "Old World lizards with the ability to change color, long sticky tongues, and eyes that move independently of each other.",
    "tarantulas": "Large, hairy spiders that are often kept as exotic pets."
}

# Dictionary of words of length 3 with the theme geography
geography_words_3 = {
    "bay": "A broad inlet of the sea where the land curves inward.",
    "cap": "A headland or promontory.",
    "dam": "A barrier constructed to hold back water and raise its level.",
    "gulf": "A deep inlet of the sea almost surrounded by land, with a narrow mouth.",
    "key": "A low-lying island or reef, especially in the Caribbean.",
    "map": "A diagrammatic representation of an area of land or sea showing physical features.",
    "pen": "A small, narrow piece of land projecting into the sea or a lake.",
    "sea": "The expanse of salt water that covers most of the earth's surface.",
    "val": "A valley, especially in a poetic or literary context.",
    "zen": "A state of calm attentiveness in which one's actions are guided by intuition rather than by conscious effort."
}
# Dictionary of words of length 4 with the theme geography
geography_words_4 = {
    "lake": "A large body of water surrounded by land.",
    "hill": "A naturally raised area of land, not as high or craggy as a mountain.",
    "reef": "A ridge of jagged rock, coral, or sand just above or below the surface of the sea.",
    "mesa": "An isolated flat-topped hill with steep sides, found in landscapes with horizontal strata.",
    "dune": "A mound or ridge of sand or other loose sediment formed by the wind, especially on the sea coast or in a desert.",
    "cape": "A headland or promontory of large size extending into a body of water, usually the sea.",
    "isle": "An island or peninsula, especially a small one.",
    "peak": "The pointed top of a mountain.",
    "cove": "A small, sheltered bay in the shoreline of a sea, river, or lake.",
    "arch": "A natural rock formation where an arch has formed with an opening underneath."
}
# Dictionary of words of length 5 with the theme geography
geography_words_5 = {
    "river": "A large natural stream of water flowing in a channel to the sea, a lake, or another river.",
    "plain": "A large area of flat land with few trees.",
    "ocean": "A very large expanse of sea, in particular each of the main areas into which the sea is divided geographically.",
    "island": "A piece of land surrounded by water.",
    "desert": "A barren area of landscape where little precipitation occurs and consequently living conditions are hostile for plant and animal life.",
    "fjord": "A long, narrow, deep inlet of the sea between high cliffs, typically formed by submergence of a glaciated valley.",
    "delta": "A landform at the mouth of a river where it flows into an ocean, sea, estuary, lake, or reservoir.",
    "basin": "A natural depression on the earth's surface, typically containing water.",
    "valley": "A low area of land between hills or mountains, typically with a river or stream flowing through it.",
    "globe": "A spherical representation of the earth or of the constellations with a map on the surface."
}
# Dictionary of words of length 6 with the theme geography
geography_words_6 = {
    "island": "A piece of land surrounded by water.",
    "desert": "A barren area of landscape where little precipitation occurs and consequently living conditions are hostile for plant and animal life.",
    "forest": "A large area covered chiefly with trees and undergrowth.",
    "canyon": "A deep gorge, typically one with a river flowing through it.",
    "lagoon": "A stretch of salt water separated from the sea by a low sandbank or coral reef.",
    "glacier": "A slowly moving mass or river of ice formed by the accumulation and compaction of snow on mountains or near the poles.",
    "tundra": "A vast, flat, treeless Arctic region in which the subsoil is permanently frozen.",
    "valley": "A low area of land between hills or mountains, typically with a river or stream flowing through it.",
    "savanna": "A grassy plain in tropical and subtropical regions, with few trees.",
    "jungle": "An area of land overgrown with dense forest and tangled vegetation, typically in the tropics."
}
# Dictionary of words of length 7 with the theme geography
geography_words_7 = {
    "isthmus": "A narrow strip of land with sea on either side, forming a link between two larger areas of land.",
    "plateau": "An area of relatively level high ground.",
    "volcano": "A mountain or hill with a crater or vent through which lava, rock fragments, hot vapor, and gas are being or have been erupted from the earth's crust.",
    "channel": "A length of water wider than a strait, joining two larger areas of water, especially two seas.",
    "prairie": "A large open area of grassland, especially in North America.",
    "harbour": "A place on the coast where vessels may find shelter, especially one protected from rough water by piers, jetties, and other artificial structures.",
    "canyon": "A deep gorge, typically one with a river flowing through it."
}
# Dictionary of words of length 8 with the theme geography
geography_words_8 = {
    "mountain": "A large natural elevation of the earth's surface rising abruptly from the surrounding level; a large steep hill.",
    "plateaus": "An area of relatively level high ground.",
    "volcanos": "Mountains or hills with craters or vents through which lava, rock fragments, hot vapor, and gas are being or have been erupted from the earth's crust.",
    "archipel": "A group of islands.",
    "waterway": "A river, canal, or other route for travel by water.",
    "headland": "A narrow piece of land that projects from a coastline into the sea.",
    "peninsula": "A piece of land almost surrounded by water or projecting out into a body of water.",
    "lowlands": "An area of land that is lower than the land around it.",
    "badlands": "Extensive tracts of heavily eroded, uncultivable land with little vegetation.",
    "highland": "An area of high or mountainous land."
}
# Dictionary of words of length 9 with the theme geography
geography_words_9 = {
    "continent": "Any of the world's main continuous expanses of land (e.g., Africa, Asia, Europe).",
    "landscape": "All the visible features of an area of land, often considered in terms of their aesthetic appeal.",
    "waterfall": "A cascade of water falling from a height, formed when a river or stream flows over a precipice or steep incline.",
    "peninsula": "A piece of land almost surrounded by water or projecting out into a body of water.",
    "archipelago": "A group of islands.",
    "mountains": "Large natural elevations of the earth's surface rising abruptly from the surrounding level.",
    "lowlands": "An area of land that is lower than the land around it.",
    "badlands": "Extensive tracts of heavily eroded, uncultivable land with little vegetation.",
    "highlands": "An area of high or mountainous land."
}
# Dictionary of words of length 10 with the theme geography
geography_words_10 = {
    "archipelago": "A group of islands.",
    "peninsulas": "A piece of land almost surrounded by water or projecting out into a body of water.",
    "waterfalls": "A cascade of water falling from a height, formed when a river or stream flows over a precipice or steep incline.",
    "continents": "Any of the world's main continuous expanses of land (e.g., Africa, Asia, Europe).",
    "landscapes": "All the visible features of an area of land, often considered in terms of their aesthetic appeal.",
    "lowlanders": "People who live in lowland areas.",
    "highlander": "A person who lives in the highlands.",
    "badlanders": "People who live in badlands, areas of heavily eroded, uncultivable land with little vegetation.",
    "mountainous": "Having many mountains.",
    "geography": "The study of the physical features of the earth and its atmosphere."
}

# Dictionary of words of length 3 with the theme fantasy
fantasy_words_3 = {
    "orc": "A mythical creature, typically depicted as a brutish, aggressive humanoid.",
    "elf": "A small, often mischievous creature from folklore.",
    "imp": "A small, mischievous devil or sprite.",
    "fey": "A term used to describe someone or something with magical or otherworldly qualities.",
    "wyr": "A mythical dragon or serpent.",
    "pix": "A small, magical creature, often depicted with wings.",
    "hob": "A small, friendly creature from folklore, similar to a brownie or hobgoblin.",
    "jot": "A giant from Norse mythology.",
    "gob": "A goblin, a small, grotesque, monstrous creature.",
    "tup": "A small, mischievous spirit or sprite."
}
# Dictionary of words of length 4 with the theme fantasy
fantasy_words_4 = {
    "mage": "A magician or learned person.",
    "troll": "A mythical, cave-dwelling being depicted as either a giant or a dwarf.",
    "fairy": "A small imaginary being of human form that has magical powers.",
    "ogre": "A man-eating giant in folklore.",
    "wand": "A slender stick or rod, especially one used for magic or divination.",
    "wolf": "A wild carnivorous mammal which is the largest member of the dog family.",
    "elf": "A small, often mischievous creature from folklore.",
    "djin": "A supernatural being in Arabian mythology.",
    "goblin": "A mischievous, ugly creature resembling a dwarf.",
    "wyrm": "A mythical dragon or serpent."
}
# Dictionary of words of length 5 with the theme fantasy
fantasy_words_5 = {
    "magic": "The power of apparently influencing events by using mysterious or supernatural forces.",
    "witch": "A woman thought to have magic powers, especially evil ones.",
    "ghost": "An apparition of a dead person which is believed to appear or become manifest to the living.",
    "giant": "An imaginary or mythical being of human form but superhuman size.",
    "dwarf": "A member of a mythical race of short, stocky humanlike creatures who are generally skilled in mining and metalworking.",
    "spell": "A form of words used as a magical charm or incantation.",
    "fairy": "A small imaginary being of human form that has magical powers.",
    "beast": "A large, dangerous animal.",
    "troll": "A mythical, cave-dwelling being depicted as either a giant or a dwarf.",
    "sword": "A weapon with a long metal blade and a hilt with a handguard, used for thrusting or striking."
}
# Dictionary of words of length 6 with the theme fantasy
fantasy_words_6 = {
    "wizard": "A man who has magical powers.",
    "dragon": "A large, serpentine legendary creature that appears in the folklore of many cultures.",
    "goblin": "A mischievous, ugly creature resembling a dwarf.",
    "spells": "A form of words used as a magical charm or incantation.",
    "knight": "A man who served his sovereign or lord as a mounted soldier in armor.",
    "sorcer": "A person who claims or is believed to have magic powers; a wizard."
}
# Dictionary of words of length 7 with the theme fantasy
fantasy_words_7 = {
    "unicorn": "A mythical animal typically represented as a horse with a single straight horn projecting from its forehead.",
    "phoenix": "A mythical bird that regenerates or is otherwise born again.",
    "griffin": "A mythical creature with the body of a lion and the head and wings of an eagle.",
    "chimera": "A fire-breathing female monster with a lion's head, a goat's body, and a serpent's tail.",
    "sorcery": "The use of magic, especially black magic.",
    "warlock": "A man who practices witchcraft; a sorcerer.",
    "dragons": "Large, serpentine legendary creatures that appear in the folklore of many cultures."
}
# Dictionary of words of length 8 with the theme fantasy
fantasy_words_8 = {
    "unicorns": "Mythical animals typically represented as horses with single straight horns projecting from their foreheads.",
    "phoenixes": "Mythical birds that regenerate or are otherwise born again.",
    "griffins": "Mythical creatures with the bodies of lions and the heads and wings of eagles.",
    "chimeras": "Fire-breathing female monsters with lion's heads, goat's bodies, and serpent's tails.",
    "sorcery": "The use of magic, especially black magic.",
    "warlocks": "Men who practice witchcraft; sorcerers.",
    "dragons": "Large, serpentine legendary creatures that appear in the folklore of many cultures."
}
# Dictionary of words of length 9 with the theme fantasy
fantasy_words_9 = {
    "sorcerers": "People who claim or are believed to have magical powers; wizards.",
    "spellbook": "A book containing a collection of magical spells.",
    "enchanter": "A person who uses magic or sorcery, especially to put someone or something under a spell.",
    "necromancy": "The practice of communicating with the dead, especially in order to predict the future.",
    "alchemist": "A person who practices alchemy, a medieval chemical science aiming to transform base metals into gold.",
    "illusionist": "A person who performs tricks that deceive the eye; a magician.",
    "elementals": "Supernatural beings or spirits associated with the elements (earth, air, fire, water).",
    "warhammer": "A weapon consisting of a hammer-like head mounted on a long handle, used in medieval warfare.",
    "spellbound": "Having your attention fixated as though by a spell.",
    "dragonborn": "A race of humanoid dragons in fantasy settings, often possessing dragon-like abilities."
}
# Dictionary of words of length 10 with the theme fantasy
fantasy_words_10 = {
    "spellbound": "Having your attention fixated as though by a spell.",
    "dragonborn": "A race of humanoid dragons in fantasy settings, often possessing dragon-like abilities.",
    "necromancy": "The practice of communicating with the dead, especially in order to predict the future.",
    "enchanters": "People who use magic or sorcery, especially to put someone or something under a spell.",
    "alchemists": "People who practice alchemy, a medieval chemical science aiming to transform base metals into gold.",
    "illusionist": "A person who performs tricks that deceive the eye; a magician.",
    "elementals": "Supernatural beings or spirits associated with the elements (earth, air, fire, water).",
    "warhammers": "Weapons consisting of hammer-like heads mounted on long handles, used in medieval warfare.",
    "sorceresses": "Women who practice sorcery; female sorcerers.",
    "spellbooks": "Books containing collections of magical spells."
}


# Dictionary of words of length 3 with the theme history
history_words_3 = {
    "war": "A state of armed conflict between different countries or different groups within a country.",
    "era": "A long and distinct period of history with a particular feature or characteristic.",
    "law": "The system of rules which a particular country or community recognizes as regulating the actions of its members.",
    "art": "The expression or application of human creative skill and imagination, typically in a visual form.",
    "map": "A diagrammatic representation of an area of land or sea showing physical features.",
    "axe": "A tool typically used for chopping wood, often associated with historical battles.",
    "bow": "A weapon for shooting arrows, typically used in historical warfare.",
    "hut": "A small, simple, single-story house or shelter.",
    "urn": "A tall, rounded vase with a base, often used in historical contexts for storing ashes.",
    "ink": "A colored fluid used for writing, drawing, printing, or duplicating."
}
# Dictionary of words of length 4 with the theme history
history_words_4 = {
    "king": "The male ruler of an independent state, especially one who inherits the position by right of birth.",
    "duke": "A male holding the highest hereditary title in the British and certain other peerages.",
    "knight": "A man who served his sovereign or lord as a mounted soldier in armor.",
    "fort": "A fortified building or strategic position.",
    "army": "An organized military force equipped for fighting on land.",
    "coin": "A flat, typically round piece of metal with an official stamp, used as money.",
    "helm": "A position of leadership.",
    "scroll": "A roll of parchment or paper for writing or painting on.",
    "spear": "A weapon with a pointed tip, typically of steel, and a long shaft, used for thrusting or throwing.",
    "tomb": "A large vault, typically an underground one, for burying the dead."
}
# Dictionary of words of length 5 with the theme history
history_words_5 = {
    "sword": "A weapon with a long metal blade and a hilt with a handguard, used for thrusting or striking.",
    "armor": "The metal coverings formerly worn by soldiers or warriors to protect the body in battle.",
    "crown": "A circular ornamental headdress worn by a monarch as a symbol of authority.",
    "plague": "A contagious bacterial disease characterized by fever and delirium, typically with the formation of buboes.",
    "siege": "A military operation in which enemy forces surround a town or building, cutting off essential supplies, with the aim of compelling those inside to surrender.",
    "knight": "A man who served his sovereign or lord as a mounted soldier in armor.",
    "realm": "A kingdom.",
    "treaty": "A formally concluded and ratified agreement between countries.",
    "relic": "An object surviving from an earlier time, especially one of historical or sentimental interest.",
    "feast": "A large meal, typically one in celebration of something."
}
# Dictionary of words of length 6 with the theme history
history_words_6 = {
    "castle": "A large building typically of the medieval period, fortified against attack.",
    "empire": "An extensive group of states or countries under a single supreme authority.",
    "knight": "A man who served his sovereign or lord as a mounted soldier in armor.",
    "plague": "A contagious bacterial disease characterized by fever and delirium.",
    "revolt": "Rise in rebellion.",
    "treaty": "A formally concluded and ratified agreement between countries.",
    "viking": "A Scandinavian seafaring pirate and trader who raided and settled in many parts of northwestern Europe in the 8th–11th centuries.",
    "weapon": "A thing designed or used for inflicting bodily harm or physical damage.",
    "battle": "A sustained fight between large organized armed forces.",
    "dynasty": "A line of hereditary rulers of a country."
}
# Dictionary of words of length 7 with the theme history
history_words_7 = {
    "knights": "A man who served his sovereign or lord as a mounted soldier in armor.",
    "crusade": "A medieval military expedition, one of a series made by Europeans to recover the Holy Land from the Muslims.",
    "empire": "An extensive group of states or countries under a single supreme authority.",
    "vassals": "A holder of land by feudal tenure on conditions of homage and allegiance.",
    "siege": "A military operation in which enemy forces surround a town or building, cutting off essential supplies, with the aim of compelling those inside to surrender.",
    "dynasty": "A line of hereditary rulers of a country.",
    "revolt": "Rise in rebellion.",
    "treaty": "A formally concluded and ratified agreement between countries.",
    "plague": "A contagious bacterial disease characterized by fever and delirium.",
    "castle": "A large building typically of the medieval period, fortified against attack."
}
# Dictionary of words of length 8 with the theme history
history_words_8 = {
    "medieval": "Relating to the Middle Ages.",
    "crusades": "A series of medieval military expeditions made by Europeans to recover the Holy Land from the Muslims.",
    "monarchy": "A form of government with a monarch at the head.",
    "artifact": "An object made by a human being, typically one of cultural or historical interest.",
    "colonial": "Relating to or characteristic of a colony or colonies.",
    "renaissance": "The revival of art and literature under the influence of classical models in the 14th–16th centuries.",
    "revolution": "A forcible overthrow of a government or social order in favor of a new system.",
    "explorer": "A person who explores an unfamiliar area; an adventurer.",
    "dynastic": "Relating to a line of hereditary rulers of a country.",
    "fortress": "A military stronghold, especially a strongly fortified town fit for a large garrison."
}
# Dictionary of words of length 9 with the theme history
history_words_9 = {
    "crusaders": "A series of medieval military expeditions made by Europeans to recover the Holy Land from the Muslims.",
    "monarchies": "Forms of government with a monarch at the head.",
    "artifacts": "Objects made by human beings, typically of cultural or historical interest.",
    "colonials": "Relating to or characteristic of a colony or colonies.",
    "renaissance": "The revival of art and literature under the influence of classical models in the 14th–16th centuries.",
    "revolutions": "Forcible overthrows of governments or social orders in favor of new systems.",
    "explorers": "People who explore unfamiliar areas; adventurers.",
    "dynasties": "Lines of hereditary rulers of a country.",
    "fortresses": "Military strongholds, especially strongly fortified towns fit for large garrisons.",
    "medievals": "Relating to the Middle Ages."
}
# Dictionary of words of length 10 with the theme history
history_words_10 = {
    "crusaders": "A series of medieval military expeditions made by Europeans to recover the Holy Land from the Muslims.",
    "monarchies": "Forms of government with a monarch at the head.",
    "artifacts": "Objects made by human beings, typically of cultural or historical interest.",
    "colonials": "Relating to or characteristic of a colony or colonies.",
    "renaissance": "The revival of art and literature under the influence of classical models in the 14th–16th centuries.",
    "revolutions": "Forcible overthrows of governments or social orders in favor of new systems.",
    "explorers": "People who explore unfamiliar areas; adventurers.",
    "dynasties": "Lines of hereditary rulers of a country.",
    "fortresses": "Military strongholds, especially strongly fortified towns fit for large garrisons.",
    "medievals": "Relating to the Middle Ages."
}
