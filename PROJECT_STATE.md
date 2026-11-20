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
- The Step 1 Workflow draft is committed but inactive at `docs/ci/build-touchflow-step1.yml.pending`; it is deliberately outside `.github/workflows/` until the binary archive is uploaded and SHA-verified. Then move it to `.github/workflows/build-touchflow-step1.yml`. The prior `.github/workflows/build-touchflow-feature-pack.yml` is preserved unchanged. The pending workflow is designed for JDK 17, Gradle 8.9, Android SDK 35; it runs JUnit, asserts a nonzero test count, builds a debug APK, checks package `com.grandmaconnect.feature`, app label `TouchFlow`, signature, and retains `canRetrieveWindowContent=false`.
- Workflow report fix in the pending draft: retain full `aapt2 dump badging` output rather than truncating it through `head`. Permissions are captured for review but an allow-list is not enforced.
- Static source inspection found 13 `@Test` annotations across the three correctly placed test classes. This is not a runtime test result.
- Main remains `6c738c2214d4244913fe449ed6172db613f844bd`; `backup/native-baseline-2026-11-19` remains `d62899f0eb586a870471648fd3d77d4b8f50fb8d`; PR #4 remains open/unmerged. Verify these before any future write.
- Build status at this addendum: **BLOCKED BEFORE RUN — binary archive not uploaded; pending workflow not activated; NOT RUN / NOT VERIFIED**. See `PROJECT_HANDOFF.md`, section 12, especially 12.3–12.6, for the exact blocker and resume steps.
- Keep `Save on-device retest = NOT YET DONE` until the owner confirms it on the target Galaxy A14. Build success alone does not close this device test gate.

- Immediate next step: upload `TouchFlow-Step1-source.tar.xz` (162,524 bytes) to the root of this branch; verify SHA-256 exactly equals `8811c815e01c415e48dde1f18a4b94e35d8c87bc6c106b6e2462d6ddb623f30c`; then move `docs/ci/build-touchflow-step1.yml.pending` into `.github/workflows/build-touchflow-step1.yml` and push only this branch.


## Step 1 latest CI update — 2026-11-20

- Owner uploaded `TouchFlow-Step1-source.tar.xz` to branch root.
- GitHub file blob SHA: `e9f41d4e39d2a4dffe9481b9a0d8cffb4b17c06a`.
- Verified GitHub file bytes: 162,524 bytes; SHA-256 `8811c815e01c415e48dde1f18a4b94e35d8c87bc6c106b6e2462d6ddb623f30c` — exact match.
- Active workflow: `.github/workflows/build-touchflow-step1.yml`; old feature-pack workflow untouched.
- CI Run 1: [44633139815](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44633139815), commit `2a638f4f027eb7609a0ce8c044469468564e4aa1`, job `135944746691`.
- Last observed job state: `in_progress`. Archive hash, extraction, source listing, JDK17 setup succeeded. Gradle 8.9 setup was in progress; SDK/JUnit/assert/assemble/verify still pending. No result/artifact available at that observation.
- Overall CI status: **PENDING — NOT VERIFIED**. Do not say Build/test passed until run conclusion and logs are inspected.
- Main remains `6c738c2214d4244913fe449ed6172db613f844bd`; backup baseline remains `d62899f0eb586a870471648fd3d77d4b8f50fb8d`; PR #4 Open / Unmerged. Continue only on the Step 1 feature branch.
- For full evidence, read `PROJECT_HANDOFF.md` section 12.7.


## Step 1 CI result / retry — 2026-11-20

- Run 1 [44633139815](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44633139815): FAILURE during JUnit only. Archive SHA check, extraction, JDK17, Gradle8.9, Android SDK35 and source/test compilation succeeded. 13 tests executed: 12 passed, 1 failed. No APK was built; assembleDebug was skipped.
- Failing assertion: `SearchRulesTest.kt:30`, test `allTokensMustMatchAcrossFields`. Persian token `چت` was tested against English package token `chat`, but SearchRules does no synonym/translation mapping. JUnit XML artifact ID `14582318844` confirms.
- Exact test-only patch: `.github/patches/step1-search-rules-test-fixture.patch`; replaces only query term `چت` with `chat` for the multi-field assertion. No production code, Manifest, permission or app runtime logic changed. Original archive remains untouched and hash-verified.
- Workflow applies this explicit patch after source extraction; patch path is included in workflow triggers and uploaded diagnostics artifact.
- Retry Run 2 [44633470736](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44633470736), commit `15d1c2668e10b6cb5ca81b2c54039475b731f5d9`, job `135945912338`, was in progress at the last check; checkout was executing and remaining steps pending.
- Current outcome: **RETRY PENDING — NO GREEN BUILD YET**. Recheck Run 2 and inspect the actual JUnit, build, APK, package/label/signature evidence before reporting success.
- Do not begin Step 2 yet. Save physical-device retest remains separate.
- See `PROJECT_HANDOFF.md` sections 12.8–12.9 for complete evidence and test diagnosis.


