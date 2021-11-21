def maximum(Array):
    if len(Array) == 1:
        return Array[0]
    else:
        a = maximum(Array[:len(Array)//2])
        b = maximum(Array[len(Array)//2:])
        if a > b:
            return a
        else:
            return b
