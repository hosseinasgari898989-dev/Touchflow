# TouchFlow v1 baseline

**Internal designation:** `TouchFlow-v1.0.0-baseline`  
**Embedded Android version:** `0.1.0-alpha-preview` (versionCode 1)  
**Status:** preserved owner-provided baseline; its source lineage is now identified with high confidence, but its signing key is not available yet.

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

## Source lineage — high-confidence match

The candidate native source is the archive produced by successful workflow run [44399759542](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44399759542):

- Source branch: `feature/expanded-capture-settings-2026-11-19`
- Source commit: `36b67597a86a84c093cc9c50ec2e32af6e4dbad8`
- Source archive: `GrandmaConnectNative-source-v2.tar.xz`
- Source archive SHA-256: `e77c6b383251cd584b60cd6f4ae6b0ab445202970758d2c851e8bdc359b97a98`

Its successful CI APK is 866,755 bytes, SHA-256 `46b48ac853739a44d8b1ff1ec7da341a984cb6fa91b4a0c541f075086f5a5770`. The APK entry comparison shows:

- AndroidManifest.xml: identical
- classes.dex, classes2.dex, classes3.dex: identical
- Kotlin builtins and accessibility_service_config.xml: identical
- resources.arsc: differs by 8 bytes (baseline 1,284 bytes; CI build 1,292 bytes)
- Overall APK size: differs by 8 bytes

This is a high-confidence source-to-baseline match at the compiled-code and manifest level. It is not a byte-for-byte match, and the reason for the 8-byte resource-table difference is not yet established.

## Update/signing blocker

The corresponding CI APK has a different debug certificate fingerprint:
`37:12:86:D4:6F:87:4E:E1:BC:BC:83:CF:77:09:02:19:06:90:EE:C2:E8:85:2E:E1:E8:5C:32:3A:8B:52:C0:75`.

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
4. Build from the selected source, inspect the manifest/signature, and test on the target phone.
5. Publish each APK as an immutable versioned artifact with checksum, source commit, build run, and release notes.
