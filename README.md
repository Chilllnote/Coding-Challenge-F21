# ACM Research Coding Challenge (Fall 2021)

## [](https://github.com/ACM-Research/Coding-Challenge-F21#no-collaboration-policy)No Collaboration Policy

**You may not collaborate with anyone on this challenge.**  You  _are_  allowed to use Internet documentation. If you  _do_  use existing code (either from Github, Stack Overflow, or other sources),  **please cite your sources in the README**.

## [](https://github.com/ACM-Research/Coding-Challenge-F21#submission-procedure)Submission Procedure

Please follow the below instructions on how to submit your answers.

1.  Create a  **public**  fork of this repo and name it  `ACM-Research-Coding-Challenge-F21`. To fork this repo, click the button on the top right and click the "Fork" button.

2.  Clone the fork of the repo to your computer using  `git clone [the URL of your clone]`. You may need to install Git for this (Google it).

3.  Complete the Challenge based on the instructions below.

4.  Submit your solution by filling out this [form](https://acmutd.typeform.com/to/zF1IcBGR).

## Assessment Criteria 

Submissions will be evaluated holistically and based on a combination of effort, validity of approach, analysis, adherence to the prompt, use of outside resources (encouraged), promptness of your submission, and other factors. Your approach and explanation (detailed below) is the most weighted criteria, and partial solutions are accepted. 

## [](https://github.com/ACM-Research/Coding-Challenge-S21#question-one)Question One

[Sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) is a natural language processing technique that computes a sentiment score for a body of text. This sentiment score can quantify how positive, negative, or neutral the text is. The following dataset in  `input.txt`  contains a relatively large body of text.

**Determine an overall sentiment score of the text in this file, explain what this score means, and contrast this score with what you expected.**  If your solution also provides different metrics about the text (magnitude, individual sentence score, etc.), feel free to add it to your explanation.   

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library/API you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible as submissions are evaluated on a rolling basis.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

# Alright, Let's begin

Hypothesis: I’ve read what was presented. I can confirm that the first paragraph, at least, is from Fahrenheit 451, so I looked back at the book for context of the scene. From looking without context, although, I can tell that the sentiment is definitely aggravated or rage. This definitely goes counter to the next paragraph that seems to be more focused on praise or positivity.

In context, when it comes to the fahrenheit 451 passage, it is with Beatty mocking Montag, challenging his belief in the books and, through a made up argument row, mockingly making a strawman of Montag that screams with rage in defense of “his” books as Beatty, nearly with boredom, laughs away his arguments with his own. I would assume this is meant to be a rage filled passage with small bouts of mockery.

The second passage is from the biography of Benjamin franklin. Now, we are shifting from the mocking of a person through the image of another to the positive speaking of a man through his biography. It's gonna be subjective, although, as it's coming from a person speaking about him in a personal sense rather than the use of neutral facts about his life. 

I’ll have to separate the paragraphs, but it’s simple what should come: rage and mockery from the first paragraph (negative), praise and positivity for the second (positive).

###### Libraries, packages, and tutorials used:

I used the packages:

Punkt
Averaged_perceptron_tagger
Stopwords
wordnet

I used the libraries:

numpy
matplotlib
math
nltk
vaderSentiment
TextBlob
pandas
re

And I used these tutorials and articles in the process of this README:

https://github.com/adashofdata (Alice Zhao has a tutorial on nltk that also helped me analyze the model sentiment over time for the text)

https://nlp.stanford.edu/courses/cs224n/2009/fp/24.pdf (This is the documentation for textBlob)

https://medium.com/@piocalderon/vader-sentiment-analysis-explained-f1c4f9101cd9 (This is an explanation for how VADER sentiment analysis works)

https://www.analyticsvidhya.com/blog/2021/06/rule-based-sentiment-analysis-in-python/#h2_5 (This is the main tutorial I followed for coding the model)

https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/03_subset_data.html (I also, of course, used the pandas documentaion in the creation of the data frame)

# How it works

So, I actually did multiple different tests for the data:

**First test (textBlob with clean data, no lemmatization):**

I got rid of all the special characters and did not process the data with lemmatization

Results were wrong, at least in my eye:

|Part of text|Cleaned text|Lemma|Subjectivity|Polarity|Analysis|
|------------|------------|-----|------------|--------|--------|
|Paragraph_1 |Stop ...    |Stop | 0.624206   |0.174603|Positive|
|Paragraph_2 |I thin...   |think| 0.585794   |0.221746|  Positive

Paragraph one returned a positive analysis for a scene that is meant to be tense and mocking of one person. It even uses language like yelled, towered, and screamed. This doesn’t even mention the mockery.

The second paragraph returned a positive with high subjectivity...for a biography on benjamin franklin. Either we found something flawed with the biography (and, in any essential detail, with talks about the founding fathers...which is not unlikely.) or the analysis was not that...good.

The good result from this, at the very least, is that Beatty’s dream contains more subjectivity than the biography...which is definitely a good thing in measure (though it could mean that, in analysis, we could not dictate the difference between something highly biased and something that was meant not to be).

**Second test (Vader sentiment analysis with clean data, no lemm):**

Same thing as the first but with VADER instead of textBlob

This resulted in a result that differed quite a bit:

| Part of text|Cleaned text |Lemma|polarity |Sentiment Vader Analysis|             
|-------------|-------------|-----|---------|------------------------|
|Paragraph_1  |Stop ...     |Stop |-0.8275  | Negative               |   
|Paragraph_2  |I thin...    |think|0.9979   | Positive               |

Like the analysis I gave of the text a while ago, Vader analysis returned that paragraph 1 is negative...though it reported that paragraph_2 was positive. Such an analysis, and one that is almost reaching highly positive in mention of the text, means that there is probably some subjective language being used, that being the most likely reason for why it isn’t neutral (This, although, aligns with my hypothesis)

**Third test (Cleaned up the data and did some lemmatization, still using vader analysis):**

Same analysis, just with the use of lemmatization

Not much change….

|Part of text|Cleaned text|Lemma|polarity| Sentiment Vader Analysis|
|------------|------------|-----|--------|-------------------------|
|Paragra...   |Stop ...   |   Stop...|    -0.7665  |       Negative |   
|Paragra...  |I thin...    |  thin... |    0.9963   |      Positive  | 

By cleaning up the data with clarification of word use via POS tagging then lemmatization of those words...we didn’t really get much of a difference. Interestingly though, there is such a low change with the franklin biography while there is almost a full .1 change for the Beatty monologue. 

**Fourth test (Cleaned up the data and did some lemmatization, used textblob):**

Same thing but with textBlob now

|Part of text| Cleaned text |     Lemma|  Subjectivity | Polarity|  Analysis|
|------------|--------------|----------|---------------|---------|----------|
|Paragra...|   Stop ...      |Stop... |  0.640909  |   0.331818 | Positive|
|Paragra... | I thin...     | thin...  | 0.597738   |  0.233452 | Positive|

Again, there is far more of a jump with Beatty's dream dialouge than Benjamin Franklin biography. Still though, textBlob is coming up short

# Curiosity got the better of me

I wanted to see __why__ there was such a difference for these models so, with the help of the tutorial from Alice Zhao, I ran some analysis of sentiment as time went on during the analysis (Lemmatization was used for both tests as the change for text was markes similarly when it was used, meaning there most likely will not be any significant change wether or not it is or isn't used):

**Testing analysis over time with textBlob:**

![Picture1](https://user-images.githubusercontent.com/22717191/132308849-403a3274-ff5b-4155-ae53-f1be10347956.png)

After separating the text of paragraph_1 into 10 segments, those segments gave scores of:

[0.2, 0.30000000000000004, 0.7, 0.0, 0.17500000000000002, 0.7, 0.2, 0.0, 0.15, 0.0]

![Picture2](https://user-images.githubusercontent.com/22717191/132308956-c5eb60a8-b1f9-4bb9-988d-b0c36ab9792c.png)

After separating the text of paragraph_1 into 10 segments, those segments gave scores of:

[0.48333333333333334, 0.1375, 0.44999999999999996, 0.0, 0.39999999999999997, 0.10000000000000002, 0.1625, 0.0025000000000000135, 0.7333333333333334, 0.08750000000000001]

**Testing analysis over time with Vader:**

![Picture3](https://user-images.githubusercontent.com/22717191/132309100-21fd545f-79d8-45a0-bc1f-de7d73301220.png)

After separating the text of paragraph_1 into 10 segments, those segments gave scores of:

[0.2617, -0.7184, 0.2837, -0.7579, -0.6602, 0.6808, 0.5267, -0.5719, 0.0, 0.4215]

![Picture4](https://user-images.githubusercontent.com/22717191/132309167-b9c7474a-3eeb-4ebc-9ca5-38cf19c65f7e.png)

After separating the text of paragraph_1 into 10 segments, those segments gave scores of:

[0.8919, 0.8883, 0.9366, 0.3919, 0.7184, 0.8591, 0.842, -0.1531, 0.4033, 0.5758]

# Why is there a differnce?


Why the difference? Well, textblob comes from the stanford NLTK set, which was trained on IMBD movie reviews. It gives a score to certain words and applies those scores to the words that we analyze in our little text here (actually, the documentation for it states that the scores and words that were gained from the reviews were hand made!). I actually looked up the dataset and searched for a lot of the words that I had seen in the two paragraphs and found quite a bit of them missing, a good amount that I can tell had connotations for negativity missing. The documentation states they used a combination of SVM, Naive Bayes, and k-means clustering (things I’m familiar with) so I looked up their uses in my old machine learning journal. Sadly, I can’t say much without doing the ensemble learning of the three models myself. Either way, that clears up some of the mystery. Still, the documentation does give some good kernels: 

“Language models, even trigram models, are deeply flawed by their reliance on only immediate preceding text and these flaws are what opens up the possibility of more generic machine learning techniques to surpass them” 

and

 “The results indicate that the first two methods implemented did little better than blind guessing and were blatantly inefficient. The third method implemented, that of stop words, was successful in a statistically significant way. Indeed, it allowed for an average of 60 percent correctness on the positive /negative set and 54 percent on the objective / subjective set. The explanation for the success of stop words reposes mainly on the fact that ignoring high count words such as the, is, and an allows the metric to stop favoring pairings between reviews of similar sizes. This is because the length of reviews is in a range which leaves a significant difference in the probability assigned to such words as the, is, and an between short and lengthy reviews

I’ll definitely be sticking to this documentation for if I do sentiment later on, as it clarifies the exact reasons for why analysis might go awry using the data from IMDB reviews. Although their model didn’t help as much as Vader, their preprocessing techniques certainly did. (https://nlp.stanford.edu/courses/cs224n/2009/fp/24.pdf)

So why does vader work better? Simple: it uses a lexical approach while textblob uses a machine learning approach. What that means is this: Vader will observe the words of a sentence and attach sentiments to them to then get the sentiment of a whole sentence __but__ it will also look at the way the sentence is written. TexTBlob will just look at the words out of context of the sentence and draw conclusions about the text without consideration of structure. That’s why it was more effective in this case.

It even uses 5 heuristics: punctuation (difference between “.” and “!!!”), capitalization (“amazing” vs “AMAZING”), degree modifiers (“effing cute” vs “sort of cute”), shift in polarity due to “but” (“I love you, but I don’t want to be with you anymore), and examining the tri-gram (this one confused me for a bit but basically there are three lexical features in examination and VADER keeps a list of negator words that multiply the sentiment of a score based on a determined value)

The documentation of VADER also contains some interesting things...but I’m afraid I’m keeping this read me a tad bit too long.

I noticed I used Vader wrong, although, as I got rid of the punctuation and structure of the sentence. So, how does the analysis look with all of those things included?

|Part of text|Raw text|Lemma|Vader Sentiment |  Vader Analysis|
|------------|--------|-----|----------------|----------------|
|Paragraph_1 | "Stop ...|    Stop...|    -0.9228 |          Negative|    
|Paragraph_2 | I thin...|    thin... |    0.9979|           Positive | 

![Picture5](https://user-images.githubusercontent.com/22717191/132310202-d148e8f9-12d2-4261-8103-28b4a627c603.png)

After separating the text of paragraph_1 into 10 segments, those segments gave scores of:

[0.2617, -0.7184, 0.3481, -0.7777, -0.7174, 0.7088, 0.0, -0.6114, 0.0, 0.4215]

![Picture6](https://user-images.githubusercontent.com/22717191/132310477-1939a273-e369-41de-ad3a-890da1992512.png)

After separating the text of paragraph_2 into 10 segments, those segments gave scores of:

[0.8919, 0.8883, 0.9366, 0.3919, 0.7184, 0.8591, 0.842, -0.1531, 0.4033, 0.5758]

It's a lot more on the extreme side, but I feel it may reflect the information a bit better when it comes to the strucutre of what we're looking at.


In looking over all the information on the two models, I found that it would be best to use textBlob for large datasets, while vader is best for small analysis of texts and stories.

...Just placing my curiosity into the bowl :)

# Conclusions

In depending on the model, you will either get that the first and second paragraph were both positive with a bit of subjectivity by the authors (TextBlob) or You will get that the first paragraph was immensley negative while the second paragraph was immensley positive (VADER). I believe VADER was the more accurate model based on what you've seen above and the error presented by TextBlob in the first test. Therefore, the sentiment of the first paragraph was negative, and the second positive.
