from google.cloud import language_v1
from google.cloud.language_v1 import enums
import sys
import os
import six
import json

class Analyzer:
    def __init__(self, infile, outfile):
        self.infile = infile
        self.outfile = outfile
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/ethansong/Documents/Pycharm Projects/HollywoodEthan/EthanGoogleAPIKey.json'

    def get_sentiment(self, content):
        client = language_v1.LanguageServiceClient()
        if isinstance(content, six.binary_type):
            content = content.decode('utf-8')

        type_ = enums.Document.Type.PLAIN_TEXT
        document = {'type': type_, 'content': content}

        response = client.analyze_sentiment(document)
        sentiment = response.document_sentiment
        returnValue = []
        returnValue.append(sentiment.score)
        returnValue.append(sentiment.magnitude)
        #print(returnValue)
        return returnValue




    def get_result(self):
        data = open(self.infile, 'r')
        dataOutput = {'tweets':
                          {'sentiment': [0.5, 0, 5],'location': ["4893", "3908439"]}
        }
        dataOutput = str(dataOutput)
        with open(self.outfile, "w+") as outfile:
            json.dump(dataOutput, outfile)
        #dataOutput = open("/Users/ethansong/Documents/Pycharm Projects/HollywoodEthan/temp.txt", "w+")
        dataOutputFinal = ""
        count = 0
        for lines in data:
            if lines.lower().__contains__('hollywood'):
                #print(lines)
                with open(self.outfile) as file:
                    dataOutput = json.load(file)
                locationDataUnprocessed = lines[lines.find('"location":["')+14: lines.find('"]},')]
                lattitude = float(locationDataUnprocessed[0:locationDataUnprocessed.find('"')])
                longitude = float(locationDataUnprocessed[locationDataUnprocessed.find('","')+3:])
                print(lattitude, longitude)
                linesToWrite = lines[lines.find(']},"') + 4: lines.find('"}')]
                sentiment = agent.get_sentiment(lines)
                dataOutput2 = {'tweet':
                    {
                        'sentiment': sentiment,
                        'location': [lattitude, longitude]
                    }
                }
                dataOutputFinal += str(dataOutput2)
                count+=1
                if(count == 10):
                    break
        jsonFile = json.dumps(dataOutputFinal)
        with open(self.outfile, "w+") as outfile:
            json.dump(jsonFile, outfile)



if __name__ == '__main__':
    agent = Analyzer(sys.argv[1], sys.argv[2])
    #print(agent.get_sentiment('This computer is amazing but the processor is horrible'))
    agent.get_result()





