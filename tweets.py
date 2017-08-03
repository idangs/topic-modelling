"""
This program filters out the twitter feeds into Nepali and English categories
"""

# -*- coding: utf-8 -*
from guess_language import guess_language
import pandas as pd


def main():

    # empty lists to store the nepalese and english usernames
    nepalese = []
    english = []
    restrictions = ['”','…', '“', '’', 'ç', '‘', '..'] #guess_language detects these symbols as non-english

    location = 'd:\Users\user\Desktop\weets.csv'
    df = pd.read_csv(location) #Dataframe containing the orgiinal tweets
    for user in df.text:
        for rest_syb in restrictions:
            user = user.replace(rest_syb, '')
        try:

            if guess_language(user) == "en":
                english.append(user)

            elif guess_language(user) == "UNKNOWN":
                english.append(user)

            elif guess_language(user) == "ne":
                nepalese.append(user)

            else:
                english.append(user)

        except:
            nepalese.append(user)



    #Creating a dataset
    NameDataSet = list(zip(nepalese, english))


    name_types = pd.DataFrame(data = NameDataSet, columns = ['Nepali Text','English Text'])
    name_types.to_csv('tweets_filter2.csv',index= False, header= True)

main()
     window.onload = init;
    </script>
  </head>
  <body>
      <h2> Circles </h2>
      <div id = "mymap"></div>
      <div id = "info"></div>
  </body>

</html> 

window.onload = init;
    </script>
  </head> 


  for(var i =0; i < visitors.length; i++){
        var circle = new google.maps.Circle({
          map:map;
          center: visitors[i].latlng,
          radius: visitors[i].radius * 10
        });
        
