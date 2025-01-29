import os
import django

# Configura la variable de entorno para Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hoteles_responsables.settings')

# Inicializa Django
django.setup()

from surveys.models import Solutions, Survey, Question, Answer

soluciones = [
    # Puntaje 26-33
    {
        "titulo": "Conservación de la biodiversidad",
        "texto": "Continuar invirtiendo en la conservación de la biodiversidad local, trabajando con expertos y asociaciones medioambientales.",
        "min": 26,
        "max": 33,
    },
    {
        "titulo": "Mejora de la eficiencia energética",
        "texto": "Aumentar el uso de tecnologías innovadoras para mejorar la eficiencia energética, como paneles solares.",
        "min": 26,
        "max": 33,
    },
    {
        "titulo": "Aguas pluviales",
        "texto": "Expandir la reutilización de aguas pluviales. Si ya cuentas con un sistema de captación de agua puedes expandirlo. En caso de no contar con él, puedes implementarlo y utilizar el agua para lavado de patios, riego de áreas verde, etc.",
        "min": 26,
        "max": 33,
    },
    {
        "titulo": "Fomento de áreas verdes nativas",
        "texto": "Establecer más áreas verdes con especies nativas. Si es necesario, te puedes acercar a un biólogo para que te oriente.",
        "min": 26,
        "max": 33,
    },
    {
        "titulo": "Gestión de residuos",
        "texto": "Crear un programa de reciclaje en el hotel, integra y capacita al personal.",
        "min": 26,
        "max": 33,
    },
    {
        "titulo": "Educación ambiental para huéspedes y comunidad en general",
        "texto": "Integrar información sobre sensibilización del uso responsable de agua, energía, áreas verdes. Puedes usar carteles o señalización en áreas comunes y en cada habitación.",
        "min": 26,
        "max": 33,
    },
    {
        "titulo": "Protección de fauna local",
        "texto": "Establecer protocolos claros que guíen al personal sobre cómo interactuar de manera respetuosa con la fauna nativa que habita o se acerca al hotel. Esto puede incluir medidas para evitar el contacto directo con animales salvajes, como no alimentarlos ni interferir en su comportamiento natural.",
        "min": 26,
        "max": 33,
    },
    {
        "titulo": "Material educativo sobre fauna local",
        "texto": "Proporcionar material educativo a los huéspedes sobre la fauna nativa de la región, destacando la importancia de respetar y proteger a los animales locales. Puedes incluir folletos informativos, señalización en áreas comunes y actividades educativas, como charlas.",
        "min": 26,
        "max": 33,
    },

    # Puntaje 18-25
    {
        "titulo": "Gestión de residuos",
        "texto": "Optimizar el sistema de gestión de residuos, ampliando el reciclaje y compostaje en todas las áreas del hotel. Es importante integrar a todo el personal y capacitarlo.",
        "min": 18,
        "max": 25,
    },
    {
        "titulo": "Mejora de la eficiencia energética",
        "texto": "Iniciar el uso de fuentes de energía renovable, como paneles solares.",
        "min": 18,
        "max": 25,
    },
    {
        "titulo": "Educación ambiental",
        "texto": "Crear un programa de educación ambiental para los huéspedes y comunidad en general, involucrándolos en prácticas sostenibles durante su estancia. Puedes usar carteles o señalización en áreas comunes y en cada habitación.",
        "min": 18,
        "max": 25,
    },
    {
        "titulo": "Aguas pluviales",
        "texto": "Revisar los sistemas de ahorro de agua y considerar la instalación de un sistema de captación de aguas pluviales. Si ya cuentas con un sistema de captación de agua puedes expandirlo. En caso de no contar con él, puedes implementarlo y utilizar el agua para lavado de patios, riego de áreas verde, etc.",
        "min": 18,
        "max": 25,
    },
    {
        "titulo": "Uso de productos ecológicos",
        "texto": "Promover el uso de productos ecológicos, como detergentes biodegradables y cosméticos naturales para huéspedes.",
        "min": 18,
        "max": 25,
    },
    {
        "titulo": "Fomento de áreas verdes nativas",
        "texto": "Establecer más áreas verdes con especies nativas. Si es necesario, te puedes acercar a un biólogo para que te oriente.",
        "min": 18,
        "max": 25,
    },
    {
        "titulo": "Protección de fauna local",
        "texto": "Establecer protocolos claros que guíen al personal sobre cómo interactuar de manera respetuosa con la fauna nativa que habita o se acerca al hotel. Esto puede incluir medidas para evitar el contacto directo con animales salvajes, como no alimentarlos ni interferir en su comportamiento natural.",
        "min": 18,
        "max": 25,
    },
    {
        "titulo": "Material educativo sobre fauna local",
        "texto": "Proporcionar material educativo a los huéspedes sobre la fauna nativa de la región, destacando la importancia de respetar y proteger a los animales locales. Puedes incluir folletos informativos, señalización en áreas comunes y actividades educativas, como charlas.",
        "min": 18,
        "max": 25,
    },

    # Puntaje 9-17
    {
        "titulo": "Ahorro de agua",
        "texto": "Implementar prácticas básicas de ahorro de agua, como la instalación de reguladores de flujo en duchas y grifos. También puedes implementar carteles en las habitaciones para concientizar a los huéspedes sobre el uso responsable del agua.",
        "min": 9,
        "max": 17,
    },
    {
        "titulo": "Gestión de residuos",
        "texto": "Establecer un programa de reciclaje básico para separar residuos reciclables de los no reciclables. Es importante integrar y capacitar a todo el personal.",
        "min": 9,
        "max": 17,
    },
    {
        "titulo": "Mejora de la eficiencia energética",
        "texto": "Empezar a utilizar energías renovables en áreas específicas, como el calentamiento del agua o iluminación exterior a través de paneles solares.",
        "min": 9,
        "max": 17,
    },
    {
        "titulo": "Sensibilización ambiental del personal",
        "texto": "Introducir la educación ambiental en el programa de inducción de nuevos empleados, para sensibilizarlos sobre la importancia de la sostenibilidad.",
        "min": 9,
        "max": 17,
    },
    {
        "titulo": "Fomento de áreas verdes nativas",
        "texto": "Considerar la plantación de especies nativas en las áreas verdes del hotel, mejorando la biodiversidad local. Si es necesario, te puedes acercar a un biólogo para que te oriente.",
        "min": 9,
        "max": 17,
    },
    {
        "titulo": "Educación ambiental para huéspedes y comunidad en general",
        "texto": "Integrar información sobre sensibilización del uso responsable de agua, energía, áreas verdes. Puedes usar carteles o señalización en áreas comunes y en cada habitación.",
        "min": 9,
        "max": 17,
    },
    {
        "titulo": "Protección de fauna local",
        "texto": "Establecer protocolos claros que guíen al personal sobre cómo interactuar de manera respetuosa con la fauna nativa que habita o se acerca al hotel. Esto puede incluir medidas para evitar el contacto directo con animales salvajes, como no alimentarlos ni interferir en su comportamiento natural.",
        "min": 9,
        "max": 17,
    },
    {
        "titulo": "Material educativo sobre fauna local",
        "texto": "Proporcionar material educativo a los huéspedes sobre la fauna nativa de la región, destacando la importancia de respetar y proteger a los animales locales. Puedes incluir folletos informativos, señalización en áreas comunes y actividades educativas, como charlas.",
        "min": 9,
        "max": 17,
    },

    # Puntaje 0-8
    {
        "titulo": "Gestión de residuos",
        "texto": "Comenzar con la implementación de sistemas de reciclaje básicos, separando residuos orgánicos e inorgánicos. Después puedes integrar un sistema de reciclaje más complejo. Es importante integrar y capacitar a todo el personal.",
        "min": 0,
        "max": 8,
    },
    {
        "titulo": "Ahorro de agua",
        "texto": "Instalar sistemas de ahorro de agua, como reguladores en los inodoros y duchas.",
        "min": 0,
        "max": 8,
    },
    {
        "titulo": "Uso de productos amigables con el medio ambiente",
        "texto": "Implementar el uso de detergentes biodegradables y productos de limpieza menos contaminantes.",
        "min": 0,
        "max": 8,
    },
    {
        "titulo": "Fomento de áreas verdes nativas",
        "texto": "Iniciar un proyecto piloto de jardines con plantas nativas para mejorar la biodiversidad en las áreas verdes del hotel. Si es necesario, te puedes acercar a un biólogo para que te oriente.",
        "min": 0,
        "max": 8,
    },
    {
        "titulo": "Educación ambiental para huéspedes y comunidad en general",
        "texto": "Integrar información sobre sensibilización del uso responsable de agua, energía, áreas verdes. Puedes usar carteles o señalización en áreas comunes y en cada habitación.",
        "min": 0,
        "max": 8,
    },
    {
        "titulo": "Protección de fauna local",
        "texto": "Establecer protocolos claros que guíen al personal sobre cómo interactuar de manera respetuosa con la fauna nativa que habita o se acerca al hotel. Esto puede incluir medidas para evitar el contacto directo con animales salvajes, como no alimentarlos ni interferir en su comportamiento natural.",
        "min": 0,
        "max": 8,
    },
    {
        "titulo": "Material educativo sobre fauna local",
        "texto": "Proporcionar material educativo a los huéspedes sobre la fauna nativa de la región, destacando la importancia de respetar y proteger a los animales locales. Puedes incluir folletos informativos, señalización en áreas comunes y actividades educativas, como charlas.",
        "min": 0,
        "max": 8,
    }
]


# ID del survey al que se asignarán las preguntas
survey_id = 1

for solution in soluciones:
    nueva_solucion = Solutions.objects.create(
        survey_id=survey_id,  
        title_solution= solution['titulo'],
        text= solution['texto'],
        score_min= solution['min'],  
        score_max= solution['max']
    )

print("Preguntas y respuestas insertadas exitosamente.")
