#code reviewed and to be optimized

test_settings = {
    "Current User Settings": '',
    "Theme": "dark",
    "Notifications": "enabled",
    "Volume": "high"
}

#for adding a new setting
def add_setting(dict_val,tuple_value):

    # Create lowercase versions of the dictionary keys
    dickeys = [k.lower() for k in dict_val.keys()]
    
    #check for empty values
    if not dict_val or not tuple_value:
        return "the values should not be empty"
    
    #check if setting already exists and if it exist return error message
    if tuple_value[0].lower() in dickeys :
        return f"Setting '{tuple_value[0].lower()}' already exists! Cannot add a new setting with this name."
    
    #add new setting using lowercase versions of the tuple values
    dict_val[str(tuple_value[0].lower())] = str(tuple_value[1].lower())
    return f"Setting '{tuple_value[0].lower()}' added with value '{tuple_value[1].lower()}' successfully!"


#for updating an existing setting
def update_setting(dict_val,tuple_value):


    #get lowercase versions of the dictionary keys
    dickeys = [k.lower() for k in dict_val.keys()]
    if not dict_val or not tuple_value:
        return "the values should not be empty"
    
    #check if setting exists and if not return error message
    if tuple_value[0].lower() not in dickeys :
        return f"Setting '{tuple_value[0].lower()}' does not exist! Cannot update a non-existing setting."
    
    #update setting value using lowercase versions of the tuple values
    dict_val[str(tuple_value[0].lower())] = str(tuple_value[1].lower())
    return f"Setting '{tuple_value[0].lower()}' updated to '{tuple_value[1].lower()}' successfully!"

#for deleting an existing setting
def delete_setting(dict_val,string_value):
     
    
    #get lowercase versions of the dictionary keys
    dickeys = [k.lower() for k in dict_val.keys()]
    if not dict_val or not string_value:
        return "the values should not be empty"
    
    #check if setting exists and if not return error message
    if string_value.lower() not in dickeys :  
        return "Setting not found!"
    
    #remove settings using pop method
    dict_val.pop(str(string_value.lower()))
    return f"Setting '{string_value}' deleted successfully!"

#fro viewing all settings
def view_settings(settings):

    #check for empty settings and if empty return error message
    if not settings:
        return "No settings available."
   
    #capitalize the first letter of each key for better readability
    settings = {key.capitalize():value for key,value in settings.items()}

    #format the settings for display
    lines = [f"{k}: {v}" for k, v in settings.items() if v]

    #create the final formatted output
    formatted_output = "Current User Settings:\n" + "\n".join(lines)

    return formatted_output + "\n"

