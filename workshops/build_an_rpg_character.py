

full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    
    if not isinstance(name, str):
        return 'The character name should be a string'

    if len(name) > 10:
        return 'The character name is too long' 

    for char in name:
        if char == " ":
            return   "The character name should not contain spaces"         

    if not all(isinstance(x, int) for x in (strength, intelligence, charisma)):
        return 'All stats should be integers'

    if any(i < 1 for i in (strength, intelligence, charisma)):
        return  'All stats should be no less than 1'   
    
    if any (j > 4 for j in (strength, intelligence, charisma)):
        return 'All stats should be no more than 4'

    if not strength + intelligence + charisma == 7:
        return 'The character should start with 7 points'    
    st_bar = ''
    for a in range(10):
        if a < strength:
            st_bar += full_dot
        else:   
            st_bar += empty_dot
    
    intel_br = ''
    for m in range(10):
        if m < intelligence:
            intel_br += full_dot
        else:
            intel_br += empty_dot
    ch_br = ''
    for q in range(10):
        if q < charisma:
            ch_br += full_dot
        else:
            ch_br += empty_dot
    return f"{name}\nSTR {st_bar}\nINT {intel_br}\nCHA {ch_br}"  
    

create_character("ren", 4, 2, 1)






