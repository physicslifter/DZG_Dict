import json
import numpy as np
import datetime

current_time = datetime.datetime.now()
TimeStamp=((str(current_time))[0:4]+(str(current_time))[5:7]+(str(current_time))[8:10]+(str(current_time))[11:13]+(str(current_time))[14:16]+(str(current_time))[17:19]+(str(current_time))[20:])
#Create a JSON Object
di=input('Dictionary name: ')
au=input('author: ')
word=input('word: ')
pos=input('part of speech: ')
pronunciation=input('pronunciation: ')
definition=input('definition')
ss=input('sample sentence: ')
num_upvotes=input('Number of downvotes: ')
num_downvotes=input('Number of upvotes: ')

def get_dictionary_entry(dictionary,author,id,word,partofSpeech,pronunciation,audio_file_link,definition,ss,num_upvotes,num_downvotes):
    json_obj = {
            "dictionary":di,
            "author":au,
            "id":word+TimeStamp,
            "word":word,
            "partofSpeech":pos,
            "definitions":[
                {
                    "pronunciation":pronunciation,
                    "audio File":audio_file_link,
                    "definition":definition,
                    "sentence":ss
                }
            
            ],
            "UpVotes":num_upvotes,
            "DownVotes":num_downvotes}

    #Write the object to file.
    filename=word+TimeStamp+'.json'
    with open(filename,'w') as jsonFile:
        json.dump(json_obj, jsonFile)
    
    print(json_obj)

    return json_obj

#The input for the audio file...
afc=input('Insert audio file for pronunciation? (Y/N)')
af=np.nan

#Handle the case that the user selected "yes" that they want to edit the audio file
if afc == 'Y':
    af = np.nan
    get_dictionary_entry(di,au,word+TimeStamp,word,pos,pronunciation,af,definition,ss,num_upvotes,num_downvotes)

#If the user does not wish to add an audio file
elif afc == 'N':
    af = np.nan

else:
    print('Error - please return Y or N')

