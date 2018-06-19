# utility-methods
This repository consists snippets of some commonly used functions

### 1. Getting timezone from postal code and country code.
This method finds the timezone in Olson format.
Example: postalcode: 60007, countycode: US -> timezone: America/Chicago.
Google API have been used for getting the location details.

### 2. Tokenizing string by sentences.
This method breaks a string into sentences irrespective of the abbreviations and designations like Mr. Jr. etc.
It can also tokenize complicated sentences like "Mr. John Johnson Jr. was born in the U.S.A but earned his Ph.D. in Israel before joining Nike Inc. as an engineer. He also worked at craigslist.org as a business analyst."

### 3. Tokenizing string by sentences (spaCy)
spaCy excels at large-scale information extraction tasks. It's written from the ground up in carefully memory-managed Cython. Independent research has confirmed that spaCy is the fastest in the world. If your application needs to process entire web dumps, spaCy is the library you want to be using.
It is the best way to prepare text for deep learning. It interoperates seamlessly with TensorFlow, PyTorch, scikit-learn, Gensim and the rest of Python's awesome AI ecosystem. With spaCy, you can easily construct linguistically sophisticated statistical models for a variety of NLP problems.

