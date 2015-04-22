Twitter Sentiment classifier
===================

- - - - 

PyPI release: https://pypi.python.org/pypi/tweet_classifier

Author: diogonal

With this tool you can analyse sentiment on tweets and classify them in positive, neutral or negative according to the computed polarity and subjectivity. Although it is oriented to tweets, you can use it for any text.

Tweets are analysed considering the following aspects:

* Emoticons contribute to perform a more accurate anlaysis.
* URL's, emails, non-ascii characters, etc, are ignored.
* Sentiment analysis is performed against the cleaned text by using TextBlob.

## Dependencies

$`pip install twitter-text-python`

$`pip install -U textblob`

$`python -m textblob.download_corpora`

Further Information about TextBlob [Here](http://textblob.readthedocs.org/en/latest/install.html)

## Installation

>`pip install tweet_classifier`

## Usage

```python
  import tweet_classifier.classifier as classifier
  sentiment = classifier.doSentimentAnalysis("I'm happy to be here! test@gmail.com All good :)")
  print(sentiment["text"])
  print(sentiment["sentiment"])
  print(sentiment["polarity"])
  print(sentiment["subjectivity"])
```
And the results will be:

```python
I'm happy to be here!  All good :)
positive
0.7333333333333334
86.66666666666667
```

## Credits

[TextBlob](https://github.com/sloria/TextBlob)

[twitter-text-python](https://github.com/edburnett/twitter-text-python)


## License

The MIT License (MIT)

Copyright (c) 2015 Diego Montufar.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
