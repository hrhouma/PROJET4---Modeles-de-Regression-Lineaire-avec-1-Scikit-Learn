# PROJET4---Modeles-de-Regression-Lineaire-avec-1-Scikit-Learn
Analysez la source de données dans le fichier 'kc-house-data.csv'. Cette source de données fait partie des bases de données disponibles dans le domaine public. Ce fichier contient 21 613 observations de biens immobiliers du comté de King dans l'État de Washington. Les données pour les 21 variables suivantes sont fournies.

Liste pour les propriétés immobilières :

1. **ID :** Identifiant numérique unique pour chaque maison vendue.
2. **Date :** La date de vente de la maison.
3. **Prix :** Le prix de vente de la maison, qui est la variable cible dans ce modèle prédictif.
4. **Chambres :** Le nombre de chambres dans la maison.
5. **Salles de bain :** Le nombre de salles de bain dans la maison.
6. **Sqft_Living :** Surface habitable de la maison en pieds carrés.
7. **Sqft_Lot :** Surface du terrain sur lequel est située la maison en pieds carrés.
8. **Étages :** Le nombre de niveaux ou d'étages dans la maison.
9. **Front de mer :** Indique si la maison a une vue sur le front de mer (0 = Non, 1 = Oui).
10. **Vue :** Indique si la maison a été visitée (0 = Non, 1 = Oui).
11. **État :** L'état général de la maison, noté sur une échelle de 1 à 5.
12. **Grade :** La note globale attribuée à la maison, basée sur le système de notation du comté de King, sur une échelle de 1 à 11.
13. **Sqft_Above :** Surface habitable de la maison excluant le sous-sol.
14. **Sqft_Basement :** Surface du sous-sol.
15. **Yr_Built :** L'année de construction de la maison.
16. **Yr_Renovated :** L'année de la dernière rénovation de la maison.
17. **Code postal :** Le code postal où se trouve la maison.
18. **Lat :** La latitude de l'emplacement de la maison.
19. **Long :** La longitude de l'emplacement de la maison.
20. **Sqft_Living15 :** La surface habitable en 2015, ce qui implique certaines rénovations.
21. **Sqft_Lot15 :** La surface du terrain en 2015, impliquant également des rénovations.

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
