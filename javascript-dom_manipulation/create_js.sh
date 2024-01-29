#!/bin/bash

for i in {0..8}
do
  touch "${i}-script.js"
  touch "${i}-main.html"
  chmod u+x "${i}-script.js"
  chmod u+x "${i}-main.html"
done
