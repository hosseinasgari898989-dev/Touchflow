# TouchFlow — Grandma Connect Android

TouchFlow is the current project/repository name. The preserved Android app baseline still identifies itself as **Grandma Connect** and uses the application ID `com.grandmaconnect.preview`.

The app records touch interactions on its own recording canvas and replays saved macros through an Android `AccessibilityService`. It is intended for personal accessibility workflows and controlled UI testing.

## Repository contents

- `GrandmaConnectNative-source.zip` — the Android native source archive used by the build workflow.
- `.github/workflows/build-android.yml` — the GitHub Actions workflow that extracts the archive, builds the Android debug APK, and uploads it as an artifact.

The workflow currently runs on a push to `main` only when `GrandmaConnectNative-source.zip` changes. Editing this README does not trigger an APK build.

## Build workflow

The workflow is named **Build Grandma Connect APK**. It:

1. Extracts `GrandmaConnectNative-source.zip` into the repository workspace.
2. Sets up JDK 17, Gradle 8.9, and Android SDK / Build Tools 35.
3. Runs `gradle --no-daemon --stacktrace -p GrandmaConnectNative assembleDebug`.
4. Uploads `app-debug.apk` as the artifact `grandma-connect-debug-apk`.

The artifact is retained by GitHub Actions for 30 days. This workflow creates a debug/testing APK; it does not publish a production release.

## Reference APK baseline

The owner-provided reference file `GrandmaConnect-preview.apk` was inspected on 2026-11-19:

- Size: 866,747 bytes
- SHA-256: `6dce713dfebcbf84ed5a175b6eb73808791765464087526875c3fe6f11bd0b89`
- Application ID: `com.grandmaconnect.preview`
- Version code: `1`
- Version name: `0.1.0-alpha-preview`
- Minimum SDK / target SDK: 24 / 35
- Android app label: `Grandma Connect`
- `debuggable=true`; `allowBackup=false`

This APK is byte-for-byte identical to the successful build artifact from [GitHub Actions run 44399521736](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44399521736), produced from source commit `36600aa02fba13430ba6a1e9e2efc09f665b7b67`.

## Current implementation and known limits

- Recording captures touches inside the app's own `TouchCanvasView`; global touch recording across other apps is not implemented.
- Playback uses `AccessibilityService.dispatchGesture`.
- The accessibility service can perform gestures but does not request access to other apps' window content.
- Macros are stored as JSON in app-private storage.
- There is no user-facing macro export/import or restore flow yet.
- The extended recording mode has a 10-minute app-level hard limit.
- Timeline/keyframe editing is not implemented in the selected native baseline; the separate WebView work is only a prototype and should not be treated as a working editor.

## Update and data-safety warning

The reference APK's signing certificate is known, but its original private debug keystore was **NOT FOUND** in the inspected source/build artifacts. A later CI build from the same source archive used a different debug certificate.

Do not assume that a newly generated APK can update the installed reference app in place. Before attempting an update, verify that the application ID and signing identity match. If the original signing key cannot be recovered, plan a separate installation and implement/test macro export and restore before uninstalling the existing app or changing its package/data identity.

## Development and release rules

- Keep the reference APK and its checksum unchanged.
- Make focused changes on separate branches and review the complete diff before merging.
- Do not remove core Kotlin modules, change storage formats, or rename package identifiers without dependency and migration checks.
- Test recording, stopping, saving, reopening, and playback on the target device.
- Treat each generated APK as a test artifact until its package identity, version, signing certificate, and device behavior have been verified.
- Do not describe a feature as complete based only on its presence in the UI.