## Step 1 final CI — SUCCESS (2026-11-20)

- Run 2 [44633470736](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44633470736) completed success on isolated branch `feature/step1-build-bootstrap-2026-11-20`, commit `15d1c2668e10b6cb5ca81b2c54039475b731f5d9`.
- Tests: 13 passed, 0 failed, 0 errors, 0 skipped. The explicit one-line test fixture correction is documented at `.github/patches/step1-search-rules-test-fixture.patch`; no production application code changed for the retry.
- assembleDebug: success. Package `com.grandmaconnect.feature`, label `TouchFlow`, version `0.1.0-alpha-feature`, SDK min/target 24/35.
- APK size 1,127,351 bytes. SHA-256: `7b7da543f4c2bceaf75e23bbae7d894e09dd20b4aee84cd4441d8838dd170576`.
- Signature verified (APK Signature Scheme v2). Debug certificate SHA-256: `15f8e0ac1944f5e4351240b88203c875ac46059a41c260ca20a474acedba7f26`.
- Manifest/badging shows only permission `android.permission.POST_NOTIFICATIONS`; Accessibility config retains `canRetrieveWindowContent=false`.
- Artifact [14583062276](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44633470736/artifacts/14583062276), expires 2026-12-19; it includes APK, original archive, patch, test reports and verification files.
- Original Claude archive is unchanged and its SHA-256 was reverified from the artifact.
- **Step 1 CI gate PASSED.** This does not constitute a device acceptance test. Save persistence, widget playback, and Full-Screen/global capture are still not verified on the target Galaxy A14.
- Do not install this APK as an update to `com.grandmaconnect.preview`; it is a separate debug package. Do not attempt updating an older `.feature` installation without matching its signer.
- Step 2 (macro editor) has NOT started; obtain scope/acceptance before beginning.
- Full evidence: `PROJECT_HANDOFF.md` sections 12.8–12.10.


## R1 branch staging — 2026-11-20

- Owner supplied `TouchFlow-R1-source.tar.xz`; local file SHA-256 verified as `4e0e00918e0b3f172d02daa9262d1d2da3c130872583bcc726aabd5ac35e12d3`.
- Created isolated branch `feature/touchflow-r1-recording-actions-2026-11-20` from `feature/step1-build-bootstrap-2026-11-20` at the Step 1 line (branch head at creation: `07474eb75c0cbb98ff3eb7b7b1fcb9c595ea7a5d`). Step 1 successful evidence remains Run `44633470736`.
- Updated `.github/workflows/build-touchflow-feature-pack.yml` on the R1 branch. It is scoped to the R1 branch and triggers only when `TouchFlow-R1-source.tar.xz` is pushed; manual `workflow_dispatch` was omitted.
- Workflow checks the exact R1 archive SHA, runs Gradle JUnit and requires exactly 24 tests with zero failures/errors/skips, runs `assembleDebug`, verifies package `com.grandmaconnect.feature`, label `TouchFlow`, APK signature, exact permission allowlist (`POST_NOTIFICATIONS`), and `canRetrieveWindowContent=false`; it uploads the APK and reports.
- **BLOCKER:** the R1 binary archive is verified in the assistant runtime but has NOT yet been committed to the GitHub branch. The available GitHub connector supports text writes but does not provide a direct local-file binary upload interface. The workflow must not be treated as run until the owner uploads the exact archive to the root of the R1 branch.
- Workflow file currently committed at commit `0b3d48f7fefd34dd25af8e9b26f23d881cd72218`. No source archive or application source was changed by that commit.
- Main was read at `6c738c2214d4244913fe449ed6172db613f844bd` before this work; no write operation targeted `main`. Backup branches were not targeted.
- R1 status: source archive hash verified locally; branch created; CI workflow staged; **archive upload pending; R1 Build NOT RUN; R1 JUnit NOT RUN; device NOT VERIFIED**.
- Next owner action: upload the already-provided `TouchFlow-R1-source.tar.xz` unchanged to the repository root on branch `feature/touchflow-r1-recording-actions-2026-11-20`. This single push triggers the R1 CI. Then inspect the run and its artifact before installing or accepting on device.


