# TouchFlow — پروندهٔ پیوست و دفتر ثبت پروژه

**آخرین تطبیق:** 2026-11-19  
**مخزن:** https://github.com/hosseinasgari898989-dev/Touchflow  
**شاخهٔ اصلی:** `main`  
**هدف این فایل:** نگهداری وضعیت واقعی پروژه، تصمیم‌ها، کارهای انجام‌شده، محدودیت‌ها و قدم بعدی؛ تا در گفتگوهای بعدی لازم نباشد زمینهٔ پروژه از ابتدا توضیح داده شود.

این فایل مکمل `PROJECT_STATE.md` است و جایگزین آن نیست. در شروع هر ادامهٔ کاری، این فایل و سپس `PROJECT_STATE.md` و سند مرتبط در `docs/` خوانده شوند. بعد از هر تغییر مهم، همین فایل با تاریخ، شاخه، commit، نتیجهٔ Build و نتیجهٔ تست به‌روزرسانی شود.

---

## 1. وضعیت فعلی کار — نقطهٔ ادامه

### آنچه انجام شده است

- طراحی مجدد ظاهر و UI موبایل TouchFlow با پلاگین **MagicPath** انجام شده است.
- کار UI شامل ظاهر صفحات و تنظیم چیدمان و ابعاد مناسب صفحهٔ موبایل بوده است.
- کاربر تأیید کرده که بررسی‌های قبلی نمونهٔ UI انجام شده و نتیجه کار کرده است؛ این مرحله را کارِ شروع‌نشده تلقی نکنید و بدون درخواست کاربر آن را از ابتدا تکرار نکنید.
- کاربر اعلام کرده که پس از این مرحله، کار وارد مسیر **سازگاری با برنامهٔ Android و افزودن قابلیت‌ها** شده است.

### قدم جاری

ادامه از طراحی موجود و رفتن به مرحلهٔ سازگاری/اتصال با سورس Android و توسعهٔ قابلیت‌ها است؛ نه ساخت دوبارهٔ یک UI از صفر.

در هر تغییر باید مشخص باشد:
1. کدام بخش از طراحی موجود به صفحه/کامپوننت Native متصل می‌شود؛
2. کدام قابلیت واقعی به آن اضافه می‌شود؛
3. چه چیزی در گوشی/نسخهٔ Android باید سازگار بماند؛
4. چه تستی انجام شده و نتیجه‌اش چیست.

**تفکیک مهم:** ساخته‌شدن و نمایش موفق UI با عملیاتی‌شدن ضبط، ذخیره‌سازی یا اجرای ماکرو یکی نیست. کد فعلی کامپوننت MagicPath صریحاً بعضی کنترل‌ها را پیش‌نمایش محلی معرفی می‌کند؛ آن‌ها هنگام اتصال به Native باید به عملیات واقعی وصل شوند.

---

## 2. طراحی UI در MagicPath — مرجع طراحی موجود

**پلاگین:** MagicPath  
**نام پروژه:** `TouchFlow – Android UI Redesign`  
**Project ID:** `474228529169580032`  
**لینک پروژه:** https://www.magicpath.ai/files/474228529169580032

**کامپوننت:**
- نام: `TouchFlow mobile UI concept`
- Component ID: `474228663873835008`
- Generated name: `wondrous-sun-8199`
- تعداد Revision ثبت‌شده: 2
- آخرین Revision انتخاب‌شده روی Canvas هنگام بررسی: `474229984953769984`
- آخرین زمان به‌روزرسانی پروژه در MagicPath: `2026-11-19T18:19:16Z`

**ابعاد و قواعد قابل مشاهده در سورس کامپوننت:**
- فریم Canvas: **360 × 800**
- حداکثر عرض ظرف موبایل: **430px**
- ارتفاع پویا: `100dvh`
- جهت رابط: راست‌به‌چپ (`dir="rtl"`)
- نوار بالا و پایین با رعایت `safe-area-inset-top` و `safe-area-inset-bottom`
- جلوگیری از اسکرول افقی ناخواسته
- صفحات/بخش‌های طراحی‌شده: خانه، ماکروها، تنظیمات و حالت ضبط
- انتخاب مدت در UI: ۴۵ ثانیه، ۲ دقیقه، ۵ دقیقه و ۱۰ دقیقه

**وضعیت:** طراحی و بررسی اولیه طبق تأیید کاربر انجام شده است. این کامپوننت مرجع بصری است؛ قبل از تغییر آن، همان پروژه و Revision موجود بررسی شود. طراحی را بدون دلیل یا درخواست کاربر از نو نسازید.

**نکتهٔ اتصال:** متن و رفتار نمونه در بعضی قسمت‌ها به‌روشنی می‌گوید «پیش‌نمایش» و «بدون اتصال به ضبط واقعی». بنابراین در مرحلهٔ سازگاری باید ظاهر حفظ شود و کنترل‌ها به سرویس/ذخیره‌سازی واقعی وصل شوند؛ نباید کلیک‌پذیری نمایشی را قابلیت تکمیل‌شده حساب کرد.

---

## 3. وضعیت مخزن GitHub در آخرین بررسی

**آخرین commit شاخهٔ `main`:**
`6c738c2214d4244913fe449ed6172db613f844bd`

این commit فقط `README.md` را هماهنگ کرده و تغییر سورس Android نیست.

ساختار فعلی `main` شامل این موارد است:
- `GrandmaConnectNative-source.zip` — آرشیو سورس Native
- `.github/workflows/build-android.yml` — گردش‌کار Build
- `PROJECT_STATE.md`، `README.md` و پوشهٔ `docs/`

در `main` سورس Android به شکل پوشهٔ استخراج‌شدهٔ Gradle نگهداری نمی‌شود؛ workflow آرشیو سورس را استخراج و Build می‌کند.

