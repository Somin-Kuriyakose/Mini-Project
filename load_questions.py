import django
import os

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from assessments.models import Question, Choice

# Questions data
QUESTIONS = [
    ("You prefer solving logical puzzles or math problems.", ["Yes, always", "Sometimes", "Rarely"]),
    ("When faced with a new gadget, you try to figure out how it works.", ["Always", "Sometimes", "Never"]),
    ("You find it easy to explain ideas to others.", ["Very easy", "Somewhat easy", "Difficult"]),
    ("You enjoy drawing, painting, or designing things.", ["Very much", "Occasionally", "Not at all"]),
    ("You like working in a team to achieve a goal.", ["Always", "Sometimes", "Prefer working alone"]),
    ("You can quickly spot patterns in numbers or shapes.", ["Always", "Sometimes", "Rarely"]),
    ("You enjoy reading books or writing stories.", ["Very much", "Occasionally", "Not at all"]),
    ("You find it easy to remember facts and figures.", ["Always", "Sometimes", "Rarely"]),
    ("You like solving real-life problems (e.g., fixing a broken item).", ["Always", "Sometimes", "Rarely"]),
    ("You enjoy learning about science and technology.", ["Very much", "Somewhat", "Not really"]),
    ("You feel comfortable speaking in front of an audience.", ["Very comfortable", "A little nervous but can manage", "Very nervous"]),
    ("You enjoy organizing tasks and planning events.", ["Yes, I like it", "Sometimes", "Not really"]),
    ("You like working with computers and software.", ["Very much", "Somewhat", "Not at all"]),
    ("You are good at remembering faces and names.", ["Always", "Sometimes", "Rarely"]),
    ("You like experimenting with new ideas or projects.", ["Always", "Sometimes", "Rarely"]),
    ("You enjoy helping others solve their problems.", ["Always", "Sometimes", "Rarely"]),
    ("You can stay focused on a task for a long time.", ["Always", "Sometimes", "Rarely"]),
    ("You enjoy learning languages or new ways of communication.", ["Very much", "Somewhat", "Not really"]),
    ("You like working with tools, machines, or technical equipment.", ["Very much", "Somewhat", "Not at all"]),
    ("You prefer making decisions based on facts rather than feelings.", ["Always", "Sometimes", "Rarely"]),
]

def run():
    for q_text, choices in QUESTIONS:
        question, created = Question.objects.get_or_create(text=q_text, is_active=True)
        if created:
            print(f"✅ Added Question: {q_text}")
        else:
            print(f"⚡ Updating Question: {q_text}")

        # Clear old choices
        question.choices.all().delete()

        # Assign new scores: 6, 4, 2
        for idx, choice_text in enumerate(choices):
            score = (len(choices) - idx) * 2   # 6, 4, 2
            Choice.objects.create(question=question, text=choice_text, score=score)
            print(f"   -> Added Choice: {choice_text} ({score} pts)")

if __name__ == "__main__":
    run()
