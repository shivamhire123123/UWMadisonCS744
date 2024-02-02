source nodes.sh

#add ssh keys to node
#scp id_ed25519* $node0:~/.ssh/.
#scp id_ed25519* $node1:~/.ssh/.
#scp id_ed25519* $node2:~/.ssh/.

scp ssh_config $node0:~/.ssh/config
scp ssh_config $node1:~/.ssh/config
scp ssh_config $node2:~/.ssh/config

#clone project repo
ssh $node0 git clone git@github.com:shivamhire123123/UWMadisonCS744.git
ssh $node1 git clone git@github.com:shivamhire123123/UWMadisonCS744.git
ssh $node2 git clone git@github.com:shivamhire123123/UWMadisonCS744.git

#ssh $node0 ~/UWMadisonCS744/cloudlabnode.sh
#ssh $node1 ~/UWMadisonCS744/cloudlabnode.sh
#ssh $node2 ~/UWMadisonCS744/cloudlabnode.sh
