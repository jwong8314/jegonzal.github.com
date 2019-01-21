
bundle exec jekyll build --baseurl 'https://people.eecs.berkeley.edu/~jegonzal'
rsync -avh _site/. login.eecs.berkeley.edu:~/public_html/.
