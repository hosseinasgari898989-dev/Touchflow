# Initial technical audit — 2026-11-19

## Scope

Read-only inspection of the owner-provided APK, the default-branch source archive, and three successful GitHub Actions build outputs. No Android source, manifest, Gradle build file, permission, or workflow was modified in this audit.

## Owner baseline

- File: `GrandmaConnect-preview.apk`
- Size: 866,747 bytes
- SHA-256: `6dce713dfebcbf84ed5a175b6eb73808791765464087526875c3fe6f11bd0b89`
- ZIP integrity: PASS
- APK signing block: present
- Signer certificate / cryptographic verification / package ID / embedded version / SDK metadata: NOT VERIFIED

The file is preserved in the current work session as `/mnt/data/TouchFlow-v1.0.0-baseline.apk`. The name v1.0.0-baseline is a project label only.

## Build-to-baseline comparisons

The baseline APK did not byte-match any of the following successful CI outputs:

| Workflow run | Branch | Result | APK size | APK SHA-256 | Baseline match |
|---|---|---:|---:|---|---|
| [44386409608](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44386409608) | main | success | 857,251 | `269003181e111024505ae34eb285e141e5364316a7f43d955bed013fba286c8f` | NO |
| [44525646233](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44525646233) | feature/touchflow-simple-runner-2026-11-19 | success | 882,575 | `58510fba7ec94ffb218597b2f813092f1a956792bc02167bdad7803511ce64d4` | NO |
| [44432787584](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44432787584) | feature/touchflow-webview-integration-20261119 | success | 928,610 | `26d7f09c403dfcd2f71b700ced611c925ce71dffd95ace3c214501c2fe8c2cb8` | NO |

A successful build confirms compilation and the workflow's configured checks, not equivalence with the supplied APK or real-device behavior.

## Source snapshots reviewed

### main source archive

- `GrandmaConnectNative-source.zip` is in the root of main (24,642 bytes; Git blob ID `281e58f37b7d336682da95e6df790ccdf6a8ac8e`).
- Successful extraction snapshot: run 44397222288, artifact `grandma-connect-native-source-snapshot`.
- It contains the legacy app name `Grandma Connect`, namespace/applicationId `com.grandmaconnect`, versionName `0.1.0-alpha`, minSdk 24 and targetSdk 35.
- The source archive is a candidate only; the build output does not match the owner APK.

### Simple runner branch

- Successful build: run 44525646233 at commit `f479a3b10d7639ae1207915f3d9f2efbfc6cbcdc`.
- It contains native `MacroSettings`, configurable capture quality and an extended-capacity switch.
- Its configured extended durations are 2, 5 and 10 minutes. A 10-minute hard ceiling remains; the switch does not remove all safety/validation limits.
- Preview identity is checked by its workflow as `com.grandmaconnect.simple` with label `TouchFlow`.
- This is a successful CI build, not evidence of physical-device regression testing.

### WebView integration branch

- Successful build: run 44432787584 at commit `5bd3a7823d8da813f1a64c5be6d4f2fb6c4810bf`.
- It adds bundled offline HTML/CSS/JS, a narrow native bridge, macro-library metadata, and a UI prototype for gesture/timeline/keyframe tools.
- The editor source explicitly labels generated track data as mock data.
- The bridge contract explicitly marks editor save, keyframe persistence/easing dispatch, backup import/export, and HTML recording control as unsupported in this slice.
- The branch's own status file says browser rendering and physical-device behavior remain unverified.
- Therefore the visual editor must not be represented as a working native keyframe editor yet.

## Cleanup decisions

1. Do not delete or rename the legacy source archive yet.
2. Do not combine the experimental branches wholesale.
3. Preserve the supplied APK as an immutable baseline; do not patch the binary directly.
4. Before selecting the source of truth, inspect the baseline APK's package, embedded version, signer, and manifest using Android SDK inspection tools, then map the candidate source/build identity.
5. For the next source PR, publish an explicit add/change/remove list with call-site, manifest, resource, Gradle, and test impact.
6. Keep UI prototype controls visibly unavailable until backed by native persistence and tested dispatch.
7. Every future APK update must be a new immutable artifact with SHA-256, source commit, build run, and release notes.

## Current outcome

The project has a preserved baseline candidate, three separately archived source candidates, and a draft documentation-only foundation. No application code has been changed or deleted. No PR has been merged. No new APK release has been published.
