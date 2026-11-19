# TouchFlow

TouchFlow is an Android application for recording and replaying touch interactions for personal accessibility workflows and controlled UI testing.

## Exact v1 baseline

The first owner-provided APK is preserved as `TouchFlow-v1.0.0-baseline.apk`. Its embedded version is `0.1.0-alpha-preview`; v1.0.0-baseline is an internal project label. The APK is byte-for-byte identical to the successful GitHub Actions artifact from run [44399521736](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44399521736), at source commit `36600aa02fba13430ba6a1e9e2efc09f665b7b67`. See [docs/BASELINE.md](docs/BASELINE.md).

## Important update limitation

The baseline app ID is `com.grandmaconnect.preview`. The original signing certificate is identified, and the exact build artifact used that certificate. However, the private debug keystore was not included in the run artifacts or source tree. Later CI runs generated a different debug certificate. A direct in-place update is blocked until the original signing key is recovered or an explicit separate-install/data-migration plan is completed. Do not install a new build over the existing app until this is resolved.

## Current implementation limits

- Recording captures touches only inside the app's own canvas; global recording across other apps is not implemented.
- Playback uses Android AccessibilityService gesture dispatch.
- Macros are kept in app-private JSON files; there is no user-facing export/import yet.
- The Accessibility service does not request access to other apps' window content.
- The extended recording feature remains subject to a 10-minute app-level hard limit.
- Timeline/keyframe WebView work remains a prototype and is not part of the selected baseline source.

## Development and release rules

- Keep the baseline APK and exact source commit immutable.
- Use timestamped backup branches and focused pull requests.
- Preserve package/app identity and signing continuity for upgrades.
- Export/import and restore-test macro data before schema or package migration.
- Publish every APK as a new immutable version with SHA-256, source commit, workflow run and test evidence.

See [docs/RELEASE_POLICY.md](docs/RELEASE_POLICY.md) and [docs/CLEANUP-PLAN.md](docs/CLEANUP-PLAN.md).
