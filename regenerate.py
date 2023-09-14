import openai
from app import get_completion

# openai.api_key = "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" #mami acct key
def regenerate_ai(prompt):
    try:
        print(openai.api_key)
        print("regen promt",prompt)
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
        # print(response , sentiment)
        return response , sentiment
    except openai.error.RateLimitError:
        # retry_time = e.retry_after if hasattr(e, 'retry_after') else 30
        print("Rate limit exceeded. Retrying in 30 seconds...")
        # get_completion(prompt)
    raise Exception("time out to regenrate")

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