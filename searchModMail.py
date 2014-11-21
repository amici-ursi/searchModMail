import praw
import re

def doReplies (replies, searchStr):
    for reply in replies:
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

    r.login("username", "password")
    print("==============================")



    try:
        inbox = r.get_mod_mail(subreddit='books', limit=1000)


        if not inbox:
            print ("no messages")
        else:

            for inboxMsg in inbox:

                if inboxMsg.replies:
                    doReplies(inboxMsg.replies, "filth")


    except Exception as e:
        print('An error has occured: %s ' % (e))


