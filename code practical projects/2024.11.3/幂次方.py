def assign(n):
    if n ==1:
        return "2(0)"
    if n ==2:
        return "2"
    if n ==3:
        return "2+2(0)"
    if n!=2:
        d=n
        list_01=[]
        while d:
            list_01.append(d%2)
            d=d//2
        out=""
        for i in range(len(list_01)-1,1,-1):
            if list_01[i] == 0:
                continue
            if list_01[i] != 0 and i==len(list_01)-1:
                out=f"2({assign(i)})"
            if list_01[i] != 0 and i <len(list_01)-1:
                out=out+"+"+f"2({assign(i)})"
        if list_01[1] !=0 :
            out =out +"+"+"2"
        if list_01[0] != 0:
            out =out +"+"+"2(0)"
        return out
print(assign(int(input())).strip())
            
        
    
    

        
   
           

            

        