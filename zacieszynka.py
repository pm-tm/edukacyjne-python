import pyjokes

def generate_joke():
    joke = pyjokes.get_joke(language='pl', category='neutral')
    return joke

if __name__ == "__main__":
    print(generate_joke())