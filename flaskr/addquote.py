from flask import Blueprint, request

status_codes = {400: "400 Bad request", 200: "Ok"}

addquote_blueprint = Blueprint("addquote", __name__)
@addquote_blueprint.route('/addquote', methods=['POST'])
def addquote():
    # assigning user input to variable
    requestjson = request.get_json()

    if requestjson == {}:
        return status_codes[400], 400
    
    if "quote" not in requestjson or "author" not in requestjson:
        return status_codes[400], 400
    
    if requestjson["quote"] == "" or requestjson["author"] == "":
        return status_codes[400], 400
    # initialazing newquote variable
    newquote = {}

    newquote["author"] = requestjson["author"]
    newquote["quote"] = requestjson["quote"]
    print(newquote)
    return status_codes[200], 200



#         newquote = {"quote": 0, "author": 0}
#         
#         newquote["quote"] = request.get_json()["quote"]
#         quotesObject["quotes"].append(newquote)

#         with open('quotes.json', "w", encoding='utf-8') as f:
#             try:
#                 json.dump(quotesObject, f)
#                 return "200 OK", 200
#             except Exception as e:
#                 return "400 Bad request: " + e, 400
#     return "406 Not Acceptable", 406