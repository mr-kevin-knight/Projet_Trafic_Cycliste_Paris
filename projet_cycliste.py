# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

###Barre latérale
#création d'un titre dans la barre latérale
st.sidebar.markdown('<style>h1{font-size:45px !important;text-align: center;margin-top: 50px;}</style>', unsafe_allow_html=True)

# Titre du sommaire dans la barre latérale
st.sidebar.title("Le trafic cycliste à Paris")

# Ajout image dans la barre latérale
st.sidebar.image("image_velo.png")

# Options du sommaire
pages = ["Introduction", "Pre-processing", "Datavisualisation", "Modelisation", "Conclusion"]
# Augmenter la taille de la police pour le sommaire dans la barre latérale
st.sidebar.markdown('<style>label[for="radio-options-0"], label[for="radio-options-1"], label[for="radio-options-2"], label[for="radio-options-3"], label[for="radio-options-4"]{font-size: 24px !important;}</style>', unsafe_allow_html=True)
page = st.sidebar.radio("", pages)

#informations
st.sidebar.info(

"Laurent Benhamou "
"\n\n"
#"[linkedIn](), "
"Kevin Chevalier "
"\n\n"
#"[linkedIn](), "
"Estelle Therin "
#"[linkedIn]()"
"\n\n"
"Bootcamp Data Analyst Juin 2023, "
"[DataScientest](https://datascientest.com/)"
"\n\n"
)


