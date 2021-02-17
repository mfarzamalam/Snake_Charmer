def get_formatted_name(firstname,lastname,middlename=''):
    if middlename:
        full_name = firstname + ' ' + middlename + ' ' + lastname
    else:
        full_name = firstname + ' ' + lastname

    return full_name.title()