# Exploration on Media polarity in the News

# Abstract
We humans have never experienced this era of information explosion before. Every day, thousands of media spread millions of pieces of news with their own remark to some degree. Instead of keeping the purity, objectivity, and neutrality of news, some media are discovered to publish diametrically opponent narratives about the same event. The media no longer work as a convenient information channel, but also the propaganda artifice of political parties and consortiums. The consistency to the truth inspires us to summarize the phenomena of media polarity. In our project, we will mine in the dataset 'News on the Web' (NOW), which contains 6.6 billion words and the worldwide newspaper and magazines. Through sampling and analyzing this authoritative data collection, we will try to find out the internal positions of some media agencies on some sensitive and controversial issues, such as the presidential election. Also, from the chronological aspect, we hope to find out whether there exist time variation for one specific media agency from 2010 to present. We might use some technologies like natural language processing, machine learning, text mining and cloud computing.

# Research questions 
* Will the media report the news objectively?
* For the same event, how different media report it? Are there any reasons behind this phenomenon？
* For the same media, will it change its view for the same news over time? 

# Dataset
We will use the dataset 'News On the Web'. In this dataset, there are many .txt files in different folders. The files under 'source' folder contains id, data, country, media, source and title. For example:
```
460137  455     13-08-17        CA      CityNews        http://www.citynews.ca/2013/08/17/sheila-copps-caught-up-in-cambodian-election-crisis/  Sheila Copps caught up in Cambodian election crisis
```
If we look at the content of the news, we can find that it is matched with the news on corresponding website. For example:
```
@@14637662 <h> Willett hears it from the Hazeltine crowd <h> Related Links <p> Chaska -- Danny Willett really had no idea what to expect during his first career match in the pressure-packed Ryder Cup .
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
  
## Discussion
## The problems we encountered during working on milestone2
### A. Select Topic
We choose the top 5 keywords to select the topic without any priority. Therefore, sometimes these 5 keywords may not be related to each other. We might choose relative keywords from the most frequent keywords in the future work.
### B. Get Original Data from Website
When we try to get the content of the news, sometimes we will also get some irrelevant data. We need to find an efficient way to get only the data we want.
### C. Conduct Sentimental Analysis
Now we use sentiment analyzer module of NLTK and TextBlob to analyse the polarity of each sentence in an article. And we set positive threshold and negative threshold to classify the polarity of the sentences. By calculating the percentage of sentences with different polarities, we determine the polarity of the whole article. 
One of the problems is that some of the content of the news might be irrelevant to the topic (e.g., Thank you for your reading) because of the incorrect data extraction. And this irrelevant sentences might have a very high or low polarity score, which has a bad influence on our results. Our solution is that we subtract the median polarity score from the mean score to avoid the bias.


