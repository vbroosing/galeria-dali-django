from django.shortcuts import render

def inicio(req):
    return render(req, 'inicio.html')

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