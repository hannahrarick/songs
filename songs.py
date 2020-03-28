from flask import Flask, render_template
app = Flask(__name__)

import csv

def convert_to_dict(filename):
    datafile = open(filename, newline='')
    my_reader = csv.DictReader(datafile)
    list_of_dicts = list(my_reader)
    datafile.close()
    return list_of_dicts

songs_list = convert_to_dict('songs.csv')

pairs_list = []
for songs in songs_list:
    pairs_list.append( (songs['\ufeffindent'], songs['Mood']) )

@app.route('/')
def index():
    return render_template('index.html', pairs=pairs_list, font_url= "https://fonts.googleapis.com/css?family=Courier+Prime&display=swap")

@app.route('/songs/<num>')
def songs(num):
    songs = songs_list[int(num) - 1]
    # above - the curly braces {} hold a variable; when this runs,
    # the value will replace the braces and the variable name
    return render_template('song.html', songs=songs, font_url="https://fonts.googleapis.com/css?family=Courier+Prime&display=swap")

if __name__ == '__main__':
    app.run(debug=True)
