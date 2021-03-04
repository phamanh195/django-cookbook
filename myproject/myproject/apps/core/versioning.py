import subprocess
from datetime import datetime


def get_git_changeset_timestamp(absolute_path):
	repo_dir = absolute_path
	git_log = subprocess.Popen(
		'git log --pretty=format:%ct --quiet -1 HEAD',
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		shell=True,
		cwd=repo_dir,
		universal_newlines=True,
	)

	timestamp = git_log.communicate()[0]
	format_time = '%Y%m%d%H%M%S'
	try:
		timestamp = datetime.utcfromtimestamp(int(timestamp))
	except ValueError:
		# Fallback to current timestamp
		return datetime.now().strftime(format_time)
	return timestamp.strftime(format_time)
