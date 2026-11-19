# TouchFlow v1 baseline

**Internal designation:** `TouchFlow-v1.0.0-baseline`  
**Embedded Android version:** `0.1.0-alpha-preview` (versionCode 1)  
**Status:** preserved owner APK; the exact successful CI build and source archive have now been identified.

## Owner-provided APK

- Original filename: `GrandmaConnect-preview.apk`
- Preserved filename: `TouchFlow-v1.0.0-baseline.apk`
- Size: 866,747 bytes
- SHA-256: `6dce713dfebcbf84ed5a175b6eb73808791765464087526875c3fe6f11bd0b89`
- ZIP integrity: PASS
- Package/application ID: `com.grandmaconnect.preview`
- Version code: `1`
- Version name: `0.1.0-alpha-preview`
- minSdk: 24
- targetSdk: 35
- App label: `Grandma Connect`
- `debuggable=true`
- `allowBackup=false`
- Declared permission: `POST_NOTIFICATIONS`
- Accessibility config: `canPerformGestures=true`, `canRetrieveWindowContent=false`
- APK v2 signing block: present
- Extracted certificate subject: `CN=Android Debug, O=Android, C=US`
- Certificate SHA-256: `7E:AE:68:77:3E:0E:AF:E0:B1:FB:A9:32:01:CE:67:DC:2B:6D:FB:21:57:FC:81:54:73:23:95:A9:C7:06:1D:08`
- Full `apksigner verify` cryptographic validation: NOT RUN in this environment.
- Matching private key/keystore: NOT FOUND.

The designation `v1.0.0-baseline` is a project label only; it does not replace the embedded app version shown above.

## Exact source and build provenance

The owner APK is byte-for-byte identical to the successful GitHub Actions build artifact from [run 44399521736](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44399521736):

- Workflow: `Build Grandma Connect APK`
- Branch: `feature/expanded-capture-settings-2026-11-19`
- Exact source commit: `36600aa02fba13430ba6a1e9e2efc09f665b7b67`
- Result: success
- APK size and SHA-256 from the run: 866,747 bytes; `6dce713dfebcbf84ed5a175b6eb73808791765464087526875c3fe6f11bd0b89`
- Source artifact: `GrandmaConnectNative-source-v2.tar.xz`
- Source archive SHA-256: `e77c6b383251cd584b60cd6f4ae6b0ab445202970758d2c851e8bdc359b97a98`
- The run's signing certificate fingerprint is the same as the owner APK.

This is an exact source-build provenance match, not merely a similar build. The archive from later run 44399759542 has the same source archive hash/content, but its output APK used a different debug certificate and differed in `resources.arsc` by 8 bytes. Do not assume later ephemeral CI builds preserve the original signing identity.

## Update/signing blocker

The baseline signing certificate is known, and the exact build run has been found. However, the private debug keystore was not included in the source or APK artifacts and was not found in the inspected repository tree.

Android accepts an in-place app update only when the application ID matches and the signing certificate matches (or an accepted signing lineage exists); the version code must also be equal or higher. See [Android app updates](https://developer.android.com/google/play/app-updates) and [Android app signing](https://developer.android.com/studio/publish/app-signing).

Therefore:
- Keep package/application ID `com.grandmaconnect.preview` for an upgrade path.
- Do not publish a replacement APK from a new ephemeral debug key.
- Recover the original private keystore/key before claiming an in-place update is possible.
- If the original key cannot be recovered, any new package ID is a separate installation; implement and verify macro export/import before moving user data.

## Baseline behavior and known limits

- The recorder currently captures touch events only inside the app's own `TouchCanvasView`; it is not yet a global recorder for other applications.
- Playback is performed through `AccessibilityService.dispatchGesture`.
- Macro files are JSON in app-private storage. Android backup is disabled, and there is no user-facing export/import flow yet.
- The accessibility service declares that it can perform gestures but cannot retrieve window content. Preserve this privacy boundary unless a separately reviewed feature genuinely requires a change.
- The current extended-recording mode still has a 10-minute app-level hard ceiling.

## Release readiness

This is a preserved baseline, not a production-signed release. Before publishing an update:
1. Recover and validate the original signing identity, or plan an explicit separate-install migration.
2. Preserve the app ID for direct updates and increment versionCode.
3. Add macro export/import and verify round-trip recovery before any package/data migration.
4. Build from the exact selected source, inspect the manifest/signature, and test on the target phone.
5. Publish each APK as an immutable versioned artifact with checksum, source commit, build run, and release notes.
