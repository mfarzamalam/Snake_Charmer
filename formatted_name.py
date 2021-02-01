def formatted_name(f_name , l_name, m_name=''):
    """Return a neatly formatted name with default value"""
    
    if m_name:
        full_name = f_name + ' ' + m_name + ' ' + l_name
    else:
        full_name = f_name + ' ' + l_name
        
    return full_name.title()

name = formatted_name('mike','alex')
print(name)