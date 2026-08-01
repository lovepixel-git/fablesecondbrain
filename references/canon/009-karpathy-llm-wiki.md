# 009. The Karpathy LLM Wiki Pattern

Andrej Karpathy, public gist, 2025. PRACTITIONER.
URL: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f (retrieved 2026-07-07)

## What it says

- Proposes maintaining a personal wiki written for and by an LLM: hot cache for recent context, an index as the master catalog, an append-only log, and atomic cross-linked notes. Paraphrase.
- The wiki is the durable memory; each session restores context cheaply from the hot cache instead of re-reading everything.

## Why it is canon here

It is the architectural ancestor of this vault's hot/index/log/overview layout and of the operator's whole brain fleet; the claude-obsidian toolkit implements it.

## How this brain applies it

- wiki/hot.md (500-word overwrite), wiki/index.md (master catalog), wiki/log.md (append-only, newest on top) follow it exactly.
- [[Brain Refresh Flow]] extends it with dated-source refresh discipline the original gist leaves implicit.
