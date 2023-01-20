import requests
import json

url = "https://filepursuit.p.rapidapi.com/"

bookName='hyperion'
#search for the book
def get_book_opt(bookName):
    querystring = {"q":bookName,"filetype":"epub","type":"ebook"}
    headers = {
    'x-rapidapi-host': "filepursuit.p.rapidapi.com",
    'x-rapidapi-key': "YOUR_API_TOKEN"
    }
    global response
    response = requests.request("GET", url, headers=headers, params=querystring)
    if (response.status_code == 200):
        print("The request was a success")
        with open("./static/results.json", "w") as res:
            res.write(response.text)
        with open("./static/results.json", "r") as responseFile:
            global data
            global dataSnippet
            data = json.load(responseFile)
            print(len(data['files_found']))
            dataSnippet = data['files_found']
            
            # if(data['status'] == "success"):
            #     bookRes(1)
            # else:
            #     bookRes(0)
                
    elif (response.status_code == 404):
        data = -1
        print("Result not found!")
    elif(response.status_code == 502):
        print("API DOWN")
        
    print(response)

# def bookRes(dataLine):
#     pro=open("./static/response.txt", "w")
#     if(dataLine==1):
#         pro.writelines(("{}" "{}" "\n" "{}" "{}" "\n" "{}" "{}" "\n" "\n" "{}" "{}" "\n" "{}" "{}" "\n" "{}" "{}" "\n" "\n" "{}" "{}" "\n" "{}" "{}" "\n" "{}" "{}" "\n" "\n" "{}" "{}" "\n" "{}" "{}" "\n" "{}" "{}" "\n"  "\n" "{}" "{}" "\n" "{}" "{}" "\n" "{}" "{}" "\n" "\n" "{}" "{}" "\n" "{}" "{}" "\n" "{}" "{}" "\n" "\n" "{}" "{}" "\n" "{}" "{}" "\n" "{}" "{}" "\n" "\n").format('ID: /', data['files_found'][0]['file_id'], 'Name: ', data['files_found'][0]['file_name'], 'URL: ', data['files_found'][0]['file_link'], 'ID: /', data['files_found'][1]['file_id'], 'Name: ', data['files_found'][1]['file_name'], 'URL: ', data['files_found'][1]['file_link'], 'ID: /', data['files_found'][2]['file_id'], 'Name: ', data['files_found'][2]['file_name'], 'URL: ', data['files_found'][2]['file_link'], 'ID: /', data['files_found'][3]['file_id'], 'Name: ', data['files_found'][3]['file_name'], 'URL: ', data['files_found'][3]['file_link'], 'ID: /', data['files_found'][4]['file_id'], 'Name: ', data['files_found'][4]['file_name'], 'URL: ', data['files_found'][4]['file_link'], 'ID: /', data['files_found'][5]['file_id'], 'Name: ', data['files_found'][5]['file_name'], 'URL: ', data['files_found'][5]['file_link'], 'ID: /', data['files_found'][6]['file_id'], 'Name: ', data['files_found'][6]['file_name'], 'URL: ', data['files_found'][6]['file_link']))
#     else:
#         pro.write("No books found with that name!")
        
def get_link(bookID):
    for id in dataSnippet:
        if(bookID) == id['file_id']:
            return id['file_link']

def get_title(bookID):
    for id in dataSnippet:
        if(bookID) == id['file_id']:
            name = id['file_name'].replace('.epub', '.txt')            
            return name
