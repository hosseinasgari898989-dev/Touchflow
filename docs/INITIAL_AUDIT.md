# Initial technical audit — 2026-11-19

## Scope

Read-only inspection of the owner APK, the source archive snapshots and successful CI APK outputs. No Android source, manifest, Gradle configuration, permission, or workflow was modified during the audit.

## Owner APK metadata

- File: `GrandmaConnect-preview.apk`
- Size: 866,747 bytes
- SHA-256: `6dce713dfebcbf84ed5a175b6eb73808791765464087526875c3fe6f11bd0b89`
- ZIP integrity: PASS
- Application ID: `com.grandmaconnect.preview`
- versionCode: 1
- versionName: `0.1.0-alpha-preview`
- minSdk / targetSdk: 24 / 35
- app label: `Grandma Connect`
- debuggable: true
- allowBackup: false
- declared permission: `POST_NOTIFICATIONS`
- Accessibility: gestures allowed; window-content retrieval disabled
- v2 APK signing block: present
- Baseline certificate SHA-256 fingerprint: `7E:AE:68:77:3E:0E:AF:E0:B1:FB:A9:32:01:CE:67:DC:2B:6D:FB:21:57:FC:81:54:73:23:95:A9:C7:06:1D:08`
- Full apksigner verification: NOT RUN
- Private signing key: NOT FOUND

## Exact source and APK match

The exact source/build is [GitHub Actions run 44399521736](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44399521736):

- Branch: `feature/expanded-capture-settings-2026-11-19`
- Commit: `36600aa02fba13430ba6a1e9e2efc09f665b7b67`
- Run result: success
- Build output: `app-debug.apk`
- Owner APK and build output have the same size (866,747 bytes) and the same SHA-256:
  `6dce713dfebcbf84ed5a175b6eb73808791765464087526875c3fe6f11bd0b89`
- The exact source artifact is `GrandmaConnectNative-source-v2.tar.xz`, SHA-256:
  `e77c6b383251cd584b60cd6f4ae6b0ab445202970758d2c851e8bdc359b97a98`
- The signing certificate fingerprint extracted from the exact build output matches the owner APK.

Therefore the source archive and run 44399521736 are the exact known provenance of the owner APK.

### Later CI behavior

Run [44399759542](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44399759542) used the same source archive hash and compiled DEX/manifest, but its APK output differed:
- It was 866,755 bytes (8 bytes larger).
- Only `resources.arsc` differed from the baseline; manifest, all three DEX files, Kotlin builtins and Accessibility config were identical.
- Its debug certificate fingerprint was `37:12:86:D4:6F:87:4E:E1:BC:BC:83:CF:77:09:02:19:06:90:EE:C2:E8:85:2E:E1:E8:5C:32:3A:8B:52:C0:75`, which differs from the baseline.

This proves the workflow can generate a different debug signing key on a later run. The original private key is not present in the source artifact, build artifact or inspected source tree.

## Signing blocker

For an in-place Android update, the application ID must match and the signing certificate must match (or a valid signing lineage must exist), and versionCode must be equal or higher. References: [Android app updates](https://developer.android.com/google/play/app-updates), [Android app signing](https://developer.android.com/studio/publish/app-signing).

The original certificate fingerprint is known, but its private key is NOT FOUND. Keep `com.grandmaconnect.preview` unchanged for a possible update, but do not publish a new CI APK as an update unless the original signing key is recovered. Otherwise use a separate-install migration after adding and testing macro export/import.

## Selected source branch and backup

The exact build commit is now the canonical source starting point:
- Immutable backup branch: `backup/touchflow-v1-exact-baseline-2026-11-19`
- Working branch: `feature/touchflow-v1-cleanup-exact-baseline-2026-11-19`
- Both start from `36600aa02fba13430ba6a1e9e2efc09f665b7b67`.

Earlier branches made from commit `36b67597a86a84c093cc9c50ec2e32af6e4dbad8` are retained unchanged as secondary rollback references. They are not the canonical exact-build starting branch.

## Functional audit

| Area | Current baseline state | Cleanup/upgrade implication |
|---|---|---|
| Recording input | Captures only inside app's TouchCanvasView | Global capture is not implemented; requires a separate platform-feasibility prototype |
| Playback | AccessibilityService dispatchGesture | Preserve explicit user confirmation and stop affordance |
| Multi-touch | Groups concurrent pointers up to Android's declared limit | Verify on actual target devices |
| Storage | JSON files in app-private storage | Add export/import and recovery before schema/package changes |
| System backup | allowBackup=false | Keep private by default; implement explicit user-controlled backup |
| Accessibility privacy | canRetrieveWindowContent=false | Preserve; no need to read other apps' content for the current playback path |
| Extended duration | 2/5/10-minute options with 10-minute hard cap | Design configurable stop behavior with independent resource/platform safety limits |
| Timeline/keyframes | Not implemented in native macro model | Do not expose prototype controls as working features |

## Android global-touch feasibility note

The target Samsung Galaxy A14 is reported as Android 13 (API 33). Android's `TouchInteractionController` is available from API 33, but it requires `FLAG_REQUEST_TOUCH_EXPLORATION_MODE` and uses a touch-interaction state machine. Android documents that once the service requests delegation or touch exploration, it stops receiving motion events for the remainder of that interaction. This means a passive, transparent recorder that sees every raw event while all input continues unchanged is not established by the current design. A device experiment must test pass-through behavior and must be disabled by default until proven.

The separate `AccessibilityService.onMotionEvent` / `setMotionEventSources` API was added in API 34, so it is not available on the Android 13 target. References:
- [TouchInteractionController (API 33)](https://developer.android.com/reference/android/accessibilityservice/TouchInteractionController)
- [AccessibilityService.onMotionEvent (API 34)](https://developer.android.com/reference/android/accessibilityservice/AccessibilityService#onMotionEvent(android.view.MotionEvent))

## File cleanup assessment

No core application source file is safe to delete based on this audit alone. The five Kotlin classes have distinct roles:
- `MainActivity.kt`: app UI and macro workflow
- `TouchCanvasView.kt`: touch capture within the app's own canvas
- `MacroModels.kt`: schema, validation, serialization and file persistence
- `MacroAccessibilityService.kt`: gesture playback and stop notification
- `MacroSettings.kt`: configurable capture profile and hard limits

The first cleanup should be targeted changes, not deletion of these core modules.

## Current outcome

- The owner APK has exact source/build provenance (run 44399521736, commit `36600aa`).
- Exact baseline APK and source artifacts are preserved.
- Baseline and later-run signing certificates differ; the original private key is not found.
- The canonical source backup and cleanup branches are based on the exact build commit.
- No application code or APK has been changed or published.
