# utility-methods
This repository consists snippets of some commonly used functions

### 1. Getting timezone from postal code and country code.
This method finds the timezone in Olson format.
Example: postalcode: 60007, countycode: US -> timezone: America/Chicago.
Google API have been used for getting the location details.

### 2. Tokenizing string by sentences.
This method breaks a string into sentences irrespective of the abbreviations and designations like Mr. Jr. etc.
It can also tokenize complicated sentences like "Mr. John Johnson Jr. was born in the U.S.A but earned his Ph.D. in Israel before joining Nike Inc. as an engineer. He also worked at craigslist.org as a business analyst."

