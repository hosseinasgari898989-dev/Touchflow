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
- Cryptographic signer verification: **NOT VERIFIED**
- Package ID, embedded version code/name, application label, min SDK, target SDK, and signer certificate: **NOT VERIFIED**.

The original upload remains available at `/mnt/data/GrandmaConnect-preview.apk`. The working copy was created and its SHA-256 was rechecked. The binary has not yet been committed to GitHub or attached to a GitHub Release.

The name `v1.0.0-baseline` is an internal project designation for the first supplied APK; it does not assert the APK's embedded version or release readiness.

## Existing source archive

The default branch contains `GrandmaConnectNative-source.zip` (24,642 bytes; Git blob SHA `281e58f37b7d336682da95e6df790ccdf6a8ac8e`). This is a Git blob ID, not a SHA-256 file checksum.

The archive is only a candidate source input. It has not yet been extracted and compared with the owner-provided APK. Do not remove or replace it until it has been inspected, built, and compared.

## Requirements before a verified v1.0.0 release

1. Extract and inspect the native source project.
2. Verify the APK's package ID, label, embedded version values, SDK levels, and signer certificate.
3. Build an APK from the selected source on a clean runner.
4. Compare its package identity and behavior with the baseline; do not assume byte-for-byte reproducibility.
5. Run installation and regression checks on the target device.
6. Publish a new immutable, versioned APK with SHA-256, source commit, build run, and release notes.

Until then this is the **initial baseline artifact**, not a verified production release.
