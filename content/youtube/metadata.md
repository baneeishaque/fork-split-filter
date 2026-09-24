# YouTube upload metadata

Copy-paste metadata per locale. Durations are the rendered video lengths. Chapter timestamps
are the English timeline (2:38); other locales shift by a few seconds — the chapter *labels*
stay valid, only the numbers need adjusting if you upload a non-English cut as the primary
video.

Full metadata (title + description + tags) is provided for the ten uploads with the widest
reach; the remaining 27 locales get a compact table with localized titles and durations.
Every locale's subtitles are in `subtitles/`, and every narrated locale's audio track is in
the master MKV (`build/video/master-multiaudio.mkv`).

## Thumbnail

Text overlay on a dark slide: **"Two panes. Two filters."** — pair with the two-pane app
screenshot (`shot-two-panes.png`) so the independent filters are visible in the thumbnail
itself.

***

## English (`en`) — 2:38

### Title

```text
Two panes, two filters: the git companion Fork doesn't have
```

### Description

```text
Two panes, two filters: a small companion TUI that gives Fork's staged and unstaged lists
independent search fields.

Every git client shares one filter box between the staged and unstaged changes. This project
fixes that papercut: a Python + Textual terminal app, launched from Fork's repository context
menu, with one search field per pane. It parses git status porcelain v2 (renames, conflicts,
and untracked files handled explicitly), keeps the filter a pure function, serializes
refreshes with one lock, and proves it all with 12 tests against real repositories.

The repository even narrates its own walkthrough: this video ships with narration in 20
languages and subtitles in 37.

Code + architecture docs: https://github.com/baneeishaque-ompventure/fork-split-filter

Chapters:
0:00 One filter is not enough
0:11 Two panes, two filters
0:23 One refresh, one pipeline
0:36 Parse the format, not the text
0:50 A filter is a pure function
1:03 Refresh without races
1:19 Keyboard-first operations
1:32 Lives inside the client
1:45 Twelve tests prove it
1:58 The trade-offs, honestly
2:14 What it adds up to
2:30 Steal the pattern

What the tool proves:
- Independent staged/unstaged filters in one terminal window
- Machine-format parsing: porcelain v2, NUL-delimited, renames and conflicts explicit
- A pure filter engine shared by both panes
- One asyncio.Lock serializing timer, keystroke, and manual refreshes
- Stage/unstage/open/reveal/copy without leaving the keyboard
- 12 tests: literal porcelain bytes, real scratch repositories, Textual pilot

Stack: Python 3.12, Textual, pytest. License: MIT
```

### Tags

```text
git, fork git client, developer tools, python, textual, tui, terminal, version control,
staged changes, unstaged changes, git status, porcelain v2, productivity, open source,
software engineering
```

***

## Hindi (`hi`) — 3:18

### Title

```text
एक फ़िल्टर काफ़ी नहीं: Fork के लिए दो पैन, दो फ़िल्टर
```

### Description

```text
दो पैन, दो फ़िल्टर: Fork के staged और unstaged पैन को अलग-अलग सर्च फ़ील्ड देने वाला एक छोटा
टर्मिनल ऐप। हर git क्लाइंट एक ही फ़िल्टर बॉक्स दोनों सूचियों के बीच साझा करता है — यह टूल
उसी छोटी समस्या का हल है।

टूल `git status --porcelain=v2 -z` पढ़ता है (rename, conflict और untracked फ़ाइलें स्पष्ट रूप
से), फ़िल्टर को एक शुद्ध फ़ंक्शन रखता है, रीफ़्रेश को एक लॉक से क्रमबद्ध करता है, और असली
रिपॉज़िटरी पर 12 टेस्ट के साथ सब कुछ साबित करता है। इस वीडियो में 20 भाषाओं में नैरेशन और
37 भाषाओं में सबटाइटल हैं।

कोड + आर्किटेक्चर डॉक्स: https://github.com/baneeishaque-ompventure/fork-split-filter

अध्याय (अंग्रेज़ी टाइमलाइन):
0:00 एक फ़िल्टर काफ़ी नहीं
0:11 दो पैन, दो फ़िल्टर
0:23 एक रीफ़्रेश, एक पाइपलाइन
0:36 फ़ॉर्मैट पार्स करें, टेक्स्ट नहीं
0:50 फ़िल्टर एक शुद्ध फ़ंक्शन है
1:03 रेस के बिना रीफ़्रेश
1:19 कीबोर्ड-पहले ऑपरेशन
1:32 क्लाइंट के अंदर रहता है
1:45 बारह टेस्ट इसे साबित करते हैं
1:58 समझौते, ईमानदारी से
2:14 कुल मिलाकर क्या बनता है
2:30 पैटर्न चुरा लें

स्टैक: Python 3.12, Textual, pytest. लाइसेंस: MIT
```

