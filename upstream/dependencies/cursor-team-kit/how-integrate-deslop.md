# deslop integration

## Patch

Replace `against main` with `against the base branch`. Preserve all other skill wording and behavior. The user chose this minimal change instead of adding scope or staging rules.

The replacement is declared in `transforms.json`; regenerate `skills/` rather than editing generated files. Upstream source hashes and its MIT license remain intact, with the local MIT notice added by the generator.

## Upstream removal

When updating A to B, inspect whether upstream uses the actual base branch rather than hardcoding `main`. If it does, remove this replacement and regenerate. Confirm deslop matches upstream, then run the source and generated-output checks. Do not merely refresh the replacement anchor without reviewing the upstream change.

## Verification

The generated SKILL.md must equal the pinned source with only `against main` replaced by `against the base branch`. No additional scope, staging, or permission rules are introduced.
