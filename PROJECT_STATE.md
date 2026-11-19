# TouchFlow project state

Last updated: 2026-11-19

## Identity

- Project: **TouchFlow**
- Repository: https://github.com/hosseinasgari898989-dev/Touchflow
- Default branch: `main`
- Documentation branch (source of PR #1): `feature/touchflow-clean-foundation-2026-11-19`
- Documentation foundation: [PR #1](https://github.com/hosseinasgari898989-dev/Touchflow/pull/1).
- Exact baseline build: [run 44399521736](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44399521736)
- Exact source commit: `36600aa02fba13430ba6a1e9e2efc09f665b7b67`
- Canonical source backup: `backup/touchflow-v1-exact-baseline-2026-11-19`
- Canonical cleanup branch: `feature/touchflow-v1-cleanup-exact-baseline-2026-11-19`
- Earlier secondary branches based on `36b67597a86a84c093cc9c50ec2e32af6e4dbad8` are preserved unchanged.

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
- The original signing private key/keystore: NOT FOUND.
- Full apksigner verification: NOT RUN.

## Exact source lineage

- Successful workflow: run 44399521736.
- Source branch: `feature/expanded-capture-settings-2026-11-19`.
- Source commit: `36600aa02fba13430ba6a1e9e2efc09f665b7b67`.
- Source archive SHA-256: `e77c6b383251cd584b60cd6f4ae6b0ab445202970758d2c851e8bdc359b97a98`.
- The run's `app-debug.apk` is byte-for-byte identical to the owner's APK; exact same size and SHA-256.
- The run's signing certificate fingerprint matches the owner APK.
- Later run 44399759542 used identical source archive content, but a new debug certificate and an 8-byte `resources.arsc` difference. This shows later ephemeral builds do not guarantee signing continuity.
- The build artifact is preserved in backup kit v3, but the private key is not.

## Current app capabilities and gaps

- Recording is in-app canvas only; no global touch recorder across other apps.
- Playback uses AccessibilityService dispatchGesture.
- App declares canRetrieveWindowContent=false.
- Macro JSON is stored privately; allowBackup=false; no user-facing export/import.
- Extended duration options reach 10 minutes, with a hard 10-minute app limit.
- WebView timeline/keyframe UI remains mock/prototype, not a working persisted editor.

## Completed

- Rebranded project documentation to TouchFlow on a dedicated branch.
- Created immutable baseline copy and backup-kit versions 1, 2 and 3.
- Matched baseline APK exactly to successful workflow run 44399521736.
- Identified exact source archive and commit for the baseline.
- Extracted baseline and later-build signer certificate fingerprints.
- Created canonical exact-source backup and cleanup branches from commit 36600aa.
- Added/updated BASELINE, RELEASE_POLICY, INITIAL_AUDIT, CLEANUP_PLAN and state documentation on the documentation branch.
- No application source, Manifest, Gradle file, workflow, permission, secret, variable or deployment config has been changed.
- `main` and `backup/native-baseline-2026-11-19` remain unchanged.
- No APK release has been published.

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


## Current continuation — 2026-11-20 (Step 1 build bootstrap)

- Active isolated work branch: `feature/step1-build-bootstrap-2026-11-20`.
- Branch base: `feature/touchflow-feature-pack-bundle-fix-2026-11-19` at `05d4f4fe8aa73aec9711aeb2c6fff6a4ab4e5137`.
- Owner approved only Step 1 source/Workflow staging and CI build on this branch. No merge to `main`, no baseline or backup changes, no start of Step 2 before Step 1 build is green and reviewed.
- Source archive supplied by Claude: `TouchFlow-Step1-source.tar.xz`, 162,524 bytes, SHA-256 `8811c815e01c415e48dde1f18a4b94e35d8c87bc6c106b6e2462d6ddb623f30c`.
- The exact binary archive is verified locally in this conversation, but **has NOT been committed to the Git branch**. The GitHub connector text-write path did not provide a direct binary upload. No `.step1-source/part-*` fragments exist in the branch; do not assume they were staged.
- A new workflow draft is prepared locally as `.github/workflows/build-touchflow-step1.yml`, but **has NOT been committed or executed**. The previous `.github/workflows/build-touchflow-feature-pack.yml` is preserved unchanged. The prepared workflow is intended to use JDK 17, Gradle 8.9, Android SDK 35; run JUnit, assert a nonzero test count, build a debug APK, check package `com.grandmaconnect.feature`, app label `TouchFlow`, signature, and retain `canRetrieveWindowContent=false`.
- Workflow report fix in the prepared draft: retain full `aapt2 dump badging` output rather than truncating it through `head`. Permissions are captured for review but an allow-list is not enforced.
- Static source inspection found 13 `@Test` annotations across the three correctly placed test classes. This is not a runtime test result.
- Main remains `6c738c2214d4244913fe449ed6172db613f844bd`; `backup/native-baseline-2026-11-19` remains `d62899f0eb586a870471648fd3d77d4b8f50fb8d`; PR #4 remains open/unmerged. Verify these before any future write.
- Build status at this addendum: **BLOCKED BEFORE RUN — binary archive not uploaded; pending workflow not activated; NOT RUN / NOT VERIFIED**. See `PROJECT_HANDOFF.md`, section 12, especially 12.3–12.6, for the exact blocker and resume steps.
- Keep `Save on-device retest = NOT YET DONE` until the owner confirms it on the target Galaxy A14. Build success alone does not close this device test gate.

- Immediate next step: upload `TouchFlow-Step1-source.tar.xz` (162,524 bytes) to the root of this branch; verify SHA-256 exactly equals `8811c815e01c415e48dde1f18a4b94e35d8c87bc6c106b6e2462d6ddb623f30c`; then move `docs/ci/build-touchflow-step1.yml.pending` into `.github/workflows/build-touchflow-step1.yml` and push only this branch.