### 1ERE PAGE - Introduction
#Insertion de l'image de couverture
if page == pages[0]:
    image = Image.open('photo_couverture.png')
    st.image(image)

    # Affichage du titre avec le trait de couleur
    st.markdown(
        """
        <h1 style='border-bottom: 5px solid #0072B2; padding-bottom: 10px;'>Le trafic cycliste à Paris</h1>
        """,
    unsafe_allow_html=True
    )

    # Sous-titre Contexte
    st.markdown(
        """
        <h2>Contexte</h2>
        <p style="font-size: 18px; text-align: justify;">La Ville de Paris déploie depuis plusieurs années des compteurs à vélo permanents pour évaluer le développement de la pratique cycliste.<br>
        Ce projet a pour objectif d’effectuer une <strong>analyse des données</strong> récoltées par ces compteurs vélo afin de visualiser les <strong>horaires</strong> et les <strong>zones d'affluences</strong> en utilisant des données de comptage détaillées.
        En explorant les schémas saisonniers et les facteurs d'influence tels que la température, l'heure de la journée ou même le jour de la semaine, nous cherchons à comprendre les <strong>tendances du trafic</strong> cycliste à travers plusieurs visualisations.<br>
        En appliquant des techniques de <strong>modélisation statistique</strong>, nous créerons des <strong>modèles de prévision</strong> pour anticiper le nombre de passages de vélos.
        Les résultats obtenus pourraient informer les initiatives de mobilité urbaine, encourager l'utilisation du cyclisme en tant que moyen de transport durable à Paris et développer les axes cyclables.
        </p>
        """,
        unsafe_allow_html=True
        )

    # Sous-titre Cartographie des compteurs de vélos
    st.markdown(
        """
        <h2>Cartographie des compteurs de vélos</h2> 
        """,
        unsafe_allow_html=True
        )
    #Importation de la carte intéractives des compteurs
    # Code obligatoire personnel pour utiliser le site Mapbox
    import os
    os.environ['MAPBOX_TOKEN'] = "pk.eyJ1IjoiZXN0ZWxsZXRoZXJpbiIsImEiOiJjbGp3eXdjaHkwcTNzM2ZwNGo0cXc0d3FhIn0.A120aMmidCQvTivL9WJXgQ"

    #importation du DataFrame df_trafic
    df_carte=pd.read_csv('df_carte_streamlit.csv')

    # Création du DataFrame qui sera utilisé pour créer la carte
   
    df_carte['NB_passage'] = round(df_carte['NB_passage'], 0)


    # Récupération du jeton d'accès Mapbox à partir de la variable d'environnement
    mapbox_token = os.environ['MAPBOX_TOKEN']

    # Utilisation du DataFrame df_carte
    fig = px.scatter_mapbox(df_carte, lat="lat", lon="lon", size="NB_passage",
                            color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=12)

    # Configuration du jeton d'accès Mapbox
    fig.update_layout(mapbox=dict(accesstoken=mapbox_token))

    # Création du texte à afficher sur chaque marqueur
    text = ['Adresse: {}, Nb_passage: {}'.format(adresse, nb_passage)
            for adresse, nb_passage in zip(df_carte['Adresse_site'], df_carte['NB_passage'])]

    # Affichage de l'adresse et du nombre de passages sur chaque marqueur
    fig.update_traces(text=text, hovertemplate='%{text}')

    # Affichage de la carte dans Streamlit
    st.plotly_chart(fig)

    #Description de la carte des compteurs
    st.markdown(
        """
        <p style="font-size: 18px; text-align: justify;"> On dénombre <strong>77 sites de comptage</strong>. La répartition des radars sur la ville 
        de Paris <strong>n’est pas équilibrée</strong>: la partie nord ouest de Paris ne compte quasiment pas de radars.</p>
    
         """,
         unsafe_allow_html=True
         )

    # Sous-titre jeu de données et description
    st.markdown(
        """
        <h2>Jeu de données</h2> 
        <p style="font-size: 18px; text-align: justify;"> Pour réaliser ce projet, nous avons utilisé le fichier mis à notre disposition: <br> <u>‘comptage-velo-donnees-compteurs.csv’</u>
        disponible sur l’open data de la Ville de Paris.<br>
        Ce fichier couvre <strong>15 mois glissants de données</strong> et représente 917 490 lignes et 16 colonnes. Il inclut les variables suivantes:</p>
        """,
        unsafe_allow_html=True
        )
    # Chargement du DataFrame à partir du fichier initial de données
    df = pd.read_csv('df_streamlit.csv',sep=',')

    # Affichage des 5 premières lignes du DataFrame
    st.dataframe(df.head())
    
    # Explication jeu de données 
    st.markdown(
        """
        <p style="font-size: 18px; text-align: justify;"> 
        A partir de ce jeu de données, plusieurs <strong>traitements</strong> ont été effectués afin de pouvoir <strong>clarifier</strong> et <strong>exploiter</strong> au mieux les données relatives
        au trafic cycliste. Ces opérations sont détaillées dans l'onglet pre-processing.</p>
        """,
        unsafe_allow_html=True
        )


