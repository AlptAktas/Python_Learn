def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name.""" # docstring
    
    return  f"{f_name.title()} {l_name.title()}" # title() capitalizes the first letter of each word

print(format_name("johN", "doe"))  # John Doe