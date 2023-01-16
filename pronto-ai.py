from git import Repo
import datetime

def wasItRufus(git_dir):
  repo = Repo(git_dir)
  assert not repo.bare
  print("active branch:",repo.active_branch.name)
  if repo.is_dirty(untracked_files=True):
    print('local changes: True')
  else:
    print("local changes: False")
  commits = list(repo.iter_commits("main"))
  head_commit = commits[0]
  author = str(head_commit.author)
  time = head_commit.authored_datetime
  date = time.date()
  today = datetime.date.today()
  last_week = []
  if author == "Rufus":
    print("blame Rufus: True")
  else:
    print("blame Rufus: False")
  

#url = '/Users/lawrencezhang/Desktop/pronto.ai-assessment'
#print(wasItRufus(url))

if __name__ == "__main__":
  git_url = input()
  wasItRufus(git_url)
