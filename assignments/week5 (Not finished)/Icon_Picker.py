p_icon_list = ['@', '#', '$', 'Σ', '߷']
p_icon_dict = {
        '1': '@',
        '2': '#',
        '3': '$',
        '4': 'Σ',
        '5': '߷',
        '6': 'ඞ'
}

def p_icon():
    while True:
        print("Which symbol you choose? Use a number corresponding to symbol")
        for i, symbol in enumerate(p_icon_list, start=1):
            print(f'{i}: {symbol}')
        p_icon = input('> ')
        if p_icon in p_icon_dict:
            print(f"You chose {p_icon_dict[p_icon]}.")
            return p_icon_dict[p_icon]
        else:
            print("Please choose a number corresponding to symbol")

if __name__ == "__main__":
    p_icon()