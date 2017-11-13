## Create a new module

To add a new module, follow these steps:

1. Fork the repo
2. Create a new branch (`git checkout -b my-new-feature`)
3. Add a new file in `modules/src/` folder (define `process` function)
4. Add some tests in `modules/tests/` folder
5. Add the module name in `src/__init__.py`
6. Commit your changes (`git commit -am 'Add some feature'`)
7. Push to the branch (`git push origin my-new-feature`)
8. Create a Pull Request 

Kindly note that your tests may fail initially as I'll have to configure wit.ai to handle these new types of queries. Just include some sample queries in your PR's description for the initial training.

## Improve an existing module

To fix a bug or enhance an existing module, follow these steps:

1. Fork the repo
2. Create a new branch (`git checkout -b improve-feature`)
3. Make the appropriate changes in the required file in `modules/src/` folder
4. Add / Edit tests in `modules/tests/` folder to reflect the changes made (run them locally with `py.test`)
5. Commit your changes (`git commit -am 'Improve feature'`)
6. Push to the branch (`git push origin improve-feature`)
7. Create a Pull Request 

## Bug / Feature Request

If you find a bug (the bot couldn't handle the query and / or gave irrelevant results), kindly open an issue [here](https://github.com/swapagarwal/JARVIS-on-Messenger/issues/new) by including your search query and the expected result.

If you'd like to request a new functionality, feel free to do so by opening an issue [here](https://github.com/swapagarwal/JARVIS-on-Messenger/issues/new) including some sample queries and their corresponding results.

## General

If you're working on something, let us know by creating an issue, or commenting on an existing one. Win-win for everyone!

Keep the code as simple as possible. No need of obfuscation / code golf.

If you have to explain your code, you're doing it wrong!

Apart from these, contributions directly to the framework are also welcome!

You can use the following commits for reference: [coin](https://github.com/swapagarwal/JARVIS-on-Messenger/commit/e3f9f587b9b6d05efb1a2769a4cd75fb4855b4f9), [lyrics](https://github.com/swapagarwal/JARVIS-on-Messenger/commit/d3e7b7c969cc3ca1f8276bab0357c9f3c680b236), [news](https://github.com/swapagarwal/JARVIS-on-Messenger/commit/59beb1ca0a0f5210ebf44809282d0cc7d3d42874), [xkcd](https://github.com/swapagarwal/JARVIS-on-Messenger/commit/e322d312525545d1993fe9bda1c5d78f1407095e), etc.

## How the AI works

[Here](https://www.youtube.com/watch?v=tLdjaKkJK_8) is a quick intro to wit.ai

<a href="https://vimeo.com/238717639" target="_blank" title="Click to open Vimeo link">
  <img src="https://i.imgur.com/qZeRlBk.jpg" alt="Wit.ai Demo" width="500">
</a>

P.S. If you've come this far, you might as well contribute.
Looking for a place to start? Take a look at some of the [low-hanging fruits](https://github.com/swapagarwal/JARVIS-on-Messenger/labels/Low-Hanging%20Fruit)!
