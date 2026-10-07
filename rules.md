# Architecture rules

These are examples, not universal laws. Keep only the rules your project can
explain, enforce, and test.

## 1. `engine-no-node`

Algorithm code stays portable and deterministic. It cannot import Node built-ins,
filesystem APIs, Electron, or platform-specific modules. Put I/O at an adapter
boundary and pass data into the engine.

## 2. `domain-no-runtime-deps`

Domain types and business rules do not import runtime libraries. Validation,
framework schemas, database clients, and UI packages belong outside the domain.

## 3. `renderer-no-electron`

The renderer does not import Electron. It receives only an explicit, typed bridge
from preload. This keeps Node APIs out of the UI process and makes the boundary
auditable.

## 4. `atomic-recovery-write`

Recovery metadata is written to a temporary file and renamed into place. A direct
write can leave a truncated manifest after a crash.

## 5. `exact-render-duration`

When a renderer has a computed duration budget, its output must be capped to that
budget. A playable MP4 that runs longer than the selected story is still wrong.

## 6. `safe-output-path`

An export path must resolve inside the configured output directory. Prefix checks
must include a path separator: `/sessions/run-17-copy` starts with
`/sessions/run-17`, but it is not inside that directory.
