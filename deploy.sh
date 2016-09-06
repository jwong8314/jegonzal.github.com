
JEKYLL_ENV=production bundle exec jekyll build --baseurl 'http://people.eecs.berkeley.edu/~jegonzal' 
rsync -avh _site/. login.eecs.berkeley.edu:~/public_html/.
