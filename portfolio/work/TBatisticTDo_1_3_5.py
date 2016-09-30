def how_eligible():
    essay = raw_input("Enter your essay: ")
    score = 0
    if "?" in essay:
        score = score + 1
    if '"' in essay:
        score = score + 1
    if "," in essay:
        score = score + 1
    if "!" in essay:
        score = score + 1
    print score
    
how_eligible()