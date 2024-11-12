import geometry
#print(dir(geometry))
def pointyShapeVolume(x,h,square):
    if square:
        base=geometry.SquareArea(x)
    else:
        base=geometry.SquareArea(x)
        return h*base/3.0
print("Area of Pyramid is :",pointyShapeVolume(4,2.6,True))
print("Area of Pyramid is :",pointyShapeVolume(4,2.6,False))    