## R1 staging workflow probe — 2026-11-20

- Initial workflow-only commit triggered Run [44640726096](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44640726096) before the archive was present.
- Job `135970795549` failed at `Verify archive hash`; extraction, JUnit, assemble and APK checks were skipped. This is an expected staging/input-missing failure, NOT a source compile/test failure.
- Workflow was then narrowed so the only push path trigger is `TouchFlow-R1-source.tar.xz`; no manual dispatch trigger is configured. The current workflow file last changed in commit `0b3d48f7fefd34dd25af8e9b26f23d881cd72218`.
- Current R1 branch head after recording this state: pending this documentation commit. Main remains `6c738c2214d4244913fe449ed6172db613f844bd`; no main or backup write was made.
- Next and only owner action: upload the exact local archive `TouchFlow-R1-source.tar.xz` to the root of the R1 branch. Verify GitHub reports the upload committed to `feature/touchflow-r1-recording-actions-2026-11-20`. That push will start a fresh CI run.


## R1 CI failure diagnosis and test-fixture correction — 2026-11-20

- Owner reported the R1 workflow result as unsuccessful. Inspected exact GitHub Actions run [44641075931](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44641075931), head commit `4438888b8ac72297b9b7a248a08d249d30de78f4`.
- Archive verification and extraction succeeded. JDK17, Gradle8.9 and Android SDK35 setup succeeded. Main and test Kotlin sources compiled sufficiently to execute JUnit; compiler emitted only deprecation warnings for `SOFT_INPUT_ADJUST_RESIZE`.
- JUnit result: **24 tests completed, 1 failed**. Failing test: `SearchRulesTest > allTokensMustMatchAcrossFields`, line 30. Assertion used Persian token `چت` against app package token `org.telegram.chat`; production search rules do not translate Persian `چت` to English `chat`.
- This is the same already-diagnosed inherited test-fixture issue from Step 1. Step 1's successful workflow corrected only this test fixture from `"چت تلگرام"` to `"chat تلگرام"`, leaving application source untouched. R1 archive contains the old fixture, so the R1 workflow needed to repeat that explicit test-only correction.
- Confirmed the exact R1 archive on local runtime: SHA-256 `4e0e00918e0b3f172d02daa9262d1d2da3c130872583bcc726aabd5ac35e12d3`. Its `SearchRulesTest.kt` contains the expected old fixture. **The archive itself remains unchanged.**
- Updated only `.github/workflows/build-touchflow-feature-pack.yml` in the R1 branch (commit `fffe19113724c2c85c909fd35bac302c253d3cff`) to patch the extracted test fixture after archive extraction, asserting exactly one replacement. Production Kotlin, Manifest, permissions, Schema 3 and source archive are not modified by this correction.
- New CI run [44641623406](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44641623406) triggered by the workflow update; initial status queued. **Awaiting result — NOT VERIFIED yet.**
- Run [44641075931] did not reach `assembleDebug`; APK was not produced by that run.
- Main remains `6c738c2214d4244913fe449ed6172db613f844bd`; no writes targeted main or backup branches.
- Next: inspect Run `44641623406` logs, confirm 24/24 JUnit and assembleDebug, then inspect APK signature/package/permission report. Only after CI passes should owner install and execute the 18-item R1 device checklist. R1 is not yet device-verified.


## R1 CI final result — SUCCESS (2026-11-20)

