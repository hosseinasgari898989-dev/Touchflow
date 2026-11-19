# TouchFlow project state

Last updated: 2026-11-19

## Identity

- Project: **TouchFlow**
- Repository: https://github.com/hosseinasgari898989-dev/Touchflow
- Default branch: `main`
- Cleanup branch: `feature/touchflow-clean-foundation-2026-11-19`
- Documentation PR: [#1 — establish TouchFlow v1 baseline and cleanup rules](https://github.com/hosseinasgari898989-dev/Touchflow/pull/1) — OPEN, DRAFT, NOT MERGED.

## Initial APK baseline

- Internal designation: `TouchFlow v1.0.0-baseline` (not a verified embedded APK version)
- Original upload: `GrandmaConnect-preview.apk`
- Preserved copy: `/mnt/data/TouchFlow-v1.0.0-baseline.apk`
- Size: 866,747 bytes
- SHA-256: `6dce713dfebcbf84ed5a175b6eb73808791765464087526875c3fe6f11bd0b89`
- ZIP integrity test: PASS
- Package/version/signer metadata: NOT VERIFIED
- Binary committed to GitHub: NO; preserved in current work session and backup-kit ZIP.
- Match to known main/simple/integration build outputs: NO; all three differ byte-for-byte.

## Backup kit

- Local bundle: `/mnt/data/TouchFlow-v1.0.0-backup-kit.zip`
- Bundle SHA-256: `2be92336c6ab173e48633b420ae9898289582fea2193c68c497be996af8976a1`
- Contains the owner APK, its SHA-256 record, three source candidate archives, and build comparison notes.
- The backup kit is downloadable from this conversation; it is not yet stored in the GitHub repository.

## Repository findings

- Main root: `.github/`, `GrandmaConnectNative-source.zip`, `README.md`
- Main workflow builds a debug APK when the source ZIP changes; it is not a versioned release pipeline.
- Existing branches:
  - `backup/native-baseline-2026-11-19`
  - `feature/expanded-capture-settings-2026-11-19`
  - `feature/touchflow-simple-runner-2026-11-19`
  - `feature/touchflow-webview-integration-20261119`
  - `work/native-source-inspection-2026-11-19`
- The source candidates and three build comparisons are documented in `docs/INITIAL_AUDIT.md`.

## Source review findings

- Main source keeps legacy `Grandma Connect` identity; Gradle says namespace/applicationId `com.grandmaconnect`, versionName `0.1.0-alpha`, minSdk 24, targetSdk 35.
- Simple Runner adds native capture settings and the TouchFlow app label. Extended capacity still has a 10-minute hard ceiling; quality and duration settings are not unlimited.
- WebView Integration adds offline UI and an allowlisted native bridge. Its gesture editor uses mock track data; keyframe persistence/easing dispatch and backup import/export are explicitly unsupported in this slice.
- Successful CI does not equal real device testing. Browser rendering and physical-device checks for these experimental branches are NOT VERIFIED.

## Completed in this task

- Created `feature/touchflow-clean-foundation-2026-11-19` from main.
- Rebranded README to TouchFlow.
- Added `docs/BASELINE.md`, `docs/RELEASE_POLICY.md`, `docs/INITIAL_AUDIT.md`, and this state file.
- Created a local baseline copy and backup-kit ZIP with checksum and three source candidate archives.
- Opened draft PR #1. It contains documentation only and has not been merged.
- No source code, manifest, build workflow, permission, secret, variable, or deployment setting changed.
- Main and `backup/native-baseline-2026-11-19` remain unchanged.
- No APK release has been published.

## Next steps

1. Inspect the owner's APK package, embedded version, and signer with Android SDK tools.
2. Identify the source/build that produced this exact APK; do not assume the main source ZIP or experimental previews are equivalent.
3. Select one clean source base after reviewing source diffs and regression risks.
4. Prepare an explicit add/change/remove list before touching application files.
5. Implement a versioned release process that stores each APK immutably with checksums and source/build evidence.

## Continuity

Update this file after every material decision, commit, test, failure, or changed next step. Record unknowns as `NOT VERIFIED`; do not infer a pass.
