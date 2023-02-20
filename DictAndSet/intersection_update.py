text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

split_text = text.split()
print(split_text)

preps_used = set(split_text).intersection(prepositions)
print(preps_used)
