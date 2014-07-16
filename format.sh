#!/bin/bash

for fn in `ls -1 issue/ | grep ".html" | sed 's/.html//'`
do
    echo $fn
    pandoc -f html -t plain -o issue/${fn}.txt issue/${fn}.html
    #pandoc -f html -t pdf -o issue/${fn}.pdf issue/${fn}.html
done
