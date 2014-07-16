#!/bin/bash

url_logo_template='https://docs.google.com/drawings/d/1VEoRTyumJIP2W06e0YV7w12ODY0p0wkZvrMbT-BkAPc/pub?' 
wget ${url_logo_template}"w=640&h=640" -O logo-640.png
wget ${url_logo_template}"w=320&h=320" -O logo-320.png
wget ${url_logo_template}"w=160&h=160" -O logo-160.png
wget ${url_logo_template}"w=80&h=80" -O logo-80.png