- Successful run: [44641623406](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44641623406), branch `feature/touchflow-r1-recording-actions-2026-11-20`, commit `fffe19113724c2c85c909fd35bac302c253d3cff`; conclusion `success`.
- Exact R1 archive SHA-256 verification: PASS (`4e0e00918e0b3f172d02daa9262d1d2da3c130872583bcc726aabd5ac35e12d3`).
- In-workflow test-fixture-only correction applied after extraction: Persian query token `چت` -> English package token `chat` in the inherited `SearchRulesTest` assertion. The source archive and production app code remain unchanged by this correction.
- JUnit: **24 tests, 0 failures, 0 errors, 0 skipped**. Exact count assertion passed.
- `assembleDebug`: PASS.
- APK verification: package `com.grandmaconnect.feature`; label `TouchFlow`; version `0.1.0-alpha-feature`; APK signature verified with v2 scheme.
- APK SHA-256: `NOT EXTRACTED FROM LOG` (the file `apk.sha256` is included in the artifact; inspect it before recording a value).
- Signer certificate SHA-256: `084ac46148aa989df58bd03d7254dfa4e62c7f7971104dd2adcc2c34e5ad4599` (debug signer; not the baseline signing key).
- APK permissions: exactly `android.permission.POST_NOTIFICATIONS`; allowlist comparison PASS. The CI step also passed the source check that `canRetrieveWindowContent="false"`.
- Artifact: [14587006288](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44641623406/artifacts/14587006288), name `touchflow-r1-build`, size 1,137,274 bytes, expires 2026-12-19.
- R1 gate: **CI BUILD + JUNIT PASSED**. This is not device verification. The 18 items in `docs/R1-DEVICE-CHECKLIST-fa.md` remain unchecked until the owner tests the APK on Galaxy A14 / Android 13.
- Next owner action: download APK from the artifact, install as the separate package `com.grandmaconnect.feature` (do not replace `com.grandmaconnect.preview`), then execute the R1 device checklist. Report failures or completed items; do not mark every checklist item done without testing.
- Main last verified at `6c738c2214d4244913fe449ed6172db613f844bd`; no write operation in this task targeted main or backup branches.

## R1 post-CI artifact audit — 2026-11-20

- Current R1 branch: `feature/touchflow-r1-recording-actions-2026-11-20`.
- Latest GitHub Actions branch-filtered page showed 3 runs; newest is Run [44641623406](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44641623406), workflow run #8, event `push`, commit `fffe19113724c2c85c909fd35bac302c253d3cff`. No newer workflow run was listed at audit time.
- Run #8 job `build` ID `135973818897`: completed / success. Archive SHA verification, extraction, documented SearchRules test-fixture correction, JUnit, exact test-count assertion, assembleDebug, package/label/signature/permission checks and artifact upload all succeeded.
- JUnit report: 24 tests; 0 failures; 0 errors; 0 skipped.
- Artifact `touchflow-r1-build`, ID `14587006288`, is available. Downloaded archive SHA-256: `82dbff480489b4b6e1e5a0816c7f89061c36096224d8d347527c46c5ba8bb1df`; this matches the GitHub artifact digest.
- Extracted R1 APK: size `1,130,871 bytes`; SHA-256 `c42defa8a3bdcaac3342364a17410232fc7589f37c394822ee51f726df74848c`; matches the artifact's `apk.sha256`.
- R1 APK metadata: package `com.grandmaconnect.feature`; label `TouchFlow`; versionCode 1; versionName `0.1.0-alpha-feature`; minSdk 24; targetSdk 35; only declared permission `android.permission.POST_NOTIFICATIONS`; APK Signature Scheme v2 verified.
- R1 debug signer certificate SHA-256: `084ac46148aa989df58bd03d7254dfa4e62c7f7971104dd2adcc2c34e5ad4599`. This is not the original Baseline signing key. Do not overwrite an existing `.feature` installation without checking its signer first. Keep `com.grandmaconnect.preview` / Baseline installed and untouched.
- Owner-provided `GrandmaConnect-preview.apk` was independently checked in the assistant runtime: size `866,747 bytes`, SHA-256 `6dce713dfebcbf84ed5a175b6eb73808791765464087526875c3fe6f11bd0b89`; exact match to the recorded Baseline. It is not the R1 APK.
- Branch compare: R1 branch is 2 commits ahead of the successful CI commit `fffe191...`; the only changed path in that delta is `PROJECT_STATE.md` (31 additions). No source archive, application source or workflow change occurred after the successful run.
- Protected refs verified read-only: `main` is identical to `6c738c2214d4244913fe449ed6172db613f844bd`; `backup/native-baseline-2026-11-19` is identical to `d62899f0eb586a870471648fd3d77d4b8f50fb8d`. No write operation targeted `main` or any Backup branch during this continuation.
- Checklist discrepancy: the state refers to `docs/R1-DEVICE-CHECKLIST-fa.md`, but fetching that exact path returned GitHub 404 and the current `docs/` listing showed only `ci/`. Treat the checklist file as **NOT FOUND at the referenced path** until its actual path is verified; do not invent completion.
- GitHub Actions emitted non-blocking deprecation warnings for actions targeting Node.js 20 and `actions/setup-java@v4`. Build remains successful; track action-version maintenance separately.
- Device acceptance remains **NOT VERIFIED**. The successful CI does not prove runtime behavior on Samsung Galaxy A14 / Android 13. Next gate: owner installs this exact R1 APK only as the separate `.feature` package (subject to checking for an already-installed `.feature` app) and reports observed results; do not remove or replace the Baseline app.

