# دليل نشر المكتبات الثلاث — FAHAD SAAD ALBALWI

## 1. إنشاء الحسابات
1. أنشئ حساب GitHub: https://github.com/signup، وفعّل البريد الإلكتروني والمصادقة الثنائية.
2. أنشئ حساب PyPI: https://pypi.org/account/register/، وفعّل البريد الإلكتروني والمصادقة الثنائية. لا تشارك كلمات المرور أو رموز الاسترداد.
3. أنشئ مستودع GitHub عام باسم `alula-python-ecosystem` وارفع محتويات *هذا المجلد* إلى الجذر مباشرة (المجلدات الثلاثة و `.github`). عند الرفع من المتصفح انتبه إلى أن المجلدات المخفية مثل `.github` قد تحتاج الرفع باستخدام Git/GitHub Desktop.

## 2. فحص المستودع
- افتح GitHub → Actions → `Python tests` → `Run workflow`، أو ادفع تعديلًا جديدًا لتعمل الاختبارات تلقائيًا.
- لا تنشر إذا فشلت الاختبارات.

## 3. إعداد النشر الموثوق في PyPI
قبل تشغيل أي عملية نشر، افتح PyPI → Publishing → Add a new pending publisher. أنشئ ثلاثة إعدادات بالبيانات التالية (اكتب اسم المستخدم الفعلي في Owner):

| Package name | GitHub repository | Workflow filename | GitHub environment |
| --- | --- | --- | --- |
| `alula-cropwatch` | `alula-python-ecosystem` | `publish-alula-cropwatch.yml` | `pypi` |
| `alula-waterwise` | `alula-python-ecosystem` | `publish-alula-waterwise.yml` | `pypi` |
| `alula-heritage` | `alula-python-ecosystem` | `publish-alula-heritage.yml` | `pypi` |

تحقق من توفر الأسماء في PyPI؛ إذا كان الاسم محجوزًا، يجب تغيير `project.name` وإعداد PyPI ووصف النشر معًا. إنشاء النشر المعلق لا يحجز الاسم قبل قبول الحزمة.

ثم افتح المستودع GitHub → Settings → Environments → New environment → سمّه `pypi`، وفعّل قيود الموافقة المناسبة. راجع سياسة أمان المستودع قبل السماح بنشر آلي.

## 4. النشر
GitHub → Actions → اختر `Publish alula-cropwatch` ثم `Run workflow`. كررها للمكتبتين الأخريين بعد نجاح الأولى، وبعد تأكدك من إعدادات PyPI. لا توجد حاجة إلى إدخال كلمة مرور أو API token في ملفات المشروع.

بعد نجاح النشر تحقق من رابط المشروع على `https://pypi.org/` وجرب `python -m pip install alula-cropwatch` في بيئة Python جديدة.

## 5. لاحقًا
ارفع رقم الإصدار في `pyproject.toml` عند كل تحديث (مثل `0.1.1` أو `0.2.0`)؛ لا تعيد نشر رقم الإصدار نفسه. سجّل ميزات وتغييرات الإصدار واختبر التثبيت في بيئة نظيفة.

المشروع مستقل وغير تابع أو معتمد من الهيئة الملكية لمحافظة العلا. الإصدار الأول تجريبي ولا يوفر بيانات أقمار صناعية أو طقس مباشرة.
