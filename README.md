<!--
    Copyright 2022-2023 TII (SSRC) and the Ghaf contributors
    SPDX-License-Identifier: CC-BY-SA-4.0
-->

# Orthus

CI/CD Database Web Application

## Directories

| Directory | Description
| --- | ---
| .github | Github actions
| githooks | Git hook scripts
| LICENSES | Licenses used in this repository

## Git commit hook

When contributing to this repo you should take the git commit hook into use. Github actions will do commit message checks the same way, so you save time and trouble by using the git hook in the first place.

This hook will check the commit message for most trivial mistakes against [current Ghaf commit message guidelines](https://github.com/tiiuae/ghaf/blob/main/CONTRIBUTING.md#commit-message-guidelines)

### Installing git hooks

Just run ``./githooks/install-git-hooks.sh`` in repository main directory, and you should be good to go. Commit message checking script will then run when you commit something.

If you encounter any issues with the git commit message hook, please report them. And while waiting for a fix, you may remove the hook by running ``rm -f .git/hooks/commit-msg`` in the main directory of the repository.

## Licensing

This repository follows the Ghaf team licensing:

| License Full Name | SPDX Short Identifier | Description
| --- | --- | ---
| Apache License 2.0 | [Apache-2.0](https://spdx.org/licenses/Apache-2.0.html) | Source code
| Creative Commons Attribution Share Alike 4.0 International | [CC-BY-SA-4.0](https://spdx.org/licenses/CC-BY-SA-4.0.html) | Documentation

See [LICENSE.Apache-2.0](./LICENSES/LICENSE.Apache-2.0) and [LICENSE.CC-BY-SA-4.0](./LICENSES/LICENSE.CC-BY-SA-4.0) for the full license text.
