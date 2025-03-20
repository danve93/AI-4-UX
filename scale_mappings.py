# SCALE_MAPPINGS.PY


# Dictionary for converting Likert scale text answers into numbers
# Please note that the values are different for each set (1,2,3…) as some of the options were repeated through different scales and had the same value, so it was not necessary to repeat them in this dictionary
likert_mapping = {
   "Pas du tout d'accord": 1,
   "Je suis pas du tout d'accord": 1,   
   "Pas du tout satisfait": 1,
   "Trop petites": 1,   
   "Très complexe": 1,
   
   "Peu satisfait": 2,   
   "Assez petites": 2,
   "Assez complexe": 2,
   "A revoir partiellement": 2,
   "Pas simple d'utilisation": 2,
   "Messagerie non intuitive": 2,
   "Pas tout à fait d'accord": 2,
   "Je suis pas tout à fait d'accord": 2,


   "D'une complexité adéquate": 3,
   "D'une complexité correcte": 3,
   "Parfaites": 3,
   "Moyennement satisfait": 3,
   "Sans avis": 3,


   "Assez simple": 4,
   "Assez grandes": 4,
   "Satisfait": 4,
   "D'accord": 4,
   "Plutôt d'accord": 4,
   "Plutôt simple": 4,


   "Très simple": 5,
   "Tout à fait d'accord": 5,
   "Je suis d'accord": 5,
   "Je suis tout à fait d'accord": 5,
   "Trop grandes": 5,
   "Très satisfait": 5,
   "Parfait": 5,
   "Parfaites": 5
}


# Dictionary for converting ordinal answers into numbers (1, 2, 3…)
ordinal_mapping = {
   "En utilisant le compositeur de courriel quiapparaît dans le coin inférieur gauche": 1,
   "Directement sous (ou au-dessus) du texte de l'e-mail": 2,
   "Je préfère n'afficher que le contenu après avoir cliqué sur un e-mail.": 3,
   "Verticale (la liste des courriels à gauche et le contenu du courriel à droite)": 1,
   "Horizontale (la liste d'adresses électroniques en haut et le contenu de l'adresse électronique en bas)": 2
}