### 2EME PAGE - Preprocessing
#Insertion de l'image de couverture
if page == pages[1]:
    image = Image.open('image_processing.jpg')
    st.image(image)

     # Affichage du titre " Traitements des données" avec le trait de couleur
    st.markdown(
        """
        <h1 style='border-bottom: 5px solid #0072B2; padding-bottom: 10px;'>Traitements des données</h1>
        """,
    unsafe_allow_html=True
    )
    
    # Sous-titre "Exploration et identification des variables"
    st.markdown(
        """
        <h2>Exploration et identification des variables</h2>
        <p style="font-size: 18px; text-align: justify;"> Depuis le jeu de données initial <u>‘comptage-velo-donnees-compteurs.csv’</u>,
        nous avons identifié les variables qui expliquaient les <strong>flux de trafic</strong> et qui apportaient des informations spatios-temporelles pertinentes. 
        Les variables répétitives ou celles qui renvoient vers fichiers inaccessibles ont été supprimées.<br> Ci-dessous un aperçu des variables 
        <strong>retenues</strong> et celles que nous avons <strong>supprimées</strong>:
        </p>
        """,
        unsafe_allow_html=True
        ) 

    # Création d'une case à cocher "Afficher les variables"
    show_variables = st.checkbox("Afficher les variables")

    # Si la case est cochée, afficher la liste des variables
    if show_variables:
        variables_retenues = ["Identifiant du compteur", "Nom du compteur", "Identifiant du site de comptage","Nom du site de comptage","Comptage horaire","Coordonnées géographiques","mois_annee_comptage"]  # Remplacez par vos variables réelles
        variables_supprimees = ["VLien vers photo du site de comptage", "Identifiant technique compteur", "ID Photos","test_lien_vers_photos_du_site_de_comptage_","id_photo_1","url_sites","type_dimage"]  # Remplacez par vos variables réelles

        st.write("Variables retenues :", variables_retenues)
        st.write("Variables supprimées :", variables_supprimees)
    
    # Sous-titre "Traitements sur les variables et ajouts de données"
    st.markdown(
        """
        <h2>Traitements et ajouts de données</h2>
        <p style="font-size: 18px; text-align: justify;"> A partir des variables retenues nous avons opéré divers traitements pour le rendre davantage exploitatable.<br>
        Ci-dessous un aperçu des <strong>traitements effectués</strong>:
        </p>
        """,
        unsafe_allow_html=True
        ) 
    # Création d'une case à cocher "Afficher les traitements"
    show_traitements = st.checkbox("Afficher les traitements")
    
    # Si la case est cochée, afficher la liste des traitements
    if show_traitements:
        traitements_effectues = [
            "Suppression des colonnes inutiles du DataFrame",
            "Renommer les colonnes à utiliser pour que les noms soient plus explicites",
            "Split de la variable ‘Date et heure de comptage’ en date_comptage et heure_comptage",
            "Insertion du jour de semaine et du mois",
            "Séparation des coordonnées GPS pour obtenir latitude et longitude",
            "Insertion du jour de semaine et du mois",
            "Réduction de la taille du jeu de données à 12 mois: 01/06/2022 au 31/05/2023"
            ]
        st.write("Traitements effectués :")
        for traitement in traitements_effectues:
            st.write("- " + traitement)

    st.markdown(
    """
    <p style="font-size: 18px; text-align: justify;"> Nous avons également <strong>complété</strong> notre jeu initial par des <strong>données extérieures</strong>.<br>
    Afin de pouvoir évaluer <strong>l'impact métérologique</strong> sur la pratique du vélo nous avons ajouté:\n\n
        - une appréciation de la meteo de chaque jour en 5 catégories: 'météo très défavorable','météo défavorable','météo correcte','météo favorable','météo idéale'",\n\n
        - des données journalières de température moyenne
    </p>
    """,
    unsafe_allow_html=True
    ) 
    
    # Charger les images météos
    image1 = "soleil.png"
    image2 = "parapluie.png"
    image3 = "neige.png"
    image4=  "orage.png"
    
    # Utiliser le widget 'columns' pour afficher les images côte à côte
    col1, col2, col3, col4 = st.columns(4)

    # Afficher les images dans chaque colonne
    col1.image(image1, use_column_width=True)
    col2.image(image2, use_column_width=True)
    col3.image(image3, use_column_width=True)
    col4.image(image4, use_column_width=True)
    

    st.markdown(
    """
    <p style="font-size: 18px; text-align: justify;"> Ci-dessous un aperçu du DataFrame obtenu après traitements:</p>
    """,
    unsafe_allow_html=True
    ) 
    
     # Chargement du DataFrame transformé "df_trafic"
    df_trafic = pd.read_csv('df_trafic_streamlit.csv')

    # Affichage des 5 premières lignes du DataFrame
    st.dataframe(df_trafic.head())
    
    # Sous-titre "Analyse du jeu de données"
    st.markdown(
        """
        <h2>Analyse du jeu de données</h2>
        <p style="font-size: 18px; text-align: justify;">Le jeu de données ne présente <strong>aucun doublon</strong> ni <strong>aucune valeur manquante</strong> à remplacer.
        Il couvre la période du 01/06/2022 au 31/05/2023 soit <strong>12 mois</strong>. <br><br> Parmi les variables on distingue la variable <strong>'NB_passage'</strong> qui correspond à notre <strong>variable cible</strong>.
        Elle est de type <strong>continue</strong> et c'est elle que nous allons chercher à prédire grâce aux modèles de machine learning. <br><br> Le reste des variables sont soit de type
        <strong>catégorielles</strong> soit de type <strong>temporelles</strong> ou <strong>continues</strong>. Elle sont essentielles pour apporter des <strong>explications</strong> à notre variable 'NB_passage'
        </p>
        """,
        unsafe_allow_html=True
        ) 
    
 ### 3EME PAGE - Datavisualisation
 #Insertion de l'image de couverture
