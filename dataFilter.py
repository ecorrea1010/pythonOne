DATA = [
    {
        'name': 'Luisa Perez',
        'age': 20,
        'organization': 'ceiba SA',
        'language': 'PHP'
    },
    {
        'name': 'Dani Lopera',
        'age': 27,
        'organization': 'digitalBots',
        'language': 'Javascript'
    },
    {
        'name': 'Eduardo Herrera',
        'age': 35,
        'organization': 'eBFactory SAS',
        'language': 'Python'
    },
    {
        'name': 'Leidys Sanchez',
        'age': 18,
        'organization': 'canonical',
        'language': 'Java'
    },
    {
        'name': 'David',
        'age': 47,
        'organization': 'eBFactory SAS',
        'language': 'c#'
    },
    {
        'name': 'Juan',
        'age': 31,
        'organization': 'Associate',
        'language': 'Javascript'
    },
    {
        'name': 'Daniela',
        'age': 19,
        'organization': 'canonical',
        'language': 'Python'
    },
    {
        'name': 'Pablo',
        'age': 48,
        'organization': 'DigiSoft',
        'language': 'Java'
    }
]

def run():
    getAllDevs('PHP')

def getAllDevs(language):
    all_devs = [developer['name'] for developer in DATA if developer['language'] == language]
    adults = list(filter(lambda developer: developer['age'] > 18, DATA))
    adults = list(map(lambda developer: developer['name'], adults))
    old_people = list(map(lambda developer: developer | {'old': developer['age'] > 40}, DATA))

    for developer in old_people:
        print(developer)

if __name__ == '__main__':
    run()