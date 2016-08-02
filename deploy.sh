

JEKYLL_ENV=production jekyll build 
rsync -avh _site/. login.eecs.berkeley.edu:~/public_html/.