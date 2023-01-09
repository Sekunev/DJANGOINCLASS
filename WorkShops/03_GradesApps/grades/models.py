from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_name = models.CharField(max_length=50)

    def __str__(self):
        return self.teacher_name
        
class Lessons(models.Model):
    lesson_name = models.CharField(max_length=50)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.lesson_name

class Students(models.Model):
    student_number = models.IntegerField()
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.first_name

class Grade(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE, related_name="student_grades")
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, related_name="lesson_grades")
    grade = models.PositiveSmallIntegerField()
    
    # Bizim çözüm
    # class Meta:
    #     unique_together = ('student', 'lesson')
    
    def __str__(self):
        return str(self.grade)

    # modelde uniquelik sağlamak için aşağıdaki metodu kullanıyoruz.Bu metotla admin panelde de kısıtlama yapmış oluyoruz. Burada yaptığımız işlem UniqueConstraint metoduna birleştiğinde unique olmasını istediğimiz fieldları veriyoruz o bizim yerimize kontrolü sağlıyor.Örneğimizde lesson ve student eşleşmeleri böylelikle istediğimiz gibi tek olmuş oluyor. Aynı isimde ders birden fazla öğrenci ile eşleşebilir ama aynı öğrenci ile eşleşemez aynı şekilde öğrenci için de öyle.
    # Not: class Meta işlemlerinde makemigrations ve migrate komutlarını çalıştırmamız gerekir   
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'lesson'], name='unique_student_lesson')
        ]