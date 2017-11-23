alien_colors = ['green', 'yellow', 'red']
alien_color = alien_colors[2]

if alien_color in alien_colors[0]:
    print ('You earn 5 points')
elif alien_color in alien_colors[1]:
    print ('You earn 10 points')
elif alien_color in alien_colors[2]:
    print ('You earn 15 points')

human_age = [2, 7, 12, 21, 40, 60]

age = 59

if age <= human_age[0]:
    print ('it\'s baby')
elif age <= human_age[1]:
    print ('it\'s kid')
elif age <= human_age[2]:
    print ('it\'s teen')
elif age <= human_age[3]:
    print ('it\'s young')
elif age <= human_age[4]:
    print ('it\'s man')
elif age <= human_age[5]:
    print ('it\'s old')
else:
    print ('Wisdom')
