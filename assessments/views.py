from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .models import Question, Choice, TestAttempt, Answer
from .services import categorize_iq

@login_required
def start_test(request):
    """Start a new test attempt and go to the first question."""
    attempt = TestAttempt.objects.create(user=request.user)
    return redirect("show_question", attempt_id=attempt.id, question_index=0)


@login_required
def show_question(request, attempt_id, question_index):
    """Display one question at a time and save answer on submit."""
    attempt = get_object_or_404(TestAttempt, id=attempt_id, user=request.user)
    questions = list(Question.objects.filter(is_active=True))

    # If user finished all questions → go to results
    if question_index >= len(questions):
        return redirect("submit_test", attempt_id=attempt.id)

    question = questions[question_index]

    if request.method == "POST":
        choice_id = request.POST.get("choice")
        if choice_id:
            choice = Choice.objects.get(id=choice_id)
            # Prevent duplicate answers for same question
            Answer.objects.update_or_create(
                attempt=attempt,
                question=question,
                defaults={"choice": choice, "score": choice.score},
            )
        # Redirect to next question
        return redirect("show_question", attempt_id=attempt.id, question_index=question_index + 1)

    return render(request, "assessments/question.html", {
        "attempt": attempt,
        "question": question,
        "question_index": question_index,
        "total_questions": len(questions),
        "choices": question.choices.all(),
    })


@login_required
def submit_test(request, attempt_id):
    """Calculate total score, categorize IQ, and show result."""
    attempt = get_object_or_404(TestAttempt, id=attempt_id, user=request.user)
    answers = Answer.objects.filter(attempt=attempt)

    total_score = sum(a.score for a in answers)
    iq_category = categorize_iq(total_score)

    attempt.total_score = total_score
    attempt.iq_category = iq_category
    attempt.submitted_at = now()
    attempt.save()

    # Update user profile
    profile = request.user.profile
    profile.last_iq_category = iq_category
    profile.save()

    # return render(request, "assessments/result.html", {
    #     "score": total_score,
    #     "iq_category": iq_category,
    # })
    return redirect("career_recommendations")

