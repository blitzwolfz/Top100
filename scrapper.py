#Made by Blitzwolfz 
#v1, supports writing to a CSV file

#Imports
from publicconfig import reddit as reddit #shutup, i like to have ugly code sometimes
import praw
import prawcore
import csv

def scrapper(subb):
    #basically scrapes the sub
    alist, lst, lst2 = [], [], []
    sub = reddit.subreddit(subb)
    for submission in sub.top("all", limit=100):
        alist.append(submission.author)
        lst.append(str(submission.title))
        lst2.append(str(submission.score))
    
    
    lst3 = [alist, lst, lst2]
    return lst3


def writer(alist):
    with open('Top100.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Rank", "Name", "Title", "Upvotes"])
                    print(len(alist))
                    print(len(alist[0]))
                    for x in range(len(alist[0])):
                        writer.writerow([x+1, str(alist[0][x]), str(alist[1][x]), str(alist[2][x])])




def main():
    userinput = input("What subreddit would you like: ")
    alist = scrapper(userinput)
    writer(alist)
    print("Done")

main()

