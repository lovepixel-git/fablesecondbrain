# 008. The Six-Cut Best Practices Kernel

Daniel Agrici, local skill at Skills/Public/best-practices, current 2026. PRACTITIONER.
Source: local repository (github.com/lovepixel-git/best-practices) (retrieved 2026-07-07)

## What it says

- Six cuts across three acts. Before: read before write; name like the next reader is hostile. During: smallest unit that works; delete more than you add. After: evidence over intuition; failure is the spec.
- Wrapped by a stance (context over text, calibrated confidence, no agreement theater) and an agent kernel (bounded slices, explorers map, workers implement, verifiers gate, closeout discipline).
- Refuses any task with no verification path; an undo plan is not optional.

## Why it is canon here

It is the operator's own engineering doctrine and governed how this brain was built: read-first exploration, bounded parallel workers, adversarial verification, git checkpoint undo.

## How this brain applies it

- [[Claim Verification Flow]] is cut five (evidence over intuition) applied to research.
- Every flow note carries a rollback_note because failure is the spec.
