from git import Repo

def wasItRufus(git_dir):
  repo = Repo(git_dir)
  assert not repo.bare
  