import matplotlib.pyplot as plt

# البيانات
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temperature = [22, 24, 19, 23, 25, 27, 26]

# إعداد شكل الرسم (الحجم والألوان)
plt.figure(figsize=(8, 5))  # حجم الرسم
plt.plot(days, temperature, color='orange', marker='o', markerfacecolor='red', 
         linestyle='-', linewidth=2, markersize=8)

# عناوين المحاور والعنوان الرئيسي
plt.xlabel('Days of the Week', fontsize=12, color='blue')
plt.ylabel('Temperature (°C)', fontsize=12, color='blue')
plt.title('🌤️ Temperature Variation Over a Week', fontsize=14, fontweight='bold')

# إضافة شبكة خلفية
plt.grid(True, linestyle='--', alpha=0.6)

# تظبيط شكل المحاور
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)

# عرض الرسم
plt.tight_layout()
plt.show()
