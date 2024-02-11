def get_slope(x1, y1, x2, y2):
    #nedokazal jsem implementovat desetina cisla
    if x2 - x1 == 0:
        return None  # Vertikální přímka
    return (y2 - y1) / (x2 - x1)

def get_intercept(x, y, slope):
    if slope is None:
        return None  # Vertikální přímka
    return y - slope * x

def check_collinear(x1, y1, x2, y2, x3, y3):
    slope1 = get_slope(x1, y1, x2, y2)
    slope2 = get_slope(x1, y1, x3, y3)
    if slope1 is None and slope2 is None:
        return True  # Všechny body jsou ve svislé linii
    elif slope1 == slope2:
        return True  # Všechny body leží na stejné přímce
    else:
        return False

def find_middle_point(x1, y1, x2, y2, x3, y3):
    if x1 == x2 == x3 and y1 == y2 == y3:
        return None  # Všechny body splývají
    elif x2 > x1 > x3 or x2 < x1 < x3:
        return "A" 
    elif x1 > x2 > x3 or x1 < x2 < x3:
        return "B"
    elif x1 > x3 > x2 or x1 < x3 < x2:
        return "C"
    elif y2 > y1 > y3 or y2 < y1 < y3:
        return "A"
    elif y1 > y2 > y3 or y1 < y2 < y3:
        return "B"
    else:
        return "C"
def overlap(x1, y1, x2, y2,): #souradnice dvou bodu
    if x1 == x2 and y1 == y2: #kontrola překrytí bodů
        return True 
    else:
        return False

def main():
    try:
        print("Bod A:")
        x1, y1 = map(float, input().split())
        print("Bod B:")
        x2, y2 = map(float, input().split())
        print("Bod C:")
        x3, y3 = map(float, input().split())
            
        if overlap(x1, y1, x2, y2) or overlap(x1, y1, x3, y3) or overlap(x2, y2, x3, y3):
            print ("některé body splyvají")

        elif check_collinear(x1, y1, x2, y2, x3, y3):
            print("Body lezi na jedne primce.")
            middle_point = find_middle_point(x1, y1, x2, y2, x3, y3)
            print ("prostřední bod je " + middle_point)
            # if middle_point:
            #
            #       print("Prostredni je bod A.")
            #    elif middle_point[0] == x2 and middle_point[1] == y2:
            #        print("Prostredni je bod B.")
            #    else:
            #        print("Prostredni je bod C.")
        else:
            print("Body nelezi na jedne primce.")

    except ValueError:
        print("Nespravny vstup.")

if __name__ == "__main__":
    main()  