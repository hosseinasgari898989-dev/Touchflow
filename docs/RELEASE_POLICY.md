# TouchFlow backup, change and release policy

## Source and baseline

- Android Gradle source is editable; APKs are immutable build outputs.
- Preserve `TouchFlow-v1.0.0-baseline.apk` and its SHA-256 forever.
- Preserve the matching source commit and its dedicated backup branch.
- Do not patch an APK directly.

## Before every source change

1. Create a timestamped backup branch from the exact commit being changed.
2. Record source commit, baseline APK checksum, signing certificate fingerprint, and intended change.
3. Use one feature branch per focused change.
4. List every file to add/change/remove with dependency and test impact.
5. Do not delete legacy archives or experimental branches during ordinary feature work.

## Compatibility and signing

For a direct app update, Android requires the same application ID and the same signing certificate or a valid signing lineage, plus an equal-or-higher versionCode. See [Android app updates](https://developer.android.com/google/play/app-updates).

- Baseline application ID: `com.grandmaconnect.preview`.
- Baseline versionCode: 1.
- Baseline signing certificate fingerprint is recorded in `docs/BASELINE.md`.
- The latest CI debug build from the matching source uses a different certificate.
- The original private signing key is currently NOT FOUND.
- Do not publish or install a purported update from a different key.
- Keep package ID/namespace stable during the first branding cleanup; branding changes do not require changing package identifiers.
- If the original key cannot be recovered, make a separate-install migration plan and add/test macro export/import before uninstalling anything.

## Macro data protection

- Current macros are JSON files in private app storage.
- `allowBackup=false`; there is no current user-facing export/import feature.
- Do not change storage schema, data directory or package ID until macro export/import and restoration tests pass.
- For each import: validate data, keep originals, reject invalid/oversized payloads, and avoid silent overwrite.
- Never silently discard malformed macro files.

## Pull request validation

- Review full diff, Manifest, Gradle, permissions, resources, storage and service behavior.
- Build from a clean checkout.
- Run unit/build tests and targeted macro schema tests.
- Verify package identity, version code/name, signing cert, APK signature and permissions.
- Test install/launch, recording, stopping, saving, reopening and playback on the target device.
- Record failed checks and known limitations truthfully.

## Immutable APK publication

Each release gets a new asset:
- `TouchFlow-vX.Y.Z.apk`
- `TouchFlow-vX.Y.Z.apk.sha256`
- changelog
- source commit
- workflow run ID and successful result
- package/version/signing verification evidence
- macro migration/export compatibility note

Never overwrite an older APK. Preview/debug builds must be clearly labeled and must not replace stable releases.

## Cleanup rules

- Do not remove code based on file name or apparent duplication alone.
- Inspect call sites, manifest declarations, Gradle dependencies, resources and tests before removing anything.
- The current audit found no safe core source-file deletions.
- Keep experimental branches isolated unless a reviewed PR selects individual files/features.
- Do not change secrets, variables, permissions, deployment settings or workflow triggers as part of cleanup.