### Tags

```text
git, fork, developer tools, python, textual, terminal, version control, productivity,
open source, hindi
```

***

## Bengali (`bn`) — 3:28

### Title

```text
একটি ফিল্টার যথেষ্ট নয়: Fork-এর জন্য দুই প্যান, দুই ফিল্টার
```

### Description

```text
দুই প্যান, দুই ফিল্টার: Fork-এর staged ও unstaged তালিকাকে আলাদা সার্চ ফিল্ড দেওয়া একটি
ছোট টার্মিনাল অ্যাপ। প্রতিটি git ক্লায়েন্ট দুই তালিকার মধ্যে একটি ফিল্টার বক্স ভাগ করে —
এই টুলটি সেই সমস্যার সমাধান।

টুলটি `git status --porcelain=v2 -z` পড়ে (rename, conflict ও untracked ফাইল স্পষ্টভাবে),
ফিল্টারকে একটি বিশুদ্ধ ফাংশন রাখে, একটি লক দিয়ে রিফ্রেশ ক্রমবদ্ধ করে, এবং আসল রিপোজিটরিতে
12টি টেস্ট দিয়ে সব প্রমাণ করে। এই ভিডিওতে 20টি ভাষায় ন্যারেশন ও 37টি ভাষায় সাবটাইটেল আছে।

কোড + আর্কিটেকচার ডক্স: https://github.com/baneeishaque-ompventure/fork-split-filter

অধ্যায় (ইংরেজি টাইমলাইন):
0:00 একটি ফিল্টার যথেষ্ট নয়
0:11 দুটি প্যান, দুটি ফিল্টার
0:23 এক রিফ্রেশ, এক পাইপলাইন
0:36 ফরম্যাট পার্স করুন, টেক্সট নয়
0:50 একটি ফিল্টার একটি বিশুদ্ধ ফাংশন
1:03 রেস ছাড়া রিফ্রেশ
1:19 কীবোর্ড-প্রথম অপারেশন
1:32 ক্লায়েন্টের ভিতরে থাকে
1:45 বারোটি টেস্ট প্রমাণ করে
1:58 আপসগুলো, সৎভাবে
2:14 সব মিলিয়ে যা দাঁড়ায়
2:30 প্যাটার্নটি চুরি করুন

স্ট্যাক: Python 3.12, Textual, pytest. লাইসেন্স: MIT
```

### Tags

```text
git, fork, developer tools, python, textual, terminal, version control, bengali,
open source, productivity
```

***

## Telugu (`te`) — 3:56

### Title

```text
ఒక వడపోత సరిపోదు: Fork కోసం రెండు పేన్‌లు, రెండు వడపోతలు
```

### Description

