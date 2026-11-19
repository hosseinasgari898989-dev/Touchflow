# Change, backup, and release policy

## Source is authoritative

- The Android Gradle source project is the editable source of truth.
- APK files are build outputs. Never patch an APK directly and never overwrite an earlier APK version.
- Keep the original baseline binary and its checksum unchanged.

## Before every change

1. Create a timestamped backup branch from the exact source commit being changed.
2. Record the source commit SHA, baseline APK SHA-256, and the intended change.
3. Work on one focused feature branch.
4. List files to be added, changed, or removed. For each removal, explain why it is safe and identify references/dependencies.
5. Keep a rollback path. Do not delete legacy source archives or experimental branches during ordinary feature work.

## Pull request requirements

Each change goes through a small pull request. Before approval:

- Review the complete diff, including build scripts, manifest, permissions, and resources.
- Build from a clean checkout.
- Run applicable unit/build checks.
- Verify APK package ID, app label, version code/name, signing certificate, and APK signature.
- Test install/launch and the changed behavior on the target Android device.
- Record any known limitations and failed tests; do not turn a missing result into a pass.

## Versioned APK publication

For every release, retain the following as immutable artifacts:

- `TouchFlow-vX.Y.Z.apk`
- `TouchFlow-vX.Y.Z.apk.sha256`
- changelog/release notes
- source commit SHA
- successful build workflow run
- package/version/signing verification results

Preview/debug builds must be labeled as previews and must not replace a stable release. A new version is a new artifact, never a replacement of the previous one.

## Cleanup rules

- Do not remove code based only on filename or apparent duplication.
- Inspect call sites, manifest declarations, Gradle dependencies, resources, and tests before removal.
- Keep independent experiments isolated until one implementation is selected.
- Do not change repository secrets, variables, permissions, deployment settings, workflow triggers, or the protected baseline as part of routine cleanup.
