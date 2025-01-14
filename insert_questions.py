import os
import django

# Configura la variable de entorno para Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hoteles_responsables.settings')

# Inicializa Django
django.setup()

from surveys.models import Question, Answer


preguntas_y_respuestas = [
    {
        "question": "¿Qué acciones han implementado para reducir el consumo de agua o mejorar su manejo?",
        "respuestas": {
            "a": {"text": "Instalamos sistemas de ahorro de agua y capacitamos al personal.", "value": 3},
            "b": {"text": "Implementamos medidas básicas, como reguladores de flujo.", "value": 2},
            "c": {"text": "Estamos en proceso de desarrollar estrategias para ahorrar agua.", "value": 1},
            "d": {"text": "No hemos implementado acciones específicas para el manejo del agua.", "value": 0},
        },
    },
    {
        "question": "¿Utilizan energías renovables?",
        "respuestas": {
            "a": {"text": "Sí, gran parte de nuestra energía proviene de fuentes renovables.", "value": 3},
            "b": {"text": "Usamos energías renovables para algunas áreas del hotel.", "value": 2},
            "c": {"text": "Estamos evaluando la posibilidad de implementar energías renovables.", "value": 1},
            "d": {"text": "No utilizamos energías renovables actualmente.", "value": 0},
        },
    },
    {
        "question": "¿Cómo gestionan los residuos generados por el hotel?",
        "respuestas": {
            "a": {"text": "Separación de residuos y reciclaje, además de compostaje orgánico.", "value": 3},
            "b": {"text": "Solo separamos residuos básicos (orgánica e inorgánica).", "value": 2},
            "c": {"text": "Realizamos un manejo básico sin medidas específicas.", "value": 1},
            "d": {"text": "No tenemos un sistema de gestión de residuos formal.", "value": 0},
        },
    },
    {
        "question": "¿Las plantas que se encuentran en sus áreas verdes son parte de la flora nativa de su región?",
        "respuestas": {
            "a": {"text": "Sí, todas nuestras plantas son nativas de la región.", "value": 3},
            "b": {"text": "La mayoría de las plantas son nativas, pero también hay algunas exóticas.", "value": 2},
            "c": {"text": "Solo una pequeña parte de nuestras plantas son nativas.", "value": 1},
            "d": {"text": "No contamos con flora nativa en nuestras áreas verdes.", "value": 0},
        },
    },
    {
        "question": "¿Cómo protegen la fauna nativa que se acerca a su hotel o sus alrededores?",
        "respuestas": {
            "a": {"text": "Seguimos protocolos para proteger a la fauna y evitar su interferencia.", "value": 3},
            "b": {"text": "Informamos a los huéspedes sobre la fauna local y cómo respetarla.", "value": 2},
            "c": {"text": "Tomamos medidas básicas, pero no tenemos un protocolo formal.", "value": 1},
            "d": {"text": "No contamos con acciones específicas para proteger la fauna nativa.", "value": 0},
        },
    },
    {
        "question": "¿Cuentan con algún sistema para tratar las aguas residuales?",
        "respuestas": {
            "a": {"text": "Sí, utilizamos un sistema avanzado de tratamiento de aguas residuales.", "value": 3},
            "b": {"text": "Contamos con un sistema básico para tratar las aguas residuales.", "value": 2},
            "c": {"text": "Estamos en proceso de implementar un sistema adecuado.", "value": 1},
            "d": {"text": "No tenemos un sistema de tratamiento de aguas residuales actualmente.", "value": 0},
        },
    },
    {
        "question": "¿Cuentan con algún sistema para reutilizar agua de lluvia?",
        "respuestas": {
            "a": {"text": "Sí, capturamos y reutilizamos el agua de lluvia en múltiples áreas.", "value": 3},
            "b": {"text": "Tenemos un sistema básico de captación y reutilización de agua.", "value": 2},
            "c": {"text": "Estamos evaluando la posibilidad de implementar este sistema.", "value": 1},
            "d": {"text": "No contamos con un sistema de reutilización de agua de lluvia.", "value": 0},
        },
    },
    {
        "question": "¿Colaboran con agricultores locales para abastecer al hotel?",
        "respuestas": {
            "a": {"text": "Sí, gran parte de nuestros alimentos provienen de agricultores locales.", "value": 3},
            "b": {"text": "Compramos algunos productos de agricultores locales.", "value": 2},
            "c": {"text": "Solo colaboramos con agricultores locales en casos puntuales.", "value": 1},
            "d": {"text": "No colaboramos con agricultores locales.", "value": 0},
        },
    },
    {
        "question": "¿Tienen huertos propios para abastecer al hotel?",
        "respuestas": {
            "a": {"text": "Sí, contamos con un huerto que abastece gran parte de nuestros alimentos.", "value": 3},
            "b": {"text": "Tenemos un huerto pequeño para complementar algunos insumos.", "value": 2},
            "c": {"text": "Estamos en proceso de establecer un huerto propio.", "value": 1},
            "d": {"text": "No contamos con huertos propios.", "value": 0},
        },
    },
    {
        "question": "Si tiene alberca, ¿cómo funciona su mantenimiento?",
        "respuestas": {
            "a": {"text": "Utilizamos sistemas ecológicos para el mantenimiento de la alberca.", "value": 3},
            "b": {"text": "Seguimos un mantenimiento tradicional con productos químicos.", "value": 2},
            "c": {"text": "Contratamos servicios externos para el mantenimiento.", "value": 1},
            "d": {"text": "No tenemos alberca.", "value": 0},
        },
    },
    {
        "question": "¿Qué tipo de detergentes utilizan para lavar la ropa de cama, toallas y otros textiles del hotel?",
        "respuestas": {
            "a": {"text": "Utilizamos exclusivamente detergentes biodegradables y certificados como amigables con el medio ambiente.", "value": 3},
            "b": {"text": "Combinamos detergentes biodegradables con opciones tradicionales según la disponibilidad.", "value": 2},
            "c": {"text": "Estamos en proceso de transición hacia el uso de detergentes más sustentables.", "value": 1},
            "d": {"text": "Utilizamos detergentes convencionales y no hemos explorado alternativas amigables con el medio ambiente.", "value": 0},
        },
    },
]


# ID del survey al que se asignarán las preguntas
survey_id = 1

# Inserción en la base de datos
for pregunta in preguntas_y_respuestas:
    # Crear la pregunta
    nueva_pregunta = Question.objects.create(
        survey_id=survey_id,
        question=pregunta["question"],
        value=0,
        type=Question.MULTIPLE_CHOICE,
    )
    
    # Crear las respuestas asociadas a la pregunta
    for inciso, datos_respuesta in pregunta["respuestas"].items():
        Answer.objects.create(
            question=nueva_pregunta,
            text=f"{datos_respuesta['text']}",
            value=datos_respuesta["value"],
        )

print("Preguntas y respuestas insertadas exitosamente.")
