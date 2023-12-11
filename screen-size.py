import math

confirm_yes = ["y", "yes"]
confirm_no = ["n", "no"]

def length_input(text):
    while True:
        try:
            numinput = input(text)
            if numinput:
                return float(numinput)
            else:
                print('No input found')
        except:
            print("Invalid entry")
            continue

# Ensures ratio is always above 1.00
def aspect_ratio(x, y):
    if x >= 1.00:
        return str(round(x, 2))
    else:
        return str(round(y, 2))

def screen_size(angle):
    lengthz = length_input('Enter the diagonal length of a screen: ')
    lengthy = math.sin(angle) * lengthz
    lengthx = math.cos(angle) * lengthz

    print(f'''
Length = {round(lengthx, 2)}
Height = {round(lengthy, 2)}
''')

# Main code
def main():
    while True:
        xrto = length_input('Enter Aspect ratio for length (x): ')
        yrto = length_input('Enter Aspect ratio for height (y): ')

        ratiox = yrto / xrto
        ratioy = xrto / yrto
        print('Aspect Ratio = '+ aspect_ratio(ratiox, ratioy))

        radianx = math.atan(ratiox)

        anglex = round(math.degrees(radianx), 2)

        print('Angle of Aspect ratio is: ' + str(anglex) + '\N{DEGREE SIGN}')

        screen_size(radianx)

        endinput = confirm('Continue Program (Y/N)? ')
        if endinput:
            continue
        elif not endinput:
            break

# Universal confirmation check
def confirm(text):
    while True:
        prompt = input(text)
        if prompt.lower() in confirm_yes:
            return True
        elif prompt.lower() in confirm_no:
            return False

# Code starts here
if __name__ == '__main__':
    main()