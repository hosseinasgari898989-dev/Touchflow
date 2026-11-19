# Initial APK baseline

**Status:** preserved reference candidate; not yet confirmed as a reproducible release.

## Owner-provided artifact

- Original filename: `GrandmaConnect-preview.apk`
- Working copy name: `TouchFlow-v1-baseline.apk`
- Size: `866,747 bytes`
- SHA-256: `6dce713dfebcbf84ed5a175b6eb73808791765464087526875c3fe6f11bd0b89`
- Container/archive integrity check: passed (`unzip -t`)
- APK Signing Block: detected by the file inspection utility
- Cryptographic signer verification: **NOT VERIFIED**
- Android package ID, version code, version name, application label, min SDK, target SDK, and signer certificate: **NOT FOUND / NOT VERIFIED** in the current inspection environment.

The local working copy is at `/mnt/data/TouchFlow-v1-baseline.apk` in the current work session. The binary has **not** been uploaded to this GitHub branch or attached to a GitHub Release yet.

## Existing source archive

The default branch currently contains `GrandmaConnectNative-source.zip` (24,642 bytes; Git blob SHA `281e58f37b7d336682da95e6df790ccdf6a8ac8e`). This is a Git blob identifier, not a SHA-256 file checksum.

The archive is a candidate source input only. Its contents have not yet been compared with the APK, and no claim is made that it produced this exact binary. Do not delete or replace it until it has been extracted, inspected, built, and compared against the baseline's package identity and behavior.

## Conditions before calling this a published v1.0.0

1. Extract and inspect the native source project.
2. Read the binary manifest and verify package ID, app label, version values, SDK levels, and signer details.
3. Build a clean APK from the candidate source.
4. Compare the rebuilt APK's identity and key behavior with the baseline; a byte-for-byte match is not assumed because build outputs can be non-reproducible.
5. Run installation and regression checks on the target device.
6. Store the APK as an immutable, versioned release asset with SHA-256 and source commit/run references.

Until these checks pass, this is the **initial baseline artifact**, not a verified production release.
