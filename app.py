from flask import Flask, render_template, request, jsonify , json
import openai

app = Flask(__name__)

# OpenAI API Key
API_key = "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"
openai.api_key = API_key


def get_completion(prompt):
    print(prompt)
    query = openai.Completion.create(
		engine="text-davinci-003",
		prompt=prompt,
		max_tokens=1024,
		n=1,
		stop=None,
		temperature=0.7,
	)
    response = query.choices[0].text
    sentiment = get_sentiment(prompt)
    return response , sentiment

def get_sentiment(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{text}\n what is the emotion catgory from this set [ Good review , Complaint ,General Query, Fake Review, Suggestion, Irrelevant ]. give answer in 1 word",
    	max_tokens=1024,
		n=1,
		stop=None,
		temperature=0.7
    )

    sentiment = response.choices[0].text.strip()
    return sentiment

@app.route("/", methods=['POST'])
def query_view():
	data = request.get_json()
	print(data)
	response_out , sentiment = get_completion(data['message'])
	print(response_out)
	return jsonify({'aiResponse': response_out, 'reviewType': sentiment})

	# return render_template('index.html')

@app.route("/")
def welcome():
	return 'welcome to customer review'

if __name__ == "__main__":
	app.run(debug=True)
