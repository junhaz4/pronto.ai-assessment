from git import Repo
import datetime

def wasItRufus(git_dir):
  # create a git.Repo object to represent the repository given
  repo = Repo(git_dir)
  # check the repository is not empty
  assert not repo.bare 
  # print names of active branches
  print("active branch:",repo.active_branch.name)
  # check whether the repository data has been modified or not 
  if repo.is_dirty(untracked_files=True):
    print('local changes: True')
  else:
    print("local changes: False")
  # get a list of commits made
  commits = list(repo.iter_commits("main"))
  # get the most recent commit 
  head_commit = commits[0]
  # get name of people who made the commit
  author = str(head_commit.author)
  # get the time
  authored_time = head_commit.authored_datetime
  # get the date
  authored_date = authored_time.date()
  authored_day = authored_date.day
  # get the current date
  cur_date = datetime.date.today()
  cur_day = cur_date.day
  # check if the most recent commit is made last week
  if 1 <= cur_day-authored_day <= 14:
    print("recent commit: True")
  else:
    print("recent commit: False")
  # check if the most recent commit is made by Rufus
  if author == "Rufus":
    print("blame Rufus: True")
  else:
    print("blame Rufus: False")
  

#url = '/Users/lawrencezhang/Desktop/self-learning-path'
#wasItRufus(url)

if __name__ == "__main__":
  git_url = input()
  wasItRufus(git_url)
