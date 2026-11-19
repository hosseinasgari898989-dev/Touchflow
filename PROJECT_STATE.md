# TouchFlow project state

Last updated: 2026-11-19

## Identity

- Project name/branding: **TouchFlow**
- Repository: https://github.com/hosseinasgari898989-dev/Touchflow
- Default branch: `main`
- Current cleanup branch: `feature/touchflow-clean-foundation-2026-11-19`

## Baseline

- Owner-provided APK: `GrandmaConnect-preview.apk`
- Preserved local copy: `TouchFlow-v1-baseline.apk`
- Size: 866,747 bytes
- SHA-256: `6dce713dfebcbf84ed5a175b6eb73808791765464087526875c3fe6f11bd0b89`
- ZIP integrity test: passed
- Package/version/signature certificate and source-to-binary match: not yet verified
- Binary uploaded to GitHub: no; currently preserved in the work session only

## Repository observations

- Root of `main`: `.github/`, `GrandmaConnectNative-source.zip`, `README.md`
- Existing main workflow: `.github/workflows/build-android.yml`; it builds a debug APK from the legacy-named source ZIP when that ZIP is pushed to `main`.
- The workflow is not a versioned production release pipeline.
- Existing branches observed:
  - `backup/native-baseline-2026-11-19`
  - `feature/expanded-capture-settings-2026-11-19`
  - `feature/touchflow-simple-runner-2026-11-19`
  - `feature/touchflow-webview-integration-20261119`
  - `work/native-source-inspection-2026-11-19`
- The experimental branches contain independent build workflows and source snapshots. They must be reviewed separately, not merged wholesale.

## Safety of current work

- `main` is unchanged.
- `backup/native-baseline-2026-11-19` is unchanged.
- Only the cleanup feature branch has been created and its README rebranded.
- No code, manifest, workflow, permission, secret, variable, or deployment configuration has been changed.

## Open work

1. Inspect the APK manifest and signing certificate with Android SDK tools.
2. Extract and inspect `GrandmaConnectNative-source.zip`; verify whether it corresponds to the owner APK.
3. Compare the experimental branches and decide which source snapshot is the clean base.
4. Define the exact source cleanup and package/app identity change list.
5. Add build/release automation only after the source and release rules are verified.

## Continuity rule

Update this file after every material decision, commit, test result, failure, or change in next steps. Keep reports factual; use `NOT FOUND` when data cannot be verified.