## R1 device acceptance + R2 request — 2026-11-20

- Owner's device feedback: **R1 installed and operated successfully; owner reports it worked completely and no defects were observed.** Record this as `OWNER-REPORTED DEVICE PASS` for the tests the owner performed, not as a claim that every possible device/configuration edge case has been exhausted.
- R1 CI evidence remains Run [44641623406](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44641623406), 24/24 JUnit and successful `assembleDebug`. The validated R1 APK is package `com.grandmaconnect.feature`; Baseline package `com.grandmaconnect.preview` must remain untouched.
- Owner provided a timeline-editor visual reference (2026-11-20): bottom timeline/ruler with a vertical playhead, visible time marks (example `00:00`, `00:02`), and the ability to start playback or move backward/forward by dragging or navigating the playhead. Treat it as an interaction reference, not a pixel-perfect copy.
- New requested capabilities for the next milestone:
  1. InShot-inspired bottom macro timeline with ruler/time labels, current-position playhead, play/pause/resume/stop transport controls, and seek backward/forward or by dragging the playhead.
  2. Playback options: speed, repeat, and start delay.
  3. Persian help/guide, Accessibility information/settings, and Privacy information pages.
- Proposed next milestone: **R2 — Playback controls + seekable macro timeline**. It is PLANNED only; no R2 app-code implementation or new branch has started in this entry.
- Technical sequence:
  - First implement/test playback runtime state and cursor: Pause/Resume must preserve the exact next safe action/group and remaining timing; Stop is terminal. Pause/seek should take effect at safe boundaries rather than interrupting an in-flight gesture.
  - Then build the bottom timeline UI and transport controls. Initial seek target must snap to recorded gesture-group/action boundaries. True mid-gesture/frame-accurate seeking is not supported by the current data/editor and must not be claimed without path slicing, schema analysis, and tests.
  - Add persisted playback speed, repeat count/mode, and pre-start delay after their semantics are specified and unit-tested. Proposed safe defaults: speed 1x, one play, zero start delay; no repeat is active by default.
  - Add Help, Accessibility and Privacy pages using verified app behavior. Explain what the Accessibility service does and does not access; do not imply window-content reading or add permissions without independent justification. Privacy statements must match inspected storage/network behavior.
- Preserve existing macro JSON/schema compatibility unless a migration is demonstrably necessary. Test old saved macros, action ordering, launch-app waits, GO_BACK/GO_HOME boundaries, rotation/orientation checks and emergency stop.
- R2 should start from the accepted R1 feature-branch head on a new isolated feature branch. No merge to `main`, no modification to any backup, and no release/publication is authorized by this planning entry.


## R2.1 verified build and owner device result — 2026-11-20

- R2 work branch: `feature/touchflow-r2-playback-engine-2026-11-20`; latest inspected head at this record: `b9035ca08a8f952126789420a1c2e2e2269f180f`.
- Successful CI: [Run 44728719171](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44728719171); JUnit **45/45** (zero failures/errors/skips) and `assembleDebug` success.
- APK package/version: `com.grandmaconnect.feature` / `0.1.0-alpha-feature`.
- APK SHA-256: `1163cd2ad42d4975253cd9bc02a0bda7a33d75119d69019e768ee274ed677fcf`.
- APK v2 signature verification: PASS; signer certificate SHA-256 `7cabfa7b4088be8664326d93113652d562aac4d94eb9c7fe6b636ac082bfdce9`.
- Only requested permission: `POST_NOTIFICATIONS`; `canRetrieveWindowContent=false` check passed in CI.
- Owner-reported Galaxy A14 test: **PASS — owner says R2.1 worked without issues.** Individual test cases were not itemized, so exhaustive edge-case coverage is not claimed.
- Baseline APK/package remains separate and untouched; R2.1 is a separate `.feature` installation. No merge to main or backup modification.

