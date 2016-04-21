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

Keep the code as simple as possible. No need of obfuscation / code golf.

If you have to explain your code, you're doing it wrong!

Apart from these, contributions directly to the framework are also welcome!
