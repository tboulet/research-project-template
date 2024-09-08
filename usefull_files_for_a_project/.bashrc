# <!> You need to put that folder in ~/

# Various commands
alias up='cd ..'
alias upp='cd ../..'
alias ..='cd ..'
alias gs='git status'
alias ga='git add'
alias gc='git commit'
alias gpush='git push'
alias gpull='git pull'

# Python/CUDA installation and test
alias cuda='nvcc --version'
alias python310='/usr/bin/python3.10'
alias venv='python3 -m venv venv_linux && source venv_linux/bin/activate'
alias activate='source venv_linux/bin/activate'
alias pip_reqs='pip install -r requirements.txt'
alias pip_torch='pip install torch torchvision torchaudio'
alias pip_tf='TODO' # TODO
alias pip_jax='pip install --upgrade "jax[cuda12_pip]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html'
alias pip_basics='pip install numpy scipy matplotlib tqdm wandb hydra-core'
alias pip_cv2='pip install opencv-python'
alias test_torch='python -c "import torch; print(torch.cuda.is_available())"'
alias test_tf='python -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000]))); print(tf.config.list_physical_devices())"'
alias test_jax='python -c "import jax; print(jax.devices())"'

# Tensorboard
alias tb='tensorboard --logdir=tensorboard'
alias tbd='rm -rf tensorboard/*'

# Access to usefull files/folders
alias user='cd /home/boulux'
alias pro='cd /home/boulux/projects' 
alias macros='code ~/.bashrc'
alias bashrc='code ~/.bashrc'
alias debugger='code ~/projects/debugger'
alias pro_windows='code /mnt/c/Users/timot/projects/'

# Code from files
alias pr='type /mnt/c/Users/timot/data_files/'
alias pr_ls='dir /mnt/c/Users/timot/data_files/'
alias pr_code='code /mnt/c/Users/timot/data_files/'

# Miscelanous
alias sna='snakeviz logs/profile_stats.prof'
alias pypi='pip install build twine && python -m build && python -m twine upload dist/*'
alias python310='/usr/bin/python3.10'
alias kill_wandb='ps aux|grep wandb|grep -v grep | awk '{print $2}'|xargs kill -9'

# Projects
alias run='python run.py --config-name=personal_config'
alias runc='python run.py --config-name'
alias pers='python personal_test.py'
alias cpers='code personal_test.py'