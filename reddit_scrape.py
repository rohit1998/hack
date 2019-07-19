import praw
import csv

with open('../output') as file:
	t = file.read()
cid = t.split('\n')[0]
cse = t.split('\n')[1]
reddit = praw.Reddit(client_id=cid,
                     client_secret=cse,
                     user_agent='Script by /u/dcusmeb')

submission = reddit.submission(url='https://www.reddit.com/r/investing/comments/cch4gu')
# print(submission.title)
submission.comments.replace_more(limit=None)
for comment in submission.comments:
    print(comment.body)
    print("\n\n\n\n")