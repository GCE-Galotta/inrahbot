# inrahbot

Quick and dirty bot for [Discord](https://discord.com/) groups. Randomly selects one card from a deck, posts it and its corresponding text to the channel.
It uses the [discordpy](https://discordpy.readthedocs.io/en/stable/index.html) library.
For more info on discord bots, refer to the [discord developer portal](https://discord.com/developers/docs/intro).
Also, [this](https://realpython.com/how-to-make-a-discord-bot-python/) is a good tutorial.

## prerequisites
* `discord.py`
* `python-dotenv`
* Images of the cards you want to use
* Tested with `Python 3.8.10`

## usage
* Place your discord token in `.env` file.
* Place card images (in .png format) in folder "Karten".
* run `python3 inrahbot`

For copyright reasons, the cards are not included. If you want to use different images, just replace them in the folder "Karten".
The card texts are taken from the "Inrah-Project" a fan project by Markus Hattenkofer, Mike Wimmer and Tobias Rosenberger.
It can be found at the [Borbarad-Projekt](https://www.borbarad-projekt.de/index.php?page=main_downloads). There are also card images available there.
