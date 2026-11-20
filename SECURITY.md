# Security policy

This is the default policy of the repositories in `nika-open`. A repository with its own
`SECURITY.md` refines it for its surface: the engine's policy, with its supported release lines
and its defense layers, is in [nika-open/nika](https://github.com/nika-open/nika/security/policy).
The others, the editor extension, the agent plugins and the workflow registry among them, follow
this one.

## Supported versions

Only the default branch (`main`) of each repository is supported, unless the repository's own
policy lists release lines.

## Reporting a vulnerability

Please do not report a vulnerability in a public issue, discussion or pull request.

Send it to **security@supernovae.studio** with:

- a description of the vulnerability and the repository it affects;
- the steps to reproduce it, or a minimal proof of concept;
- the commit, release version or deployed URL where you observed it;
- your assessment of the impact.

You will get an acknowledgement within 72 hours, and a first triage with an expected timeline
within 7 days. Supply-chain reports, about anything that ships to users (extension packages,
registry entries, Homebrew formulas, npm packages, container images, install scripts), are
treated as highest severity.

## Disclosure

1. Triage: a maintainer verifies the report and confirms its scope.
2. Fix: the patch is written privately.
3. Release: a GitHub security advisory and a patched release.
4. Credit: the reporter is named in the advisory, unless they ask to stay anonymous.

We aim for at most 90 days between the report and its public disclosure, and less for a
vulnerability that is actively exploited.
