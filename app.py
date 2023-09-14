from flask import Flask, render_template, request, jsonify , json
import openai
from flask_ngrok import run_with_ngrok
import regenerate as regen
import time

app = Flask(__name__)
# run_with_ngrok(app)

# OpenAI API Key
API_key = "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"
# openai.api_key = API_key

# def get_completion(prompt):
#     print(prompt)
#     query = openai.Completion.create(
# 		engine="text-davinci-003",
# 		prompt=prompt,
# 		max_tokens=1024,
# 		n=1,
# 		stop=None,
# 		temperature=0.7,
# 	)
#     response = query.choices[0].text
#     sentiment = get_sentiment(prompt)
#     return response , sentiment
# API_key = ["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","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"]
# second_API_key = "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"
openai.api_key = API_key


def get_completion(prompt):
	try:
		print(prompt)
		# print(openai.api_key)
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
	except openai.error.RateLimitError:
			print("Rate limit exceeded. Retrying in 20 seconds...")
			time.sleep(5)
			openai.api_key = "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"
			return regen.regenerate_ai(prompt)
		

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
	app.run()