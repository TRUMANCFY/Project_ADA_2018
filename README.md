# Media polarity

# Abstract
A 150 word description of the project idea, goals, dataset used. What story you would like to tell and why? What's the motivation behind your project?
We humans have never experienced this era of information explosion before. Every day, thousands of media spread millions of pieces of news with their own remark to some degree. Instead of keeping the purity, objectivity, and neutrality of news, some media are discovered to publish diametrically opponent narratives about the same event. The media no longer work as a convenient information channel, but also the propaganda artifice of political parties and consortiums. The consistency to the truth inspires us to summarize the phenomena of media polarity. In our project, we will mine in the dataset 'News on the Web' (NOW), which contains 6.6 billion words and the worldwide newspaper and magazines. Through sampling and analyzing this authoritative data collection, we will try to find out the internal positions of some media agencies on some sensitive and controversial issues, such as the presidential election. Also, from the chronological aspect, we hope to find out whether there exist time variation for one specific media agency from 2010 to present.

# Research questions 
* Will the media report the news objectively?
* For the same event, how different media report it? Are there any reasons behind this phenomenon？
* For the same media, will it change its view for the same news over time? 

# Dataset
We will use the dataset 'News On the Web'. In this dataset, there are .txt files storing id, data, country, media, source and title. 
For example:
```
460137  455     13-08-17        CA      CityNews        http://www.citynews.ca/2013/08/17/sheila-copps-caught-up-in-cambodian-election-crisis/  Sheila Copps caught up in Cambodian election crisis
```
What's more, it also provides files containing word, lemma and PoS.
```
14637200        4738387006      Trailing        trail   vvg_jj
```
1. We will extract the useful news related to different media. And we may sort the data on country, date and some key words.
1. We may use some natural language processing methods and make use of the dataset containing lemma and PoS, to find out the polarity of the words and the whole news.


# A list of internal milestones up until project milestone 2
1. 11.11: 
  * Extract and sample the useful data from raw dataset
  * Build subdataset locally and clean the data.
  * Apply some natural language processing methods to analyze the data.
1. 11.18: 
  * Get prelimiary result from the sample dataset and modify our functions if needed
  * Deal with the whole dataset in the cluster and modify some functions if needed
  * Get prelimiary result from the complete dataset
1. 11.25:
  * Do the data vitualization
  * Debug
  * finalize the notebook
  



