# JARVIS on Messenger

Just A Rather Very Intelligent System, now on Messenger!

[![Build Status](https://travis-ci.org/swapagarwal/JARVIS-on-Messenger.svg?branch=master)](https://travis-ci.org/swapagarwal/JARVIS-on-Messenger)
![Python](https://img.shields.io/badge/python-2.7-blue.svg)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![Gitmoji](https://img.shields.io/badge/gitmoji-%20🚀%20🐳-FFDD67.svg)](https://gitmoji.carloscuesta.me)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/swapagarwal/JARVIS-on-Messenger/master/LICENSE)
[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/swapagarwal/JARVIS-on-Messenger?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Contributors](https://img.shields.io/github/contributors/swapagarwal/JARVIS-on-Messenger.svg)](https://github.com/swapagarwal/JARVIS-on-Messenger/graphs/contributors)
[![Beginner Issues](https://img.shields.io/github/issues/swapagarwal/JARVIS-on-Messenger/Low-Hanging%20Fruit.svg?label=low-hanging%20fruits)](https://github.com/swapagarwal/JARVIS-on-Messenger/labels/Low-Hanging%20Fruit)

Messenger is now used by 1.2 billion people every month. With the launch of Send/Receive API, bots are about to [take](http://time.com/4291214/facebook-messenger-bots/) [over](http://www.computerworld.com/article/3055588/social-media/an-army-of-chatbots-will-take-over-facebook-here-s-why.html).

### Usage

JARVIS is at your service [here](https://m.me/J.A.R.V.I.S.on.Messenger).

### Demo (Vimeo)

<a href="https://vimeo.com/226022581" target="_blank" title="Click to open Vimeo link">
  <img src="https://i.vimeocdn.com/video/645512677_640.jpg" alt="JARVIS on Messenger Demo" width="300">
</a>

### Why?

I created JARVIS with two goals in mind:

1. It should have a lot of useful features (both fun and commonly used).
1. Anyone can contribute to this project. (As this is module-based, anybody with a decent knowledge of Python can contribute.) One of the prime goals of this project is to lower the entry barrier into the world of open source.

Take a look at the [contributing guidelines](https://github.com/swapagarwal/JARVIS-on-Messenger/blob/master/CONTRIBUTING.md) to see how easy it is to add your own code. I'll be waiting for your pull request! :wink:

A massive Thank You to all [contributors](https://github.com/swapagarwal/JARVIS-on-Messenger/graphs/contributors), and congratulations to people who made their first open-source contribution! :tada:

### Modules

Feel free to add to this list by opening an Issue/Pull Request.

| Name | Sample Query | Source (w/ Attribution) |
|:-:|:-:|:-:|
| anime | death note anime | Kitsu |
| book | anything you want book | Powered by Goodreads |
| bye | goodbye | --- |
| coin | flip a coin | --- |
| currency | usd to eur rate | Fixer.io |
| dice | roll a die | --- |
| dictionary | define comfort | Words API |
| fact | tell me a fact | [JARVIS](https://github.com/swapagarwal/JARVIS-on-Messenger/blob/master/data/facts.json) |
| hello | Hi, Jarvis! | --- |
| help | What can you do? | --- |
| joke | tell me a joke | [JARVIS](https://github.com/swapagarwal/JARVIS-on-Messenger/blob/master/data/jokes.json) |
| lyrics | paradise lyrics | Powered by musiXmatch |
| movie | iron man 2 movie plot | <img src="/images/powered_by_tmdb.png"/> |
| music | songs by linkin park | Spotify |
| news | latest news | Powered by NewsAPI |
| ping | ping google.com | Is it up? |
| quote | random quote | [JARVIS](https://github.com/swapagarwal/JARVIS-on-Messenger/blob/master/data/quotes.json) |
| request | report a bug <br> request a feature | --- |
| thanks | Thank you! | --- |
| time | time in seattle | TimeZoneDB API |
| url | shorten google.com <br> expand http://goo.gl/7aqe | Google URL Shortener |
| video | videos of sia | YouTube |
| weather | weather in london | Info provided by OpenWeatherMap |
| wiki | wiki html | MediaWiki API |
| xkcd | show a random xkcd comic | [xkcd](https://xkcd.com/json.html) |

More sample queries can be found [here](https://github.com/swapagarwal/JARVIS-on-Messenger/tree/master/modules/tests).

### Structure

```sh
├── modules/         # home for various features
├── modules/src/     # code goes here
├── modules/tests/   # tests go here
├── data/            # home for shared data
├── templates/       # for sending structured messages
├── CONTRIBUTING.md  # contributing guidelines
└── jarvis.py        # the main bot
```

### Local Development / Testing

1. Clone this repo.
2. Linux:  
a) Debian (Ubuntu, Linux Mint, etc.): `sudo apt-get install python-dev libffi-dev libssl-dev`  
b) Arch Linux: `sudo pacman -S python2 libffi openssl`  
c) Fedora: `sudo yum install python-devel libffi-devel openssl-devel`  
Windows: These should already be pre-installed in your Python bundle.  
Mac/OS X:  
a) If you install Python using brew, the relevant headers are already installed for you. In other words, you don't need python-devel.  
b) `brew install pkg-config libffi`  
`export PKG_CONFIG_PATH=/usr/local/Cellar/libffi/3.0.13/lib/pkgconfig/` # May change with libffi version  
`pip install cffi`  
c) `brew install libtins`  
3. `pip install -r requirements.txt`
4. `python jarvis.py`
5. Visit the following URLs to see results:  
`http://localhost:5000/process/?q=<<YOUR_QUERY>>` returns the intent of the query.  
`http://localhost:5000/search/?q=<<YOUR_QUERY>>` returns the search result of the query.

![result](/images/result_hello.png)

![result](/images/result_joke.png)

* The "process" endpoint returns what module the system classifies your query e.g. a dictionary query, a song search, etc. Visit the following URLs to understand the output format:  
`http://localhost:5000/process/?q=tell%20me%20a%20joke`  
`http://localhost:5000/process/?q=time%20in%20seattle`  
`http://localhost:5000/process/?q=convert%2025%20usd%20to%20eur`  
> You can mock the results for local testing by adding your queries [here](https://github.com/swapagarwal/JARVIS-on-Messenger/blob/master/local/wit.json).
* The "search" endpoint returns the actual bot output, which you get when you interact with the bot using that query.

Note that for the search query to work, you have to set your own key (of the module that you want to test) in config.py  

If you want a public endpoint, use the below button to deploy on Heroku and fill the relevant API keys that you would like to use:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### TL;DR for Beginners

1. J.A.R.V.I.S. runs on Python 2
1. For the search query to work, you have to set your own key (of the module that you want to test) in config.py
1. The best place to ask anything: https://gitter.im/swapagarwal/JARVIS-on-Messenger
1. Some issues are reserved for you! https://github.com/swapagarwal/JARVIS-on-Messenger/labels/Low-Hanging%20Fruit
1. If you're working on something, let everyone know by either creating an issue or commenting on an existing one so that work is not duplicated.
1. Prefer using an IDE (Use [PyCharm](https://www.jetbrains.com/pycharm/download/) if you don't have any preference yet)

### History

I started out with a rule-based model, but it didn't scale well so now I've shifted to Natural Language Processing.
Rest assured, I'll strive to keep it as simple as possible so that you, yes you, can contribute!

If you'd like to contribute to the old model, you are welcome to do so as well.
I've created a new branch [`legacy`](https://github.com/swapagarwal/JARVIS-on-Messenger/tree/legacy) for this purpose. I'll be accepting Pull Requests to this branch also. :smile:

P.S. If you've come this far, you might as well contribute.
Looking for a place to start? Take a look at some of the [low-hanging fruits](https://github.com/swapagarwal/JARVIS-on-Messenger/labels/Low-Hanging%20Fruit)!

### References

* https://github.com/toddmotto/public-apis
