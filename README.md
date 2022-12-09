# config
Kitty, Vim, color schemes, etc... Everything related to dev environment and accesed via ~/.config

# info
`/profiles` are all symlinks from `~/`

They were created like this `ln -s ~/.zshrc ~/.config/profiles/.zshrc` etc

`/bin` is a custom bin folder added to the zshrc PATH. This works in combination with the `/demos` directory, which is not included in this repo. It's a seperate repo. Clone that repo into `~/.config`

```zsh
cd ~/.config
git clone https://github.com/ferry-creator/demos.git --recursive
```


### Setup (MacOS):
To setup, simply download rep, and place into dot files folder on system.
Navigate to the folder and run the shell script.

```cd ~/.config```

```chmod +x SETUP_DOTFILES.sh```
```sh SETUP_DOTFILES.sh```

### Some nice brews (MacOS):
```brew install no-more-secrets``` (for nms-demo)

```brew install globe```

```brew install yoggy/tap/sendosc```
