# Grandma Connect — Android Native

This repository contains the CI workflow for building the Android debug APK.

## Add the native source archive

1. Download `GrandmaConnectNative-source.zip` from the ChatGPT conversation.
2. In this repository, choose **Add file → Upload files**.
3. Upload the ZIP to the repository root. Keep the exact filename `GrandmaConnectNative-source.zip`.
4. Commit the upload to `main`.

That push starts **Build Grandma Connect APK** automatically. The workflow extracts the archive, builds `app-debug.apk`, and uploads it as the artifact `grandma-connect-debug-apk`.

The build must pass before the APK should be installed. This is a debug APK for testing, not a production release. The Accessibility Service must be enabled manually in Android Settings by the device owner.
