# Initial APK baseline

**Project designation:** `TouchFlow v1.0.0-baseline`  
**Status:** first owner-provided reference APK; not yet verified as a reproducible or signed release.

## Owner-provided artifact

- Original filename: `GrandmaConnect-preview.apk`
- Preserved copy in this work session: `/mnt/data/TouchFlow-v1.0.0-baseline.apk`
- Size: `866,747 bytes`
- SHA-256: `6dce713dfebcbf84ed5a175b6eb73808791765464087526875c3fe6f11bd0b89`
- ZIP integrity test: passed (`unzip -t`)
- APK Signing Block: present
- Cryptographic signer verification, package ID, embedded version code/name, application label, min SDK, target SDK, and signer certificate: **NOT VERIFIED**.

The original upload remains available at `/mnt/data/GrandmaConnect-preview.apk`. The binary has not yet been committed to GitHub or attached to a GitHub Release. A backup kit is available in the current work session.

The name `v1.0.0-baseline` is an internal project designation for the first supplied APK; it does not assert the APK's embedded Android version or release readiness.

## Source relationship

The default branch contains `GrandmaConnectNative-source.zip` (24,642 bytes; Git blob SHA `281e58f37b7d336682da95e6df790ccdf6a8ac8e`). This is a Git blob ID, not a SHA-256 checksum.

Three successful CI APK outputs were compared with the supplied file. None matched byte-for-byte:
- main run 44386409608: 857,251 bytes, SHA-256 `269003181e111024505ae34eb285e141e5364316a7f43d955bed013fba286c8f`
- TouchFlow Simple run 44525646233: 882,575 bytes, SHA-256 `58510fba7ec94ffb218597b2f813092f1a956792bc02167bdad7803511ce64d4`
- TouchFlow WebView Integration run 44432787584: 928,610 bytes, SHA-256 `26d7f09c403dfcd2f71b700ced611c925ce71dffd95ace3c214501c2fe8c2cb8`

Therefore the source archive that produced the owner-provided APK is **NOT IDENTIFIED**. See [docs/INITIAL_AUDIT.md](INITIAL_AUDIT.md).

## Requirements before a verified v1.0.0 release

1. Inspect the supplied APK manifest and signer with Android SDK tools.
2. Select and inspect the matching native source project.
3. Build from a clean runner and verify package ID, app label, embedded version, SDK levels, and signing details.
4. Compare key behavior with the baseline; byte-for-byte reproducibility is not assumed.
5. Run installation and regression checks on the target device.
6. Publish a new immutable, versioned APK with SHA-256, source commit, build run, and release notes.

Until then this is the **initial baseline artifact**, not a verified production release.