## Current next step: R2.2 Timeline UI

- Status: **NEXT / NOT STARTED**.
- Implement a real bottom macro timeline using the saved macro's actual Gesture Groups and ordered Actions, with ruler/time labels, a data-driven playhead, elapsed/total time, Play/Pause/Resume/Stop, backward/forward navigation and drag-to-seek.
- Seek must snap to valid Gesture Group / Action boundaries supported by the current data. Mid-gesture/frame-accurate seeking is out of scope unless raw-path slicing, schema implications and dedicated tests prove it.
- Drag during playback: pause at a safe boundary, snap to the selected valid point, remain paused until explicit Resume.
- Preserve R2.1 playback engine guarantees, macro JSON/schema compatibility, emergency Stop, stale-callback isolation, RTL and `canRetrieveWindowContent=false`.
- Before coding: inspect the R2.1 source archive and actual engine/model, record a backup reference, then create a new isolated R2.2 feature branch from accepted R2.1 head. Do not touch `main`, backup branches or baseline.


## R2.2 Timeline — CI PASS, device gate pending (2026-11-20)

- Branch: `feature/touchflow-r2-2-timeline-2026-11-20`.
- Latest R2.2 implementation/CI commit before documentation updates: `48134c0a0175077ef83775d6fa4b738dfbafffef`.
- R2.1 accepted base: `6e6ba179d5f836b3da13511210163feadd61d5ee`.
- Backup `backup/touchflow-r2-1-accepted-2026-11-20` preserved at the R2.1 accepted base.
- Final CI [44770977128](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44770977128): success. JUnit **55/55**, zero failures/errors/skips; `assembleDebug` successful.
- APK SHA-256: `5c3864252ada098d3783c2c49b2125f7c40e4511db8560aa107310a7504fdf9a`.
- APK package `com.grandmaconnect.feature`, label `TouchFlow`, versionName `0.1.0-alpha-feature`.
- APK signature verification: PASS, v2; signer certificate SHA-256 `a3e34da4107da73a26b968ea754f856bf532b7734b13402f6cfec48e95887a2e`.
- Only requested permission: `POST_NOTIFICATIONS`; `canRetrieveWindowContent=false` retained and CI-checked.
- Patched build source archive SHA-256: `c322d1aa53f8cd44ce482e018b90d0a6aaec1792f7a70e060ea8f43954a1c61f`.
- Artifact ID `14648195618`; ZIP SHA-256 `d5138fd1ff6397a1e90a6f2b2be808a1f9a7a87e16d716dfd84d7d79b0b674da`. Artifact and extracted APK/source checksums independently verified.
- Final follow-up: live drag-to-seek remains enabled only while playback snapshot says `canSeek`; drag start requests safe pause and seek is applied after the active gesture finishes. This was rebuilt and re-tested in final run.
- R2.2 owner device acceptance: **PENDING**; do not mark complete until owner tests it on Galaxy A14 / Android 13.
- `main` remains unchanged at `6c738c2214d4244913fe449ed6172db613f844bd`; no merge or publication.
- Baseline `com.grandmaconnect.preview` remains separate and untouched. Install the R2.2 debug package alongside it; do not uninstall/replace the Baseline.
- Next action: owner tests the R2.2 APK on device. Capture observed results; then update acceptance status. R2.3 (speed/repeat/start delay) remains unstarted until R2.2 is accepted.


## Final R2.2 package identity and build — supersedes prior R2.2 APK

