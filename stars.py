#part I
# def draw_stars(arr):
    
#     for num in arr:
#         stars = ""        
#         for i in range(num):
#             stars += "*"
#         print stars

# draw_stars([4, 6, 1, 3, 5, 7, 25])

#part II

def draw_stars(arr):
    
    for item in arr:
        if type(item) is str:
            string = "" 
            for i in range(len(item)):
                string += item[0].lower()
            print string
        else: 
            string = ""        
            for i in range(item):
                string += "*"
            print string

draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]) 