در زمان بررسی:
- PRهای مستنداتی #1، #2 و #3 بسته شده بودند.
- PR باز دیگری در نتایج جست‌وجوی همان زمان پیدا نشد.
- شاخه‌های کاری و پشتیبان جداگانه وجود دارند؛ وجود یک شاخه به‌تنهایی به معنی ادغام آن در `main` نیست.
- هیچ‌کدام از Buildهای آزمایشی زیر را نباید با نسخهٔ ادغام‌شده در `main` اشتباه گرفت.

**شاخه‌های مهم دیده‌شده:**
- `feature/expanded-capture-settings-2026-11-19`
- `feature/touchflow-clean-foundation-2026-11-19`
- `feature/touchflow-simple-runner-2026-11-19`
- `feature/touchflow-v1-cleanup-exact-baseline-2026-11-19`
- `feature/touchflow-v1-native-cleanup-2026-11-19`
- `feature/touchflow-webview-integration-20261119`
- `backup/touchflow-v1-exact-baseline-2026-11-19`
- `backup/touchflow-v1-native-source-2026-11-19`

شاخهٔ فعال برای ادامهٔ تغییرات بعدی باید پیش از هر کار با وضعیت واقعی GitHub تأیید شود؛ از روی نام شاخه حدس نزنید.

---

## 4. Baseline اصلی و ایمنی نصب/به‌روزرسانی

**APK مرجع صاحب پروژه:** `GrandmaConnect-preview.apk`  
**نام محفوظ در مستندات:** `TouchFlow-v1.0.0-baseline.apk`

- اندازه: 866,747 bytes
- SHA-256: `6dce713dfebcbf84ed5a175b6eb73808791765464087526875c3fe6f11bd0b89`
- Application ID: `com.grandmaconnect.preview`
- versionCode: 1
- versionName: `0.1.0-alpha-preview`
- minSdk / targetSdk: 24 / 35
- نام نمایشی APK مرجع: Grandma Connect

**منشأ دقیق Baseline:**
- Workflow run موفق: [44399521736](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44399521736)
- سورس دقیق: commit `36600aa02fba13430ba6a1e9e2efc09f665b7b67`
- شاخهٔ سورس آن Build: `feature/expanded-capture-settings-2026-11-19`
- APK صاحب پروژه با Artifact آن Run از نظر بایت و SHA-256 یکسان گزارش شده است.

**مانع امضای APK:**
- اثرانگشت گواهی APK مرجع ثبت شده است.
- فایل خصوصی keystore/key مربوط به همان امضا در بررسی قبلی **NOT FOUND** بوده است.
- Buildهای بعدی با امضای Debug متفاوت تولید شده‌اند.
- بنابراین نصب یک APK تازه روی نسخهٔ مرجع یا حفظ داده‌های آن را تضمین‌شده فرض نکنید. قبل از هر نصب/به‌روزرسانی باید package و گواهی امضا مقایسه شوند.
- تا قبل از تعیین مسیر امضا یا مهاجرت داده، APK مرجع و داده‌های ماکرو نباید حذف یا جایگزین شوند.

---

## 5. نمونه‌های Native و Buildهای آزمایشی ثبت‌شده

این موارد در شاخه‌های جداگانه ساخته شده‌اند و با هم یا با `main` یکی نیستند.

| مسیر/شاخه | مدرک Build | وضعیت ثبت‌شده |
|---|---|---|
| WebView Integration — `feature/touchflow-webview-integration-20261119` | [Run 44432787584](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44432787584) | موفق؛ سورس شامل `assets/touchflow/index.html`، `TouchFlowBridge.kt` و `TouchFlowMacroMetadata.kt` بوده است. Artifact APK: 919,771 bytes |
| Simple Native Runner — `feature/touchflow-simple-runner-2026-11-19` | [Run 44525646233](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44525646233) | موفق؛ Build آزمایشی با شناسهٔ جداگانهٔ `com.grandmaconnect.simple`. Artifact APK: 874,560 bytes. اصلاح Layout مربوط به ScrollView در مرحلهٔ Build workflow اعمال شده است |
| TouchFlow Branding Preview — `feature/touchflow-v1-cleanup-exact-baseline-2026-11-19` | [Run 44565048023](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44565048023) | موفق؛ نام نمایشی TouchFlow و شناسهٔ جداگانهٔ `com.grandmaconnect.touchflowpreview`. Artifact APK: 858,768 bytes |
| تلاش پیشین برای آرشیو ۸ قسمتی | [Run 44562721605](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44562721605) | ناموفق؛ تلاش بعدی با Run 44565048023 موفق شده است |

این Runها مدرک Build شدن همان ورودی‌های شاخه‌های مربوط‌اند؛ به معنی تست کامل همهٔ قابلیت‌ها روی گوشی یا ادغام در `main` نیستند.

---

## 6. قابلیت‌های موجود و مرزهای فنی شناخته‌شده

### وضعیت سورس Baseline ثبت‌شده در اسناد

- ضبط فعلی در `TouchCanvasView` داخل خود برنامه انجام می‌شود؛ ضبط سراسری لمس در برنامه‌های دیگر در Baseline پیاده‌سازی نشده است.
- اجرای ژست‌ها از `AccessibilityService.dispatchGesture` استفاده می‌کند.
- سرویس فعلی محتوای پنجرهٔ برنامه‌های دیگر را دریافت نمی‌کند (`canRetrieveWindowContent=false`).
- ماکروها به‌صورت JSON در حافظهٔ خصوصی برنامه ذخیره می‌شوند.
- Export/Import قابل استفاده برای کاربر و بازیابی ماکروها در Baseline وجود ندارد.
- سقف فعلی حالت ضبط توسعه‌یافته ۱۰ دقیقه است.
- Timeline/Keyframe در شاخهٔ WebView قبلی نمونه/Mock بوده و نباید آن را ویرایشگر پایدار و متصل به دادهٔ واقعی حساب کرد.

