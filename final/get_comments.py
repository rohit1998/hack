import praw
import pdb

def process_comments(objects):
    for object in objects:
        
        if type(object).__name__ == "Comment":
            process_comments(object.replies) # Get replies of comment
            print((object.body))
            print("\n\n\n\n")
            # Do stuff with comment (object)

        elif type(object).__name__ == "MoreComments":
            process_comments(object.comments()) # Get more comments at same level


with open('../../output') as file:
	client = file.read()
client_id,client_secret = client.split('\n')[0],client.split('\n')[1]

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent='Script by /u/dcusmeb')

submission = reddit.submission(url='https://www.reddit.com/r/investing/comments/cch4gu')

print(submission.title)
process_comments(submission.comments)