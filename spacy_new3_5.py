import spacy 
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_trf")

doc = nlp("I like Landon adn Berlin.")
matcher = Matcher(nlp.vocab, validate=True)
pattern = [{"TEXT": {"FUZZY": "London"}}, {"TEXT": {"FUZZY": "and"}}, {"TEXT": {"FUZZY": "Berlin"}} ]
matcher.add("pattern", [pattern])
matches = matcher(doc)

for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]  # Get string representation
    span = doc[start:end]  # The matched span
    print(match_id, string_id, start, end, span.text)
# 15329811787164753587 pattern 2 5 Landon adn Berlin


"""
Fuzzy matching allows you to match tokens with alternate spellings, typos, etc. without specifying every possible variant.
Matches "favourite", "favorites", "gavorite", "theatre", "theatr", ...
pattern = [{"TEXT": {"FUZZY": "favorite"}},
           {"TEXT": {"FUZZY": "theater"}}]

 By default FUZZY allows a Levenshtein edit distance of at least 2 and up to 30% of the pattern string length. 
 Using the more specific attributes FUZZY1..FUZZY9 you can specify the maximum allowed edit distance directly.


Match lowercase with fuzzy matching (allows 3 edits)
pattern = [{"LOWER": {"FUZZY": "definitely"}}]

Match custom attribute values with fuzzy matching (allows 3 edits)
pattern = [{"_": {"country": {"FUZZY": "Kyrgyzstan"}}}]

Match with exact Levenshtein edit distance limits (allows 4 edits)
pattern = [{"_": {"country": {"FUZZY4": "Kyrgyzstan"}}}]

Starting in spaCy v3.5, both REGEX and FUZZY can be combined with the attributes IN and NOT_IN

pattern = [{"TEXT": {"FUZZY": {"IN": ["awesome", "cool", "wonderful"]}}}]
pattern = [{"TEXT": {"REGEX": {"NOT_IN": ["^awe(some)?$", "^wonder(ful)?"]}}}]
"""