def liiguta(asukoht, suund):
    x, y = asukoht
    
    if suund == "Edasi":
        return (x, y + 1)
    elif suund == "Tagasi":
        return (x, y - 1)
    elif suund == "Vasakule":
        return (x -1, y)
    elif suund == "Paremale":
        return (x + 1, y)
    else:
        return asukoht