if page == pages[2]:
    image = Image.open('graphique_paris.jpeg')
    st.image(image)

    
    # Affichage du titre " Data visualisation" avec le trait de couleur
    st.markdown(
        """
        <h1 style='border-bottom: 5px solid #0072B2; padding-bottom: 10px;'>Data visualisation</h1>
        """,
        unsafe_allow_html=True
        )

    # Sous-titre "Evolution temporelle"
    st.markdown(
        """
        <h2>Evolution temporelle du trafic</h2>
        """,
        unsafe_allow_html=True
        )
    image = Image.open('evol_temporelle.png')
    st.image(image)
    st.markdown(
        """
        <p style="font-size: 18px; text-align: justify;"> La réprésentation graphique de nos 12 mois de données nous permet de constater que le trafic cycliste <strong>diffère selon les mois</strong>. Les mois de <strong>vacances scolaires</strong> ou de <strong>conditions météorologiques</strong> plus exigeantes témoignent d'un <strong>trafic réduit</strong>.<br>
        De même, des jours d'exception, tels que les <strong>grèves nationales</strong>, se traduisent par des <strong>pics</strong> inhabituels, tandis que les <strong>jours fériés</strong> sont marqués par une relative accalmie.<br>
        Les données semble suivre un <strong>schéma rythmique hebdomadaire</strong>, avec des fluctuations plus ou moins régulières d'une semaine à l'autre.<br><br> Il semble donc exister des <strong>interactions</strong> entre la météo, les événements majeurs et les habitudes cyclistes.<br>
        Ces constatations sont analysées plus en détails dans les visualisations ci-dessous.
        </p>
        """,
        unsafe_allow_html=True
        ) 

    # Sous-titre "Analyse du trafic par jour de semaine"
    st.markdown(
        """
        <h2>Analyse du trafic par jour de semaine</h2>
        """,
        unsafe_allow_html=True
        ) 

    # Affichage du graphique du trafic par jour de semaine
    image = Image.open('trafic_jour_sem.png')
    st.image(image)
    st.markdown(
        """
        <p style="font-size: 18px; text-align: justify;"><strong>Les jours de semaine</strong> se distinguent par une affluence cycliste particulièrement <strong>intense</strong>.<br>
        En contraste, <strong>les jours de week-end</strong> sont nettement plus <strong>modérés</strong>, laissant entrevoir une possible association entre le trafic vélo et des <strong>déplacements à caractère professionnel</strong>.
        </p>
        """,
        unsafe_allow_html=True
        ) 
    
    # Sous-titre "Analyse du trafic par heure par jour de semaine"
    st.markdown(
        """
        <h2>Analyse du trafic par heure</h2>
        """,
        unsafe_allow_html=True
        ) 
    # Création de la liste déroulante "semaine" et "week-end"
    selected_option = st.selectbox("Sélectionnez une option", ["semaine (lun-ven)", "week-end (sam-dim)"])

    # Affichage du graphique en fonction de l'option sélectionnée
    if selected_option == "semaine (lun-ven)":
        image = Image.open("heure_semaine.png")
        st.image(image)
    elif selected_option == "week-end (sam-dim)":
        image = Image.open("heure_weekend.png")
        st.image(image)
        
    st.markdown(
        """
        <p style="font-size: 18px; text-align: justify;">La distribution des valeurs <strong>'NB_passage'</strong> ne présente pas le même <strong>profil</strong> en semaine et le week-end.<br>
        Les créneaux horaires de <strong>7h à 10h</strong> et de <strong>17h à 21h</strong> connaissent un trafic nettement plus élevé en <strong>semaine</strong>. Ces observations corroborent l'idée que l'utilisation du vélo est principalement <strong>professionnelle en semaine</strong> et davantage axée sur les <strong>loisirs le week-end</strong>. 
        En effet, les utilisateurs privilégient les créneaux entre <strong>12h et 20h</strong> durant les jours de repos.
        </p>
        """,
        unsafe_allow_html=True
        ) 
    
    # Sous-titre "Analyse du trafic par adresse"
    st.markdown(
        """
        <h2>Analyse du trafic par adresse</h2>
        """,
        unsafe_allow_html=True
        ) 
    
    # Affichage du graphique du trafic par adresse
    image = Image.open('trafic_adresse.png')
    st.image(image)
    st.markdown(
        """
        <p style="font-size: 18px; text-align: justify;">Une <strong>dispersion significative</strong> est observée dans les données relatives aux adresses.<br> 
        Un <strong>top 5</strong> émergent se dessine, reflétant des <strong>emplacements dotés d'aménagements spécifiques</strong> favorables à la pratique du vélo.<br>
        En parallèle, quelques adresses à forte renommée <strong>touristique</strong>, comme l'Avenue des Champs-Élysées, présentent des chiffres de passage plus <strong>modestes</strong>, potentiellement en raison de <strong>l'absence d'aménagements dédiés</strong> à la circulation des vélos.
        </p>
        """,
        unsafe_allow_html=True
        )
    
    # Sous-titre "Analyse du trafic par conditions métérologique"
    st.markdown(
        """
        <h2>Analyse du trafic par conditions météos</h2>
        """,
        unsafe_allow_html=True
        ) 
    
    # Création de la liste déroulante "condition météo" et "temperature"
    selected_option = st.selectbox("Sélectionnez une option", ["condition météo", "température"])

    # Affichage du graphique en fonction de l'option sélectionnée
    if selected_option == "condition météo":
        image = Image.open("trafic_meteo.png")
        st.image(image)
    elif selected_option == "température":
        image = Image.open("trafic_temperature.png")
        st.image(image)
    st.markdown(
        """
        <p style="font-size: 18px; text-align: justify;">Ces graphiques montrent que le trafic est plus <strong>bas lors de météos extrêmes</strong>: très défavorables, défavorables mais aussi idéales.<br>
        Ce phénomène semble être davantage observable sur les week-end pour une utilisation loisir que sur les cœurs de semaine.
        Un effet similaire est observé sur la <strong>température</strong>: le trafic <strong>baisse</strong> pour les <strong>plus basses et les plus hautes températures</strong>.
        </p>
        """,
        unsafe_allow_html=True
        )
    
    # Création d'une case à cocher "Analyse statistique"
    show_test = st.checkbox("Afficher l'analyse statistique")
    
    # Si la case est cochée, afficher le test statistique d'ANOVA
    if show_test:
        st.markdown(
            """
            <p style="font-size: 18px; text-align: justify;">Analyse des liaisons entre notre variable catégorielle <strong>'eval_meteo'</strong> météo et notre variable continue <strong>'NB_passage'</strong> de vélo.<br>
            Le test <strong>d'ANOVA</strong> nous permet d'étudier le lien entre ces deux variables. <br><br>
            Question:<i> Est-ce que le type météo (<strong>'eval_meteo'</strong>) a un effet statistique significatif sur le nombre de passage de vélos (<strong>'NB_passage'</strong>) ?</i><br>
            
                Deux hypothèses:
                H0 : Il n'y a pas d'effet significatif de la variable catégorielle sur la variable continue 
                H1 : Il y a un effet significatif de la variable catégorielle sur la variable continue
            </p>
            """,
            unsafe_allow_html=True
            )
        image = Image.open("resultat_test.png")
        st.image(image)
        st.markdown(
           """
           <p style="font-size: 18px; text-align: justify;"> La p-valeur est très petite (< 0.05) => on rejette H0 et on <strong>accepte H1</strong> selon laquelle 
           il y a un <strong>effet significatif</strong> de la variable catégorielle 'eval_meteo' météo sur la variable continue 'NB_passage'.
           </p>
           """,
           unsafe_allow_html=True
           )

 ### 4EME PAGE - Modelisation
 #Insertion de l'image de couverture
