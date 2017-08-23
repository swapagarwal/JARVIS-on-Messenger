#rewrite the program and then release it onto telegram and messenger!
''' argh what cocktail can i make with these ingredients? search and return a cocktail which has
the most matching ingredients'''
import enchant

def search(drinks, cocktails):
    matched_drinks = {x: drinks[x] for x in cocktails}
    print(matched_drinks)



def spell_check(word):
    d = enchant.Dict("en_GB")
    if word in cocktails:
        pass
    elif word not in cocktails:
        d.check(word)
        d.suggest(word)

def print_nice():



def matches():




cocktails = {

    "Mojito":{"White Rum":"50 ml", "Soda Water": "1 Dash", "Caster Sugar": "2 tsp", "Lime Wedges":"2", "Mint": "1 Sprig"},
    "Pina Colada":{"White Tequila": "50 ml", "Coconut Cream": "50 ml", "Pineapple Juice": "110 ml", "Pineapple": "3 Slices"},
    "Margarita": {"White Tequila": "50 ml", "Orange Liqueur": "35 ml", "Lime Juice": "25 ml"},
    "Long Island Ice Tea": {"Dark Rum": "17.5 ml", "Vodka": "17.5 ml", "Gin": "17.5 ml", "White Tequila": "17.5 ml", "Orange Liqueur": "17.5 ml", "Sugar Syrup": "17.5 ml", "Lemon Juice": "17.5 ml", "Lime Juice": "17.5 ml", "Cola": "To Top Up", "Lemon": "1 Slice"},
    "Strawberry Daiquiri": {"Dark Rum": "50 ml", "Lime Juice": "25 ml", "Sugar Syrup": "25 ml", "Strawberries": "3 chopped", "Strawberry": "To Garnish"},
    "Caipirinha": {"Dark Rum": "50 ml", "Sugar": "1 tsp", "Lime": "3 Wedges"},
    "Sex On The Beach": {"Peach Schnapps": "9 ml", "Vodka":"35 ml", "Orange Juice": "35 ml", "Cranberry Juice": "35 ml"},
    "Gin and Tonic": {"Gin": "25 ml", "Tonic": "125 ml", "Lime Juice": "10 ml", "Lime": "2 Wedges"},
    "Old Fashioned": {"Whisky": "50 ml", "Angostura Bitters": "1 Dash", "Sugar": "1 Cube", "Cherry": "1", "Orange": "1 Slice"},
    "Espresso Martini": {"Vodka": "25 ml", "Irish Cream Liqueur": "25 ml", "Espresso": "25 ml", "Honey": "10 ml", "Coffee Bean": "3 To Garnish"},
    "White Russian": {"Vodka": "25 ml", "Irish Cream Liqueur": "25 ml", "Milk": "25 ml"},
    "Mai Tai": {"Dark Rum": "35 ml", "Orange Liqueur": "10 ml", "Lime Juice":"25 ml", "Orgeat Syrup": "10 ml", "Pineapple Juice": "50 ml", "Orange": "1 Wedge"},
    "Cuba Libre": {"Dark Rum": "50 ml", "Cola": "125 ml", "Lime": "1 Wedge"},
    "Blue Lagoon": {"Vodka": "50 ml", "Blue Curacao Liqueur": "25 ml", "Lemonade": "150 ml", "Lemon": "1 Slice"},
    "Chi Chi": {"Vodka": "50 ml", "Cream of Coconut": "25 ml", "Pineapple Juice": "100 ml", "Pineapple": "1 Wedge"},
    "French Martini": {"Vodka": "40 ml", "Raspberry Liqueur": "20 ml", "Pineapple Juice": "50 ml", "Lemon": "1 twist"},
    "Alabama Slammer": {"Gin": "25 ml", "Whiskey":"25 ml", "Amaretto liqueur": "25 ml", "Orange Juice": "25 ml", "Orange": "A Slice"},
    "Zombie": {"Dark Rum": "75 ml", "Orange Liqueur": "15 ml", "Apricot Brandy": "15 ml", "Orange Juice": "50 ml", "Lime Juice": "25 ml", "Grenadine": "15 ml", "Oragne": "A Slice", "Pineapple": "1 Piece", "Mint": "A Sprig"},
    "Aviation": {"Gin": "60 ml", "Maraschino Liqueur": "15 ml", "Creme de Violette": "10 ml", "Lemon Juice": "25 ml"},
    "Raspberry Collins": {"Vodka": "50 ml", "Rasperberries": "9", "Lemon Juice": "25 ml", "Sugar Syrup": "10 ml", "Soda Water": "1 Dash"},
    "Cosmopolitan": {"Vodka": "35 ml", "Orange Liqueur": "10 ml", "Cranberry Juice": "45 ml", "Lime Juice": "10 ml", "Lime": "To Garnish"},
    "Vodka Martini": {"Vodka": "50 ml", "Vermouth": "12 ml", "Lemon Zest": "A Sprinkle", "Large Thin Lemon Zest": "To Garnish"},
    "Grog": {"Dark Rum": "50 ml", "Runny Honey": "1 tsp", "Lime Juice": "15 ml", "Lemon": "1 Slice", "Angosturra Bitters": "2 Dashes"},
    "Eggnog": {"Dark Rum": "50 ml", "Egg": "1", "Single Cream": "15 ml", "Sugar Syrup": "15 ml", "Milk": "60 ml", "Nutmeg": "12 Grinds"},
    "Whisky Sour": {"Whisky": "50 ml", "Lemon Juice": "35 ml", "Sugar Syrup": "17.5 ml", "Egg": "White"},
    "Martini": {"Gin": "50 ml", "Dry Vermouth": "5 ml", "Olive": "To Garnish"},
    "Gimlet": {"Gin": "25 ml", "Lime Juice": "25 ml", "Sugar": "1 tsp", "Lemon Peel": "To Garnish"},
    "Negroni": {"Gin": "25 ml", "Vermouth Rosso": "25 ml", "Campari": "25 ml", "Orange": "To Garnish"},
    "Tom Collins": {"Gin": "50 ml", "Lemon Juice": "25 ml", "Sugar Syrup": "10 ml", "Soda Water": "1 Splash", "Lemon": "1 Wedge"},
    "Kir": {"White Wine": "100 ml", "Creme de Cassis": "100 ml"},
    "Tequila Mojito": {"White Tequila": "25 ml", "Lime": "2 Wedges", "Lime Juice": "50 ml", "Water": "50 ml", "Lemon Juice": "110 ml", "Mint": "9 Leaves"},
    "Fireman": {"Dark Rum": "40 ml", "Lime Juice": "20 ml", "Grenadine": "10 ml", "Egg": "White", "Lime": "1 Wedge"},
    "Sazerac": {"Bourbon": "60 ml", "Sugar": "1 Cube", "Peychaud's Bitters": "4 Dashes", "Angosturra Bitters": "2 Dashes","Absinthe": "5 ml", "Lemon Peel": "To Garnish"},
    "Between the Sheets": {"Dark Rum": "25 ml", "Orange Liqueur": "25 ml", "Brandy": "25 ml", "Lemon Juice": "25 ml", "Lemon Zest": ""},
    "Bloody Mary": {"Vodka":"50 ml", "Tomato Juice": "100 ml", "Tobasco Sauce": "4 Dashes", "Worcestor Sauce": "4 Dashes", "Black Pepper": "", "Celery":"1 Stick", "Lemon": "2 Wedges"},
    "Moscow Mule": {"Vodka": "50 ml", "Ginger Beer": "125 ml", "Angosturra Bitters": "1 Dash", "Lime Juice": "1 Wedge"},
    "Dark N Stormy": {"Dark Rum": "50 ml", "Ginger Beer": "1 Dash", "Lime": "1 Wedge"},
    "Martinez": {"Gin": "50 ml", "Red Vermouth": "10 ml", "Dry Vermouth": "5 ml", "Maraschino Liqueur": "5 ml", "Angosturra Bitters": "1 Dash", "Orange Peel": "To Garnish"},
    "Rob Roy": {"Single Malt Whisky": "50 ml", "Sweet Vermouth": "25 ml", "Cherry": "1"},
    "Manhattan": {"Whisky": "50 ml", "Sweet Vermouth": "25 ml", "Angosturra Bitters": "1 Dash", "Orange peel": "To Garnish", "Marraschino Cherry": "1"},
    "Singapore Sling": {"Gin": "25 ml", "Cherry Brandy": "25 ml", "Benedictine": "5 ml", "Lemon Juice": "25 ml", "Grenadine": "10 ml", "Soda Water": "1 Splash"},
    "Sloe Gin Fizz": {"Sloe Gin": "50 ml", "Sparkling Water": "100 ml", "Lemon Juice": "25 ml", "Sugar Syrup": "10 ml", "Orange": "1 Slice", "Cherry": "1"},
    "French 75": {"Gin": "25 ml", "Lemon Juice": "10 ml", "Sugar Syrup": "5 ml", "Champagne": "To Top Up", "Lemon Peel": "To Garnish"},
    "Rum Punch": {"Dark Rum": "75 ml", "Apple Juice": "50 ml", "Lemon Juice": "20 ml", "Caramel Syrup": "15 ml", "Ginger Beer": "50 ml", "Angosturra Bitters": "1 Dash", "Ginger": "1 piece grated", "Cinnamon Stick": "", "Lemon": "2 Wedges", "Orange": "1 Wedge"},
    "Sprtiz Al Bitter": {"Prosecco": "90 ml", "Campari": "45 ml", "Soda Water": "To Top Up", "Orange": "1 Slice"},
    "Aperol Aperitivo": {"Soave Wine":"90 ml", "Aperol": "60 ml", "Soda Water": "To Top Up"},
    "Macapeel": {"Brandy": "50 ml", "Stewed Apples": "1 tbsp", "Raisins": "5", "Sugar Syrup": "5 ml", "Cinnamon": "A Pinch", "Ginger": "A Pinch", "Nutmeg": "A Pinch", "Orange Zest": "1 tsp", "Egg": "White", "Lemon Juice": "10 ml"},
             }


base_spirits = ["whiskey", "vodka", "tequila", "gin", "brandy"]
liqueur_list = ["cointreau", "amaretto"]


spirit1 = input("What spirit do you have?")
spell_check(spirit1)

if spirit1 in cocktails:
    search(spirit1)
    spirit2 = input("Do you have a second spirit to add?")
    spell_check(spirit2)
    if spirit2 in cocktails:
        search(spirit2, spirit1)
        liqueur1 = input("Do you have a liqueur to add?")
        spell_check(liqueur1)
    else:
        liqueur1 = input("Do you have a liqueur to add?")
        search(liqueur1, spirit1)
        print("How does a %s sound to you?" %(search(liqueur1, spirit1)))

        if liqueur1 in cocktails:
            search(liqueur1, spirit2)

            print("How does a %s sound to you?" %(search(liqueur1, spirit2)))

        elif liqueur1 not in cocktails:
            print()
            print("No Liqueur and just one spirit, ok well let's make a highball")
            mixer = input("What mixer do you have?")
            spell_check(mixer)
            search(mixer, spirit1)
            print("How does a %s sound to you?" %(search(mixer, spirit1)))

