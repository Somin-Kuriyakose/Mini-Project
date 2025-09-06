import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from users.models import Skill

skills = [
    "Programming",
    "Math",
    "Communication",
    "Design",
    "Problem-Solving",
    "Leadership",
    "Creativity",
    "Critical Thinking",
    "Writing",
    "Teamwork",
]

for s in skills:
    skill, created = Skill.objects.get_or_create(name=s)
    if created:
        print(f"Added skill: {s}")
    else:
        print(f"Skill already exists: {s}")
