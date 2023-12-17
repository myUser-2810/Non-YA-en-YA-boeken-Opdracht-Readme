# YA en Non-YA Boeken Moeilijkheidsgraad Analyse
# Beschrijving
Het project draait om het analyseren en vergelijken van de moeilijkheidsgraad tussen kinderboeken (niet-Young Adult) en jeugdboeken (Young Adult). Het maakt gebruik van Python om tekstbestanden van beide categorieën te verzamelen, analyseren en statistisch te vergelijken op basis van woord- en zinslengte, evenals de frequentie van speciale leestekens. De conclusie is gebaseerd op een T-test die aantoont of er een significant verschil is tussen de moeilijkheidsgraden van deze boeken.
# Vereisten
Externe modules die worden gebruikt zijn onder andere:

-Jupiter Notebooks

-Python 3.x

-Calibre

-Project Gutenberg

-SciPy

-Matplotlib
# Inhoud van de projectmap
De andere bestanden moeten in de volgende volgorde worden uitgevoerd:
1) Data processing_nltk.py map: Maakt gebruik van de `os`-module om de huidige map op te halen en creëert een bestandspad voor een bestand genaamd 'data.csv'.
Downloadt via de `nltk`-bibliotheek het 'punkt'-model dat wordt gebruikt voor zinsegmentatie (sent_tokenize) en het identificeren van leestekens in tekst. 

2) Boeknamen in categorien.txt map: Haalt bestandsnamen op in de mappen 'YA boeken' en 'non YA boeken' voor verdere verwerking en analyse. Zowel de YA als non YA boeken omvatten een reeks bestaande ebooks, en werden verzameld via de Project Gutenberg-website en de online bibliotheek. 

3) Ya boeken analyse statistieken map: Analyseert YA-boeken en berekent statistieken zoals aantal woorden, zinnen en speciale tekens, en het gemiddelde aantal woorden en speciale tekens per zin.

4) Non-YA boeken analyse statistieken map: Voert soortgelijke analyses uit op non-YA-boeken en berekent statistieken voor deze categorie.

5) Moeilijkheidsgraad tussen YA en Non-YA plot map: Gebruikt SciPy en Matplotlib om grafieken te genereren en T-tests uit te voeren voor verschillende statistieken tussen YA- en non-YA-boeken. Het visualiseert de gegevens en bepaalt of er significante verschillen zijn tussen de twee categorieën op basis van de uitgevoerde statistische tests.
# Gebruik
Anderen kunnen de code gebruiken door de Jupiter Notebooks en Python-scripts te openen in een omgeving met Jupiter Notebook en Python 3.x. Ze moeten ervoor zorgen dat de vereiste externe modules (Calibre, SciPy, Matplotlib) zijn geïnstalleerd. Door de code door te lopen, kunnen ze de stappen begrijpen die zijn genomen voor gegevensverzameling, -analyse en conclusievorming met betrekking tot de moeilijkheidsgraad van Young Adult en niet-Young Adult boeken. Men kan de mappen; YA boeken Analyse statistieken en Non-YA boeken Analyse statistieken gebruiken voor het analyseren van tekstuele inhoud, zoals het tellen van woorden, zinnen en speciale tekens. Men kan door de Moeilijkheidsgraad tussen YA en Non-YA plot map, bepaalde statistieken berekenen en visueel presenteren door het vergelijken van datasets.