if page == pages[3]:
    image = Image.open('compteur_velo.jpg')
    st.image(image)

    
    # Affichage du titre " Machine learning" avec le trait de couleur
    st.markdown(
        """
        <h1 style='border-bottom: 5px solid #0072B2; padding-bottom: 10px;'>Machine learning</h1>
        """,
        unsafe_allow_html=True
        )
    # Sous-titre "classification du problème"
    st.markdown(
        """
        <h2>Classification du problème</h2>
        <p style="font-size: 18px; text-align: justify;"> Notre objectif a été d'élaborer une prédiction pour la variable <strong>'NB_passage'</strong> dans le cadre d'un <strong>apprentissage supervisé</strong>.<br>
        Notre premier essai a impliqué l'utilisation d'un modèle de <strong>régression linéaire</strong>, cependant, les résultats n'ont pas été probants avec une précision de seulement <strong>0.35</strong> tant sur l'ensemble d'entraînement que sur l'ensemble de test.<br>
        En conséquence, nous avons rapidement orienté notre démarche <strong>vers des modèles de machine learning adaptés aux séries temporelles</strong>.
        </p>
        """,
        unsafe_allow_html=True
        ) 
    # Sous-titre "Choix du modèle et optimisation"
    st.markdown(
        """
        <h2>Choix du modèle et optimisation</h2>
        <p style="font-size: 18px; text-align: justify;"> Pour notre modélisation, nous avons travaillé avec une <strong>série temporelle</strong> représentant <strong>le nombre total de passages de vélos</strong> par jour (365 jours) provenant des <strong>77 sites de comptage</strong>.<br>
        Les différentes phases de <strong>décomposition</strong>, comprenant la <strong>différenciation</strong> pour détecter les <strong>tendances</strong> et la <strong>saisonnalité</strong> de la série, nous ont conduits à sélectionner un <strong>modèle SARIMAX</strong>.<br>
        Les analyses graphiques ainsi que le test d'AD-Fuller ont mis en évidence <strong>l'absence de tendance notable</strong> dans la série, mais ont confirmé une <strong>saisonnalité sur un cycle de 7 jours</strong>.<br>
        Ces observations ont guidé notre choix des ordres <strong>p, d et q</strong> (pour les données non saisonnières) ainsi que <strong>P, D, Q et S</strong> (pour les données saisonnières).
        
                model= sm.tsa.SARIMAX(serie_temporelle_jour, order=(0, 1, 1),seasonal_order=(0, 1, 1, 7))
        </p>
    
        """,
        unsafe_allow_html=True
        ) 
    # Création d'une case à cocher "Analyse statistique"
    show_test = st.checkbox("Afficher les résultats statistiques")
    
    # Si la case est cochée, afficher les résultats du modèles SARIMAX
    if show_test:
        image = Image.open("resultat_sarimax.png")
        st.image(image)
        st.markdown(
           """
           <p style="font-size: 18px; text-align: justify;">La ligne Model montre le modèle entraîné sur une saisonnalité de 7 jours génère des p-values de 0, donc quasiment parfaites.
           </p>
           """,
           unsafe_allow_html=True
           )
    
    # Sous-titre "Visualisation des résultats"
    st.markdown(
        """
        <h2>Visualisation graphique des résultats</h2>
        
        """,
        unsafe_allow_html=True
        ) 
    image = Image.open("graphique_sarimax.png")
    st.image(image)
    
    # Création de la liste déroulante des mois de la période étudiée
    selected_option = st.selectbox("Visualisation par mois", ["juin 2022","juillet 2022","août 2022","septembre 2022","octobre 2022","novembre 2022","decembre 2022","janvier 2023","février 2023","mars 2023","avril 2023","mai 2023"])

    # Affichage du graphique en fonction de l'option sélectionnée
    if selected_option == "juin 2022":
        image = Image.open("trafic_juin.png")
        st.image(image)
    elif selected_option == "juillet 2022":
        image = Image.open("trafic_juillet.png")
        st.image(image)
    elif selected_option == "août 2022":
        image = Image.open("trafic_aout.png")
        st.image(image)
    elif selected_option == "septembre 2022":
        image = Image.open("trafic_septembre.png")
        st.image(image)
    elif selected_option == "octobre 2022":
        image = Image.open("trafic_octobre.png")
        st.image(image)
    elif selected_option == "novembre 2022":
        image = Image.open("trafic_novembre.png")
        st.image(image)
    elif selected_option == "decembre 2022":
        image = Image.open("trafic_decembre.png")
        st.image(image)
    elif selected_option == "janvier 2023":
        image = Image.open("trafic_janvier.png")
        st.image(image)
    elif selected_option == "fevrier 2023":
        image = Image.open("trafic_fevrier.png")
        st.image(image)
    elif selected_option == "mars 2023":
        image = Image.open("trafic_mars.png")
        st.image(image)
    elif selected_option == "avril 2023":
        image = Image.open("trafic_avril.png")
        st.image(image)
    elif selected_option == "mai 2023":
        image = Image.open("trafic_mai.png")
        st.image(image)
    
    st.markdown(
      """
      <p style="font-size: 18px; text-align: justify;">La <strong>prédiction</strong> faite avec l'entrainement du modèle SARIMAX <strong>semble visuellement plutôt satisfaisante</strong> puisque la courbe des données prédites suit <strong>étroitement</strong> celle des données réélles.<br>
      On a calculé <strong>l'erreur relative moyenne de notre modèle: -1,82%</strong>.  En moyenne notre modèle se trompe de 1,8% par rapport aux données réelles.<br> On <strong>sous-estime</strong> un peu le nombre de passages de vélos par rapport à la réalité mais cela reste <strong>assez faible</strong>.
      </p>
      """,
      unsafe_allow_html=True
      )  
    
