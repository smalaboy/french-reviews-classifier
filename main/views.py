from django.http import JsonResponse
from django.shortcuts import render
import tensorflow as tf

from classifier.settings import BASE_DIR

CLASSES_MAP = {
    0: 'Négatif',
    1: 'Positif'
}

# Modèle de classification
# model = tf.keras.models.load_model(BASE_DIR / 'static/final_saved_models/model')

def infer(text: str)->tuple[str, float]:
    """
    Inférence sur le modèle de machine learning
    :param text: Texte à classer
    :return: la classe et la probabilité d'appartenance
    """
    model = tf.keras.models.load_model(BASE_DIR / 'static/final_saved_models/model')
    probs = model.predict([text])
    print(probs)
    prediction = tf.argmax(tf.constant(probs[0]))
    print(prediction)
    return CLASSES_MAP[int(prediction)], float(probs[0][prediction])


def classify(request):
    """
    API de classification. Appelle la fonction infer pour obtenir les résultats
    :param request: WSGIRequest
    :return: la prediction et la probabilité sous forme de json
    """
    text = request.GET.get('text')
    class_, proba = infer(text)
    return JsonResponse({
        "prediction": class_,
        "probability": proba
    })


def home_page(request):
    """
    Vue de la page d'accueil
    :param request: WSGIRequest
    :return:
    """
    return render(request, 'home.html')
