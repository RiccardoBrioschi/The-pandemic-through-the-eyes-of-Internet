# People's thoughts expressed in online world during the coronavirus pandemic 
This is the repo for the project of the course Applied Data Analysis at EPFL [(CS-401)](https://dlab.epfl.ch/teaching/fall2022/cs401/).

## Abstract
Due to the coronavirus pandemic, year 2020 was a year of big changes in the world. Because of reduced mobility during that period people started to live in an ‘online’ world, expressing their thoughts and opinions on social media like Twitter. Additionally, they used Wikipedia, the largest and most-read online encyclopedia, as the main source for investigating more about anything they would like to know. 

Starting from West et al.’s work about attention shifts on Wikipedia during the COVID-19 crisis, this project aims to analyse human digital traces and to understand how the pandemic has impacted human thoughts and interests, with particular attention to how communication has been affected by the virus. To reach this goal, we are analysing which topics people were interested in the most during the pandemic, both on Twitter and Wikipedia. Moreover, we want to investigate how interest in some topics was affected by influencing people on Twitter. And finally, to wrap up the story, we want to see did influencing people on Twitter had an impact on people's mobility before official lockdowns.

## Research questions

To figure out how people's thoughts and interests changed in response both to the disease itself and to the massive mobility restrictions during pandemic, we ask following questions:

1) How people's interest in different topics on Wikipedia and Twitter changed in the early stage of the pandemic in different countries? Is there any correlation between these two? Do tweets reflect the same changes in nature of information seeking as shown by Wikipedia pageview logs?

2) How has the behavior of influential people on Twitter impacted people's thinking and interest during the pandemic, with particular attention to the early stage?

3) Did countries with a higher presence of covid information and warnings on Twitter, mostly from influential people, have a better situation in terms of new cases and the number of deaths, than countries that didn’t?

## Datasets
To answer those questions we used the following datasets:
- `Global_Mobility_Report` (given): in this dataset are collected all the metrics regarding mobility.
- `aggregated_timeseries` (given): here we find the date and the number of clicks on wikipedia pages of different topics (e.g. Covid, Geography, STEM, ...)
- `interventions` (given): in this dataset we can find all the date of the most important events during the pandemics for some countries.  
- `WHO-COVID-19-global-data`(added): dataset downloaded from the official website of World Health Organization [(here)](https://covid19.who.int/data). We have decided to add this dataset to have a better understanding in our analysis on how pandemics was going.
- `Twitter data` (added): we are collecting tweets (both from influencing people and normal daily users) in different periods of the pandemic to get answers on mentioned RQ

## Methods

In this section, we will give an overview of the preprocessing, processing, and the data analysis part which needs to be done to answer on RQs. Moreover, we will explain the problem-solving process as well as the feasibility of each task.

* Task1: Tweets retrieval and first analysis

*We want to analyze which were the most discussed topics on Twitter in the early stage of the pandemic, in order to verify whether users’ behavior has been similar between Wikipedia and the social network. Since we are interested in comparing the data from Twitter with the results obtained by West et al., there is no need to adopt a difference-in-difference methodology but it is enough to compute the frequency with which the topics of the ORES article topic were mentioned in different tweets. This first analysis serves as an introducton to understand whic topics have been discussed on Twitter: it would be interesting to see whether the idea of a medical emergency started to arise / be discussed before the actual lockdown and limitations were set by governments.*
 
*We import tweets for each one of the 12 countries using Twitter API. Tweets may be retrieved on a daily or weekly basis at particular times of the day (moments of major usage of the platform). In order to label each tweet with a topic, we use empath library which performs well with a wide variety of languages. To compare Twitter results with Wikipedia pageviews, various data visualization techniques may be adopted.*

* Task2: Tweets from influential people -  the power of communication during the epidemic

*We retrieve tweets posted by influential people in each country (politicians, influencers, public figures from music, sports, etc.) and we perform a sentiment analysis of these posts using TextBlob. We compute both a sentiment (polarity) score and a subjectivity value for each comment. We then try to quantify whether these tweets were meant to warn the population. Anaysing which have been the most discussed hastags and used words might also be useful to understand the way communication has changed during the pandemic.*

*We retrieved a sufficient amount of tweets published by 10 influential people in each country. The nature of the posts can be of different kinds (Covid, Vaccination, etc)  and the posting dates should be uniformly distributed throughout the period preceding the official lockdown in the analysed country. We then analyze the time series of the obtained sentiment values with mobility data and deaths data (WHO Dataset)*

* Causality among mobility and tweets from influential users - EXPLAIN how
* Why is this feasibile

*We can finally observe whether famous people influenced people’s mobility (using panicking words, warnings etc) before and after official limitations were published and see if stronger words were used in countries having the strongest lockdown.*


```mermaid
graph LR
A[Square Rect] -- Link text --> B((Circle))
A --> C(Round Rect)
B --> D{Rhombus}
C --> D
```

## Proposed timeline


|Period                         |Tasks                        |
|-------------------------------|-----------------------------|
|`November 21st - November 27th ` |TBD                          |
|`November 28st - December 04th ` |TBD                          |
|`December 05th - December 11th ` |TBD                          |
|`December 12th - December 18th ` |TBD                          |
|`December 19th - December 23th ` |Data story                   |


## Organization within the team


|Task        |Responsibility *             |
|------------|-----------------------------|
|Task 1      |R, F                          |
|Task 2      |M, L                          |
|Task 2      |R, M, L, F                    |

*M = Maja, F = Federico, L = Lazar, R = Riccardo


## Authors

The `4ADA` team is composed by:
- Riccardo Brioschi: [@RiccardoBrioschi](https://github.com/RiccardoBrioschi)  
- Federico Di Gennaro: [@FedericoDiGennaro](https://github.com/FedericoDiGennaro)  
- Lazar Milikić: [@LazarMilikic](https://github.com/Lemmy00) <br/>
- Maja Skoko: [@MajaSkoko](https://github.com/s-maja)

## References

West R. et al.,  "Sudden Attention Shifts on Wikipedia During the COVID-19 Crisis", 2020 https://arxiv.org/pdf/2005.08505.pdf 
