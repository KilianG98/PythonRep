def Restriction(Cuts, n, circ=False):
    if Cuts ==[]:
        return[n]

    lengthOfSubstrings = []
    pos = 0

    if not circ:
        for i in range (len(Cuts)):
            for cut in Cuts[i]:
                lengthOfSubstrings.append([cut - pos])
                pos = cut
        if (n-pos) != 0:
            lengthOfSubstrings.append([n-pos])
    else:
        bool = True
        for i in range (len(Cuts)):
            for cut in Cuts[i]:
                if cut > pos:
                    lengthOfSubstrings.append([cut - pos])
                    pos = cut
                else:
                    bool = False
                    lengthOfSubstrings.append([n-pos+cut])
                    pos = cut
        if bool:
            lengthOfSubstrings.append([n-pos])


    return(lengthOfSubstrings)
