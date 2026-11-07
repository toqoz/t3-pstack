# Formal verification adoption

Statechart, create-formal-verification-skill, and maintain-formal-verification-skill are adopted unchanged. No T3, Patch, or Design transformation is needed. Host permissions and storage conventions continue to apply without duplicating them in the skill text.

The source and license are recorded in [the upstream guide](../../README.md). Statechart includes its original TypeScript implementation, shell launcher, fixtures, and tests. All are copied with locked source hashes and modes. No TLC JAR, Java runtime, Pele package, or node_modules is redistributed.

## Runtime dependencies

The original launcher supports current Node, Bun, or Deno versions stated in its error. The implementation pins TLC 1.7.4 with SHA-256 936a262061c914694dfd669a543be24573c45d5aa0ff20a8b96b23d01e050e88. Its default mise provisioning and TLA2TOOLS/JAVA override remain unchanged. The rendering reference pins Pele 1.9.0. External dependency installation is an invocation-time concern, not an additional integration runtime.

The [TLC v1.7.4 license](https://raw.githubusercontent.com/tlaplus/tlaplus/v1.7.4/LICENSE) is MIT. Original pstack notices govern the distributed skill implementation. Preserve applicable third-party notices if a future change redistributes those dependencies; this adoption does not.

## Executed evidence

Downloaded the pinned TLC JAR into workspace cache and verified its exact SHA-256. Used an ephemeral Nix JRE (Zulu OpenJDK 21.0.11) and existing Node 24.14.1 without editing environment configuration or installing mise. Actual TLC runs passed Counter and MediaPlayerFixed; MediaPlayer exited 1 and reported a one-step LoudWhenStopped invariant violation. Pele 1.9.0 rendered the generated fixed-model Mermaid into SVG.

Four original upstream test files previously passed 192 of 193 cases. The failing relative-symlink fixture passed when TMPDIR used a canonical workspace-local path instead of the macOS temporary-path alias. No launcher patch was made.

These checks validate the checker/renderer path on fixtures. They do not prove a model faithfully represents a real product, visually validate the SVG, exercise default mise provisioning, or establish an end-to-end generated formal skill lifecycle. Creation and maintenance retain upstream correspondence, mutation, counterexample replay, sync-commit, and scope requirements; no product proof is claimed by packaging them.
