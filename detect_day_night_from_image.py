# Read image foem input
values = []
days = 0
nights = 0
while True:
    try:
        line = input()
        pixels = line.split(' ')
        for i in range(len(pixels)):
            chanels = pixels[i].split(',')
            gray_pixel_value = 0.07*float(chanels[0]) + 0.72*float(chanels[1]) + 0.21*float(chanels[2])
            if gray_pixel_value > 78 :
                days = days + 1
            else:
                nights = nights + 1        
    except EOFError:
        break;
if days > nights:
    print('day')
else:
    print('night')