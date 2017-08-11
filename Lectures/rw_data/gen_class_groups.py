def assign_class_groups():
    class_groups = {
            'Courtney Trutna': 'Kristen Slappey',
            'Jaya Pokuri': 'Aniruddh Prakash',
            'Zach Visco': 'Mike Duch',
            'Keaton Armentrout': 'Leighanne Oh, Lyndsey Garcia',
            'Daniel Hull': 'Benjamin Hoover, Varun Gudapati',
            'David Whisler': 'Caroline Kittle',
            'Zoe Roecker': 'Manish Nair',
            'Derek Chan': 'Collyn Heier',
            'Kyle Decker': 'Willie Long',
            'Amy Zhao': 'Katherine Lee',
            'Paige Belliveau': 'Gary Chang',
            'Nia Christian': 'Alissa Ebong',
            'Bora Guner': 'Alden Harwood',
            'Moss Jackson-Atogi': 'Tamma Ketsiri',
            'Anna Knight': 'Cody Morris',
            'Christina Lai': 'Jasmine Lu',
            'Rajalekha Rajamahendiran': 'Samantha Manzer',
            'Filip Mazurek':  'Kelly Sooch',
            'Maitreyee Mittal': 'Jake Son',
            'Kevin Murgas': 'Sai Nimmagadda',
            'Joost Op T Eynde': 'Shu Rayaz',
            'Tommy Sandridge': 'Derek Schulte',
            'Rachel Van Fleet': 'Everardo Villasenor',
            'Vera Xu': 'Ringo Yen',
            'Anthony Yu': 'David Zhou'
            }

    return class_groups
        

def write_csv(class_groups):
    with open('class_groups.csv', 'w') as f:
        [f.write('{0}, {1}\n'.format(k, v)) for (k, v) in class_groups.items()]


def write_json(class_groups):
    import json
    with open('class_groups.json', 'w') as f:
        json.dump(class_groups, f, indent=4)


if __name__ == "__main__":
    class_groups = assign_class_groups()
    write_csv(class_groups)
    write_json(class_groups)
