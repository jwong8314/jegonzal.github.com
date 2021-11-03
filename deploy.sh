
bundle exec jekyll build --baseurl 'https://people.eecs.berkeley.edu/~jegonzal'
rsync -avh _site/. watson.millennium.berkeley.edu:~/public_html/.
