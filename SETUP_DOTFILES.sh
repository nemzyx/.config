#!/bin/bash
echo "\n---- Creating vim-plug plugins directory as '~/.config/nvim/plugged'"
mkdir ~/.config/nvim/plugged

echo "\n---- Installing Nvim plugins (vim-plug)..."
nvim +PlugInstall +qall

echo "\n\nEnjoy.\n\n\n\n"
