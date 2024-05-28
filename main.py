#Shape Calculator

while True:
    shape_selection = input(' 1. Circle\n a1. Sphere\n 2. Triangle\n b1. Pyramid Volume\n b2. Cone Volume'
                            '\n 3. Rectangle\n 4. Square\n\n"Press 0 to exit"\n Select: ')
    if shape_selection == '0':
        break
    match shape_selection:
        case '1':  # Circle
            circle_option = input('\n 1. Circumference\n 2. Area\n\n Select: ')
            match circle_option:
                case '1':
                    radius = input('Radius: ')
                    print(2 * 3.1415926536 * int(radius))  # Circle circumference
                case '2':
                    radius = input('Radius: ')
                    print(3.1415926536 * int(radius) * int(radius))  # Circle area

        case 'a1':  # Sphere
            sphere_option = input('\n 1. Volume\n 2. Surface Area\n\n Select: ')
            match sphere_option:
                case '1':
                    radius = input('Radius: ')
                    print(4/3 * 3.1415926536 * int(radius)**3)  # Sphere volume
                case '2':
                    radius = input('Radius: ')
                    print(4 * 3.1415926536 * int(radius)**2)  # Sphere surface area

        case '2':  # Triangle
            triangle_option = input('\n 1. Perimeter\n 2. Area\n\n Select: ')
            match triangle_option:
                case '1':
                    side_a, side_b, side_c = input('Side A, Side B, Side C: ').split()
                    print(int(side_a) + int(side_b) + int(side_c))  # Triangle perimeter
                case '2':
                    base, height = input('Base, Height: ').split()
                    print(int(base) * int(height) / 2)  # Triangle area

        case 'b1':  # Pyramid Volume
            base_width, base_length, height = input('Base Width, Base Length, Height: ').split()
            print(int(base_length) * int(base_width) * int(height) / 3)  # Pyramid volume

        case 'b2':  # Cone Volume
            radius, height = input('Radius, Height: ').split()
            print(3.1415926536 * int(radius)**2 * int(height) / 3)  # Cone volume

        case '3':  # Rectangle
            rectangle_option = input('\n 1. Perimeter\n 2. Area\n\n Select: ')
            match rectangle_option:
                case '1':
                    width, height = input('Width, Height: ').split()
                    print(2 * (int(width) + int(height)))  # Rectangle perimeter
                case '2':
                    width, height = input('Width, Height: ').split()
                    print(int(width) * int(height))  # Rectangle area

        case '4':  # Square
            square_option = input('\n 1. Perimeter\n 2. Area\n\n Select: ')
            match square_option:
                case '1':
                    side = input('Side: ')
                    print(int(side) * 4)  # Square perimeter
                case '2':
                    side = input('Side: ')
                    print(int(side) ** 2)  # Square area
