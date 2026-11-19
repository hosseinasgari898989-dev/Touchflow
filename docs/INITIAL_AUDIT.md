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

## Source lineage identified

High-confidence matching source archive:
- Workflow run: [44399759542](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44399759542)
- Branch: `feature/expanded-capture-settings-2026-11-19`
- Commit: `36b67597a86a84c093cc9c50ec2e32af6e4dbad8`
- Archive: `GrandmaConnectNative-source-v2.tar.xz`
- Archive SHA-256: `e77c6b383251cd584b60cd6f4ae6b0ab445202970758d2c851e8bdc359b97a98`

Comparison with that workflow's APK output:
- Owner APK: 866,747 bytes, SHA-256 `6dce713dfebcbf84ed5a175b6eb73808791765464087526875c3fe6f11bd0b89`
- CI output: 866,755 bytes, SHA-256 `46b48ac853739a44d8b1ff1ec7da341a984cb6fa91b4a0c541f075086f5a5770`
- AndroidManifest.xml, all three DEX files, Kotlin builtins and accessibility_service_config.xml: identical.
- Only differing ZIP entry: resources.arsc (1284 vs 1292 bytes).
- APK total-size difference: 8 bytes.

Conclusion: the expanded-capture source is a high-confidence match for the owner's baseline compiled code and manifest. Exact whole-APK equivalence is not claimed.

## Signing blocker

The CI APK built from the matched source uses a different debug certificate:
`37:12:86:D4:6F:87:4E:E1:BC:BC:83:CF:77:09:02:19:06:90:EE:C2:E8:85:2E:E1:E8:5C:32:3A:8B:52:C0:75`.

The baseline certificate is `7E:AE:68:77:3E:0E:AF:E0:B1:FB:A9:32:01:CE:67:DC:2B:6D:FB:21:57:FC:81:54:73:23:95:A9:C7:06:1D:08`. The matching private keystore is not present in the inspected repo/source/artifacts. Do not assume a new CI APK can update an existing install.

Android's update requirements: same application ID, same signing certificate or valid signing lineage, and equal-or-higher versionCode. References: [Android app updates](https://developer.android.com/google/play/app-updates), [Android app signing](https://developer.android.com/studio/publish/app-signing).

## Existing source candidates

### Main source archive

- Root file: `GrandmaConnectNative-source.zip`
- It is the legacy base and not the source snapshot most closely matching the owner APK.
- Its Gradle configuration uses namespace/applicationId `com.grandmaconnect`, base versionName `0.1.0-alpha`, minSdk 24, targetSdk 35.

### Expanded capture settings source — selected baseline

- Adds `MacroSettings.kt` and modifies `MainActivity.kt`, `MacroModels.kt`, `MacroAccessibilityService.kt` and `TouchCanvasView.kt`.
- Provides standard capture limits plus an extended mode for 2, 5 or 10 minutes.
- A hard 10-minute ceiling remains; the current UI does not mean unlimited capture.
- This is the chosen source base for the next cleanup branch.

### TouchFlow Simple and WebView integration prototypes

- Simple branch adds related capture settings and some macro actions; its APK package identity and compiled code do not match the owner baseline.
- WebView integration branch contains a UI prototype. Its timeline/keyframe track data is marked as mock data; keyframe persistence/easing dispatch and backup import/export are unsupported in that slice.
- Do not merge either branch wholesale into the selected baseline.

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

- The baseline APK and an updated backup kit are preserved.
- High-confidence source lineage is identified.
- A source backup branch and a dedicated cleanup branch have been created from the matching source commit.
- No application code or APK has been changed or published.
- The original signing key remains the principal blocker for in-place updates.