### نیازهای محصول که باید در توسعه حفظ/پیگیری شوند

این‌ها نیازهای کاری پروژه‌اند؛ وجودشان در UI به معنی پیاده‌سازی کامل نیست:
- ضبط و اجرای لمس‌ها با زمان‌بندی، از جمله Tap، Swipe، Long Press و Multi-touch.
- دکمهٔ توقف و مسیر خروج/ناوبری نباید به‌عنوان بخشی از ماکروی ضبط‌شده ذخیره شوند.
- مدیریت ماکروها: ذخیره، فهرست، بازکردن مجدد و اجرای مجدد.
- تنظیمات قابل‌کنترل برای مدت/ظرفیت ضبط؛ رفتار محدودیت‌ها باید از تنظیمات و منابع واقعی برنامه بیاید، نه فقط متن ثابت UI.
- ابزارهای Timeline و Frame/Keyframe که روی دادهٔ واقعی ماکرو کار کنند و تغییراتشان پس از بستن و بازکردن باقی بماند.
- بررسی امکان ضبط بیرون از خود برنامه با APIهای مجاز Android؛ تا وقتی آزمایش فنی آن موفق نشده، ضبط سراسری را قابلیت موجود معرفی نکنید.

**دستگاه هدف ثبت‌شده برای تست:** Samsung Galaxy A14، مدل SM-A145F/DS، Android 13 / One UI Core 5.1.

---

## 7. ترتیب ادامهٔ کار

1. همین طراحی MagicPath را مرجع UI نگه دار؛ کار طراحی را از صفر شروع نکن.
2. سورس Native فعلی و شاخهٔ کاری مناسب را از GitHub بازخوانی کن؛ قبل از تغییر، commit پایه و backup را ثبت کن.
3. صفحات طراحی را با ساختار واقعی Android تطبیق بده: اندازه‌ها، RTL، safe area، نوار وضعیت/ناوبری، اندازهٔ فونت و صفحه‌های کوچک‌تر.
4. هر کنترل UI را به قابلیت واقعی متصل کن؛ کنترل نمایشی یا Mock را با عملیات واقعی اشتباه نگیر.
5. قابلیت‌ها را کوچک و مستقل پیاده‌سازی کن؛ ابتدا مسیر ضبط/توقف/ذخیره/بازکردن/اجرا و سپس ابزارهای توسعه‌یافته مثل Timeline/Keyframe.
6. برای قابلیت‌های وابسته به دسترسی سیستم، محدودیت Android را بررسی و روی دستگاه هدف آزمایش کن؛ مجوزهای اضافی را بی‌دلیل درخواست نکن.
7. بعد از هر تغییر، Build تمیز، بررسی Manifest/package/signature و تست‌های مرتبط انجام و نتیجه ثبت شود.
8. هیچ APK آزمایشی را بدون بررسی امضا و سازگاری روی نصب مرجع جایگزین نکن.

---

## 8. قواعد ثابت کار

- `main` و APK مرجع Baseline را بدون تصمیم و بررسی مشخص تغییر نده.
- هر تغییر کد در شاخهٔ مستقل، کوچک و قابل بازبینی انجام شود؛ PR و Diff کامل بررسی شوند.
- این فایل یا `PROJECT_STATE.md` بعد از هر تصمیم، Build، تست، خطا یا تغییر شاخه به‌روز شود.
- برای هر مورد یکی از وضعیت‌های **DONE / IN PROGRESS / TODO / BLOCKED / NOT VERIFIED** ثبت شود.
- هرگز نتیجهٔ Build را معادل تست روی گوشی یا تکمیل قابلیت ندان.
- فایل‌های اصلی Kotlin، Manifest، شناسه‌های package، ساختار ذخیره‌سازی و schema ماکرو را بدون تحلیل وابستگی و برنامهٔ مهاجرت تغییر نده.
- فایل‌های Baseline، آرشیو سورس و شاخه‌های پشتیبان را پاک نکن.
- رازها، توکن‌ها، کلیدهای امضا و اطلاعات محرمانه را در این فایل یا گزارش‌ها ننویس.

---

## 9. الگوی ثبت پیشرفت‌های بعدی

برای هر تغییر جدید، یک ورودی با این قالب اضافه شود:

```text
### YYYY-MM-DD — عنوان کار
Status: DONE | IN PROGRESS | TODO | BLOCKED | NOT VERIFIED
Branch:
Base commit:
Commit / PR:
Files changed:
What changed:
Build run and result:
Device / Android version:
Tests performed and results:
Known limitations / follow-up:
```

### 2026-11-19 — ثبت وضعیت طراحی و تحویل ادامهٔ کار
Status: DONE (documentation entry)
- MagicPath project and component IDs ثبت شدند.
- ابعاد طراحی 360×800 و قواعد responsive قابل مشاهده ثبت شدند.
- تأیید کاربر دربارهٔ تکمیل بررسی قبلی UI ثبت شد.
- شاخه‌های Native و Buildهای آزمایشی موجود ثبت شدند.
- مرحلهٔ جاری برای ادامه: سازگاری/اتصال با Native و افزودن قابلیت‌ها.
- این ورودی فقط سند است؛ سورس Android، APK مرجع و تنظیمات Build تغییر نکرده‌اند.


---

# آپدیت ۱ — بستهٔ قابلیت‌های ضبط، ویرایش و اجرای سریع

