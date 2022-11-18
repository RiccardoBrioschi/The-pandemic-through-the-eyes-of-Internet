# Importance of *online world* during the coronavirus pandemic 
This is the repo for the project of the course Applied Data Analysis at EPFL [(CS-401)](https://dlab.epfl.ch/teaching/fall2022/cs401/).

## Abstract
Due to the coronavirus pandemic, year 2020 was a year of big changes in the world. Because of reduced mobility during that period people started to live in an ‘online’ world, expressing their thoughts and opinions on social media like Twitter. Additionally, they used Wikipedia, the largest and most-read online encyclopedia, as the main source for investigating more about anything they would like to know. 

Starting from West et al.’s work about attention shifts on Wikipedia during the COVID-19 crisis [[1]](##References), this project aims to analyse human digital traces and to understand how the pandemic has impacted human thoughts and interests, with particular attention to how communication has been affected by the virus. To reach this goal, we are analysing which topics people were interested in the most during the pandemic, both on Twitter and Wikipedia. Moreover, we want to investigate how interest in some topics was affected by influencing people on Twitter. And finally, to wrap up the story, we want to check did countries with a higher presence of covid topics, both on Twitter and Wikipedia, had an impact on the number of new cases and deaths based on different observed variables.

## Research questions

To figure out how people's thoughts and interests changed in response both to the disease itself and to the massive mobility restrictions during pandemic, we ask following questions:

1) How people's interest in different topics on Wikipedia and Twitter changed in the early stage of the pandemic in different countries? Do tweets reflect the same changes in nature of information seeking as shown by Wikipedia pageview logs?

2) What was the behavior of influential people on Twitter during pandemic, and how they impacted people's thinking and interest during that period, with particular attention to the early stage of pandemic?

3) Did countries with a higher presence of covid related topics on Wikipedia and a higher presence of tweets about covid, mostly from influential people, have a better situation in terms of new cases and the number of deaths, than countries that didn’t?

## Datasets
To answer those questions we used the following datasets:
- `Global_Mobility_Report` (given): in this dataset are collected all the metrics regarding mobility.
- `aggregated_timeseries` (given): here we find the date and the number of clicks on wikipedia pages of different topics (e.g. Covid, Geography, STEM, ...)
- `interventions` (given): in this dataset we can find all the date of the most important events during the pandemics for some countries.  
- `WHO-COVID-19-global-data`(added): dataset downloaded from the official website of World Health Organization [(here)](https://covid19.who.int/data). We have decided to add this dataset to have a better understanding in our analysis on how pandemics was going.
- `Twitter data` (added): we are collecting tweets (both from influencing people and normal daily users) in different periods of the pandemic to get answers on mentioned RQ

## Methods

In this section, we will give an overview of the preprocessing, processing, and the data analysis part which needs to be done to answer on RQs. Moreover, we will explain the problem-solving process as well as the feasibility of each task.

#### Analysis of Wikipedia usage and tweets from *normal* daily users  

We want to analyze which were the most discussed topics on Twitter in the early stage of the pandemic, in order to verify whether users’ behavior has been similar between Wikipedia and the social network. Since we are interested in comparing the data from Twitter with the results obtained by West et al., there is no need to adopt a difference-in-difference methodology but it is enough to compute the frequency with which the topics of the ORES article topic were mentioned in different tweets. This first analysis serves as an introducton to understand whic topics have been discussed on Twitter: *it would be interesting to see whether the idea of a medical emergency started to arise / be discussed before the actual lockdown and limitations were set by governments.*
 
We import tweets for each one of the 12 countries using Twitter API. To make our analysis more convinient, we are translating each tweet from its original langugage to english using google translator python library. During process of retriving tweets, we are avoiding retweets and tweets which contains videos, images or similar media since for our analysis only text is useful. Tweets are retrieved on a daily basis at particular times of the day (moments of major usage of the platform). In order to label each tweet with a topic and emotions with related to tweets, we use empath library. To compare Twitter results with Wikipedia pageviews, various data visualization techniques may be adopted.

#### Analysis of tweets from influential people - the power of communication during the pandemic

In this part of analysis, we are retrieving tweets posted by influential people in each country (politicians, influencers, public figures from music, sports, etc.), again translating it to english. Since this is limited number of users, in this part we can retreive all tweets from some periods, no need of limiting to some time periods during the day. Again, in order to label each tweet with a topic and emotions with related to tweets, we use empath library. Additionally, we perform a sentiment analysis of tweets using TextBlob library. We compute both a sentiment (polarity) score and a subjectivity value for each comment. We then try to quantify whether these tweets were meant to warn the population. Moreover, analysing the most common hastags and used words might also be useful to understand the way communication has changed during the pandemic.

*How we are planning to see impact? Or should be change RQ2 a bit if we do not know.*

####  Causality among covid related topics on Wiki and Twitter and covid new cases/deaths

Finally, we want to observe whether tweets of influencing people had an impact on pandemic situation in country obersving different covariates such as mobility data,... after official limitations were published.

Explan...

```mermaid
graph LR
B((GDP)) -- Link text --> A((Propensity score))
C((HDI)) --> A
D((Mobility)) --> A
E((Lockdown)) --> A
F((Population)) --> A
A ---> G((Treatment))
A --> H((Outcome))
G -->H
I((Unobserved covariates)) --> G

style A fill:#aaa,stroke:#555,stroke-width:2px
style I fill:#9bb,stroke:#999,stroke-width:2px
```

#### Feasibility

We have licence for 60M tweets, it is around 2GB of data which is apropriate amount of data for our machines with 16GB of RAM memory. 
We are using models... explain why we are safe to use them.

## Proposed timeline


|Period                           |Milestones                              |
|---------------------------------|----------------------------------------|
|`November 21st - November 27th ` | Twitter data retrieval & answering RQ1 |
|`November 28st - December 04th ` | Answering RQ2                          |
|`December 05th - December 11th ` | Focusing on RQ3                        |
|`December 12th - December 18th ` | Overall conslusion & Data story        |
|`December 19th - December 23th ` | Final checks and revisions             |


## Organization within the team


|Task                        |Responsibility *             |
|----------------------------|-----------------------------|
|Wikipedia usage & tweets from *normal* daily users | R, F |
|Tweets from influential people                     | M, R |
|Causality Twitter/Wiki to new cases                | L, M |
|Mobility & WHO data analysis                       | F    |

*M = Maja, F = Federico, L = Lazar, R = Riccardo


## Authors

The `4ADA` team is composed by:
- Riccardo Brioschi: [@RiccardoBrioschi](https://github.com/RiccardoBrioschi)  
- Federico Di Gennaro: [@FedericoDiGennaro](https://github.com/FedericoDiGennaro)  
- Lazar Milikić: [@LazarMilikic](https://github.com/Lemmy00) <br/>
- Maja Skoko: [@MajaSkoko](https://github.com/s-maja)

## References

[1] West R. et al.,  "Sudden Attention Shifts on Wikipedia During the COVID-19 Crisis", 2020 https://arxiv.org/pdf/2005.08505.pdf 
