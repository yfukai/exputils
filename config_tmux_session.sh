tmux split-window -h
tmux split-window -v

tmux new-window
tmux split-window -h
tmux select-pane -L
tmux split-window -v

tmux select-window -t :0
#main vim
cd lib/exputils/exputils

tmux select-window -t :0
tmux select-pane -R
#test vim
cd lib/exputils/test
#tmux select-pane -D
#test dir
#cd lib/exputils/test

tmux select-window -t :1
#git
#git add . -A ; git commit -a -m"autocommit" ; git push
#version
#vim version.py
#pip
#pip install git+https://github.com/yskflute/exputils.git