**تاریخ شروع:** 2026-11-19  
**درخواست صاحب پروژه:** full-screen recording، تعریف چند برنامه در جریان ماکرو و ادامهٔ اجرای لمس‌ها، ویرایشگر ساده برای Split زمانی، فرمان بازگشت، اجرای ماکرو از ویجت/میانبر بدون بازماندن پنجرهٔ برنامه، و فونت فارسی مناسب.  
**شاخهٔ پیاده‌سازی:** `feature/touchflow-first-feature-pack-2026-11-19`  
**Backup پیش از تغییر:** `backup/touchflow-before-feature-pack-2026-11-19`  
**Base source commit:** `f479a3b10d7639ae1207915f3d9f2efbfc6cbcdc` از شاخهٔ `feature/touchflow-simple-runner-2026-11-19`  
**وضعیت بسته:** IN PROGRESS

## نیازهای قفل‌شدهٔ این آپدیت

1. **ضبط تمام‌صفحه:** قابلیت تمام‌صفحهٔ موجود حفظ شود؛ نوارهای سیستم هنگام ضبط immersive باشند و کنترل‌های توقف/بازگشت در دسترس باقی بمانند. ضبط فعلی فقط TouchCanvasView داخل TouchFlow را ثبت می‌کند.
2. **چند برنامه در یک ماکرو:** کاربر بتواند چند اقدام Launch App را در مرزهای مختلف ماکرو اضافه کند. هنگام پخش، AccessibilityService برنامهٔ انتخابی را باز کند، مکث قابل تنظیم را انجام دهد و ژست‌های بعدی را ادامه دهد. ترتیب اقدام‌هایی که در یک مرز قرار می‌گیرند باید پایدار باشد.
3. **مرز فنی ضبط چندبرنامه‌ای:** ضبط خام و شفاف لمس‌های داخل برنامه‌های دیگر روی Android 13 به‌عنوان قابلیت موجود فرض نمی‌شود. TouchInteractionController و onMotionEvent محدودیت تحویل رویداد دارند؛ تا وقتی روی دستگاه هدف یک راهکار معتبر و بدون مختل‌کردن لمس ثابت نشده، فقط sequence چندبرنامه‌ای در مرحلهٔ playback ارائه شود. هیچ مجوز window-content اضافه نشود.
4. **ویرایشگر سادهٔ زمانی:** کاربر بتواند بین گروه‌های لمس Split بگذارد و Split را بردارد. Split فقط یک مرز زمانی/ساختاری ذخیره می‌کند؛ هیچ گروه، نقطه، مختصات، زمان یا اقدام خودکاری حذف/بازنویسی نشود. فاصلهٔ زمانی بین گروه‌ها در UI نشان داده شود.
5. **فرمان بازگشت:** نوع اقدام `GO_BACK` به کاربر اجازه دهد در یک مرز مشخص، فرمان Back اندروید را اجرا کند. `GO_HOME` موجود باقی بماند.
6. **ویجت اجرای ماکرو:** برای هر ویجت یک ماکرو انتخاب و ذخیره شود. ضربه روی ویجت، ماکروی انتخاب‌شده را مستقیماً از AccessibilityService اجرا کند؛ در مسیر موفق، Activity TouchFlow باز نشود/باز نماند. اگر سرویس یا مجوز لازم آماده نیست، خطای روشن و مسیر بازیابی نمایش داده شود.
7. **خروج خودکار Activity:** اجرای موفق از کارت داخل برنامه نیز پس از پذیرفته‌شدن شروع playback، Activity را ببندد؛ سرویس دسترس‌پذیری و اعلان توقف باید ادامه یابند.
8. **فونت فارسی:** فونت Arabic/Persian خوانا به‌صورت local داخل APK قرار گیرد و در تمام TextView/EditText/Button/Switch/RadioButtonها اعمال شود؛ به بارگیری شبکه‌ای فونت وابسته نباشد. منبع و مجوز فونت باید در repo ثبت شود.

## تصمیم‌های فنی این بسته

- مبنا Native Runner شاخهٔ `feature/touchflow-simple-runner-2026-11-19` است؛ چون MacroFlowAction و اجرای Launch App را دارد و لازم نیست قابلیت را موازی از صفر بسازیم.
- فایل ماکرو به Schema 3 ارتقا می‌یابد؛ خواندن Schema 1 و 2 حفظ می‌شود. فیلد جدید `splitAfterGroupCounts: List<Int>` مرز Split را به‌صورت تعداد گروه‌های قبل از مرز ذخیره می‌کند.
- Split در مرز بین گروه‌ها مجاز است: مقدار هر marker باید در بازهٔ `1 until groups.size`، یکتا و صعودی باشد. این کار از شکستن یک Stroke یا Multi-touch group جلوگیری می‌کند.
- ترتیب Splitها، Launch App و GO_BACK نباید با هم تداخل داده‌ای داشته باشند؛ split marker صرفاً UI segmentation است و در زمان playback روی ترتیب event/action اثر ندارد.
- Widget با AppWidgetProvider + Activity پیکربندی ساخته می‌شود؛ widgetId به macroId متصل می‌شود و کلیک به BroadcastReceiver می‌رود.
- برای شروع موفق از Widget، سرویس singleton موجود استفاده می‌شود؛ در نبود سرویس یا مجوز اعلان، widget به‌تنهایی playback را آغاز نمی‌کند و به‌جای fail silently پیام/مسیر بازیابی می‌دهد.
- فونت این نسخه: `sans-serif` داخلی Android با fallback فارسی/عربی سیستم؛ هیچ فونت خارجی هنگام اجرا بارگیری نمی‌شود و APK با فونت بسته‌بندی‌شده سنگین‌تر نشده است. خوانایی و شکل‌دهی فارسی روی Galaxy A14 هنوز NOT VERIFIED است.

## برنامهٔ اجرا و آزمون

