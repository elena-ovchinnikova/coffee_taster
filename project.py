from simpleimage import SimpleImage

DEFAULT_FILE = 'countries.jpg'


def main():
    print("\nHello! My name is Coffee Taster, and I will help you navigate through the world of coffee :)")
    print("It's grown in many countries, and its taste differs depending on the climate.")
    print("Tell me what coffee you like, and I will show countries that grow it!")
    answer = input("\nPress ENTER to continue. Type 'all' to see the map. Type 'q' to quit. ")
    while answer != 'q':
        if answer == '':
            color = get_taste()
            countries = filter_color(color)
            describe(color)
            countries.show()
        elif answer == 'all':
            SimpleImage(DEFAULT_FILE).show()
        answer = input("\nPress ENTER to continue. Type 'all' to see the map. Type 'q' to quit. ")


def get_taste():
    # input: a word from user (acidic, sweet, bitter/dark)
    # output: a color corresponding to a taste
    taste = input("\nWhat coffee do you like: acidic, sweet, or bitter? ")
    taste_palette = {'acidic': 'green', 'sweet': 'red', 'bitter': 'blue'}
    while taste_palette.get(taste) == None:
        taste = input("Please, type one of these words: acidic, sweet, or bitter. ")
    color = taste_palette.get(taste)

    return color


def filter_color(color):
    """
    this function leaves only pixels of given and black color
    and returns a map
    """
    image = SimpleImage(DEFAULT_FILE)
    for px in image:
        green = px.green < (px.red + px.blue)
        red = px.red < (px.blue + px.green)
        blue = px.blue < (px.green + px.red)
        average = (px.red + px.green + px.blue) / 3
        if average > 75:
            if color == 'blue' and blue == True:
                px.red = 255
                px.green = 255
                px.blue = 255
            elif color == 'red' and red == True:
                px.red = 255
                px.green = 255
                px.blue = 255
            elif color == 'green' and green == True:
                px.red = 255
                px.green = 255
                px.blue = 255

    return image


def describe(color):
    # input: taste of coffee: acidic, sweet or bitter
    # output: list of countries on the map, three descriptors
    if color == 'blue':
        print("\nYemen, India, Indonesia, Peru, and Brazil grow coffee that you like! \nCoffee from these countries tastes somewhat heavy and nutty.")
    elif color == 'red':
        print("\nRwanda, Uganda, Kenya, China, Vietnam, Thailand, and Colombia grow coffee that you like! \nCoffee from these countries tastes like fruit or chocolate.")
    elif color == 'green':
        print("\nEthiopia and Burundi grow coffee that you like! \nCoffee from these countries tastes like candied fruit or berry.")


if __name__ == '__main__':
    main()