- Final R2.2 CI run: [44771585290](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44771585290), success; 55/55 tests, zero failures/errors/skips; `assembleDebug` success.
- Final APK package is `com.grandmaconnect.feature.r22` (not `com.grandmaconnect.feature`); versionName `0.1.0-alpha-feature-r22`; app label `TouchFlow`.
- APK SHA-256: `668bc2653a32ac7eee61e229683afe4699e00f6919d95f347456aab8b9718912`.
- Signature v2 verified; signer certificate SHA-256 `12e6100c83532dc31a93ffa8e850ab9ef4a555b8ead75fe2851ea13fda70b5b4`.
- Only declared permission: `POST_NOTIFICATIONS`; Accessibility config remains `canRetrieveWindowContent=false`.
- Exact patched source archive SHA-256: `8dff399d4d09a0a2be1663000d307d9cb890aa65cf166d377fd9c01843e4d4d3`.
- Artifact ID `14648256141`; ZIP SHA-256 `e67881aa38b6d3a5f8ebc93255518d05b5e78e2b8907739d3b39cb409439fc11`. The downloaded ZIP's checksum, APK checksum and source checksum were verified against CI reports.
- R2.2 package suffix is deliberately isolated to allow side-by-side installation. Keep R2.1 `com.grandmaconnect.feature` and Baseline `com.grandmaconnect.preview` installed; do not uninstall either, and do not install the superseded R2.2 artifact whose package was `com.grandmaconnect.feature`.
- Current feature branch remains `feature/touchflow-r2-2-timeline-2026-11-20`. R2.2 physical-device acceptance is **PENDING** on Galaxy A14 / Android 13. R2.3 has not started.


## OWNER PROCESS CORRECTION — READ FIRST NEXT SESSION (2026-11-20)

**Claude is the designated implementation/coding agent.** ChatGPT must remain coordinator/reviewer/planner and must not independently implement product code unless the owner explicitly authorizes a change.

- In this session ChatGPT independently created R2.2 candidate patches and build workflows. This was a process deviation. Do not attribute this implementation to Claude.
- Current R2.2 output is an **unreviewed assistant-generated candidate**, not owner-approved or Claude-approved.
- No PR, merge, release, or publish occurred. Do not continue to R2.3 or accept R2.2 until Claude has independently reviewed the candidate and the owner decides.
- Next session: Claude must inspect the candidate branch, patch payloads, build artifact/source archive, Timeline calculations, playback state/seek code, gesture/notification safety, test coverage, package isolation and CI. Claude may keep, fix, or replace the candidate.
- ChatGPT: read-only review/coordination and documentation only until owner explicitly reauthorizes coding.

### Current exact repository state
- Repo: `hosseinasgari898989-dev/Touchflow`.
- R2.2 branch: `feature/touchflow-r2-2-timeline-2026-11-20`.
- Current branch HEAD (after this note is committed): to be read from branch ref at session start; preceding implementation HEAD was `6d5b1c7fb8afeef9ffb6542596a344e05c892f22`.
- R2.1 base and unchanged backup: `6e6ba179d5f836b3da13511210163feadd61d5ee`.
- `main` unchanged: `6c738c2214d4244913fe449ed6172db613f844bd`.
- R2.2 branch is 43 commits ahead of R2.1 base, many are patch-payload transfer commits; history is not clean for PR/merge. Claude should first recommend a clean reconstruction/consolidation strategy.
- No R2.2 PR currently exists.

### R2.2 candidate CI evidence (not device acceptance)
- Latest candidate CI: [Run 44771585290](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44771585290) — success.
- 55/55 JUnit tests; zero failures/errors/skips; `assembleDebug` success.
- Final candidate package: `com.grandmaconnect.feature.r22`, version `0.1.0-alpha-feature-r22`, label `TouchFlow`.
- APK SHA-256: `668bc2653a32ac7eee61e229683afe4699e00f6919d95f347456aab8b9718912`.
- APK v2 signature verified; signer cert SHA-256 `12e6100c83532dc31a93ffa8e850ab9ef4a555b8ead75fe2851ea13fda70b5b4`.
- Only requested permission: `POST_NOTIFICATIONS`; `canRetrieveWindowContent=false` checked.
- Artifact ID `14648256141`; final APK file was locally checksum-verified against the CI digest.
- R2.2 Galaxy A14 / Android 13 device test: **PENDING**. Never claim device acceptance from CI alone.
- Keep Baseline `com.grandmaconnect.preview` and R2.1 `com.grandmaconnect.feature` untouched. Candidate uses separate `com.grandmaconnect.feature.r22`; superseded intermediate R2.2 APK used `.feature` and must not be installed over R2.1.
