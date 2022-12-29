from django.db import models


class Todo(models.Model):
    PRIORITY = (
        (1, 'High'),  
        (2, 'Medium'),
        (3, 'Low')
    )
    # neden Tuple? Çünkü değişmeyecek ve daha az yer. daha hızlı.
    task = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    priority = models.SmallIntegerField(choices=PRIORITY, default=2)
    # priority ile öncelik durumunu belirliyoruz. Bunu Dropdown ile (PRIORITY) standart bir formata çevirebiliriz.
    is_done = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task

    # class Meta:
    #     ordering = ["priority"] # priority göre sıralama
