import json

def load_data(filename):
    with open (filename,'r') as file:
        data = json.load(file)

    return data


# data=load_data("codebook.json")

def display_data(data):
    print("The Data Information \n")
    for user in data['users']:
        print(f"Id {user['id']}. {user['name']} have friends with {user['friends']} and liked pages are {user['liked_pages']} \n")

    for user in data['pages']:
        print(f"Id {user['id']}. {user['name']} \n ")
        



def cleaned_data(data):
    #remove the empty names.
    data['users']=[users for users in data['users'] if users['name'].strip() ]

    #remove duplicate values.
    for user in data['users']:
        user['friends']= list(set(user['friends']))

    #remove the empty friends and liked pages
    data['users']=[users for users in data['users'] if users['friends'] or users['liked_pages']]

    #remove duplicate duplicate ids in pages
    unique_keys={}
    for page in data['pages']:
        unique_keys[page['id']]=page

    data['pages']=list(unique_keys.values())

    return data




def  friend_suggestions(user_id,data):
    user_friends={}
    for user in data['users']:
        user_friends[user['id']]=set(user['friends'])

    if user_id not in user_friends:
        return []

    direct_friends =user_friends[user_id]
    suggestions={}

    for friend in direct_friends:
        for mutual in user_friends[friend]:
            if mutual!=user_id and mutual not in direct_friends:                
                suggestions[mutual]=suggestions.get(mutual,0)+1

    sorted_suggestion=sorted(suggestions.items(),key=lambda x:x[1],reverse=True)
    return [user_id for user_id, _ in sorted_suggestion] 



def pages_recomendation(user_id,data):

    user_pages={}
    for user in data['users']:
        user_pages[user['id']]=set(user['liked_pages'])


    if user_id not in user_pages:
        return []

    user_liked_pages=user_pages[user_id]   

    page_suggestions={}

    for other_user,pages in user_pages.items():
        if  other_user!=user_id:
            shared_pages=user_liked_pages.intersection(pages)
            for page in pages:
                if page not in user_liked_pages:
                    page_suggestions[page]=page_suggestions.get(page,0)+len(shared_pages)

    sorted_suggestions=sorted(page_suggestions.items(),key = lambda x:x[1],reverse=True)

    return[page_id for page_id,_ in sorted_suggestions]


# -------------------- MAIN PROGRAM --------------------

data = load_data("codebook.json")


# Clean the Data
cleaned = cleaned_data(data)

print("\nData Cleaned Successfully!")

# Test for a single user
user_id = 1

# Friend Recommendations
friend_result = friend_suggestions(user_id, cleaned)
print("\n------------------------------------")
print(f"People You May Know for User {user_id}")
print("------------------------------------")
print(friend_result)

# Page Recommendations
page_result = pages_recomendation(user_id, cleaned)
print("\n------------------------------------")
print(f"Pages You Might Like for User {user_id}")
print("------------------------------------")
print(page_result)



      
  











       




    







       
