#!/usr/bin/env python3
import webbrowser

url = input()

url = url[:12] + 'ss' + url[12:]

webbrowser.open(url)