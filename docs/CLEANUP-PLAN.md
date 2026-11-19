# TouchFlow native cleanup plan

This plan is based on the exact build commit `36600aa02fba13430ba6a1e9e2efc09f665b7b67`, whose successful GitHub Actions output is byte-for-byte identical to the owner-provided APK. No source deletion is approved by this audit.

## Branch safety

- Canonical immutable source backup: `backup/touchflow-v1-exact-baseline-2026-11-19`
- Canonical working branch: `feature/touchflow-v1-cleanup-exact-baseline-2026-11-19`
- Both branches start at exact baseline source commit `36600aa02fba13430ba6a1e9e2efc09f665b7b67`.
- Earlier secondary branches based on `36b67597a86a84c093cc9c50ec2e32af6e4dbad8` are retained unchanged.
- Keep `main` and `backup/native-baseline-2026-11-19` unchanged.
- Make small changes through PRs. No merge or release without explicit review.

## File-by-file plan

### KEEP — no deletion

| File | Why it stays |
|---|---|
| `app/src/main/java/com/grandmaconnect/MainActivity.kt` | Main UI, recording workflow, macro selection, settings and playback controls |
| `app/src/main/java/com/grandmaconnect/TouchCanvasView.kt` | Captures touch sequences within the in-app canvas |
| `app/src/main/java/com/grandmaconnect/MacroModels.kt` | Macro data schema, validation, JSON serialization and persistence |
| `app/src/main/java/com/grandmaconnect/MacroAccessibilityService.kt` | Accessibility playback, callbacks, playback state and stop notification |
| `app/src/main/java/com/grandmaconnect/MacroSettings.kt` | Capture profiles, quality options, configurable duration and hard limits |
| `app/src/main/res/xml/accessibility_service_config.xml` | Declares gesture capability and current no-window-content privacy setting |
| `app/src/main/AndroidManifest.xml` | Declares app entry points, service, receiver and permission |
| `app/build.gradle.kts`, root Gradle files | Required Android/Kotlin build configuration |
| `app/src/main/res/values/styles.xml` | App theme resources |

No dead core module or safe source-file deletion has been established.

### CHANGE — branding only, preserving compatibility

| File | Proposed change | Must remain unchanged |
|---|---|---|
| `app/src/main/AndroidManifest.xml` | App label and Accessibility service label become TouchFlow | Component names, intent action, exported flags, BIND_ACCESSIBILITY_SERVICE, POST_NOTIFICATIONS |
| `app/src/main/res/values/strings.xml` | app_name and service description branding | Meaning of the privacy description |
| `MainActivity.kt` | Visible titles, dialogs and instructions say TouchFlow | Workflow logic and explicit user confirmation |
| `MacroAccessibilityService.kt` | Visible notification title and channel text say TouchFlow | Playback/stop logic, action ID and existing channel ID during first upgrade |
| `README-fa.md`, `TEST-CHECKLIST-fa.md` | Remove stale Grandma Connect/arena instructions and document TouchFlow | Existing test coverage and warnings |
| Root `README.md` | Keep repo/build instructions aligned with TouchFlow | Build triggers unless separately reviewed |

### COMPATIBILITY — do not rename in the first update

- Preserve applicationId `com.grandmaconnect.preview` for an in-place upgrade.
- Preserve namespace `com.grandmaconnect` initially; package relocation is not a branding requirement.
- Preserve JSON schema version 1 and current macro directory until a migration/export process is tested.
- Preserve SharedPreferences file/key names.
- Preserve receiver action `com.grandmaconnect.STOP_PLAYBACK`.
- Preserve the notification channel ID to avoid unexpected user notification behavior.
- Increment versionCode only after the signing key and update path are verified.
- The exact baseline build is known, but the private debug keystore was not in its artifacts. A later run used a different debug key. Do not promise in-place update until the original key is recovered or separately plan a migration.

### ADD — staged features

1. **Explicit macro backup/restore**
   - Export selected/all macros into a versioned archive with manifest and checksums.
   - Validate every imported macro before writing; avoid silent overwrite.
   - Use staging and atomic commit/rollback.
   - Preserve private-by-default storage; don't add cloud/network sync.
   - Test corrupted, duplicate, oversized, empty and older-schema archives.

2. **Visible storage/recovery errors**
   - Do not silently drop malformed macro files from the saved list.
   - Surface a recoverable warning and preserve the original file for user export/recovery.
   - Replace non-atomic fallback writes only after crash/recovery tests.

3. **Configurable recording stop**
   - Current choices are 45 seconds by default and 2/5/10 minutes in extended mode.
   - Add a user-controlled time-limit mode only with bounded resource, point-count and platform gesture limits.
   - Never describe the mode as truly unlimited; stop safely on memory/storage/resource thresholds.
   - Existing 10-minute cap can be relaxed only after a stress-test matrix is defined.

4. **Global input recording feasibility**
   - Current TouchCanvasView records only inside the app.
   - Prototype API 33 TouchInteractionController on the Galaxy A14, with explicit user opt-in and an immediate disable path.
   - Measure whether gestures reach the target app unchanged; because controller state transitions stop event delivery during delegated/touch-exploring interactions, do not claim transparent capture until tests prove it.
   - Do not request window-content retrieval just to capture touch coordinates.

5. **Real timeline and keyframes**
   - Build editor actions on actual macro schema/events, not the WebView branch's mock data.
   - Persist edits, validate, reopen and replay saved macros before presenting the editor as functional.
   - Keep unsupported controls hidden/disabled.

## Explicit REMOVE list

- **No app source files are approved for deletion now.**
- Do not delete the legacy source ZIP, .source-v2 chunks, experimental branches, or previous backup kits.
- After source is imported and verified into a normal project layout, redundant archive/chunk storage can be considered for removal in a separate PR, while retaining a tagged release/source archive.
- Stale README references can be replaced, but no source behavior is to be removed as part of branding cleanup.

## Required validation before any APK release

- Clean build from exact baseline source commit.
- Verify package ID, versionCode/name, min/target SDK, debuggable state, permissions and service metadata.
- Verify APK signature and compare certificate/lineage with the baseline.
- Round-trip macro export/import and reopen old schema-1 macros.
- Target-device install, record, stop, save, reopen and playback tests.
- If package/signer migration is necessary, test export, uninstall/reinstall and restore on a spare macro dataset before touching the grandmother's installed app.