### Task 1 — مدل Split زمانی و مهاجرت Schema 3
- [ ] تست RED: افزودن Split فقط در مرز معتبر؛ مرز ابتدا/انتها، تکراری و خارج از محدوده رد شود.
- [ ] تست RED: حذف Split فقط marker مورد نظر را بردارد و هیچ گروه/اقدامی تغییر نکند.
- [ ] پیاده‌سازی `MacroSplitRules` و فیلد `splitAfterGroupCounts` در `TouchMacro`.
- [ ] ارتقای serializer به Schema 3 و نگه‌داشتن خواندن Schema 1/2.
- [ ] تست round-trip برای markerها و fixtureهای قدیمی.

### Task 2 — ویرایشگر زمانی ساده
- [ ] صفحهٔ Timeline پس از ذخیرهٔ ماکرو به مدیریت اضافه شود.
- [ ] نمایش گروه‌ها با زمان شروع و فاصله تا گروه بعد.
- [ ] دکمهٔ Split/Unsplit فقط روی boundary بین گروه‌ها.
- [ ] بازگشت به مدیریت و ذخیرهٔ atomic؛ در خطا فایل قبلی حفظ شود.

### Task 3 — چندبرنامه‌ای و فرمان‌های ناوبری
- [ ] اضافه‌کردن `GO_BACK` به enum و schema، با اعتبارسنجی و حفظ backward compatibility.
- [ ] اضافه‌کردن گزینهٔ Back در editor اقدامات و نمایش آن در فهرست.
- [ ] اجرای `performGlobalAction(GLOBAL_ACTION_BACK)` در AccessibilityService.
- [ ] تأیید ترتیب چند Launch App در یک یا چند boundary و ادامهٔ ژست‌های بعدی پس از مکث.
- [ ] خطای واضح برای برنامهٔ حذف‌شده/غیرقابل launch و توقف امن playback.

### Task 4 — ویجت اجرای یک ماکرو
- [ ] AppWidgetProvider و layout.
- [ ] Activity پیکربندی برای انتخاب یک ماکرو به ازای widgetId.
- [ ] ذخیرهٔ mapping هر widgetId به macroId.
- [ ] Receiver امن با اعتبارسنجی ماکرو، وضعیت Accessibility و اعلان توقف.
- [ ] حذف mapping هنگام حذف Widget؛ مدیریت ماکروی حذف‌شده.
- [ ] مسیر fallback وقتی سرویس آماده/فعال نیست.

### Task 5 — خروج خودکار و تمام‌صفحه
- [ ] بعد از شروع موفق از Activity، `finishAndRemoveTask()` اجرا شود.
- [ ] در صورت خطای شروع، Activity بسته نشود.
- [ ] وضعیت نوار سیستم و جهت صفحه پس از توقف/خروج/مرگ Activity بازیابی شود.
- [ ] رفتار فعلی تمام‌صفحه و دکمهٔ شناور توقف رگرسیون تست شود.

### Task 6 — فونت و یکپارچه‌سازی
- [ ] فونت local و license اضافه شود.
- [ ] فونت در تم برنامه به صورت عمومی اعمال شود و در Widget از fallback سیستم استفاده شود.
- [ ] Build clean، آزمون‌های مدل و Manifest/resource validation.
- [ ] تست دستگاه Galaxy A14 / Android 13 برای recording، action sequence، Back، widget، auto-close، system bars و خوانایی فارسی.

## معیار پذیرش

- فایل‌های Schema 1 و 2 همچنان باز می‌شوند و ذخیرهٔ مجدد بدون از دست رفتن داده انجام می‌شود.
- Split/Unsplit هیچ ژست یا actionی را حذف/جابجا نمی‌کند؛ فقط marker را عوض می‌کند.
- چند اقدام Launch App و GO_BACK در ترتیب مورد انتظار اجرا می‌شوند و بعد از مکث، ژست بعدی ادامه می‌یابد.
- کلیک موفق Widget ماکرو را شروع می‌کند و پنجرهٔ اصلی TouchFlow باز نمی‌ماند؛ توقف از اعلان موجود باشد.
- خطای service/permission/missing macro باعث شروع ناقص یا خروج اشتباه از Activity نشود.
- فونت روی تمام صفحات اصلی فارسی درست نمایش داده شود.
- APK روی نسخهٔ مرجع نصب نمی‌شود مگر package + signature identity با baseline بررسی و تأیید شده باشد.

## دفتر اجرای زنده

| تاریخ | Task | وضعیت | شاخه/Commit | Build/Test | یادداشت |
|---|---|---|---|---|---|
| 2026-11-19 | ثبت درخواست و تصمیم‌ها | DONE | `feature/touchflow-first-feature-pack-2026-11-19` | هنوز اجرا نشده | UI از نو طراحی نمی‌شود؛ پیاده‌سازی Native از Simple Runner آغاز می‌شود |

**آخرین گام انجام‌شده:** شاخهٔ backup و feature ساخته شده‌اند. سورس از artifact موفق Run 44525646233 بازیابی شده است. قبل از هر ادعای تکمیل، نتیجهٔ تست و Build باید در همین فایل ثبت شود.


