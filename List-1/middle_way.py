def middle_way(a, b):
    x=len(a)
    y=len(b)
    if x%2!=0 and y%2!=0:
        if x%2!=0:
            middle=int((x-1)/2)
            middle_element1=a[middle]
        if y%2!=0:
            middle=int((y-1)/2)
            middle_element2=b[middle]
        return [middle_element1,middle_element2]    
        