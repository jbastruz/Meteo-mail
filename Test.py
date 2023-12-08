import requests
import smtplib

# Paramètres de l'API OpenWeatherMap
API_KEY = "ffc1be89ebd96754d96ded5a9351de80"

# Définition des fonctions
def get_weather(city):
    """Récupère les données météo pour une ville donnée"""

    # URL de l'API OpenWeatherMap
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=fr&appid={}".format(city, API_KEY)

    # Récupération des données météo
    response = requests.get(url)
    response.raise_for_status()

    # Dictionnaire contenant les données météo
    weather = response.json()

    return weather

def send_mail(to_address, subject, body):
    """Envoi un mail"""

    # Connexion au serveur SMTP
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("jbastruz@gmail.com", "xoqk asvz beou rrmh")

    # Envoi du mail
    message = "Subject: {}\n\n{}".format(subject, body)
    server.sendmail("jbastruz@gmail.com", to_address, message.encode("utf-8"))

    server.quit()

# Programme principal
if __name__ == "__main__":
    # Nom de la ville
    city = "Brussels"

    # Récupération des données météo
    weather = get_weather(city)
    
    # Données météo
    temperature = weather["main"]["temp"]
    weather_description = weather["weather"][0]["description"]

    # Envoi du bulletin météo par mail
    send_mail("jbastruz@protonmail.com", "Météo à Bruxelles", "La température à Bruxelles est de {} degrés. Il fait {}.".format(temperature, weather_description))
