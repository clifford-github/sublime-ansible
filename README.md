Syntax highlighting for Ansible files
=====================================

## Screenshot

With color scheme Monokai

![Screenshot](/doc/images/syntax1.PNG?raw=true)

## Installation

### Package Manager

First, install the Package Control plugin, instructions here: http://wbond.net/sublime_packages/package_control.

Once you install Package Control, restart Sublime Text and bring up the Command Palette (`Command+Shift+P` on OS X, `Control+Shift+P` on Linux/Windows).

Select "Package Control: Install Package", wait while Package Control fetches the latest package list, then select "Ansible" when the list appears.

The advantage of using this method is that Package Control will automatically keep this package up to date with the latest version.

### Manual
Clone the repository in your Sublime Text "Packages" directory:

    git clone https://github.com/clifford-github/sublime-ansible.git Ansible

The "Packages" directory is located at:

* OS X:
    `~/Library/Application Support/Sublime Text 2/Packages/`
* Linux:
    `~/.Sublime Text 2/Packages/`
* Windows:
    `%APPDATA%/Sublime Text 2/Packages/`
