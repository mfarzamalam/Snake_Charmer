alien_1 = {
    'color':'blue',
    'height':6,
    'speed':'slow'
}

alien_2 = {
    'color':'green',
    'height':8,
    'speed':'medium'
}

alien_3 = {
    'color':'yellow',
    'height':12,
    'speed':'medium'
}

aliens = [alien_1,alien_2,alien_3]

for alien in aliens:
    print(alien)


aliens = []

for alien in range(1,11):
    new_alien = {'color':'green','height':0 + alien,'speed':'medium'}
    aliens.append(new_alien)

print(str(len(aliens)))

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'slow'
    print(alien)


print(aliens)

fav_language = {
    'sarah':['c','python'],
    'jen':['java'],
    'jacob':['jerry']
}

for name,languages in fav_language.items():
    if len(languages) > 1:
        print("\n"+name.title() +" fav language are ")
    else:
        print("\n"+name.title() +" fav language is ")
    
    for language in languages:
        print(language.title())