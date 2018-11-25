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


# Milestone 2 timeline
1. 11.11:    
   * Build subdataset locally and clean the data.
     * The dataset has size more than 300 GB, thus to enable fault tolerant development, we selected the news of the United States from August to October in 2016.
     * By exploring the data content, we found out that there are a lot of meaningless characters, e.g., punctuations which would bring difficulties for further analysis. So we cleaned the data by using regular expression to remove them.
   * Apply some natural language processing methods to analyze the data.
     * We found out that some type of news are more popular than others and thus more suitable for analysis. To select those popular topics out, we apply tf-idf to the news documents.
     * To enable further investigation on polarity of media, the polarities of pieces of news are necessary. Therefore, we utilized nltk and textblob sentimental analyzers to obtain those numbers of news. 
1. 11.18: 
   * Get preliminary result from the sample dataset
     * Through investigating into the popularity of topics, we found out that *Trump* was far more popular than others in           our sampled dataset. So we select this topic as a starting point of analysis on polarity.
     * For simplicity we started our analysis on the data in Oct 2016.
     * Then we obtained the polarity of each piece of news.  Multiple methods were tried in this section and they will be discussed in details in the Discussion part C.
     * We then got polarity of each media.
1. 11.25:
   * Do the data visualization
     * We used boxplot to illustrate the polarity distribution of medias.
   * Extension to bigger datasets
     * After validating the results on one month basis, we took three months into account both individually and collectively. The polarity distribution of each month and the change through months were visualized.

  
## Discussion
## The problems we encountered during working on milestone2
### A. Select Topic
We choose the top 5 keywords to select the topic without any priority. Therefore, sometimes these 5 keywords may not be related to each other. We might choose relative keywords from the most frequent keywords in the future work.
### B. Get Original Data from Website
When we try to get the content of the news, sometimes we will also get some irrelevant data. We need to find an efficient way to get only the data we want.
### C. Conduct Sentimental Analysis
Now we use sentiment analyzer module of NLTK and TextBlob to analyse the polarity of each sentence in an article. And we set positive threshold and negative threshold to classify the polarity of the sentences. By calculating the percentage of sentences with different polarities, we determine the polarity of the whole article. 
One of the problems is that some of the content of the news might be irrelevant to the topic (e.g., Thank you for your reading) because of the incorrect data extraction. And this irrelevant sentences might have a very high or low polarity score, which has a bad influence on our results. Our solution is that we subtract the median polarity score from the mean score to avoid the bias.

# Milestone 3 timeline
1. 12.1
    * Build up our classifier on polarity of article
    * Extend our range to bigger datasets using spark

2. 12.9
    * Modify our classifier (if needed) to better decide the polarity about other topics
    * Explore the polarity comparisons from different perspective:
      * Variance of polarity of same media on same topic overtime 
      * Variance of polarity of different media on same topic
      * Variance of polarity of same media on different topics
3. 12.15 
    * Finish analysis and visualization of polarity from above viewpoints