```text
రెండు పేన్‌లు, రెండు వడపోతలు: Fork యొక్క staged మరియు unstaged జాబితాలకు వేర్వేరు సెర్చ్
ఫీల్డ్‌లు ఇచ్చే చిన్న టెర్మినల్ యాప్. ప్రతి git క్లయింట్ ఒకే ఫిల్టర్ బాక్స్‌ను రెండు
జాబితాల మధ్య పంచుకుంటుంది — ఈ టూల్ ఆ సమస్యకు పరిష్కారం.

ఇది `git status --porcelain=v2 -z`ను చదువుతుంది (rename, conflict, untracked ఫైళ్లు స్పష్టంగా),
ఫిల్టర్‌ను స్వచ్ఛమైన ఫంక్షన్‌గా ఉంచుతుంది, ఒక లాక్‌తో రిఫ్రెష్‌లను క్రమబద్ధం చేస్తుంది,
నిజమైన రిపాజిటరీలపై 12 పరీక్షలతో నిరూపిస్తుంది. ఈ వీడియోలో 20 భాషల్లో నెరేషన్ మరియు 37
భాషల్లో సబ్‌టైటిల్స్ ఉన్నాయి.

కోడ్ + ఆర్కిటెక్చర్ డాక్స్: https://github.com/baneeishaque-ompventure/fork-split-filter

అధ్యాయాలు (ఆంగ్ల టైమ్‌లైన్):
0:00 ఒక వడపోత సరిపోదు
0:11 రెండు పేన్‌లు, రెండు వడపోతలు
0:23 ఒక రిఫ్రెష్, ఒక పైప్‌లైన్
0:36 ఫార్మాట్‌ను పార్స్ చేయండి, వచనాన్ని కాదు
0:50 వడపోత ఒక స్వచ్ఛమైన ఫంక్షన్
1:03 రేసులు లేని రిఫ్రెష్
1:19 కీబోర్డ్ మొదటి కార్యకలాపాలు
1:32 క్లయింట్ లోపల నివసిస్తుంది
1:45 పన్నెండు పరీక్షలు నిరూపిస్తాయి
1:58 రాజీలు, నిజాయితీగా
2:14 మొత్తం ఏమి వస్తుంది
2:30 ఈ నమూనాను దొంగిలించండి

స్టాక్: Python 3.12, Textual, pytest. లైసెన్స్: MIT
```

### Tags

```text
git, fork, developer tools, python, textual, terminal, telugu, version control,
open source, productivity
```

***

## Tamil (`ta`) — 3:46

### Title

```text
ஒரு வடிகட்டி போதாது: Fork-க்கான இரண்டு சாளரங்கள், இரண்டு வடிகட்டிகள்
```

### Description

```text
இரண்டு சாளரங்கள், இரண்டு வடிகட்டிகள்: Fork-இன் staged மற்றும் unstaged பட்டியல்களுக்கு தனித்தனி
தேடல் புலங்களைத் தரும் சிறிய முனைய செயலி. ஒவ்வொரு git கிளையண்டும் ஒரே வடிகட்டிப் பெட்டியை
இரு பட்டியல்களுக்கும் பகிர்ந்து கொள்கிறது — இந்தக் கருவி அந்தச் சிக்கலுக்கான தீர்வு.

இது `git status --porcelain=v2 -z`-ஐ வாசிக்கிறது (rename, conflict, untracked கோப்புகள்
வெளிப்படையாக), வடிகட்டியை ஒரு தூய சார்பாக வைத்திருக்கிறது, ஒரு lock மூலம் புதுப்பிப்புகளை
வரிசைப்படுத்துகிறது, உண்மையான களஞ்சியங்களில் 12 சோதனைகளுடன் நிரூபிக்கிறது. இந்த வீடியோவில்
20 மொழிகளில் குரல் மற்றும் 37 மொழிகளில் வசன வரிகள் உள்ளன.

குறியீடு + கட்டமைப்பு ஆவணங்கள்: https://github.com/baneeishaque-ompventure/fork-split-filter

அத்தியாயங்கள் (ஆங்கில காலவரிசை):
0:00 ஒரு வடிகட்டி போதாது
0:11 இரண்டு சாளரங்கள், இரண்டு வடிகட்டிகள்
0:23 ஒரு புதுப்பிப்பு, ஒரு வழித்தடம்
0:36 வடிவத்தைப் பாகுபடுத்து, உரையை அல்ல
0:50 வடிகட்டி ஒரு தூய சார்பு
1:03 ரேஸ் இல்லாத புதுப்பிப்பு
1:19 விசைப்பலகை முதன்மை செயல்பாடுகள்
1:32 கிளையண்டுக்குள் வாழ்கிறது
1:45 பன்னிரண்டு சோதனைகள் நிரூபிக்கின்றன
1:58 சமரசங்கள், நேர்மையாக
2:14 இதன் மொத்த விளைவு
2:30 இந்த முறையைத் திருடுங்கள்

ஸ்டாக்: Python 3.12, Textual, pytest. உரிமம்: MIT
```

### Tags

```text
git, fork, developer tools, python, textual, terminal, tamil, version control,
open source, productivity
```

***

## Kannada (`kn`) — 3:59

