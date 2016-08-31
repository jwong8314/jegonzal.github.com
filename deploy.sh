
JEKYLL_ENV=production bundle exec jekyll build 
rsync -avh _site/. login.eecs.berkeley.edu:~/public_html/.
