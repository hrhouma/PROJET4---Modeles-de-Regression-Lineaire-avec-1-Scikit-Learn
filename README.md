# PROJET4---Modeles-de-Regression-Lineaire-avec-1-Scikit-Learn
Analysez la source de données dans le fichier 'kc-house-data.csv'. Cette source de données fait partie des bases de données disponibles dans le domaine public. Ce fichier contient 21 613 observations de biens immobiliers du comté de King dans l'État de Washington. Les données pour les 21 variables suivantes sont fournies.

Liste pour les propriétés immobilières :

1. ID : Un identifiant unique pour la propriété.
2. Date : La date de mise en liste ou de la transaction.
3. Prix : Le prix de vente ou le prix de liste de la propriété.
4. Chambres : Le nombre de chambres à coucher dans la propriété.
5. Salles de bains : Le nombre de salles de bains.
6. Pieds carrés habitables : La superficie habitable en pieds carrés.
7. Pieds carrés de terrain : La superficie totale du terrain en pieds carrés.
8. Étages : Le nombre d'étages du bâtiment.
9. Bord de l'eau : Si la propriété est située près d'un plan d'eau.
10. Vue : Description des vues offertes par la propriété.
11. État : L'état général de la propriété.
12. Grade : Une évaluation de la qualité et de la finition de la propriété.
13. Pieds carrés au-dessus : La superficie des étages supérieurs en pieds carrés.
14. Pieds carrés de sous-sol : La superficie du sous-sol en pieds carrés.
15. Année de construction : L'année de construction de la propriété.
16. Année de rénovation : L'année où la propriété a été rénovée, si applicable.
17. Code postal : Le code postal de la localisation de la propriété.
18. Latitude : La latitude géographique de la propriété.
19. Longitude : La longitude géographique de la propriété.
20. Pieds carrés habitables15 : Peut-être une référence à la superficie habitable dans un certain contexte ou période, comme les 15 dernières années.
21. Pieds carrés de terrain15 : Similaire à ci-dessus, peut-être une référence à la superficie du terrain dans un certain contexte ou période.


Lisez le fichier source de données brutes 'kc-house-data.csv'. Construisez un modèle de régression linéaire en utilisant les variables suivantes.

Variable de réponse :

•	prix (numérique)

Variables prédicteurs :

•	sqft_living (numérique)
•	chambres (numérique)
•	bord de l'eau (catégorique): Niveaux de bord de l’eau : 0 = pas de bord de l'eau, 1 = bord de l'eau
•	état (catégorique): Niveaux d'état: 1,2,3,4,5
 
Problème#1
Construisez un modèle de régression en utilisant les caractéristiques suivantes.
•	Langage de programmation : Python
•	Plateforme Cloud : Colab
•	Package : Scikit-Learn
Vérifiez que votre équation de régression est la suivante.
𝑝𝑟𝑖𝑐𝑒 = 66,581.53 + 305.72 ∗ 𝑠𝑞𝑓𝑡𝑙𝑖𝑣𝑖𝑛𝑔 − 52,704.36 ∗ 𝑏𝑒𝑑𝑟𝑜𝑜𝑚𝑠 + 783,090.68 ∗ 𝑤𝑎𝑡𝑒𝑟𝑓𝑟𝑜𝑛𝑡
−25,698.33 ∗ 𝑐𝑜𝑛𝑑𝑖𝑡𝑖𝑜𝑛2 − 8,811.75 ∗ 𝑐𝑜𝑛𝑑𝑖𝑡𝑖𝑜𝑛3 + 28,198.78 ∗ 𝑐𝑜𝑛𝑑𝑖𝑡𝑖𝑜𝑛4 + 100,565.72 ∗ 𝑐𝑜𝑛𝑑𝑖𝑡𝑖𝑜𝑛5

Prédisez le prix d'une maison avec les caractéristiques suivantes :
•	sqft_living = 3 000
•	chambres = 4
•	waterfront = Non (0)
•	condition = 4
Vérifiez que le𝑃𝑟𝑒𝑑𝑖𝑐𝑡𝑒𝑑 𝑝𝑟𝑖𝑐𝑒 = 801 112,20 $
