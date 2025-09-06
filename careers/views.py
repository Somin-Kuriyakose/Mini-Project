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
    interests = list(profile.interests.all())
    skills = list(profile.skills.all())

    careers = Career.objects.filter(is_active=True)
    scored_careers = []

    for career in careers:
        score = 0

        # --- IQ weighting ---
        if career.category == "ACADEMIC" and iq_category == "High":
            score += 50
        elif career.category == "TECHNICAL" and iq_category in ["Average", "High"]:
            score += 40
        elif career.category == "VOCATIONAL" and iq_category == "Low":
            score += 40
        elif career.category == "CREATIVE":
            score += 30  # open for all, weaker

        # --- Interest Matching ---
        matched_interests = set(career.interests.all()) & set(interests)
        score += len(matched_interests) * 20

        # --- Skills Matching ---
        if career.skills_required:
            required_skills = [s.strip().lower() for s in career.skills_required.split(",")]
            user_skills = [s.name.lower() for s in skills]
            overlap = set(required_skills) & set(user_skills)
            score += len(overlap) * 15

        scored_careers.append((career, score))

    # Sort by relevance
    scored_careers.sort(key=lambda x: x[1], reverse=True)
    top_careers = [c for c, s in scored_careers if s > 0]

    return render(request, "careers/recommendations.html", {
        "careers": top_careers,
        "iq_category": iq_category,
        "interests": interests,
        "skills": skills,
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
