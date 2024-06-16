# Website Crawl and Check

## Docs

Documentation is stored in `/docs` folder as markdown files and available [here](https://accesspc.github.io/website-crawl-and-check/).

```bash
# Local development server
docker run -it --rm -v ${PWD}:/docs -p 8000:8000 accesspc/mkdocs-material
```

```bash
# Build documentation
docker run -it --rm -v ${PWD}:/docs accesspc/mkdocs-material build
```

```bash
# Build and deploy to github pages
docker run -it --rm -v ${PWD}:/docs -v ~/.ssh:/home/mkdocs/.ssh accesspc/mkdocs-material gh-deploy
```
