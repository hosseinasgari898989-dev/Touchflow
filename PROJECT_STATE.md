# TouchFlow project state

Last updated: 2026-11-19

## Identity

- Project: **TouchFlow**
- Repository: https://github.com/hosseinasgari898989-dev/Touchflow
- Default branch: `main`
- Documentation branch: `feature/touchflow-clean-foundation-2026-11-19`
- Documentation PR: [#1](https://github.com/hosseinasgari898989-dev/Touchflow/pull/1) — open, draft, not merged.
- Selected source commit: `36b67597a86a84c093cc9c50ec2e32af6e4dbad8`
- Immutable source backup branch: `backup/touchflow-v1-native-source-2026-11-19`
- Native cleanup work branch: `feature/touchflow-v1-native-cleanup-2026-11-19`

## Baseline APK

- Original filename: `GrandmaConnect-preview.apk`
- Preserved filename: `TouchFlow-v1.0.0-baseline.apk`
- Size: 866,747 bytes
- SHA-256: `6dce713dfebcbf84ed5a175b6eb73808791765464087526875c3fe6f11bd0b89`
- Package: `com.grandmaconnect.preview`
- versionCode: 1
- versionName: `0.1.0-alpha-preview`
- minSdk / targetSdk: 24 / 35
- Label: Grandma Connect
- debuggable: true
- allowBackup: false
- Baseline certificate fingerprint: `7E:AE:68:77:3E:0E:AF:E0:B1:FB:A9:32:01:CE:67:DC:2B:6D:FB:21:57:FC:81:54:73:23:95:A9:C7:06:1D:08`
- Original private signing key: NOT FOUND.
- Full apksigner verification: NOT RUN.

## Source lineage

- High-confidence matching source: artifact of workflow run 44399759542.
- Branch: `feature/expanded-capture-settings-2026-11-19`.
- Source commit: `36b67597a86a84c093cc9c50ec2e32af6e4dbad8`.
- Source archive SHA-256: `e77c6b383251cd584b60cd6f4ae6b0ab445202970758d2c851e8bdc359b97a98`.
- CI APK from that source: 866,755 bytes; SHA-256 `46b48ac853739a44d8b1ff1ec7da341a984cb6fa91b4a0c541f075086f5a5770`.
- Manifest, all DEX files, Kotlin builtins and Accessibility config are identical; only resources.arsc differs by 8 bytes.
- CI build signer differs from baseline; in-place update is blocked pending original key recovery.

## Current app capabilities and gaps

- Recording is in-app canvas only; no global touch recorder across other apps.
- Playback uses AccessibilityService dispatchGesture.
- App declares canRetrieveWindowContent=false.
- Macro JSON is stored privately; allowBackup=false; no user-facing export/import.
- Extended duration options reach 10 minutes, with a hard 10-minute app limit.
- WebView timeline/keyframe UI remains mock/prototype, not a working persisted editor.

## Completed

- Rebranded project documentation to TouchFlow on a dedicated branch.
- Created immutable baseline copy and backup-kit versions 1 and 2.
- Identified high-confidence source lineage by comparing every APK ZIP entry.
- Extracted baseline and CI signer certificate fingerprints; determined they differ.
- Created backup and native cleanup branches from the matched source commit.
- Added/updated BASELINE, RELEASE_POLICY, INITIAL_AUDIT and CLEANUP_PLAN docs (on documentation branch).
- No application source, Manifest, Gradle file, workflow, permission, secret, variable or deployment config has been changed.
- `main` and `backup/native-baseline-2026-11-19` remain unchanged.
- No APK release published and no PR merged.

## Next steps

1. Search for/recover the original signing keystore or document the separate-install migration path.
2. Review the exact cleanup plan; do not delete any core Kotlin module.
3. Begin a small branding-only source PR while retaining package IDs and internal identifiers.
4. Add and test user-controlled macro export/import before data/package migrations.
5. Prototype API33 TouchInteractionController on the Galaxy A14 as a separate opt-in experiment; no promise of transparent global recording until proven.
6. Implement timeline/keyframe only against actual native macro data and tested persistence.
7. Build, inspect signature/version/package and run device regression before any publication.

## Continuity

Update after every material decision, branch, PR, commit, test or failure. Mark unknowns NOT FOUND / NOT VERIFIED; do not infer success.
