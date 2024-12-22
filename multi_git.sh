check_if_in_gitlab="/usr/bin/grep url .git/config"
place=$($check_if_in_gitlab | xargs) #Removes spaces from above command
#--
gitlab="url = git@gitlab.com:gmastrokostas/server_data_collector.git"
github="url = git@github.com:gmastrokostas/server_data_collector.git"

cookies () {
	check_if_in_main=`/usr/bin/git branch | cut -d ' ' -f 2 | grep -v ^$`
	good_branch="main"
	if [ "$check_if_in_main" == "$good_branch" ];
        then
		sed -i 's/gitlab/github/g' .git/config
		git push
		sed -i 's/github/gitlab/g' .git/config
		echo "Pushed data to gihub"
		echo "Reverted config file back to gitlab"
		grep url .git/config
	else
        	echo "You are not into main branch in gitlab"
		echo "I am not pushing anything to anyone"
		echo "Switch to main in gitlab -- git switch main"
	fi
}


if [ "$place" == "$gitlab" ];
then
	echo "You are into main brainch in gitlab"
	echo "Doing a git pull"
	echo "Will now push data into github main"
	/usr/bin/git pull
	echo "------------------------------------"
	cookies
else
	echo "No action taken"
	echo "Check where you git config points to"
fi