### Title

```text
ಒಂದು ಫಿಲ್ಟರ್ ಸಾಕಾಗುವುದಿಲ್ಲ: Fork ಗಾಗಿ ಎರಡು ಫಲಕ, ಎರಡು ಫಿಲ್ಟರ್
```

### Description

```text
ಎರಡು ಫಲಕ, ಎರಡು ಫಿಲ್ಟರ್: Fork ನ staged ಮತ್ತು unstaged ಪಟ್ಟಿಗಳಿಗೆ ಪ್ರತ್ಯೇಕ ಹುಡುಕಾಟ ಕ್ಷೇತ್ರಗಳನ್ನು
ನೀಡುವ ಸಣ್ಣ ಟರ್ಮಿನಲ್ ಆ್ಯಪ್. ಪ್ರತಿ git ಕ್ಲೈಂಟ್ ಒಂದೇ ಫಿಲ್ಟರ್ ಬಾಕ್ಸ್ ಅನ್ನು ಎರಡೂ ಪಟ್ಟಿಗಳ ನಡುವೆ
ಹಂಚಿಕೊಳ್ಳುತ್ತದೆ — ಈ ಪರಿಕರ ಆ ಸಮಸ್ಯೆಯ ಪರಿಹಾರ.

ಇದು `git status --porcelain=v2 -z` ಅನ್ನು ಓದುತ್ತದೆ (rename, conflict, untracked ಫೈಲ್‌ಗಳು
ಸ್ಪಷ್ಟವಾಗಿ), ಫಿಲ್ಟರ್ ಅನ್ನು ಶುದ್ಧ ಫಂಕ್ಷನ್ ಆಗಿ ಇರಿಸುತ್ತದೆ, ಒಂದು lock ನಿಂದ ರಿಫ್ರೆಶ್‌ಗಳನ್ನು
ಕ್ರಮಬದ್ಧಗೊಳಿಸುತ್ತದೆ, ನಿಜವಾದ ರಿಪೊಗಳಲ್ಲಿ 12 ಪರೀಕ್ಷೆಗಳಿಂದ ಸಾಬೀತು ಮಾಡುತ್ತದೆ. ಈ ವೀಡಿಯೊದಲ್ಲಿ
20 ಭಾಷೆಗಳಲ್ಲಿ ನೆರೇಶನ್ ಮತ್ತು 37 ಭಾಷೆಗಳಲ್ಲಿ ಉಪಶೀರ್ಷಿಕೆಗಳಿವೆ.

ಕೋಡ್ + ಆರ್ಕಿಟೆಕ್ಚರ್ ಡಾಕ್ಸ್: https://github.com/baneeishaque-ompventure/fork-split-filter

ಅಧ್ಯಾಯಗಳು (ಇಂಗ್ಲಿಷ್ ಟೈಮ್‌ಲೈನ್):
0:00 ಒಂದು ಫಿಲ್ಟರ್ ಸಾಕಾಗುವುದಿಲ್ಲ
0:11 ಎರಡು ಫಲಕ, ಎರಡು ಫಿಲ್ಟರ್
0:23 ಒಂದು ರಿಫ್ರೆಶ್, ಒಂದು ಪೈಪ್ಲೈನ್
0:36 ಪಠ್ಯವನ್ನಲ್ಲ, ಸ್ವರೂಪವನ್ನು ಪಾರ್ಸ್ ಮಾಡಿ
0:50 ಫಿಲ್ಟರ್ ಒಂದು ಶುದ್ಧ ಫಂಕ್ಷನ್
1:03 ರೇಸ್‌ಗಳಿಲ್ಲದೆ ರಿಫ್ರೆಶ್
1:19 ಕೀಬೋರ್ಡ್-ಮೊದಲ ಕಾರ್ಯಾಚರಣೆಗಳು
1:32 ಕ್ಲೈಂಟ್‌ನ ಒಳಗೇ ವಾಸಿಸುತ್ತದೆ
1:45 ಹನ್ನೆರಡು ಪರೀಕ್ಷೆಗಳು ಸಾಬೀತು ಮಾಡುತ್ತವೆ
1:58 ಒಳಿತು-ಕೆಡುಕುಗಳು, ಪ್ರಾಮಾಣಿಕವಾಗಿ
2:14 ಇದೆಲ್ಲ ಸೇರಿ ಏನಾಗುತ್ತದೆ
2:30 ಮಾದರಿಯನ್ನು ಕದಿಯಿರಿ

ಸ್ಟಾಕ್: Python 3.12, Textual, pytest. ಪರವಾನಗಿ: MIT
```

