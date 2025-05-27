# 🛠️ Static Site Generator

A simple and fast Static Site Generator (SSG) built in Python for transforming Markdown content into clean, styled HTML pages. 
Based on [Boot.dev's Static Site Generator project](https://blog.boot.dev/projects/build-a-static-site-generator/)

## ✨ Features

- 🔧 Converts Markdown (`.md`) files to HTML  
- 🕐 Fast build times for small to medium sites  
- 💡 Simple command-line interface (CLI). Just run ```./build.sh``` and watch the magic happen in your terminal!
- 📚 Ideal for blogs, portfolios, and documentation  


## Requirements
- Python 3.10+: Several class methods use "match"

## Limitations
- While nested inline elements (such as a bolded italic) exists in nature, the current scope of this project does not allow for such cases. Support for multiple levels of nested inline text types may be added in the future, but is _**not currently planned**_.