### 5EME PAGE - Conclusion
#Insertion de l'image de couverture
if page == pages[4]:
    image = Image.open('image_conclusion.jpeg')
    st.image(image)

    # Affichage du titre " Conclusion et ouvertures" avec le trait de couleur
    st.markdown(
    """
    <h1 style='border-bottom: 5px solid #0072B2; padding-bottom: 10px;'>Conclusion et ouvertures</h1>
    """,
    unsafe_allow_html=True
    )
    
    # Sous-titre "Résultats issus des graphiques et modèle"
    st.markdown(
        """
        <h2>Résultats issus des graphiques et modèle</h2>
        <p style="font-size: 18px; text-align: justify;">Notre modèle a joué un rôle essentiel en confirmant la présence d'une <strong>saisonnalité hebdomadaire</strong> marquée dans nos données.<br>
        Nos analyses visuelles ont éclairé <strong>plusieurs éléments clés qui influencent considérablement la circulation à vélo</strong>. Parmi ces éléments, nous avons identifié des <strong>facteurs</strong> tels que la température, le jour de la semaine, le créneau horaire, les périodes de vacances scolaires ou jours fériés ou même les événements inhabituels.<br>
        Une <strong>conclusion significative</strong> émerge de cette étude : l'utilisation du vélo tend à être davantage <strong>associée à des déplacements professionnels</strong> qu'à des loisirs.<br><br>
        Ces observations stratégiques serviront de base pour guider <strong>les décisions</strong> relatives à la <strong>mobilité urbaine</strong>, la conception <strong>d'infrastructures cyclables</strong> plus adaptées et la promotion continue du vélo en tant qu'alternative de <strong>transport durable</strong> au cœur de la ville de Paris.
        </p>
       
        """,
        unsafe_allow_html=True
        )
    
    # Sous-titre "Améliorations et perspectives"
    st.markdown(
        """
        <h2>Améliorations et perspectives</h2>
        <p style="font-size: 18px; text-align: justify;">L'incorporation de données couvrant <strong>une période plus étendue</strong> dans notre modèle aurait sans doute permis de <strong>discerner des tendances</strong> au-delà de la saisonnalité. Cette approche aurait contribué à <strong>améliorer la précision de nos prévisions pour les données futures</strong>.<br><br>
        De plus, il serait intéressant de développer un modèle de machine learning englobant <strong>l'ensemble de nos variables explicatives</strong> en lien avec la variable "NB_passage". Cette approche plus complète pourrait potentiellement <strong>renforcer la qualité de nos prédictions</strong>.<br><br>
        Pour élargir encore davantage notre projet, une étude du trafic en fonction <strong>des types d'aménagements cyclables</strong> serait pertinente. Identifier les corrélations éventuelles entre ces facteurs et les habitudes de pratique cyclique fournirait des informations significatives pour <strong>guider la planification d'aménagements futurs</strong>. Les aménagements du plan vélo 2021-2026
        de la ville de Paris sont détaillés <a href="https://www.paris.fr/pages/un-nouveau-plan-velo-pour-une-ville-100-cyclable-19554">ici</a> et les données sont disponibles sur l'open data <a href="https://opendata.paris.fr/explore/dataset/plan-velo-2026/table/?dataChart=eyJxdWVyaWVzIjpbeyJjb25maWciOnsiZGF0YXNldCI6InBsYW4tdmVsby0yMDI2Iiwib3B0aW9ucyI6e319LCJjaGFydHMiOlt7ImFsaWduTW9udGgiOnRydWUsInR5cGUiOiJjb2x1bW4iLCJmdW5jIjoiQ09VTlQiLCJzY2llbnRpZmljRGlzcGxheSI6dHJ1ZSwiY29sb3IiOiIjMDAzMzY2In1dLCJ4QXhpcyI6InJlc2VhdSIsIm1heHBvaW50cyI6NTAsInNvcnQiOiIifV0sInRpbWVzY2FsZSI6IiIsImRpc3BsYXlMZWdlbmQiOnRydWUsImFsaWduTW9udGgiOnRydWV9&location=12,48.85893,2.34801&basemap=jawg.streets">ici</a>.
        </p>
       
        """,
        unsafe_allow_html=True
        )
    # Sous-titre "Bibliographie"
    st.markdown(
    """
    <h2>Bibliographie</h2>
    <ul>
       
    <li>Données météos journalières: <a href="https://www.historique-meteo.net">https://www.historique-meteo.net</a></li>
    <li>Données des températures: <a href="https://public.opendatasoft.com/">https://public.opendatasoft.com/</a></li>
    <li>Données des compteurs vélo Paris: <a href="https://opendata.paris.fr/explore/dataset/comptage-velo-donnees-compteurs/information/?disjunctive.id_compteur&disjunctive.nom_compteur&disjunctive.id&disjunctive.name">https://opendata.paris.fr</a></li>
    </ul>
    """,
    unsafe_allow_html=True
)
    
