#!/bin/bash

echo "Message pour le commit : "
read message
git add .
git commit -m "$message"
git push
