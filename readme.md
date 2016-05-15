# A Partial Introduction to Digital Literary Studies

This repository is a collection of files designed for my workshop on digital literary studies for Scott Weingart's Digital Humanities Workshop at Carnegie Mellon University (May 2016). The two-hour workshop/tutorial focuses on giving absolute beginners a taste of what it's like to engage in computational literary analysis (which might include things like text mining, stylometry, authorship attribution, and distant reading). The repo is divided into several sections:

## Workshop Schedule and Instructions

15-20 minutes: Activity reading text excerpts.
30-40 minutes: Basics of Python 3 (interactive).
30-40 minutes: Unpacking Ted Underwood and Jordan Sellers on "Literary Diction."
20 minutes: Wrapping up, next steps, reflecting.

## Instructions
### Text Excerpts Activity:
Workshop participants should break into groups of 2-4 people, dpeneding on the size of the audience. Each group gets a text excerpt printout. (If you're viewing this on Github, these excerpts are in the excerpts folder). Each group should read their text and formulate a hypothesis of what time period it comes from. be prepared to explain why your group thinks so.

### Basics of Python 3:

In this repository are snippets of Python code to run in a Jupyter Notebook. Workshop participants can use the Jupyter Notebook server I've set up on my supercomputing account. Anyone else can try these snippets by clicking the Binder link below. Doing so will launch a temporary Notebook server pre-configured to run all the scripts in the repo.

Once the Notebook launches, click for_snippets.ipynb to launch the empty Notebook (Python 3 kernel). Then paste code into a cell and hit the play button to interact with it. If you're still confused, check out this video on using Jupyter Notebooks: https://www.youtube.com/watch?v=Rc4JQWowG5I

### The snippet files, in their original order, are:

1. basic_types.py
2. loops_function_conditionals.py
3. libraries.py
4. working_with_text.py

Note: I've preloaded working_with_text.py into a Python Notebook called MattLavin.ipynb. If you want to run those snippets, you can do so all at once by launching that Notebook using the Mybinder link. The challenge at the bottom, to "make a loop to remove stopwords and see which ones are most common," is solved in solution.py but, the list of stopwords in English depends on data downloaded from nltk-download(), which will not work on mybinder.org. So solution.py has the original code commented out and includes a local list of the same stopwords. If running this script on mybinder, uncomment lines 8-21 and comment lines 4-5.

### Interactive Demo
The script for this portion of the workshop is in underwood_sellers_demo.py. The article descriving their work is here: http://journalofdigitalhumanities.org/1-2/the-emergence-of-literary-diction-by-ted-underwood-and-jordan-sellers/
The demo does not replicate their work precisely but instead attempts to sketch out some of the fundamental computational text analysis skills necessary to do something like what they did. For convenience, my version works with a much smaller set of texts and does not employ an intervening database (although it could be adapted to do so quite easily).

Note: This demo trains a unigram tagger using data downloaded from nltk-download(), which will not work on mybinder.org. As a result, I've modified the  If running this script on mybinder, uncomment lines 22-24 and comment lines  8-19.

## Additional Topics and Resources
These topics and links are here for the benefit of workshop participants, but others might find them useful.

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/repo/mjlavin80/basics_of_text_analysis_in_python)