### 2026-11-19 — پیاده‌سازی مرحلهٔ اول در working copy
Status: IN PROGRESS (کد محلی آمادهٔ بسته‌بندی؛ هنوز به شاخه Push نشده)
Branch: `feature/touchflow-first-feature-pack-2026-11-19`
Base commit: `f479a3b10d7639ae1207915f3d9f2efbfc6cbcdc`
Files changed locally:
- `app/src/main/java/com/grandmaconnect/MacroSplitRules.kt` — قانون‌های خالص Split بین گروه‌های کامل لمس.
- `app/src/main/java/com/grandmaconnect/MacroModels.kt` — Schema 3، نگهداری Split markerها و خواندن Schema 1/2؛ نوع اقدام `GO_BACK`.
- `app/src/main/java/com/grandmaconnect/MainActivity.kt` — Timeline editor ساده، درج برنامه هنگام ضبط در boundary کامل، گزینهٔ GO_BACK، خروج Activity پس از شروع موفق playback، و استفادهٔ مستقیم از LayoutParams صحیح.
- `app/src/main/java/com/grandmaconnect/TouchCanvasView.kt` — بررسی boundary امن برای افزودن action هنگام ضبط.
- `app/src/main/java/com/grandmaconnect/MacroAccessibilityService.kt` — اجرای GO_BACK و اعتبارسنجی جهت صفحه/اجازهٔ اعلان پیش از playback.
- `app/src/main/java/com/grandmaconnect/MacroWidget.kt` — Widget انتخاب ماکرو به‌ازای هر widgetId و اجرای مستقیم در AccessibilityService.
- `app/src/main/res/layout/widget_macro.xml`, `drawable/widget_macro_background.xml`, `xml/widget_macro_info.xml`, Manifest و strings — پوسته و ثبت ویجت.
- `app/src/test/java/com/grandmaconnect/MacroSplitRulesTest.kt` — تست JUnit.
- `tools/MacroSplitRulesTest.kt` — تست standalone برای اجرای سریع محلی.
- `app/build.gradle.kts` — وابستگی JUnit.

Tests performed:
- TDD RED: تست Split پیش از وجود implementation با خطای unresolved reference شکست خورد؛ پس از اضافه‌شدن MacroSplitRules سبز شد.
- Kotlin standalone: `MacroSplitRulesTest: 10 assertions passed`.
- XML parsing: تمام ۷ فایل XML فعلی بدون خطای syntax parse شدند.
- Build محلی: NOT RUN؛ در محیط فعلی Gradle و Android SDK نصب نیستند. Build باید از GitHub Actions گرفته شود.
- تست گوشی: NOT RUN؛ هنوز روی Galaxy A14 تست نشده است.

Important current behavior:
- ضبط full-screen پیشین حفظ شده؛ دکمهٔ شناور «＋ برنامه» هنگام ضبط، فقط پس از پایان کامل gesture group اجازهٔ درج Launch App می‌دهد.
- چند برنامه با ترتیب درج‌شده در action list قابل ثبت‌اند؛ هنگام playback هر Launch App مکث دارد و gesture group بعدی پس از مکث اجرا می‌شود.
- Splitها فقط marker هستند و group/point/timing/action را حذف یا تغییر نمی‌دهند.
- ویجت برای هر widgetId یک macroId دارد؛ اگر دسترسی یا اعلان موجود نباشد، playback خاموش و بی‌خبر انجام نمی‌شود و برنامه پیام راهنما باز می‌کند.
- فونت اختصاصی داخل APK هنوز اضافه نشده؛ تم از `sans-serif` سیستم و fallback فارسی/عربی Android استفاده می‌کند. خوانایی روی گوشی باید تست شود.

Next:
1. رفع ریزه‌کاری‌های UI/Manifest و تست‌های اضافه.
2. بسته‌بندی سورس به آرشیو hash-locked در `.touchflow-feature/`.
3. افزودن workflow مختص شاخهٔ feature و اجرای `testDebugUnitTest assembleDebug`.
4. بازبینی Diff/Build و به‌روزرسانی همین فایل با نتیجهٔ واقعی CI.
5. تست دستی Widget و playback چندبرنامه‌ای روی دستگاه هدف قبل از ادغام.


### 2026-11-19 — اعتبارسنجی منطق Split و بسته‌بندی سورس
Status: IN PROGRESS (آمادهٔ CI؛ Build Android هنوز منتظر نتیجهٔ GitHub Actions)
Branch: `feature/touchflow-first-feature-pack-2026-11-19`
Source archive: `TouchFlowFeaturePack-source.tar.xz`
Archive SHA-256: `8288df571300bccf54489bbb82289991d3b2a1a59a2ca4014b3859055ded8532`
Archive size: 25,088 bytes
Git path: `.touchflow-feature/part-00` … `.touchflow-feature/part-08` (9 ordered Base64 text segments; workflow concatenates before decoding)
Local checks:
- `MacroSplitRulesTest: 10 assertions passed`
- تمام XMLهای Android با XML parser خوانده شدند.
- Build محلی هنوز اجرا نشده؛ Android SDK/Gradle در محیط موجود نیست.
- سورس شامل Widget، config Activity، editor timeline، action درج برنامه حین ضبط، GO_BACK، Schema 3 و JUnit test است.
- Preview build باید package id جداگانهٔ `com.grandmaconnect.feature` داشته باشد؛ APK baseline نباید جایگزین شود.

**قانون تداوم:** اگر چت قطع شد، از همین فایل و همین شاخه ادامه بده؛ ابتدا نتیجهٔ آخرین Actions run را بررسی کن، نه اینکه از ابتدا پیاده‌سازی را شروع کنی.


### 2026-11-19 — بستهٔ نهایی برای Build آزمایشی آماده شد
Status: IN PROGRESS (منتظر ثبت archive/workflow و نتیجهٔ CI)
- Archive نهایی پس از آخرین تغییرهای Manifest و بررسی جهت صفحه بازسازی شد.
- SHA-256 نهایی: `8288df571300bccf54489bbb82289991d3b2a1a59a2ca4014b3859055ded8532`
- حجم آرشیو: 25,156 bytes.
- Workflow مخصوص شاخهٔ feature آماده شده: `.github/workflows/build-touchflow-feature-pack.yml`.
- Workflow قرار است `testDebugUnitTest assembleDebug` را اجرا کند و package جداگانهٔ `com.grandmaconnect.feature` را با label `TouchFlow Feature Preview` و signature معتبر بررسی کند.
- آخرین تست محلی pure Kotlin: 10/10 assertion passed.
- آخرین بررسی XML: همهٔ resourceهای XML قابل parse هستند.
- Android Build و APK هنوز NOT VERIFIED تا دریافت نتیجهٔ Actions.


