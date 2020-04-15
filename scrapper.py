#Made by Blitzwolfz 
#v1, supports writing to a CSV file

#Imports
from config import reddit as reddit #shutup, i like to have ugly code sometimes
import praw
import prawcore
import csv

def scrapper(subb):
    #basically scrapes the sub
    alist, lst, lst2 = [], [], []
    sub = reddit.subreddit(subb)
    count = 0
    for submission in sub.top("all", limit=100):
        alist.append(submission.author)
        lst.append(str(submission.title))
        lst2.append(str(submission.score))

    return alist, lst, lst2


def writer(alist, lst, lst2):
    with open('Top100.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Rank", "Name", "Title", "Upvotes"])
                    for x in range(len(alist)):
                        writer.writerow([x+1, str(alist[x]), str(lst[x]), str(lst2[x])])



def main():
    userinput = input("What subreddit would you like: ")
    alist, lst, lst2 = scrapper(userinput)
    writer(alist, lst, lst2)
    print("Done")

main()