### Tags

```text
git, fork, developer tools, python, textual, terminal, kannada, version control,
open source, productivity
```

***

## Malayalam (`ml`) — 2:35

### Title

```text
ഒരു ഫിൽട്ടർ മതിയാകില്ല: Fork-നായി രണ്ട് പാനൽ, രണ്ട് ഫിൽട്ടർ
```

### Description

```text
രണ്ട് പാനൽ, രണ്ട് ഫിൽട്ടർ: Fork-ന്റെ staged, unstaged ലിസ്റ്റുകൾക്ക് വെവ്വേറെ സെർച്ച് ഫീൽഡുകൾ
നൽകുന്ന ചെറിയ ടെർമിനൽ ആപ്പ്. ഓരോ git ക്ലയന്റും ഒരേ ഫിൽട്ടർ ബോക്സ് രണ്ട് ലിസ്റ്റുകൾക്കിടയിൽ
പങ്കിടുന്നു — ഈ ടൂൾ ആ പ്രശ്നത്തിന്റെ പരിഹാരമാണ്.

ഇത് `git status --porcelain=v2 -z` വായിക്കുന്നു (rename, conflict, untracked ഫയലുകൾ
വ്യക്തമായി), ഫിൽട്ടറിനെ ഒരു ശുദ്ധ ഫങ്ക്ഷനായി നിലനിർത്തുന്നു, ഒരു lock ഉപയോഗിച്ച്
പുതുക്കലുകൾ ക്രമീകരിക്കുന്നു, യഥാർത്ഥ റിപ്പോകളിൽ 12 പരിശോധനകളോടെ തെളിയിക്കുന്നു. ഈ
വീഡിയോയിൽ 20 ഭാഷകളിൽ നരേഷൻ, 37 ഭാഷകളിൽ സബ്ടൈറ്റിലുകൾ എന്നിവയുണ്ട്.

കോഡ് + ആർക്കിടെക്ചർ ഡോക്സ്: https://github.com/baneeishaque-ompventure/fork-split-filter

അധ്യായങ്ങൾ (ഇംഗ്ലീഷ് ടൈംലൈൻ):
0:00 ഒരു ഫിൽട്ടർ മതിയാകില്ല
0:11 രണ്ട് പാനൽ, രണ്ട് ഫിൽട്ടർ
0:23 ഒരു പുതുക്കൽ, ഒരു പൈപ്പ്ലൈൻ
0:36 ടെക്സ്റ്റല്ല, ഫോർമാറ്റ് പാർസ് ചെയ്യൂ
0:50 ഫിൽട്ടർ ഒരു ശുദ്ധ ഫങ്ക്ഷൻ
1:03 റേസുകളില്ലാതെ പുതുക്കൽ
1:19 കീബോർഡ്-പ്രഥമ പ്രവർത്തനങ്ങൾ
1:32 ക്ലയന്റിനുള്ളിൽ ജീവിക്കുന്നു
1:45 പന്ത്രണ്ട് പരിശോധനകൾ തെളിയിക്കുന്നു
1:58 വിട്ടുവീഴ്ചകൾ, സത്യസന്ധമായി
2:14 ഇതെല്ലാം കൂടിയാൽ എന്താകുന്നു
2:30 പാറ്റേൺ മോഷ്ടിക്കൂ

സ്റ്റാക്ക്: Python 3.12, Textual, pytest. ലൈസൻസ്: MIT
```

### Tags

```text
git, fork, developer tools, python, textual, terminal, malayalam, version control,
open source, productivity
```

***

## Arabic (`ar`) — 4:46

### Title

```text
مرشّح واحد لا يكفي: لوحتان ومرشّحان لـ Fork
```

### Description

