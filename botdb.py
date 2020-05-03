from pymongo import MongoClient
import praw
import time

reddit = praw.Reddit(client_id="nkqe0fIHQLbvWA",
                    client_secret="CHmrxOz61_6l4YUMb8IJVolglp4",
                    password="14526378977s",
                    username="blitzwolfz",
                    user_agent="ryzen-bot by /u/blitzwolfz")

##client = MongoClient("mongodb+srv://blitz:Iamtheflas10@blitz-zczbr.mongodb.net/test?retryWrites=true&w=majority")
##db = client['menu']
##collection = db['users']
##
##user = db.users
##
##_userdata = {
##    'name': 'blitzwolfz',
##    'content': 'PyMongo is fun, you guys',
##    'author': 'Scott'
##}
##result = user.insert_one(_userdata)
##print('One post: {0}'.format(result.inserted_id))


def newpost_(username, postid, postutc, commentid, commetutc):
    client = MongoClient("mongodb+srv://blitz:Iamtheflas10@blitz-zczbr.mongodb.net/test?retryWrites=true&w=majority")
    db = client['botwatch']
    #collection = db['person']
    user = db[username]

    _userdata = {
    'name': username,
    'postid': postid,
    'postutc': postutc,
    'commentid': commentid,
    'commentutc': commentutc    
    }

    result = user.insert_one(_userdata)


def averagetime():
    pass

def getsell(username):
    for comment in reddit.redditor(username).comments.new(limit=None):
        comment = reddit.comment(id=comment.id)

        comment.reply_sort = 'new'
        comment.reply_limit = 0
        comment.refresh()
        replies = comment.replies
        
        for ok in replies:
            

            if ok.author in ["FederalReserveDank"] and str(ok.body).find("!sell") != -1:
                return ok.submission.id, ok.submission.created_utc, comment.id, comment.created_utc

def getlast(username):
    client = MongoClient("mongodb+srv://blitz:Iamtheflas10@blitz-zczbr.mongodb.net/test?retryWrites=true&w=majority")
    db = client['botwatch']
    #collection = db['person']
    user = db[username]

    #find() will find all commenid
    #.sort goes from the last document to the first one
    #.limit limits it to last one
    for x in user.find({}, {'commentid'}).sort([('commentid', -1)]).limit(1):
        return x

# userlist = ["blitzwolfz", "--__username__--", "bubulle099"]
# for x in range(len(userlist)):
#     postid, postutc, commentid, commentutc = getsell(userlist[x])
#     newpost_(userlist[x], postid, postutc, commentid, commentutc)


while True:
    userlist = ["blitzwolfz", "--__username__--", "bubulle099"]

    for x in range(len(userlist)):
        check = getlast(userlist[x])
        postid, postutc, commentid, commentutc = getsell(userlist[x])

        if commentid != check["commentid"]:
            newpost_(userlist[x], postid, postutc, commentid, commentutc)
            time.sleep(90)
            check = getlast(userlist[x])
        
        else:
            print(userlist[x], "didn't comment")
        
        #print(getlast())
        #print(type(getlast))
        #print(type(check))
        #print(check)
        #print(check["commentid"])


