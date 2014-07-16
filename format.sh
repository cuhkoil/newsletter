#!/bin/bash

for fn in `ls -1 issue/ | grep ".html" | sed 's/.html//'`
do
    echo $fn
    pandoc -f html -t plain -o issue/${fn}.txt issue/${fn}.html
    # Pandoc can not fetch remote images specified with abs URL
    #pandoc -f html -t pdf -o issue/${fn}.pdf issue/${fn}.html
    wkhtmltopdf --page-width 680 issue/${fn}.html issue/${fn}.pdf
    wkhtmltoimage --disable-smart-width --width 680 issue/${fn}.html issue/${fn}.jpg
done
