import pandas as pd

# # This script will collect the required datasets from the source website
# #     Those datasets are of UFOs of shape 'Circle', 'Triangle', and 'Fireball'
# # It will then clean the datasets and output them to a more usable CSV format
# TODO Make this work. It takes forever and has no end in sight.

# Collect the datasets
circURL = 'http://www.nuforc.org/webreports/ndxsCircle.html'
circDF = pd.read_html(circURL)
trigURL = 'http://www.nuforc.org/webreports/ndxsTriangle.html'
trigDF = pd.read_html(trigURL)
fireURL = 'http://www.nuforc.org/webreports/ndxsFireball.html'
fireDF = pd.read_html(fireURL)

# Merge the dataframes
frames = [circDF[0], trigDF[0], fireDF[0]]
ufoDF = pd.concat(frames)

# Write to CSV
ufoDF.to_csv('../UFOSightings.csv')
