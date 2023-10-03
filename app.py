from flask import Flask
import en_emotion_detection
from flask import Flask, jsonify, request
from flask import render_template, Markup


def roundoff(dict_y):
    for k, v in dict_y.items():
        v=round(v,2)
        dict_y[k]=v
    return dict_y


nlp = en_emotion_detection.load()

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/web')
def get_emotions():
    return render_template('get_emotions.html')


@app.route("/emotion_predictor", methods=['GET'])
def emotion_predictor():

    data_dict ={}
    text_sentence = request.args.get('text_message')

    if not text_sentence:
        return jsonify({
            'error': 'No parameters supplied',
            "status": 400,
            "service": 'emotion_predictor'
        })


    try:
        doc = nlp(text_sentence)
        data_dict['emotions'] = roundoff(doc.cats)
        emotions = roundoff(doc.cats)
        labels = []
        scores = []
        for key, value in emotions.items():
            labels.append(key)
            scores.append(value)

        data_dict['status'] = 200
    except:
        data_dict['status'] = 400

    if data_dict['status'] != 200:
        data_dict['status'] = 400
        return jsonify(data_dict)
    else:
        #return jsonify(data_dict)
        return render_template('indicator_chart.html',values = scores, labels = labels)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
