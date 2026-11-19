# TouchFlow project state

Last updated: 2026-11-19

## Identity

- Project: **TouchFlow**
- Repository: https://github.com/hosseinasgari898989-dev/Touchflow
- Default branch: `main`
- Cleanup branch: `feature/touchflow-clean-foundation-2026-11-19`

## Initial baseline

- Internal designation: `TouchFlow v1.0.0-baseline` (not a verified embedded APK version)
- Original upload: `GrandmaConnect-preview.apk`
- Preserved working copy: `/mnt/data/TouchFlow-v1.0.0-baseline.apk`
- Size: 866,747 bytes
- SHA-256: `6dce713dfebcbf84ed5a175b6eb73808791765464087526875c3fe6f11bd0b89`
- ZIP integrity test: PASS
- APK signer verification and package/version metadata: NOT VERIFIED
- Binary committed to GitHub: NO; it remains in this work session pending a suitable binary-preserving upload route.

## Repository findings

- Main root: `.github/`, `GrandmaConnectNative-source.zip`, `README.md`
- Main workflow: `.github/workflows/build-android.yml`; pushes of the source ZIP to main trigger a debug APK build. This is not a versioned release workflow.
- Existing branches observed:
  - `backup/native-baseline-2026-11-19`
  - `feature/expanded-capture-settings-2026-11-19`
  - `feature/touchflow-simple-runner-2026-11-19`
  - `feature/touchflow-webview-integration-20261119`
  - `work/native-source-inspection-2026-11-19`
- Experimental branches have independent workflows/source snapshots; do not merge them wholesale.

## Completed in this task

- Created `feature/touchflow-clean-foundation-2026-11-19` from main.
- Rebranded README to TouchFlow.
- Added `docs/BASELINE.md`, `docs/RELEASE_POLICY.md`, and this state file.
- No source code, manifest, build workflow, permissions, secrets, variables, or deployment settings changed.
- Main and `backup/native-baseline-2026-11-19` remain unchanged.
- Branch is four commits ahead of main, zero behind, with four documentation-only changed paths.

## Next steps

1. Find a binary-safe way to preserve the APK in GitHub Releases or an immutable repository artifact; keep the local copy unchanged meanwhile.
2. Extract and inspect `GrandmaConnectNative-source.zip`.
3. Verify the APK manifest/signature and whether the source archive corresponds to this binary.
4. Compare the experimental source snapshots and select one clean source base.
5. Produce an exact add/change/remove list before source cleanup.
6. Establish a validated, versioned APK build-and-release flow.

## Continuity

Update this file after every material decision, commit, test, failure, or changed next step. Record unknowns as `NOT VERIFIED`; do not infer a pass.
