# JARVIS on Messenger

Just A Rather Very Intelligent System, now on Messenger!

[![Build Status](https://travis-ci.org/swapagarwal/JARVIS-on-Messenger.svg?branch=master)](https://travis-ci.org/swapagarwal/JARVIS-on-Messenger)
![Python](https://img.shields.io/badge/python-2.7-blue.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/swapagarwal/JARVIS-on-Messenger/master/LICENSE)
[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/swapagarwal/JARVIS-on-Messenger?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Messenger is now used by 900 million people every month. With the launch of Send / Receive API, bots are about to [take](http://time.com/4291214/facebook-messenger-bots/) [over](http://www.computerworld.com/article/3055588/social-media/an-army-of-chatbots-will-take-over-facebook-here-s-why.html).

### Why?

I created JARVIS with two goals in mind:

1. It should have a lot of useful features (both fun and commonly used).
2. Anyone can contribute to this project. (As this is module-based, anybody with a decent knowledge of Python can contribute.) One of the prime goals of this project is to lower the entry barrier in the world of open source.

Take a look at the [contributing guidelines](https://github.com/swapagarwal/JARVIS-on-Messenger/blob/master/CONTRIBUTING.md) to see how easy it is to add your code. I'll be waiting for your pull request! :wink:

### Demo (Vimeo)

<a href="https://vimeo.com/163328859" target="_blank" title="Click to open Vimeo link">
  <img src="https://i.vimeocdn.com/video/566604309_640.jpg" alt="JARVIS on Messenger Demo" width="300">
</a>

### TODO

There are a lot of features that I've planned for JARVIS. Feel free to add to this list by opening an issue / PR.

- [ ] Book Rating
- [x] Movie Rating
- [ ] News
- [ ] Weather
- [ ] Currency Conversion
- [ ] Random Quote / Fact
- [x] Random Joke
- [x] Dictionary ([#1](https://github.com/swapagarwal/JARVIS-on-Messenger/pull/1))
- [ ] Wikipedia Summary
- [ ] Weather

Some advanced features:

- [ ] Add templates support (Structured Messages)
- [x] Integrate with [Wit.ai](https://wit.ai/swapagarwal/JARVIS-on-Messenger) to parse Natural Language
- [ ] Retain context between queries

### Structure

```sh
├── modules/         # home for various features
├── modules/src/     # code goes here
├── modules/tests/   # tests go here
├── CONTRIBUTING.md  # contributing guidelines
└── jarvis.py        # the main bot
```

### Usage

JARVIS is at your service [here](http://m.me/J.A.R.V.I.S.on.Messenger). Currently, it's pending approval before the public can engage. If you'd like to be a tester, post [here](https://www.facebook.com/J.A.R.V.I.S.on.Messenger/posts/551338921704902).

### Sample Queries

`Hi, Jarvis!`  
`Are you there?`  
`tell me a joke`  
`iron man movie`  
`define a superhero`  
More examples can be found [here](https://github.com/swapagarwal/JARVIS-on-Messenger/tree/master/modules/tests).

### Local Development / Testing


1. Clone this repo.
For LINUX users:
2. `sudo apt-get install python-dev libffi-dev libssl-dev`
For Mac/OSX users:
a) If you install Python using brew, the relevant headers are already installed for you. In other words, you don't need python-devel.
b) brew install pkg-config libffi
   export PKG_CONFIG_PATH=/usr/local/Cellar/libffi/3.0.13/lib/pkgconfig/ # May change with libffi version
   pip install cffi
c) brew install libtins
3. `pip install -r requirements.txt`
4. `python jarvis.py`
5. Visit the following URLs to see results:  
`http://localhost:5000/process/?q=<YOUR_QUERY>` returns the intent of the query.  
`http://localhost:5000/search/?q=<YOUR_QUERY>` returns the search result of the query.

### History

I started out with rule-based model but it didn't scale well so now I've shifted to Natural Language Processing.
Rest assured, I'll strive to keep it as simple as possible so that you, yes you, can contribute!

If you'd like to contribute to the old model, you are welcome to do so as well.
I've created a new branch [`legacy`](https://github.com/swapagarwal/JARVIS-on-Messenger/tree/legacy) for this purpose. I'll be accepting Pull Requests to this branch also. :smile:
