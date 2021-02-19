call plug#begin('~/.config/nvim/plugged')

Plug 'mhinz/vim-startify'
Plug 'neoclide/coc.nvim', {'branch': 'release'}

call plug#end()



"---------------- Configs ----------------------------

source ~/.config/nvim/plug-configs/coc.conf
source ~/.config/nvim/plug-configs/startify.conf