```text
لوحتان ومرشّحان: تطبيق طرفية صغير يمنح قائمتي staged و unstaged في Fork حقلي بحث مستقلّين.
كل عميل git يشارك مربّع تصفية واحدًا بين القائمتين — هذه الأداة هي الحل.

يقرأ التطبيق `git status --porcelain=v2 -z` (إعادة التسمية والتعارضات والملفات غير المتتبَّعة
بشكل صريح)، ويُبقي المرشّح دالة نقية، ويرتّب التحديثات بقفل واحد، ويثبت ذلك كله بـ 12 اختبارًا
على مستودعات حقيقية. يتضمّن هذا الفيديو سردًا بعشرين لغة وترجمات بسبع وثلاثين لغة.

الكود ووثائق البنية: https://github.com/baneeishaque-ompventure/fork-split-filter

الفصول (الخط الزمني الإنجليزي):
0:00 مرشّح واحد لا يكفي
0:11 لوحتان، ومرشّحان
0:23 تحديث واحد، وخطّ واحد
0:36 حلّل الصيغة، لا النص
0:50 المرشّح دالة نقية
1:03 تحديث بلا تسابقات
1:19 عمليات تبدأ من لوحة المفاتيح
1:32 يعيش داخل العميل
1:45 اثنا عشر اختبارًا تثبته
1:58 المقايضات، بصدق
2:14 إلى ماذا يؤدي ذلك
2:30 اسرق النمط

التقنيات: Python 3.12 وTextual وpytest. الرخصة: MIT
```

### Tags

```text
git, fork, developer tools, python, textual, terminal, arabic, version control,
open source, productivity
```

***

## German (`de`) — 3:34

### Title

```text
Zwei Bereiche, zwei Filter: der Git-Begleiter, den Fork nicht hat
```

### Description

```text
Zwei Bereiche, zwei Filter: eine kleine Terminal-App, die den Staged- und Unstaged-Listen in
Fork jeweils ein eigenes Suchfeld gibt. Jeder Git-Client teilt ein einziges Filterfeld
zwischen beiden Listen — dieses Tool behebt genau das.

Es liest `git status --porcelain=v2 -z` (Renames, Konflikte und untracked Dateien explizit),
hält den Filter als reine Funktion, serialisiert Refreshes mit einem Lock und beweist alles
mit 12 Tests gegen echte Repositories. Dieses Video liefert Narration in 20 Sprachen und
Untertitel in 37.

Code + Architektur-Doku: https://github.com/baneeishaque-ompventure/fork-split-filter

Kapitel (englische Timeline):
0:00 Ein Filter reicht nicht
0:11 Zwei Bereiche, zwei Filter
0:23 Ein Refresh, eine Pipeline
0:36 Das Format parsen, nicht den Text
0:50 Ein Filter ist eine reine Funktion
1:03 Refresh ohne Wettläufe
1:19 Tastaturzentrierte Bedienung
1:32 Lebt im Client
1:45 Zwölf Tests beweisen es
1:58 Die Kompromisse, ehrlich
2:14 Was dabei herauskommt
2:30 Stiehl das Muster

Stack: Python 3.12, Textual, pytest. Lizenz: MIT
```

### Tags

```text
git, fork, developer tools, python, textual, terminal, version control, deutsch,
open source, productivity
```

***

## Spanish (`es`) — 2:59

### Title

```text
Dos paneles, dos filtros: el compañero de Git que Fork no tiene
```

### Description

```text
Dos paneles, dos filtros: una pequeña app de terminal que da campos de búsqueda independientes
a las listas staged y unstaged de Fork. Cada cliente de git comparte un único cuadro de filtro
entre ambas listas — esta herramienta resuelve justo eso.

Lee `git status --porcelain=v2 -z` (renombrados, conflictos y archivos sin seguimiento de forma
explícita), mantiene el filtro como una función pura, serializa las actualizaciones con un lock
y lo demuestra con 12 pruebas contra repositorios reales. Este vídeo incluye narración en 20
idiomas y subtítulos en 37.

Código + documentación de arquitectura: https://github.com/baneeishaque-ompventure/fork-split-filter

Capítulos (línea de tiempo en inglés):
0:00 Un filtro no es suficiente
0:11 Dos paneles, dos filtros
0:23 Una actualización, un pipeline
0:36 Analiza el formato, no el texto
0:50 Un filtro es una función pura
1:03 Actualiza sin carreras
1:19 Operaciones primero con el teclado
1:32 Vive dentro del cliente
1:45 Doce pruebas lo demuestran
1:58 Los compromisos, con honestidad
2:14 Lo que suma todo esto
2:30 Roba el patrón

Stack: Python 3.12, Textual, pytest. Licencia: MIT
```

