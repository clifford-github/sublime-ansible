sublime-ansible
===============

## Recommended

First, go to the awesome sublime tutorials and learn about snippets
https://tutsplus.com/lesson/key-bindings/


## Language Definition

...

## Tab Completion

Work In Progress.  Suggestions, pull requests welcome.

We extract the snippet information from ansible on github
https://github.com/ansible/ansible/tree/devel/library

###Installation: 

```
export SUBLIME_USER_DIR="/path/to/sublime/Packages/User directory"
```
On a mac, this is "$HOME/Library/Application Support/Sublime Text 2/Packages/User" and it is discovered automatically.
Take care with quoting because of spaces in the path name.
```
export ANSIBLE_HOME="location of ansible modules"
```
library is a subdirectory of ANSIBLE_HOME and is what the
tab_completion.py module uses to extract snippets.

In the directory where tab_completion.py is located
```
python tab_completion.py
```

This will generate snippets for each ansible module in SUBLIME_USER_DIR/<Language> named ansible-<module>.sublime-snippet, like this for "file"
```
<snippet>
    <content><![CDATA[ - name: ${1:.}
   file: src=${2:nodefault}
         force=${3:no}
         selevel=${4:s0}
         seuser=${5:nodefault}
         recurse=${6:no}
         state=${7:file}
         serole=${8:nodefault}
         mode=${9:nodefault}
         path=${10:nodefault}
         owner=${11:nodefault}
         group=${12:nodefault}
         setype=${13:nodefault}
         ]]></content>
    <tabTrigger>fil</tabTrigger>
    <scope>source.yaml</scope>
    <description>Sets attributes of files</description>
</snippet>
```

Close all sublime-text sessions.

###Usage:

Open sublime text and load an ansible file with .yml extension.
Type the first three letters of your favorite ansible module.  Hit "Tab" key.  For copy, you should see:

```
 - name: .
   copy: content=nodefault
         src=nodefault
         force=yes
         others=nodefault
         dest=nodefault
         validate=nodefault
         backup=no
```
You can tab through the various options.
Ctrl+Shift+K to kill a line.
You may wish to edit the snippet file located in 
SUBLIME_USER_HOME/<Language> (Language default is Yaml for now, Ansible soon) 
where named ansible-<module>.sublime-snippet to eliminate options 
you never use, and the tabTrigger (letters typed before tabbing) or 
scope (files associated).  For example, below we edited
the snippet to only use our favorite options and changed the tab 
trigger to "file" from "fil".
```
<snippet>
    <content><![CDATA[ - name: ${1:.}
   file: src=${2:nodefault}
         recurse=${6:no}
         state=${7:file}
         mode=${9:nodefault}
         path=${10:nodefault}
         owner=${11:nodefault}
         group=${12:nodefault}
         ]]></content>
    <tabTrigger>file</tabTrigger>
    <scope>source.yaml</scope>
    <description>Sets attributes of files</description>
</snippet>
```


#####Coming soon:
An option to set the policy of generating snippits with only the required
fields with tab completion the first three letters + _ eg. "fil_" + TAB 
would generate the file snippet with only.

I tried setting the language to Ansible to mesh with the language 
definitions.  Something is not working yet.  So I'm sticking with Yaml
for now.  Default language will be Ansible soon, and it will be set from
the commandline in the future.

#####Known Bugs: 
I got this working using Yaml as the language which maches source.yaml as an extension type.  When I switched to Ansible the tab completion is not working yet.  It may be that source.x needs to be adjusted in the tab_completion.py:emit_snippet code.  I don't have time
to go through the sublime-text tutorials on snippets right now to debug.

There are now a few modules with identical first three letters like "file" and "filesystem".  For now, manually edit the tabTrigger field so that they are different or delete the obscuring module option you do not use.

Sublime's auto tab completion for words you have typed before sometimes obscures a tab trigger.  Either tab to the correct choice or modify tab_completion.py emit_snippet method to make a more unique trigger like fil_ for file. 

