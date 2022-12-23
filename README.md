# Internet as tool to fight pandemics
You can find our data story [here](https://4ada.github.io/4ada_datastory/), enjoy!

* [Abstract](#Abstract)
* [Research questions](#Research-questions)
* [Datasets](#Datasets)
* [Methods](#Methods)
* [Organization within the team](#Organization-within-the-team)
* [Authors](#Authors)
* [References](#References)

## Abstract
Due to the coronavirus pandemic, year 2020 was a year of big changes in the world. Because of reduced mobility during that period people started to live in an ‘online’ world, expressing their thoughts and opinions on social media like Twitter. Additionally, they used Wikipedia, the largest and most-read online encyclopedia, as the main source for investigating more about anything they would like to know. 

Starting from West et al.’s work about attention shifts on Wikipedia during the COVID-19 crisis [[1]](#References), this project aims to analyse human digital traces and to understand how the pandemic has impacted human interests, with particular attention to how communication has been affected by the virus. To reach this goal, we are analysing which topics people were interested in the most during the pandemic, both on Twitter and Wikipedia. Moreover, we will analyise tweets posted by influential people on the semantic level to see the power of communication during the pandemic. Finally, to wrap up the story, the main question of our research is:  
“Were countries which paid more attention about COVID-19 in the early stage of the pandemic the ones that better handled the initial spread of the virus?”

## Research questions

To figure out how people's interests changed in response both to the disease itself and to the massive mobility restrictions during the pandemic, we ask the following questions:

1) How did people's interests in different topics on Wikipedia and Twitter change in the early stage of the pandemic in different countries? Do tweets reflect the same changes in nature of information seeking as shown by Wikipedia pageview logs and if not, why?

2) What was the behavior of influential people on Twitter during the pandemic, and how did their words impact people during that period, with particular attention to the early stage of the pandemic?

3) Did countries with a higher presence of COVID-19 related topics in Wikipedia pagelogs and a higher presence of tweets about the virus, mostly from influential people, have a better situation in terms of new cases and the number of deaths, than countries that didn’t?

## Datasets
To answer those questions we used the following datasets:
- `Global_Mobility_Report` (given to us): in this dataset all the information regarding mobility are collected.
- `aggregated_timeseries` (given to us): here we find the date and the number of clicks on wikipedia pages of different topics (e.g. Covid, Geography, STEM, ...)
- `interventions` (given to us): in this dataset we can find all the date of the most important events during the pandemic for some countries.  
- `WHO-COVID-19-global-data`(added by us): dataset downloaded from the official website of World Health Organization [(here)](https://covid19.who.int/data). We have decided to add this dataset to have a better understanding of how the pandemic was going.
- `Twitter data` (added by us): we collected tweets (both from influential people and normal daily users) in different periods of the pandemic to get answers on mentioned RQs.
- `countries.csv` (added by us): dataset containing additional information about analysed countries, e.g. area, GDP, population etc.

## Methods

In this section, we will give an overview of the preprocessing, processing, and the data analysis part that had to be done to answer our RQs. Moreover, we will explain the problem-solving process as well as the feasibility of each task.

#### Analysis of Wikipedia usage and tweets from *normal* daily users. 

We analysed which were the most discussed topics on Twitter in the early stage of the pandemic, in order to verify whether users’ behavior has been similar between Wikipedia and the social network. Since we are interested in comparing data from Twitter with the results obtained by West et al.[[1]](#References), there is no need to adopt a difference-in-difference methodology but it is enough to compute the frequency with which the topics of the ORES article topic were mentioned in different tweets. Therefore, this first analysis serves as an introduction to understand which topics have been discussed on Twitter: we want to detect whether the idea of a medical emergency started to arise in the discussed topics in order to identify which countries immediately began to pay attention to the virus. Twitter revealed to be an incredible tool to get insights about people's behaviour and beliefs. As a matter of fact, we notice that, even though COVID-19 Wikipedia page existed before the actual start of the pandemic, it took a bit of time to have a complete page to look at. On the other hand, on Twitter, people started to talk about Covid immediatly. Therefore, this task also represents a justification for our decision of using Twitter data in addition to the provided datasets.
 
For what regards our methodology, we firstly retrieved tweets (of "normal people") from the same countries analysed in Coronawiki dataset with the exception of Great Britain (English Wikipedia pages are consulted by people from different countries, thus making difficult to draw conclusion about Great Britain). We retrieved tweets posted during the 3 weeks preceding the lockdown in each country because we want to study what was the initial response of the population to the unusual situation. During the process of retrieving tweets, we are avoiding retweets and tweets which contain videos, images, or similar media since for our analysis only text is useful. Tweets are retrieved on a daily basis at particular times of the day (moments of major usage of the platform). In order to label each tweet with a topic and emotions, we use Empath library and we traslated them to English; notice that for some of the topics we chose to analyse we had to create our own category in empath. To compare Twitter results with Wikipedia pageviews, we did a min-max scaling separately for both Twitter and Wikipedia data. The plot we obtained gave us insights about the trends of topics in the two platforms: since they seemed capture different type of behavior, we decided to  combine them in our further analysis instead of using only Wikipedia data.

#### Analysis of tweets from influential people - the power of communication during the pandemic.

In this part of analysis we retrieved tweets posted by influential people in each country (politicians, influencers, public figures from music, sports, etc.). We adopted an approach similar to the one used for the previous task, translating each retrieved tweet to English in order to simplify our analysis. Since we are analysing a limited number of users, in this part we can retrieve all tweets from the period of interest (3 weeks before lockdown). In order to label each tweet with a topic and emotions, we use empath library. Additionally, we perform a sentiment analysis of tweets using TextBlob library. We compute both a sentiment (polarity) score and a subjectivity value for each comment. We then try to quantify whether these tweets were meant to warn the population by looking at the most used words and hashtags. This last analysis might also be useful to understand the way communication has changed during the pandemic. Finally, we used LDA in order to quantify how much covid realted tweets are important in different countries. By using LDA we try to reconstruct the topic model (bag of words) that might have generated the tweets we retreived. Notice that some of the insights obtained at the end of this task are going to be considered as observed covariates for the following analysis.

####  Impact of "attention score" on infections.

In this part of analysis, we explored whether an overall interest in COVID-19 had an impact on reducing/slowing the number of new cases and deaths in different countries. To do so we computed a new variable that we called "attention score". To do so, we firstly utilize the LDA topic model of previous task to pick up the key topics talked about by influential people on Twitter. Thus, we can find the topic that is related to pandemics, covid, lockdown, and so on, and find the percentage of tokens related to it. This percentage is our score for the presence of COVID on social media. Next, we use the `aggregated_timeseries.json` dataset to get the average percentage of pageviews going to covid-related pages per day for pages in the appropriate language for the country we analyze.  
Finally, we average these two results by Harmonic mean to obtain the Covid attention score. We use the Harmonic mean to evenly weight the influence of each of the percentage scores we use.
After having computed the attention score for the 12 countries, we divided them in two categories: 6 countries were labeled as "low-attention" countries and the other 6 countries were labeled as "high-attention" countries.
Then we divided our main dataframe in two dataframe based on low and high attention, obtaining 6 rows for each new dataframe. Then we decided to do an exact matching of these two dataset on the variable `had_lockdown` (1 if the country had a lockdown, 0 otherwise).  
After this matching, we end up with 18 couples. Then we compute the "4ADA similarity score" defined by:  
$$\text{4ADA-Similarity}(x_1, x_2) = 1 - \frac{1}{N}\sum_{x^i_1, x^i_2}{|x^i_1 - x^i_2|} $$
where $x^i_j$, $j\in\{1, 2\}$ is the $i$-th feature of the $j$-th country in the pair.
Then we built a graph containing all the 18 pairs we had so far where each edeges were weighted by the 4ADA-Similarity and we take the best matches possibile.
For these matches, we computed a paired t-test on the new daily cases (through bootstrap) with a Bonferroni adjustment in order to see if there is statistical evidence to say that countries with an higher attention had lower infections (main research question). We kindly ask you to look at our datastory [here](https://4ada.github.io/4ada_datastory/) to discover the interesting results!

#### Feasibility

We obtained the license from Twitter for working with 60M tweets, which are around 70GB of data which were splitted into 2 datasets (influential and normal people). This however is the maximum amount of data we could retrieve, but we less tweets were needed to draw useful insights.


## Organization within the team


|Task                        |Responsibility *             |
|----------------------------|-----------------------------|
|Wikipedia usage & tweets from *normal* daily users | R, F |
|Tweets from influential people                     | M, R |
|Attention score analysis                           | L, F |
|Website                                            | M, L |
|Data story writing                                 | M, F, R, L |

*M = Maja, F = Federico, L = Lazar, R = Riccardo


## Authors

The `4ADA` team is composed of:
- Riccardo Brioschi: [@RiccardoBrioschi](https://github.com/RiccardoBrioschi)  
- Federico Di Gennaro: [@FedericoDiGennaro](https://github.com/FedericoDiGennaro)  
- Lazar Milikić: [@LazarMilikic](https://github.com/Lemmy00) <br/>
- Maja Skoko: [@MajaSkoko](https://github.com/s-maja)

## References

[1] West R. et al.,  "Sudden Attention Shifts on Wikipedia During the COVID-19 Crisis", 2020 https://arxiv.org/pdf/2005.08505.pdf 
