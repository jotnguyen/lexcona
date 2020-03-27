import lexnlp.extract.en.amounts
# import lexnlp.extract.en.definitions
text = "the two Discloser will retain all interest and property rights to the ten dogs"
print(list(lexnlp.extract.en.amounts.get_amounts(text)))
# print(list(lexnlp.extract.en.definitions.get_sentence_span(text)))
