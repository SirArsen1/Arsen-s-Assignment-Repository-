import cowsay, pyjokes

joke = (pyjokes.get_joke(language='en'))
cowsay.cow(joke)