# Personal Website & Builder

A custom, lightweight static site generator (SSG) built from scratch for my personal portfolio website and portfolio. It uses Python, Jinja templates, and GNU Make for document compilation.

## Motivation

After graduating from undergrad and losing access to my Adobe Portfolio website, I ini­tially migrated to Jekyll to manage my work on GitHub Pages.

Eventually, I wanted complete, program­matic control over the document structure down to the raw HTML level. This project abandons bloated template ecosystems in favor of a lean static site generator specifically tailored for my content.

## Architecture & Performance

Designed to be lightweight, the engine utilizes:

- **Python & Jinja**: A modular pipeline that compiles `.html.jinja` and `.css.jinja` source templates directly into production‐ready static markup.
- **Color Space Generation**: Integrates procedural color tools like Coloraide to dynamically compute and format precise color palettes across the site.
- **Makefile Orchestration**: Automates local development builds, asset compi­lation, and deployment tasks with zero configuration drift.
