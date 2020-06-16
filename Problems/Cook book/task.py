pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

recipe1 = "pasta time!"
recipe2 = "apple pie time!"
recipe3 = "ratatouille time!"
recipe4 = "chocolate cake time!"
recipe5 = "omelette time!"

ingred = input()

# can use if ingred in pasta: print(recipe1) for future uses

# if ingred in "pasta":
#    print(recipe1)

if ingred == "salt":
    print(recipe1,
          recipe2,
          recipe3,
          recipe4,
          recipe5)

if ingred == "tomato":
    print(recipe1)
    print(recipe3)
    print(recipe5)

if ingred == "basil" or ingred == "pasta":
    print(recipe1)

if ingred == "garlic":
    print(recipe1)
    print(recipe3)

if ingred == "olive oil":
    print(recipe1)
    print(recipe3)

if ingred == "apple" or ingred == "cinnamon":
    print(recipe2)

if ingred == "sugar" or ingred == "flour" or ingred == "butter":
    print(recipe2)
    print(recipe4)

if ingred == "egg":
    print(recipe2)
    print(recipe5)

if ingred == "aubergine" or ingred == "carrot" or ingred == "onion":
    print(recipe3)

if ingred == "pepper":
    print(recipe3)
    print(recipe5)

if ingred == "chocolate" or ingred == "coffee":
    print(recipe4)

if ingred == "milk" or ingred == "bacon":
    print(recipe5)