### 2026-11-19 — سورس نهایی به شاخهٔ GitHub منتقل شد
Status: IN PROGRESS (سورس بخش‌بندی و ثبت شد؛ Build CI در انتظار)
Branch: `feature/touchflow-first-feature-pack-2026-11-19`
Source baseline: `f479a3b10d7639ae1207915f3d9f2efbfc6cbcdc`
Archive: `TouchFlowFeaturePack-source.tar.xz`
Archive SHA-256: `8288df571300bccf54489bbb82289991d3b2a1a59a2ca4014b3859055ded8532`
Archive size: 25,376 bytes
Transfer representation: 9 ordered Base64 text parts at `.touchflow-feature/part-00` through `part-08`.
Workflow now concatenates these parts, decodes, verifies SHA-256 and tar integrity before extracting/building.
Local final verification immediately before transfer:
- `MacroSplitRulesTest: 10 assertions passed`
- 6 Android XML files parsed successfully.
- Android/Gradle local build: NOT RUN (toolchain absent).
- Device test: NOT RUN.


### 2026-11-19 — تأیید مستقل آرشیو پس از انتقال GitHub
Status: DONE (integrity check); IN PROGRESS (Android CI pending)
- هر ۹ فایل `.touchflow-feature/part-00` تا `part-08` مستقیماً از GitHub خوانده شدند.
- طول قطعات: `4200, 4200, 4200, 4200, 4200, 4200, 4200, 4200, 236` کاراکتر.
- طول Base64 ترکیب‌شده: 33,836 کاراکتر.
- پس از Base64 decode: 25,376 bytes.
- SHA-256 محاسبه‌شده از بایت‌های آرشیو: `8288df571300bccf54489bbb82289991d3b2a1a59a2ca4014b3859055ded8532`.
- نتیجه: MATCH با SHA-256 محلی؛ تمامیت آرشیو انتقال‌یافته تأیید شد.
- اصلاح: `part-05` و `part-07` هر دو به طول کامل 4,200 کاراکتر تصحیح شدند؛ هیچ padding یا دادهٔ حدسی اضافه نشده است.
- GitHub blob نهایی `part-05`: `00329522e7c4bb5b38a8106e7b74321e8e84a706`.
- GitHub blob نهایی `part-07`: `ca5e5385d988b52dcb31598b59fb33d06d434c14`.
- اکنون می‌توان READY و workflow را اضافه کرد و CI را اجرا کرد.


### 2026-11-19 — تشخیص و اصلاح اولین شکست کامپایل
Status: FIX APPLIED LOCALLY; CI RETEST PENDING
Previous run: [44600591255](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44600591255)
Previous run result:
- Archive verification: SUCCESS.
- Preview identity isolation: SUCCESS.
- JDK 17, Gradle 8.9, Android SDK 35 setup: SUCCESS.
- Kotlin compilation: FAILED.
- Exact compiler diagnostics:
  - `MacroWidget.kt:82:5 'onCreate' overrides nothing.`
  - `MacroWidget.kt:82:47 Unresolved reference 'Bundle'.`
- Root cause: `MacroWidgetConfigureActivity.onCreate(savedInstanceState: Bundle?)` lacked `import android.os.Bundle`.
- Minimal correction: added only `import android.os.Bundle` to `MacroWidget.kt`; no lifecycle behavior changed.
- Local pure Kotlin split test rerun after the fix: `MacroSplitRulesTest: 10 assertions passed`.
- Current source archive regenerated:
  - SHA-256: `117becdf5b48a585303c1a9cc4d2648038795abdcada00639f2c4b5a7989a4d0`
  - Size: 25,384 bytes.
  - Base64 chars: 33,848.
  - Segments: 9 (8 × 4,200 + 248).
- Correction is isolated to branch `feature/touchflow-feature-pack-bundle-fix-2026-11-19`.
- Backup branch `backup/touchflow-feature-pack-before-ci-fix-2026-11-19` preserves failed-CI state.
- Retry workflow will run only when `.touchflow-feature/READY` changes, preventing partial source updates from triggering duplicate Builds.
- Next: upload all 9 updated segments, verify reconstructed SHA, update READY last, then inspect the new CI result.


---

# نقطهٔ توقف پایدار — 2026-11-19 23:19 (Europe/Berlin)

## وضعیت دقیق شاخه
- شاخهٔ اجرایی فعال: `feature/touchflow-feature-pack-bundle-fix-2026-11-19`
- آخرین commit تأییدشده: `80e62c645a378366431119eaae243945d56e9177`
- Backup قبل از اصلاح CI: `backup/touchflow-feature-pack-before-ci-fix-2026-11-19`
- شاخهٔ اصلی: تغییری نکرده است؛ merge انجام نشده.
- PR برای این بسته هنوز ساخته نشده است.

## وضعیت Build قبلی
- Run: [44600591255](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44600591255)
- آرشیو و جداسازی package تأیید شدند؛ JDK 17، Gradle 8.9 و Android SDK 35 نیز آماده شدند.
- کامپایل Kotlin شکست خورد؛ علت ریشه‌ای فقط import جاافتادهٔ `android.os.Bundle` در `MacroWidget.kt` بود.
- import در سورس اصلاح شد. تست مستقل Split: 10/10 assertion passed.
- APK در آن Run تولید نشد؛ مرحله‌های verify و upload اجرا نشدند.

