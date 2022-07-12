from transformers import pipeline

def load_model():
    '''Loads and returns Facebook BART model trained on CNN Daily Mail for text summarization.'''
    model = pipeline("summarization", model="./bart")
    return model


def summarize_text(text: str, model):
    summary_text = model(text)
    return summary_text


if __name__ == "__main__":
    model = load_model()
    text = '''
    The Elder Scrolls V: Skyrim is an action role-playing video game developed by Bethesda Game Studios and published by Bethesda Softworks. It is the fifth main installment in the Elder Scrolls series, following 2006's The Elder Scrolls IV: Oblivion, and was released worldwide for Microsoft Windows, PlayStation 3, and Xbox 360 on November 11, 2011.

The game is set 200 years after the events of Oblivion, and takes place in Skyrim, the northernmost province of Tamriel. Its main story focuses on the player's character, the Dragonborn, on their quest to defeat Alduin the World-Eater, a dragon who is prophesied to destroy the world. Over the course of the game, the player completes quests and develops the character by improving skills. The game continues the open-world tradition of its predecessors by allowing the player to travel anywhere in the game world at any time, and to ignore or postpone the main storyline indefinitely.

Skyrim was developed using the Creation Engine, which was rebuilt specifically for the game. The team opted for a unique and more diverse open world than Oblivion's Imperial Province of Cyrodiil, which game director and executive producer Todd Howard considered less interesting by comparison. Upon release, the game received critical acclaim, with praise for its character advancement, world design, visuals, and dual-wielding combat, and is considered by many to be one of the greatest video games ever made. Criticism targeted the melee combat, the dragon battles, and the numerous technical issues present at launch. The game shipped over seven million copies within the first week of its release, and sold 30 million copies on all platforms by 2016, making it one of the best-selling video games in history.

Three downloadable content (DLC) add-ons were released separately—Dawnguard, Hearthfire and Dragonborn—which were bundled along with the base game into The Elder Scrolls V: Skyrim – Legendary Edition and released in June 2013. A remastered version, titled The Elder Scrolls V: Skyrim – Special Edition, was released for Windows, PlayStation 4 and Xbox One in October 2016, with all three DLC expansions and a graphical upgrade. A port for the Nintendo Switch was released in November 2017. A separate VR-only version, titled The Elder Scrolls V: Skyrim VR, was released in November 2017 for PlayStation 4 using PlayStation VR, and for Windows-based VR headsets in April 2018. In addition, the Special Edition was released on PlayStation 5 and Xbox Series X/S as part of the compilation The Elder Scrolls V: Skyrim – Anniversary Edition in November 2021.


    '''
    results = summarize_text(text,model)[0]
    print(results)