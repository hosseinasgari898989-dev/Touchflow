# TouchFlow

TouchFlow is an Android application for recording and replaying touch interactions for personal accessibility workflows and controlled UI testing.

## Project status

The project is being re-established around a preserved APK baseline. The first owner-provided binary is recorded in [docs/BASELINE.md](docs/BASELINE.md). It is a reference artifact, not editable source code.

The repository still contains legacy Grandma Connect naming and experimental branches. They are being reviewed individually; they are not being merged or deleted as part of this baseline setup.

## Source and build

- The existing native source archive is `GrandmaConnectNative-source.zip`.
- The current default-branch workflow, `.github/workflows/build-android.yml`, builds a **debug APK** from that archive. It is a test-build workflow, not yet a versioned release pipeline.
- The source archive has not yet been proven to produce the owner-provided baseline APK. See [docs/BASELINE.md](docs/BASELINE.md).

An APK is a compiled output. Make changes in the Android source project, then build and verify a new APK. Do not try to edit or overwrite the binary APK as if it were source code.

## Change and backup rules

1. Keep `main` and the existing native-baseline backup unchanged during the cleanup.
2. Make each change on a dedicated feature branch and review it through a pull request.
3. Before changing or removing source files, record the exact paths, reason, dependency impact, and rollback point.
4. Preserve each released APK as an immutable, versioned artifact with a SHA-256 checksum.
5. Do not merge experimental branches together without a separate diff and regression review.

See [docs/RELEASE_POLICY.md](docs/RELEASE_POLICY.md) for the update and release procedure.