### Tags

```text
git, fork, developer tools, python, textual, terminal, version control, español,
open source, productivity
```

***

## Compact metadata (remaining 27 locales)

Localized video titles (the hook line from each locale's `translations/<locale>.json`) and
rendered durations. All 27 are subtitle-only locales except `fr`, `id`, `it`, `ja`, `ko`,
`pt`, `ru`, `th`, `tr`, `vi`, and `zh`, which also carry narration in the master MKV.

| Locale | Title                                                        | Duration |
| ------ | ------------------------------------------------------------ | -------- |
| `as`   | এটা ফিল্টাৰে যথেষ্ট নহয়                                      | 3:02     |
| `brx`  | मोनसेबे फिल्टारजों हाया                                        | 3:14     |
| `doi`  | इक फिल्टर काफी नेईं                                            | 3:41     |
| `gu`   | એક ફિલ્ટર પૂરતું નથી                                          | 3:27     |
| `kok`  | एक फिल्टर पुरो न्हय                                            | 2:59     |
| `ks`   | اَکھ فلٹر کٲفی چھُ نہٕ                                          | 3:48     |
| `mai`  | एकटा फिल्टर पर्याप्त नै अछि                                    | 3:38     |
| `mni`  | ꯐꯤꯜꯇꯔ ꯑꯃꯅ ꯃꯇꯤꯛ ꯂꯩꯇꯦ                                          | 3:12     |
| `mr`   | एक फिल्टर पुरत नाही                                            | 3:01     |
| `ne`   | एउटा फिल्टर पर्याप्त छैन                                       | 3:01     |
| `or`   | ଗୋଟିଏ ଫିଲ୍ଟର ଯଥେଷ୍ଟ ନୁହେଁ                                        | 3:05     |
| `pa`   | ਇੱਕ ਫਿਲਟਰ ਕਾਫ਼ੀ ਨਹੀਂ                                           | 3:37     |
| `sa`   | एकः शोधकः न पर्याप्तः                                          | 2:41     |
| `sat`  | ᱢᱤᱫ ᱯᱷᱤᱞᱴᱟᱨ ᱵᱟᱝ ᱯᱩᱨᱟᱹᱣᱟ                                          | 3:29     |
| `sd`   | هڪ فلٽر ڪافي ناهي                                             | 3:51     |
| `ur`   | ایک فلٹر کافی نہیں                                            | 3:54     |
| `fr`   | Un seul filtre ne suffit pas                                 | 3:17     |
| `id`   | Satu filter tidak cukup                                      | 3:48     |
| `it`   | Un solo filtro non basta                                     | 3:05     |
| `ja`   | フィルターは一つでは足りない                                  | 3:57     |
| `ko`   | 필터 하나로는 부족합니다                                      | 3:26     |
| `pt`   | Um filtro não basta                                          | 3:48     |
| `ru`   | Одного фильтра мало                                          | 3:20     |
| `th`   | ฟิลเตอร์เดียวไม่พอ                                            | 4:12     |
| `tr`   | Tek filtre yetmez                                            | 3:31     |
| `vi`   | Một bộ lọc là chưa đủ                                        | 3:26     |
| `zh`   | 一个过滤器不够用                                              | 3:28     |

## Uploading

1. **Per-locale uploads (simplest):** upload `build/video/<locale>-subtitled.mp4` as separate
   videos (or unlisted variants), using this file for each locale's title and description. Set
   the subtitle language from the matching `subtitles/<locale>.srt` if the embedded track is
   not picked up automatically.
2. **Single video with multi-language audio (Studio feature):** upload `build/video/en.mp4`
   first, then add each narrated locale's audio track (Subtitles → Add audio track) and
   subtitle file from `subtitles/`. Availability of multi-language audio depends on channel
   eligibility.
3. **Local distribution:** `build/video/master-multiaudio.mkv` plays in VLC (Audio → Audio
   Track, Subtitles → Subtitle Track) and is the artifact to archive.
