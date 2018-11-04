# Study of the influence of driver profile, canton and vehicle type on car accidents in Switzerland

# Abstract

​	In 2017, there were 17,799 accidents on Swiss roads causing bodily injuries. Even though the number of victims is decreasing since 25 last years, Switzerland still faces more than 20,000 victims each year. In this data story, we try to investigate three main factors influencing car accidents: driver profile, accident per canton and car type. Identifying which profiles are more dangerous is an interesting result for policy makers and insurance companies, considering an annual cost of car accidents equal to 4 billion francs. Factors of difference between each profile are also a targeted, to tackle the issue at its roots. Furthermore, swiss cantons benefit from a high political responsibility. Studying the distribution of accidents at this scale is therefore valuable, as well as their potential cultural factors based on past votings. Finally, a study of vehicle type influence on accidents is also carried out. All datasets used in this study were collected on Federal Statistical Office website.

# Research questions

> Is there a high influence of the driver profile (age, gender, driving experience) on car accident risk?

> What could be the main factors triggering that difference between driver profiles?

> Based on votations and urban data, what could be the main factors triggering the difference of accidents between cantons?

> Does car type have an influence on car accidents? 

> Based on our results, can we identify uesful recommandations for insurance companies or policy makers?


# Dataset

​	We would like to use multiple datasets about driving accidents in Switzerland. Most of them were found on Federal Statistical Office website. 

The main dataset is gathering swiss aggregated data about car accidents according to various factors such as driver's and victim's profile, road type and condition, causes of accident, state of the driver and road signs. This overall dataset contains about 5 million data, and has been split into 4 sub-datasets by the SFO. As a result the first step will be to identify and merge columns of interest from these four tables, and exclude useless and heavy additional data from the processed dataframe. 

Links towards first dataset: 

- [Accidents de la circulation routière: accidents avec victimes (1)](https://www.pxweb.bfs.admin.ch/pxweb/fr/px-x-1106010100_102/-/px-x-1106010100_102.px) 
- [Accidents de la circulation routière: accidents avec victimes (2)](https://www.pxweb.bfs.admin.ch/pxweb/fr/px-x-1106010100_103/-/px-x-1106010100_103.px )
- [Accidents de la circulation routière: victimes](https://www.pxweb.bfs.admin.ch/pxweb/fr/px-x-1106010100_104/-/px-x-1106010100_104.px)
- [Accidents de la circulation routière: objets impliqués](https://www.pxweb.bfs.admin.ch/pxweb/fr/px-x-1106010100_105/-/px-x-1106010100_105.px )

When comparing drivers' profiles, we would like to use proportions of the population instead of absolute quantities since different profile groups might have different size. It will require to merge the dataset on car accidents with a complementary dataset on swiss demography.

- [Population résidante permanente et non permanente selon le canton, le sexe, l'état civil et l'âge](https://www.pxweb.bfs.admin.ch/pxweb/fr/px-x-0102010000_102/-/px-x-0102010000_102.px)

In a second part, we would like to study geographical distribution of car accidents, therefore two datasets have been selected. One is relating car accident victims to cantons over last 25 years, and another one is providing insecurity data in swiss towns, includind car accidents. An interesting outcome concerning city versus country-side might be found. 

- [Accidents de la circulation routière: accidents avec victimes par canton](https://www.pxweb.bfs.admin.ch/pxweb/fr/px-x-1106010100_101/-/px-x-1106010100_101.px)
- [Qualité de vie dans les villes et agglomérations (agglo 2000): sécurité personnelle](https://www.pxweb.bfs.admin.ch/pxweb/fr/px-x-2105000000_107/-/px-x-2105000000_107.px) 
Then, the results of votations per cantons would also be collected and processed to be compared to accidents per cantons. Indeed, a correlation might be found between cantons voting against road safety, and quantity of accidents. This dataset however contains data for all  swiss votations, therefore it should be first cleaned to have only votings about road safety occuring in sufficiently recent years to still make sense today. 
- [Votations populaires (résultats au niveau des cantons depuis 1866)](https://www.pxweb.bfs.admin.ch/pxweb/fr/px-x-1703030000_100/-/px-x-1703030000_100.px )
- [Initiative populaire fédérale 'pour plus de sécurité à l'intérieur des localités grâce à une vitesse maximale de 30 km/h assortie d'exceptions (Rues pour tous)'](https://www.admin.ch/ch/f//pore/vi/vis271.html)
- [Votation no  476 - Résultats dans les cantons](https://www.bk.admin.ch/ch/f/pore/va/20010304/can476.html)

Finally, a study on influence of car type on proportion of victims of car accidents would be carried out. A dataset presenting number of vehicles per type per canton has also been selected. The study here would only measure a correlation between car type and proportion of victims out of data for each canton, therefore we might stay careful with the conclusions. 

- [Parc de véhicules routiers: véhicules de transport de personnes depuis 1990](https://www.pxweb.bfs.admin.ch/pxweb/fr/px-x-1103020100_123/-/px-x-1103020100_123.px)

# A list of internal milestones up until project milestone 2

​	We have three weeks left to identify useful factors for our study, clean the data, compute statistics, measure correlations and visualize results.  

<u>Until 11th of November:</u>
- Identify useful data out of sets and join relevant sets together

- Clean the data  

   

<u>Until 18th of November:</u> 
- Compute statistics on drivers profiles

- Look for factors of difference between drivers profiles

- Investigate potential correlation between cantons votings and number of accidents*


<u>Until 25th of November:</u> 

- Visualize results for the first part (driver profile) and second part (accident per canton)
- Compute the correlation between car type and accidents per canton + Visualization
