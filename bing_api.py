import requests

# Specify the endpoint URLs for Bing Spell Check and AutoSuggest APIs
spell_check_url = "https://api.bing.microsoft.com/v7.0/spellcheck"
auto_suggest_url = "https://api.bing.microsoft.com/v7.0/Suggestions"

# Set your Bing API subscription key
subscription_key = "6d613560747942509ba9999dcaf6e6a4"

# Set your query text
query = "Hello, how are yuo?"

# Spell Check API request
spell_check_params = {
    "text": query,
    "mode": "proof",
}

spell_check_headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Ocp-Apim-Subscription-Key": subscription_key,
}
spell_check_response = requests.post(spell_check_url, params=spell_check_params, headers=spell_check_headers)
spell_check_data = spell_check_response.json()

print(spell_check_data)
# # Get the corrected query from the Spell Check API response
# corrected_query = spell_check_data["flaggedTokens"][0]["suggestions"][0]["suggestion"]

# # AutoSuggest API request
# auto_suggest_params = {
#     "q": corrected_query,
#     "mkt": "en-US",
# }

# auto_suggest_headers = {
#     "Ocp-Apim-Subscription-Key": subscription_key,
# }

# auto_suggest_response = requests.get(auto_suggest_url, params=auto_suggest_params, headers=auto_suggest_headers)
# auto_suggest_data = auto_suggest_response.json()

# # Get the suggested queries from the AutoSuggest API response
# suggested_queries = [suggestion["displayText"] for suggestion in auto_suggest_data["suggestionGroups"][0]["searchSuggestions"]]

# # Print the results
# print("Corrected Query: ", corrected_query)
# print("Suggested Queries: ", suggested_queries)