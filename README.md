<a href="http://www.qualya.us">Qualya</a>
===

A sentiment visualizer for a subset of popular US equities and exchange-traded funds. Designed primarily as an application for the mobile web, it's also responsive to desktop and tablet devices as well.

* <a href="#about">About</a>
* <a href="#home-page">Home Page</a>
* <a href="#universe-data">Universe Data</a>
* <a href="#historical-data">Historical Data</a>

---
### <a name="about"></a>About

Qualya is a <a href="https://github.com/django/django">Django</a>-based application whose front-end depends on <a href="https://github.com/gionkunz/chartist-js">Chartist.js</a>.

The model used to evaluate sentiment was trained on a wide variety of tagged segments. Keyword and keyword combinations compose the features, which are then weighted by the number and position of other keywords in the input status. The ultimate feature set is selected by the ordered information content. Finally, there are several component results in the ensemble that are then synthesized into a final score. The distribution over sentiment closely matches the actual tagged data.
<br>

---
### <a name="home-page"></a>Home Page

Search for the latest sentiment across the universe of stocks by selecting the 'All' option from the dropdown menu. Choose any other option from the menu to view sentiment for that symbol in a historical context.

<br>
<img alt="Home Page - mobile" src="https://drive.google.com/uc?export=download&id=0B3rehuqgDPeVajEtbEctaEJ4c0U">

---
### <a name="universe-data"></a>Universe Data

Each day, scores generated by the model are sorted into five sentiment categories: "Strongly-Negative" (crimson), "Negative" (red), "Neutral" (gray), "Positive" (light green) and "Strongly-Positive" (forest green). Below, on December 12th, 2016, TWTR had the following sentiment profile: 24.24% "Negative", 36.36% "Neutral", 30.3% "Positive" and 9.1% "Strongly-Positive".

Symbols are ranked according to a smoothed function of the number of scores collected for that day. To complement this, the heights of the sentiment bars are variable on this page to give a sense of the distance between rankings. This day, TWTR was considerably less-mentioned than AAPL, whose profile was 2.4% "Negative", 48.2% "Neutral", 47% "Positive" and 2.4% "Strongly-Positive".

Touch or click the arrow buttons in the sub-navigation menu to advance backward or forward one day in time. Do the same to any bar to view historical data for that symbol. Users can also adjust the date parameter in the URL directly.

<br>
<img alt="Universe Data - mobile" src="https://drive.google.com/uc?export=download&id=0B3rehuqgDPeVcFhtZkxCU05OVjA">

---
### <a name="historical-data"></a>Historical Data

Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...

Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...

Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...Historical...

<br>
<img alt="Historical Data - mobile" src="https://drive.google.com/uc?export=download&id=0B3rehuqgDPeVckdHemhsbG1aTTg">