## وضعیت آرشیو اصلاح‌شده
- آرشیو محلی: `/mnt/data/touchflow-feature-source-fix1.tar.xz`
- فایل Base64 محلی: `/mnt/data/touchflow-feature-source-fix1.b64`
- SHA-256 تأییدشده با Python و `sha256sum`: `117becdf5b48a585303c1a9cc4d2648038795abdcada00639f2c4b5a7989a4d0`
- حجم: 25,384 bytes؛ Base64: 33,848 chars.
- ساختار قطعات: 8 قطعهٔ 4,200 کاراکتری + قطعهٔ پایانی 248 کاراکتری.
- هر ۹ قطعه از GitHub مجدداً خوانده شدند؛ Git Blob SHA هر قطعه با SHA متناظر قطعهٔ محلی برابر است.
- قطعهٔ ناسازگار قبلی فقط `part-07` بود؛ اکنون به مقدار دقیق محلی تصحیح شده و Git Blob SHA آن `4c76f01cde974d12e31df7c9e032695f797b89b7` است.
- نکتهٔ ابزار: یک پیاده‌سازی دستی SHA-256 در محیط JS عدد متفاوتی گزارش کرد؛ به آن خروجی اعتماد نکن. معیار قابل اتکا فعلاً SHA-256 محلی Python و برابری Git Blob هر ۹ قطعه است. CI با `sha256sum -c` مرجع نهایی تطبیق آرشیو روی Runner خواهد بود.

## وضعیت Workflow اصلاحی
- فایل: `.github/workflows/build-touchflow-feature-pack.yml`
- فقط روی branch `feature/touchflow-feature-pack-bundle-fix-2026-11-19` اجرا می‌شود.
- فقط تغییر `.touchflow-feature/READY` آن را trigger می‌کند؛ آپلود تکه‌های آرشیو باعث Build ناقص یا چندباره نمی‌شود.
- expected SHA در Workflow به `117becdf5b48a585303c1a9cc4d2648038795abdcada00639f2c4b5a7989a4d0` تغییر کرده است.
- **گام بعدی فوری:** محتوای `.touchflow-feature/READY` را به همین SHA تغییر بده؛ این تغییر Run اصلاحی را آغاز می‌کند.

## تعداد مراحل باقی‌مانده
1. **CI مجدد:** تغییر READY، بررسی sha256/tar و اجرای JUnit + assembleDebug. (هنوز انجام نشده)
2. **رفع خطاهای احتمالی:** فقط بر اساس خطای واقعی CI، با backup و checkpoint تازه. (در انتظار)
3. **اعتبارسنجی APK:** package باید `com.grandmaconnect.feature`، label باید `TouchFlow Feature Preview` و امضا معتبر باشد؛ سپس Artifact APK بارگذاری شود. (در انتظار)
4. **تست واقعی Galaxy A14 / Android 13:** تمام‌صفحه، درج برنامه در مرز gesture، اجرای چند برنامه، Back، Split/Unsplit و عدم تغییر دادهٔ ماکرو، Widget، شروع سریع و بسته‌شدن Activity، توقف از اعلان، نمایش فارسی. (در انتظار؛ CI به‌تنهایی جای این تست را نمی‌گیرد)
5. **بازبینی نهایی و PR:** Diff کامل و نتایج تست بررسی شوند؛ PR بساز، اما تا تأیید صریح صاحب پروژه merge نکن. (در انتظار)

## محدودیت‌ها و تصمیم‌های تثبیت‌شده
- ضبط فعلی داخل TouchFlow است. ضبط خام لمس‌های سایر برنامه‌ها روی Android 13 هنوز قابلیت اثبات‌شده نیست؛ فعلاً sequence چندبرنامه‌ای در playback از طریق AccessibilityService ارائه می‌شود.
- تمام‌صفحهٔ موجود حفظ می‌شود؛ هنگام ضبط، «＋ برنامه» فقط در مرز امن پس از پایان گروه کامل لمس درج می‌شود تا خود دکمه/انتخاب برنامه داخل ماکرو ذخیره نشود.
- Split فقط marker میان گروه‌های کامل است؛ نباید event، coordinate، timestamp یا action حذف/جابجا شود.
- ویجت برای هر widgetId به macroId مشخص متصل می‌شود؛ اجرای موفق باید Activity را باز نگذارد و توقف از Notification ممکن باشد.
- فونت اختصاصی هنوز اضافه نشده؛ این نسخه از `sans-serif` سیستم و fallback فارسی/عربی Android استفاده می‌کند. خوانایی روی گوشی تأیید نشده است.
- نسخهٔ آزمایشی با package جدا ساخته می‌شود؛ هرگز APK مرجع یا نصب فعلی را overwrite نکن.


### 2026-11-19 23:20 — اجرای CI اصلاح‌شده آغاز شد
Status: IN PROGRESS
- Latest branch HEAD: `8f4092e077eaa82c196d6b8403201b3ed3df72a8`.
- READY اکنون SHA اصلاح‌شده `117becdf5b48a585303c1a9cc4d2648038795abdcada00639f2c4b5a7989a4d0` را دارد.
- Workflow run: [44602552416](https://github.com/hosseinasgari898989-dev/Touchflow/actions/runs/44602552416).
- Run head SHA: `8f4092e077eaa82c196d6b8403201b3ed3df72a8`.
- Archive verification: SUCCESS (including sha256sum, tar list/extract and required source file checks).
- Preview identity isolation: SUCCESS.
- JDK 17: SUCCESS.
- در آخرین بررسی Gradle 8.9 در حال آماده‌سازی بود؛ Android SDK و تست/Build هنوز pending بودند.
- Artifact APK هنوز ایجاد نشده است.
- تعداد milestoneهای اصلی باقیمانده: 5؛ milestone شمارهٔ 1 (CI retest) اکنون در حال اجراست؛ پس از موفقیت آن 4 milestone اصلی دیگر باقی می‌ماند.
