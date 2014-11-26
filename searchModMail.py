import praw
import re
import sys

def doReplies (replies, searchStr):
    for reply in replies:

        #if reply.author:
        #    if reply.author.name == "drocklin":
        #        print(reply.body)
        #
        #if "2i5uxj" in reply.parent_id:
        #    print (reply.body)

        if re.search(searchStr, reply.body, re.I):
            print ("https://www.reddit.com/message/messages/" + reply.parent_id[3:])
            return True

        if reply.replies:
            if doReplies(reply.replies, searchStr):
                return True

    return False



if __name__=='__main__':
    #
    # init and log into reddit
    #


    SUBREDDIT = "books"

    print("==============================")

    r = praw.Reddit(user_agent="/u/boib readModMail")
    # so that reddit wont translate '>' into '&gt;'
    r.config.decode_html_entities = True

    r.login("password", "username")
    print("==============================")


    if len(sys.argv) > 1:
        searchStr = sys.argv[1]
    else:
        print ("enter search term on cmd line")


#    try:
    if True:
        inbox = r.get_mod_mail(subreddit='books', limit=1000)


        if not inbox:
            print ("no messages")
        else:

            for inboxMsg in inbox:

                if re.search(searchStr, inboxMsg.body, re.I):
                    print ("https://www.reddit.com/message/messages/" + inboxMsg.fullname[3:])
                    continue

                if inboxMsg.replies:
                    doReplies(inboxMsg.replies, searchStr)


#    except Exception as e:
#        print('An error has occured: %s ' % (e))




