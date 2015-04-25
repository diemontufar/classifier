from distutils.core import setup
setup(
  name = 'tweet_classifier',
  packages = ['tweet_classifier'],
  version = '1.1.3',
  package_data={'': ['sentiments.json']},
  description = 'A sentiment classifier for tweets',
  author = 'Diego Montufar',
  author_email = 'diogonal0@gmail.com',
  url = 'https://github.com/diogonal/classifier', 
  download_url = 'https://github.com/diogonal/classifier/tarball/v1.1.3', 
  keywords = ['tweet', 'sentiment', 'classifier'], 
  classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic',
    ],
)