# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .models import Career, CareerBookmark


# @login_required
# def career_recommendations(request):
#     profile = request.user.profile
#     iq_category = profile.last_iq_category
#     interests = list(profile.interests.all())

#     careers = Career.objects.filter(is_active=True)

#     scored_careers = []

#     for career in careers:
#         score = 0

#         # --- IQ weighting ---
#         if career.category == "ACADEMIC" and iq_category == "High":
#             score += 50
#         elif career.category == "TECHNICAL" and iq_category in ["Average", "High"]:
#             score += 40
#         elif career.category == "VOCATIONAL" and iq_category == "Low":
#             score += 40
#         elif career.category == "CREATIVE":
#             score += 30  # Open for all, but weaker

#         # --- Interest Matching ---
#         matched_interests = set(career.interests.all()) & set(interests)
#         score += len(matched_interests) * 20

#         scored_careers.append((career, score))

#     # Sort by relevance
#     scored_careers.sort(key=lambda x: x[1], reverse=True)
#     top_careers = [c for c, s in scored_careers if s > 0]

#     return render(request, "careers/recommendations.html", {
#         "careers": top_careers,
#         "iq_category": iq_category,
#         "interests": interests,
#     })


# # @login_required
# # def career_recommendations(request):
# #     profile = request.user.profile
# #     iq_category = profile.last_iq_category
# #     interests = profile.interests.all()

# #     careers = Career.objects.filter(is_active=True)

# #     # 🎯 IQ-based filtering
# #     if iq_category == "Low":
# #         careers = careers.filter(category__in=[Career.Category.VOCATIONAL, Career.Category.CREATIVE])
# #     elif iq_category == "Average":
# #         careers = careers.filter(category__in=[Career.Category.TECHNICAL, Career.Category.CREATIVE])
# #     elif iq_category == "High":
# #         careers = careers.filter(category__in=[Career.Category.ACADEMIC, Career.Category.TECHNICAL])

# #     # 🎯 Interest-based filtering
# #     if interests.exists():
# #         careers = careers.filter(interests__in=interests).distinct()

# #     return render(request, "careers/recommendations.html", {
# #         "careers": careers,
# #         "iq_category": iq_category,
# #         "interests": interests,
# #     })

# @login_required
# def bookmark_career(request, career_id):
#     career = get_object_or_404(Career, id=career_id)
#     CareerBookmark.objects.get_or_create(user=request.user, career=career)
#     return redirect("career_recommendations")


# @login_required
# def my_bookmarks(request):
#     bookmarks = CareerBookmark.objects.filter(user=request.user).select_related("career")
#     return render(request, "careers/bookmarks.html", {"bookmarks": bookmarks})


# @login_required
# def add_bookmark(request, career_id):
#     career = get_object_or_404(Career, id=career_id, is_active=True)
#     CareerBookmark.objects.get_or_create(user=request.user, career=career)
#     return redirect("bookmarked_careers")

# @login_required
# def bookmarked_careers(request):
#     bookmarks = CareerBookmark.objects.filter(user=request.user).select_related("career")
#     return render(request, "careers/bookmarks.html", {"bookmarks": bookmarks})

# @login_required
# def remove_bookmark(request, bookmark_id):
#     bookmark = get_object_or_404(CareerBookmark, id=bookmark_id, user=request.user)
#     bookmark.delete()
#     return redirect("bookmarked_careers")
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Career, CareerBookmark
@login_required
def career_recommendations(request):
    profile = request.user.profile
    iq_category = profile.last_iq_category

    # Normalize case (capitalize first letter)
    if iq_category:
        iq_category = iq_category.capitalize()

    interests = list(profile.interests.all())
    skills = list(profile.skills.all())

    careers = Career.objects.filter(is_active=True)
    scored_careers = []

    for career in careers:
        details = {"iq": 0, "interests": 0, "skills": 0}
        score = 0

        # --- IQ Weighting ---
        iq_boost = {
            "ACADEMIC": {"High": 50, "Average": 30, "Low": 10},
            "TECHNICAL": {"High": 45, "Average": 40, "Low": 20},
            "VOCATIONAL": {"Low": 40, "Average": 25, "High": 10},
            "CREATIVE": {"High": 30, "Average": 30, "Low": 30},
        }
        iq_score = iq_boost.get(career.category.upper(), {}).get(iq_category, 0)
        details["iq"] = iq_score
        score += iq_score

        # --- Interest Matching ---
        matched_interests = set(career.interests.all()) & set(interests)
        if career.interests.exists():
            interest_score = (len(matched_interests) / career.interests.count()) * 30
        else:
            interest_score = 0
        details["interests"] = round(interest_score, 2)
        score += interest_score

        # --- Skills Matching ---
        overlap = []
        if career.skills_required:
            required_skills = [s.strip().lower() for s in career.skills_required.split(",")]
            user_skills = [s.name.lower() for s in skills]
            overlap = set(required_skills) & set(user_skills)

            if required_skills:
                skills_score = (len(overlap) / len(required_skills)) * 40
            else:
                skills_score = 0
        else:
            skills_score = 0

        details["skills"] = round(skills_score, 2)
        score += skills_score

        scored_careers.append({
            "career": career,
            "total_score": round(score, 2),
            "details": details,
            "matched_interests": [i.name for i in matched_interests],
            "matched_skills": list(overlap),
        })

    # --- Filtering ---
    filter_interest = request.GET.get("filter_interest") == "1"
    filter_skills = request.GET.get("filter_skills") == "1"

    scored_careers = [
        c for c in scored_careers
        if c["total_score"] >= 31
        and (not filter_interest or c["details"]["interests"] > 0)
        and (not filter_skills or c["details"]["skills"] > 0)
    ]

    # --- Sorting ---
    sort_by = request.GET.get("sort", "score")  # default: score
    if sort_by == "salary":
        scored_careers.sort(key=lambda x: (x["career"].salary_max or 0), reverse=True)
    else:
        scored_careers.sort(key=lambda x: x["total_score"], reverse=True)

    return render(request, "careers/recommendations.html", {
        "careers": scored_careers,
        "iq_category": profile.last_iq_category,  # original for display
        "interests": interests,
        "skills": skills,
        "filter_interest": filter_interest,
        "filter_skills": filter_skills,
        "sort_by": sort_by,
    })

# ---------------- Bookmarks ---------------- #

@login_required
def bookmark_career(request, career_id):
    career = get_object_or_404(Career, id=career_id, is_active=True)
    CareerBookmark.objects.get_or_create(user=request.user, career=career)
    return redirect("bookmarked_careers")


@login_required
def bookmarked_careers(request):
    bookmarks = CareerBookmark.objects.filter(user=request.user).select_related("career")
    return render(request, "careers/bookmarks.html", {"bookmarks": bookmarks})


@login_required
def remove_bookmark(request, bookmark_id):
    bookmark = get_object_or_404(CareerBookmark, id=bookmark_id, user=request.user)
    bookmark.delete()
    return redirect("bookmarked_careers")
