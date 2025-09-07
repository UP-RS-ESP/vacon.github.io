https://stackoverflow.com/questions/37720892/you-dont-have-write-permissions-for-the-var-lib-gems-2-3-0-directory

sudo apt-get remove ruby
sudo apt update
sudo apt install git curl libssl-dev libreadline-dev zlib1g-dev autoconf bison build-essential libyaml-dev libreadline-dev libncurses5-dev libffi-dev libgdbm-dev

curl -sL https://github.com/rbenv/rbenv-installer/raw/main/bin/rbenv-installer | bash -
source ~/.bashrc
rbenv install 3.4.5
source ~/.bashrc
rbenv global 3.4.5
source ~/.bashrc
ruby -v


git clone https://github.com/UP-RS-ESP/VACON.git
cd VACON
rm -fr .editorconfig .gitattributes .github docs test CHANGELOG.md minimal-mistakes-jekyll.gemspec README.md screenshot-layouts.png screenshot.png
