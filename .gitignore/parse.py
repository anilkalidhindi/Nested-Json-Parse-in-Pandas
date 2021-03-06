from pandas.io.json import json_normalize
import json
import pandas as pd

'''
json_normalize(data, ['apps', 'events'], ['deviceId', 'vinPart', ['apps', 'app'], ['apps', 'appID'], ['apps', 'appV'], ['apps', 'framework'], ['apps', 'events', ['p', 'time']]])  
'''

data =  [ 
{  
   "deviceId":"123-123-123-123-123asdf",
   "vinPart":"abcdef",
   "apps":[  
      {  
         "app":"xyz",
         "appID":"12345678",
         "appV":"1.1.1",
         "framework":"abc-1.1.1",
         "events":[  
            {  
               "e":"appStart",
               "t":1515091942784,
               "p":{  
                  "time":1515091942784
               }
            },
            {  
               "e":"appClose",
               "t":1515091942797,
               "p":{  
                  "time":1515091942797
               }
            }
         ]
      },
      {  
         "app":"def",
         "appID":"345678",
         "appV":"1.1.11",
         "framework":"def-1.1.123",
         "events":[  
            {  
               "e":"appStart",
               "t":1515091949000,
               "p":{  
                  "time":1515091948999
               }
            },
            {  
               "e":"loading",
               "t":1515091951462,
               "p":{  
                  "lifecycle":"show"
               }
            },
            {  
               "e":"splashExit",
               "t":1515091952795,
               "p":{  

               }
            },
            {  
               "e":"flowChange",
               "t":1515091952806,
               "p":{  
                  "previous":"_ngi:init",
                  "current":"_ngi:terms"
               }
            },
            {  
               "e":"loading",
               "t":1515091952840,
               "p":{  
                  "lifecycle":"hide"
               }
            },
            {  
               "e":"routeChange",
               "t":1515091953199,
               "p":{  
                  "isEntry":"false",
                  "layout":"Terms",
                  "flow":"_ngi:terms",
                  "route":"list",
                  "timestamp":1515091953191,
                  "path":"_ngi:terms.list"
               }
            },
            {  
               "e":"eventDispatch",
               "t":1515091961003,
               "p":{  
                  "key":"layout",
                  "actionIndex":0
               }
            },
            {  
               "e":"appClose",
               "t":1515091961303,
               "p":{  
                  "time":1515091961303
               }
            }
         ]
      }
   ]
}
]

df1 = json_normalize(data,  [ 'apps', 'events', 'p'], [[ 'apps', 'events', 'p'], ['apps', 'events', 'e'], ['apps', 'events', 't'] ,['apps', 'appID'],['apps', 'app'] , ['apps', 'appV'] , ['apps', 'framework'], 'deviceId', 'vinPart'])
df2 = df1['apps.events.p'].apply(pd.Series)
df_final = pd.concat([df1, df2], 1)

df_final['time'] = df_final['time'].apply(lambda x: '{:.0f}'.format(x))
df_final['timestamp'] = df_final['timestamp'].apply(lambda x: '{:.0f}'.format(x))

df_final = df_final.drop('apps.events.p', 1).add_prefix('apps.')
