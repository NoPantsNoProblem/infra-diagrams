
###############################################################################################################################
#   key to push to github
#   ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJYM9aKV8Mg63fxMJ8Avw35OT/vuU4DQ0brYOoY5mNMH arthur.taradejna@gmail.com

#   github
#   ==================================
#   password for private/public ssh key

#    5SpOMPmSrb4



#   =================================================
#   1st set name and email default globals 
#   create SSH key public/private with passwordsince this is 
#   a public site. 

##############################################################################################################################


#   ******    Output   *********
#   Enter passphrase for key '/c/Users/family/.ssh/id_ed25519':
#   Enumerating objects: 3, done.
#   Counting objects: 100% (3/3), done.
#   Writing objects: 100% (3/3), 222 bytes | 222.00 KiB/s, done.
#   Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
#   To github.com:NoPantsNoProblem/swap.git
#   * [new branch]      main -> main
#   Branch 'main' set up to track remote branch 'main' from 'origin'.


echo "edit 3" >> zoinks.txt  #edit file

git branch -M origin  #set branch

# set remote origin.
#git remote add origin git@github.com:NoPantsNoProblem/infra-diagrams.git
#git push -u origin big-diagrams 
git init
git add zoinks.txt
git commit -m "zoinks"


