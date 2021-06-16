# Project One - Artificial Meat Review Predictions

This is a group project by Tamar Brand-Perez, Tiffany Price, Ben Tubbs, and Jose Santos.

## Topic

The topic of our project involves artificial meat review predictions.  

## The Why

We selected this topic because the artificial meat industry is becoming increasingly popular as of late.  We find it the industry very interesting and want to understand how consumer experience and resulting reviews can predict ratings. After pulling and cleaning our data set from Amazon, we are going to use the Natural Language Processing machine learning model to train a sentiment classifier. During the cleaning process, both five and one star reviews will be maintained, while two, three and four star ratings will be removed.  Next, we will pull reviews without ratings and direct the machine to predict the ratings based on the analysis of the reviews.  

## Source Data

Our data set was pulled from the Amazon Grocery and Gourmet Food section (http://deepyeti.ucsd.edu/jianmo/amazon/index.html).  We are currently working through the process of determining the site from which we will pull the reviews without ratings.  

## Goals

In this project we will use a Natural Language Processing machine learning model to train a sentiment classifier on an Amazon dataset of Grocery and Gourmet Food reviews (https://jmcauley.ucsd.edu/data/amazon/) containing over 1 million reviews.  

The goal of this classifier is to predict user sentiment (positive or negative) for fake meat products.  We believe this analysis will help artificial meat producers understand how reviews will impact ratings and have a potential impact on thier popularity and future sales.

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

### Week 1

The data was cleaned and exported to this csv file ( https://drive.google.com/file/d/1gEXXLB23iYxTxxyPFyhmQ-dfvjoEhTOl/view?usp=sharing ) by Tamar.  I am currently reading the data from the file rather than the database because we are still working on getting the data in a database.

I read in the file and stored the data in an array, then removed the header.  I wanted to clean up the data for better processing, so I removed “stop words” which are words that do not add a lot of meaning to the content such as words like “the”, “in”, “at”, etc.  I also normalized the data by converting everything to lowercase.

Next I tokenized the data which means splitting it by word and then created a list of tuples which contains two items.  The first item is the list of strings of words contained within the text, and the second item is either the string “pos” or the string “neg”.  We are working with a dataset of Amazon reviews which is absolutely huge, so I am using five star reviews as positive and one star reviews as negative.  Tamar removed all of the two, three and four star reviews in her preprocessing step.

I then shuffled up the positive reviews for randomness and included the same number of positive and negative reviews in one giant list.  I then shuffled this giant list which contains 809,640 items half of which are positive and half of which are negative reviews.  We can see some of the list items in the file.

I plan to use a bag of words model with a Naive Bayes classifier for starters in order to classify the texts.  We will see what kind of accuracy we can get with that type of model.  We are going to scrape some data about fake meat products to classify as either positive or negative.

