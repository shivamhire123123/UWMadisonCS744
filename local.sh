source nodes.sh

#add ssh keys to node
scp id_ed25519* $node0:~/.ssh/.
scp id_ed25519* $node1:~/.ssh/.
scp id_ed25519* $node2:~/.ssh/.

scp ssh_config $node0:~/.ssh/config
scp ssh_config $node1:~/.ssh/config
scp ssh_config $node2:~/.ssh/config

#clone project repo
ssh $node0 << EOF
	if [ -d "UWMadisonCS744" ]; then
		cd UWMadisonCS744
		git pull
	else
		git clone git@github.com:shivamhire123123/UWMadisonCS744.git
	fi
EOF
ssh $node1 << EOF
	if [ -d "UWMadisonCS744" ]; then
		cd UWMadisonCS744
		git pull
	else
		git clone git@github.com:shivamhire123123/UWMadisonCS744.git
	fi
EOF
ssh $node2 << EOF
	if [ -d "UWMadisonCS744" ]; then
		cd UWMadisonCS744
		git pull
	else
		git clone git@github.com:shivamhire123123/UWMadisonCS744.git
	fi
EOF

ssh $node0 bash UWMadisonCS744/cloudlabnode.sh
ssh $node1 bash UWMadisonCS744/cloudlabnode.sh
ssh $node2 bash UWMadisonCS744/cloudlabnode.sh
