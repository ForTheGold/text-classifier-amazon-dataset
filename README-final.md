# Project One - Artificial Meat Review Predictions
### Group Members & Respective Roles:
 - Tamar Brand-Perez, Database Lead
 - Tiffany Price, Project Manager
 - Ben Tubbs, Machine Learning Lead
 - Jose Santos, Dashboard Lead

## Topic

The topic of our project involves artificial meat review predictions.  

## The Why

We selected this topic because the artificial meat industry is becoming increasingly popular as of late.  We find it the industry very interesting and want to understand how consumer experience and resulting reviews can predict ratings. After pulling and cleaning our data set from Amazon, we are going to use the Natural Language Processing machine learning model to train a sentiment classifier. During the cleaning process, both five and one star reviews will be maintained, while two, three and four star ratings will be removed.  Next, we will pull reviews without ratings and direct the machine to predict the ratings based on the analysis of the reviews.  

## Source Data

Our data set was pulled from the Amazon Grocery and Gourmet Food section (http://deepyeti.ucsd.edu/jianmo/amazon/index.html).  We scraped Amazon's website to pull reviews and ratings for our visualization. 

## Goals

In this project we will use a Natural Language Processing machine learning model to train a sentiment classifier on an Amazon dataset of Grocery and Gourmet Food reviews (https://jmcauley.ucsd.edu/data/amazon/) containing over 1 million reviews.  

The goal of this classifier is to predict user sentiment (positive or negative) for fake meat products.  Upon having ratings predicted based on the reviews through NLP, We believe this analysis will help store owners identify which fake meat brands to sell. Having access to a model to predict ratings will allow the stakeholder to understand how reviews affect ratings and, in turn, impact future sales of fake meat products.

## Database

Link to Google doc:

groceries_trimmed.csv:

https://drive.google.com/file/d/1RrqXXbHTOJ8rPADNauFVRPBzMXwekjYP/view?usp=sharing

The mockup database format for now is:

columns:

index, overall, reviewText

the overall is the rating number between one and five. We are focusing on 1 and 5 only. The review Text is the review content that we will analyze using NLP.

## Algorithm

The algorithm uses a bag of words model and a Naive Bayes classifier.  It is explained in much greater detail below.

### Week 1 (Machine Learning)

The data was cleaned and exported to this csv file ( https://drive.google.com/file/d/1gEXXLB23iYxTxxyPFyhmQ-dfvjoEhTOl/view?usp=sharing ) by Tamar.  I am currently reading the data from the file rather than the database because we are still working on getting the data in a database.

I read in the file and stored the data in an array, then removed the header.  I wanted to clean up the data for better processing, so I removed “stop words” which are words that do not add a lot of meaning to the content such as words like “the”, “in”, “at”, etc.  I also normalized the data by converting everything to lowercase.

Next I tokenized the data which means splitting it by word and then created a list of tuples which contains two items.  The first item is the list of strings of words contained within the text, and the second item is either the string “pos” or the string “neg”.  We are working with a dataset of Amazon reviews which is absolutely huge, so I am using five star reviews as positive and one star reviews as negative.  Tamar removed all of the two, three and four star reviews in her preprocessing step.

I then shuffled up the positive reviews for randomness and included the same number of positive and negative reviews in one giant list.  I then shuffled this giant list which contains 809,640 items half of which are positive and half of which are negative reviews.  We can see some of the list items in the file.

I plan to use a bag of words model with a Naive Bayes classifier for starters in order to classify the texts.  We will see what kind of accuracy we can get with that type of model.  We are going to scrape some data about fake meat products to classify as either positive or negative.


### Week 2 - Update on Progress
We continued to clean and organize the data set to finalize the machine learning process and database.  We also started working on the dashboards and website we plan to create. Using Tableau, graphs will display static information regarding the correlation between months/years and ratings. We also are creating an interactive site that will allow a user to input review words, which will populate the predicted positive or negative rating.  This site will be available through Heroku.  Finally, work has begun on the slide deck for the final presentation.

### Week 3 - Update on Progress
We finalized the cleaning and organization of the data set to finalize the machine learning process and database.  We also continued working on the dashboards and website we have created. Using Tableau, graphs will display static information regarding the correlation between months/years and ratings. We also have created an interactive site that will allow a user to input review words, which will populate the predicted positive or negative rating.  This site will be available through Heroku.  Finally, work has continued on the slide deck for the final presentation.

## Dashboard
We have identified possible graphs to reflect our information, such as a line graph and/or a heat map. This is still a work in progress; we plan to use Tableau.

## Presentation
A copy of the draft slides has been uploaded to our repository.

### Progress
Our team meets at least three times per week and touches base regularly. We have found a productive cadence around roles and responsibilities and are continuing to make progress toward the final product.
