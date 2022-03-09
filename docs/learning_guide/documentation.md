# Documentation with [**Material for MkDocs**](https://squidfunk.github.io/mkdocs-material/)

!!! abstract "Learning Objectives"
    By the end of this section, you should be able to:

    * Explain why **Material for MkDocs** is an optimal choice to build your documentation
    * Know how to navigate the official documentation of **Material for MkDocs** 
    * Build your own documentation from scratch 
    * Explain how the `quizli` documentation was built

## What is **Material for MkDocs**?


**Material for MkDocs** is a [**Material Design**](https://material.io/) theme for [**MkDocs**](https://www.mkdocs.org/).

!!! info
    !!! quote "Material"
        A design system created by Google to help teams build high-quality digital experiences for Android, iOS, Flutter, and the web.
    !!! quote "MkDocs"
        A fast, simple and downright gorgeous static site generator that's geared towards building project documentation. Documentation source files are written in Markdown, and configured with a single YAML configuration file.

With **Material for MkDocs** you can, quoting it's Github Readme, create
> a branded static site from a set of Markdown files to host the documentation of your Open Source or commercial project - customizable, searchable, mobile-friendly, 50+ languages. Set up in 5 minutes.

!!! tip "Alternative themes"
    If you don't like the look of the Material theme, there is a list of
    [alternative MkDocs themes](https://www.mkdocs.org/user-guide/choosing-your-theme/)
    
## Why **Material for MkDocs**?

Here is a list of features that make **Material for MkDocs** a great choice: 

1. Geared towards (technical) project documentation
2. Future-proof & simple to use thanks to using Markdown source
3. Generates a SEO-friendly site
4. It's Open-Source & has a permissive license (MIT)
5. It's customizable (via `JavaScript` and `CSS`) and extendable (via plugins)
6. Easy to publish via Gitlab/Github Pages

!!! info "Alternative static site generators"

    Read the following section in **Material for MkDocs'** documentation to see how it compares to alternative
    static site generators: [Alternatives](https://squidfunk.github.io/mkdocs-material/alternatives/)

To prove to you how easy it is to generate a basic documentation for your existing project, we point to the following example:

### Example
!!! example "Minimal Example"

    1. Install **Material for MkDocs** with:
    ```
    pip install mkdocs-material
    ```
    2. Move your existing Markdown files into a `docs/` folder
    3. Add a `mkdocs.yml` file in your project root with the minimal content:

    ``` yaml
    theme:
      name: material
    ```

    !!! hint
        For new projects steps 2. and 3. can be even abbreviated further with the `mkdocs new .` command

    :rocket: That's all you need. 
    Just serve your docs with `mkdocs serve` and enjoy them in your browser.

Amazingly, for many projects this simple setup already leads to a great documentation since **Material for MkDocs** uses reasonable defaults.

Still, there is plenty room for improvement. So in the following subsections we walk you through some customizations to build a more sophisticated documentation.

## How to Create your own Documentation from Scratch?

Instead of (doing a bad job in) rewriting the existing documentation of **Material for MkDocs**, we will instead point out and guide you through the relevant sections.

### 1. The Getting Started Section

If you are new to **Material for MkDocs**, first check out its [Getting Started section](https://squidfunk.github.io/mkdocs-material/getting-started/).
It contains installation instructions, an example of how to create a minimal documentation, and a few brief discussions of more advanced topics like publishing your documentation.
At the end of it, you should already be equipped with a bare-bones documentation.

### 2. The Setup Section

Next, I suggest you read through the [setup section](https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/) in order to add more features to
your documentation and to customize it.


!!! info
    Below you can see all customization options that currently exist. 
    
    I added a checkmark for those options that are used by `quizli`.
    
* [x] Changing the colors
* [ ] Changing the fonts
* [ ] Changing the language
* [x] Changing the logo and icons
* [x] Setting up navigation
* [x] Setting up site search
* [ ] Setting up site analytics
* [ ] Setting up social cards
* [ ] Setting up tags
* [ ] Setting up versioning
* [ ] Setting up the header
* [x] Setting up the footer
* [x] Adding a git repository
* [x] Adding a comment system

### 3. The Reference Section

I bet at this point your documentation looks quite amazing already, but we can improve it even more by leveraging the [reference secion](https://squidfunk.github.io/mkdocs-material/reference/).

!!! info 
    As of time of writing, the reference section comprises the following parts.
    
    Again we add checkmarks for those features that we used for `quizli's` docs.

* [ ] Abbreviations
* [x] Admonitions
* [ ] Annotations
* [ ] Buttons
* [x] Code blocks
* [x] Content tabs
* [x] Data tables
* [ ] Diagrams
* [x] Footnotes
* [x] Formatting
* [x] Icons + Emojis
* [ ] Images
* [x] Lists
* [ ] MathJax


## Learning by Example: `quizli`

After reading the previous sections, you might want see some examples on how 

I encourage you to browse through `quizli's` documentation and whenever you see something you like,
or you are curious of how things are done, take a look at the corresponding sections in the
[`docs`](https://github.com/pwenker/quizli/tree/main/docs) folder.

!!! tip "Tip: Learning by Example"

    Many popular projects use **Material for MkDocs**. 
    
    Their creators are often experienced and creative developers who
    put a lot of effort into their documentation. 
    
    Hence a great way to learn is to read through their documentation
    and see what you can adapt.

    Some examples:
    
    - [FastAPI](https://fastapi.tiangolo.com/)
    - [AWS Copilot CLI](https://aws.github.io/copilot-cli/)
    - [Pydantic](https://pydantic-docs.helpmanual.io/)
    - [Traefik](https://doc.traefik.io/traefik/)

    And [plenty more](https://github.com/squidfunk/mkdocs-material#trusted-by-)!


### Configuring the documentation

Below you find the configuration settings of `quizli's` documentation. 

For each block of settings, I added a link to the corresponding 
section in the **Material for MkDocs** documentation for further reference. 


``` yaml title="The configuration file: mkdocs.yml "
--8<-- "mkdocs.yml"
```

### Publish your documentation

!!! info "Info: Gitlab pages support"

    While our example below shows a Github Workflow, you could publish
    your documentation equally well with Gitlab pages.

    This might come especially handy if you want to host your own private
    documentation.

    Instructions can be found again in the
    [Publishing your site](https://squidfunk.github.io/mkdocs-material/publishing-your-site/) 
    section

There is a dedicated section in the **Material for MkDocs** documentation on how to [Publish your documentation](https://squidfunk.github.io/mkdocs-material/publishing-your-site/).

For our purposes, we automate the deployment of the project documentation with a GitHub Actions workflow.

``` yaml title="Publishing your docs: .github/workflows/deploy_docs.yml "
--8<-- ".github/workflows/deploy_docs.yml"
```

This way, our documentation is conveniently updated every time we push changes to our git repository.

### Using Plugins

There is a great collection of third-party [**MkDocs** plugins](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Plugins).

Below we shortly describe two that we use to further improve `quizli's` documentation. Feel free to browse the collection for
other plugins that suit your needs.

#### [mkdocstrings](https://mkdocstrings.github.io/)

With this plugin we can automatically generate documentation from source code.

To enable the plugin we add it to our `mkdocs.yml` file:

```yaml
theme:
  name: "material"

plugins:
  - search
  {==- mkdocstrings==}
```

Now we can reference `quizli's` source code and it will nicely show up in the documentation.
For example, since we have documented `quizli's` source code properly, the following simple 
reference to it's `quiz` module:

``` yaml title="Example: quiz"
--8<-- "docs/code_reference/quiz.md"
```
will turn out the following way in the documentation: [Quiz - code reference](../code_reference/quiz.md).

You find more advanced usage examples in `mkdocstring`'s [documentation](https://mkdocstrings.github.io/usage/).


#### [mkdocs-jupyter](https://github.com/danielfrg/mkdocs-jupyter)

!!! info "Alternative: `mknotebooks`"
    There is an alternative plugin with a similar feature set:
    [`mknotebooks`](https://github.com/greenape/mknotebooks)

    If you want to include jupyter notebooks into your project's documentation
    check out which one fits your needs better. 
    
This plugin allows us to render jupyter notebooks (or Python scripts) in our documentation.

After installing it, we can enable the plugin again by simply adding a line to our `mkdocs.yml` file:

``` yaml
plugins:
  - search
  - mkdocstrings
  {==- mkdocs-jupyter==}
```  

To give you an example of how it turns out, take a look at the following [`notebook`](../notebooks/quizli.ipynb).
