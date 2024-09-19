from django.shortcuts import render

def inicio(req):

    obras = [
        {
            'img': 'src/img/img01.jpg',
            'title': 'La Persistencia de la Memoria',
            'description': 'Una fiesta con surrealismo donde el tiempo se toma una siesta.',
            'url': 'obra',
            'id': 1,
            'time': '9 mins'
        },
        {
            'img': 'src/img/img02.jpg',
            'title': 'Los Elefantes',
            'description': 'Estos elefantes caminan con sus piernas largas, delgadas y frágiles.',
            'url': 'obra',
            'id': 2,
            'time': '9 mins'
        },
        {
            'img': 'src/img/img03.jpg',
            'title': 'El Sacramento de la Última Cena',
            'description': 'Las figuras bíblicas reciben una transformación surrealista.',
            'url': 'obra',
            'id': 3,
            'time': '9 mins'
        },
        {
            'img': 'src/img/img05.jpg',
            'title': 'La Metamorfosis de Narciso',
            'description': 'Un laberinto de espejos lleno de significado que nos deja reflexionando.',
            'url':'obra',
            'id': 5,
            'time': '10 mins'

        },
        {
            'img': 'src/img/img06.jpg',
            'title': 'El Enigma de Hitler',
            'description': 'Una piñata política que desafía nuestra percepción del poder.',
            'url':'obra',
            'id': 6,
            'time': '15 mins'

        },
        {
            'img': 'src/img/img07.jpg',
            'title': 'El Rabo de las Golondrinas',
            'description': 'Una farsa cósmica de caos y orden.',
            'url':'obra',
            'id': 7,
            'time': '15 mins'

        },
        {
            'img': 'src/img/img08.jpg',
            'title': 'El Gran Masturbador',
            'description': 'Una exploración atrevida de fantasías freudianas.',
            'url':'obra',
            'id': 8,
            'time': '18 mins'

        },
        {
            'img': 'src/img/img09.jpg',
            'title': 'El Galacidalacidesoxiribunucleiccacid',
            'description': 'Un paisaje fantástico donde las criaturas bailan en una salsa surrealista.',
            'url':'obra',
            'id': 9,
            'time': '20 mins'

        },
        {
            'img': 'src/img/img04.jpg',
            'title': 'Cisnes Reflejando Elefantes',
            'description': 'Un baile surrealista junto al lago, con cisnes y elefantes intercambiando roles en un tango.',
            'url':'obra',
            'id': 4,
            'time': '22 mins'

        },
        ]


    return render(req, 'inicio.html', {'obras': obras})

def obra(req, set_id):
    sets = {
        '1': ['img01.jpg', ],
        '2': ['img02.jpg', ],
        '3': ['img03.jpg', ],
        '4': ['img04.jpg', ],
        '5': ['img05.jpg', ],
        '6': ['img06.jpg', ],
        '7': ['img07.jpg', ],
        '8': ['img08.jpg', ],
        '9': ['img09.jpg', ],
        
    }
    imagenes = sets.get(set_id, [])
    return render(req, 'obra.html', {'imagenes': imagenes}) 