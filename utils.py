import spacy


def eng_tokenizer(text, eng):

    return [token.text for token in eng.tokenizer(text)]


def get_tokens(data_iter):
    for item in data_iter:
        yield eng_tokenizer(item)
