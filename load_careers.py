import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from careers.models import Career, Interest

def run():
    careers_data = [
    {
        "title": "Software Engineer",
        "category": "TECHNICAL",
        "description": "Designs, develops, and maintains software applications.",
        "skills_required": "Programming, problem-solving, teamwork",
        "education_pathway": "Bachelor’s in Computer Science or related field",
        "salary_min": 400000,
        "salary_max": 1200000,
        "interests": ["technology", "science"],
    },
    {
        "title": "Data Scientist",
        "category": "ACADEMIC",
        "description": "Analyzes and interprets complex data to help organizations make decisions.",
        "skills_required": "Statistics, machine learning, Python/R",
        "education_pathway": "Bachelor’s/Master’s in Data Science, Statistics, or related field",
        "salary_min": 600000,
        "salary_max": 1500000,
        "interests": ["science", "technology"],
    },
    {
        "title": "Graphic Designer",
        "category": "CREATIVE",
        "description": "Creates visual concepts to communicate ideas and messages.",
        "skills_required": "Creativity, Adobe tools, visual storytelling",
        "education_pathway": "Diploma/Bachelor’s in Design, Fine Arts",
        "salary_min": 250000,
        "salary_max": 800000,
        "interests": ["design", "arts"],
    },
    {
        "title": "Electrician",
        "category": "VOCATIONAL",
        "description": "Installs and maintains electrical systems in buildings.",
        "skills_required": "Technical skills, troubleshooting, safety knowledge",
        "education_pathway": "ITI/Diploma in Electrical Engineering",
        "salary_min": 200000,
        "salary_max": 500000,
        "interests": ["technology"],
    },
    {
        "title": "Doctor",
        "category": "ACADEMIC",
        "description": "Diagnoses and treats patients to maintain health and prevent disease.",
        "skills_required": "Medical knowledge, empathy, problem-solving",
        "education_pathway": "MBBS + specialization",
        "salary_min": 600000,
        "salary_max": 2000000,
        "interests": ["science"],
    },
    {
        "title": "Mechanical Engineer",
        "category": "TECHNICAL",
        "description": "Designs and develops mechanical systems and machines.",
        "skills_required": "Engineering principles, CAD, problem-solving",
        "education_pathway": "Bachelor’s in Mechanical Engineering",
        "salary_min": 400000,
        "salary_max": 1200000,
        "interests": ["technology", "science"],
    },
    {
        "title": "Fashion Designer",
        "category": "CREATIVE",
        "description": "Designs clothing and accessories with aesthetic appeal.",
        "skills_required": "Creativity, drawing, knowledge of fabrics",
        "education_pathway": "Bachelor’s in Fashion Design",
        "salary_min": 300000,
        "salary_max": 1000000,
        "interests": ["design", "arts"],
    },
    {
        "title": "Teacher",
        "category": "ACADEMIC",
        "description": "Educates students in various subjects and skills.",
        "skills_required": "Communication, subject knowledge, patience",
        "education_pathway": "Bachelor’s + B.Ed / Master’s in subject",
        "salary_min": 250000,
        "salary_max": 700000,
        "interests": ["arts", "science"],
    },
    {
        "title": "Chef",
        "category": "VOCATIONAL",
        "description": "Prepares and cooks food in restaurants, hotels, or cafes.",
        "skills_required": "Cooking, creativity, time management",
        "education_pathway": "Diploma in Culinary Arts or Hotel Management",
        "salary_min": 200000,
        "salary_max": 600000,
        "interests": ["arts", "design"],
    },
    {
        "title": "Architect",
        "category": "CREATIVE",
        "description": "Designs buildings and structures focusing on safety and aesthetics.",
        "skills_required": "Design, CAD, structural knowledge",
        "education_pathway": "Bachelor’s in Architecture",
        "salary_min": 400000,
        "salary_max": 1500000,
        "interests": ["design", "technology"],
    },
    {
        "title": "Civil Engineer",
        "category": "TECHNICAL",
        "description": "Plans and designs infrastructure projects such as roads and bridges.",
        "skills_required": "Engineering, CAD, project management",
        "education_pathway": "Bachelor’s in Civil Engineering",
        "salary_min": 350000,
        "salary_max": 1100000,
        "interests": ["technology", "science"],
    },
    {
        "title": "Psychologist",
        "category": "ACADEMIC",
        "description": "Studies mental processes and behavior to help people improve wellbeing.",
        "skills_required": "Empathy, research, communication",
        "education_pathway": "Bachelor’s/Master’s in Psychology",
        "salary_min": 300000,
        "salary_max": 900000,
        "interests": ["arts", "science"],
    },
    {
        "title": "Plumber",
        "category": "VOCATIONAL",
        "description": "Installs and repairs water systems and pipelines.",
        "skills_required": "Technical skills, problem-solving",
        "education_pathway": "ITI/Diploma in Plumbing",
        "salary_min": 180000,
        "salary_max": 450000,
        "interests": ["technology"],
    },
    {
        "title": "Animator",
        "category": "CREATIVE",
        "description": "Creates animated films, graphics, and effects for media.",
        "skills_required": "Creativity, animation software, storytelling",
        "education_pathway": "Bachelor’s in Animation or Fine Arts",
        "salary_min": 300000,
        "salary_max": 1000000,
        "interests": ["design", "arts"],
    },
    {
        "title": "Accountant",
        "category": "ACADEMIC",
        "description": "Manages financial records and ensures compliance with laws.",
        "skills_required": "Accounting, Excel, attention to detail",
        "education_pathway": "B.Com, CA, or CMA",
        "salary_min": 250000,
        "salary_max": 900000,
        "interests": ["science"],
    },
    {
        "title": "Automobile Mechanic",
        "category": "VOCATIONAL",
        "description": "Repairs and maintains cars, bikes, and other vehicles.",
        "skills_required": "Technical knowledge, troubleshooting",
        "education_pathway": "ITI/Diploma in Automobile Engineering",
        "salary_min": 180000,
        "salary_max": 500000,
        "interests": ["technology"],
    },
    {
        "title": "Musician",
        "category": "CREATIVE",
        "description": "Performs or composes music professionally.",
        "skills_required": "Instrument/vocal skills, creativity",
        "education_pathway": "Diploma/Bachelor’s in Music",
        "salary_min": 200000,
        "salary_max": 1000000,
        "interests": ["arts"],
    },
    {
        "title": "Lawyer",
        "category": "ACADEMIC",
        "description": "Represents clients in legal matters and provides legal advice.",
        "skills_required": "Law knowledge, communication, research",
        "education_pathway": "LLB + bar exam",
        "salary_min": 400000,
        "salary_max": 1500000,
        "interests": ["arts"],
    },
    {
        "title": "Web Developer",
        "category": "TECHNICAL",
        "description": "Builds and maintains websites and web applications.",
        "skills_required": "HTML, CSS, JavaScript, Python/Django",
        "education_pathway": "Bachelor’s in Computer Science or training courses",
        "salary_min": 300000,
        "salary_max": 1000000,
        "interests": ["technology", "design"],
    },
    {
        "title": "Photographer",
        "category": "CREATIVE",
        "description": "Captures photos for artistic, commercial, or journalistic purposes.",
        "skills_required": "Creativity, technical camera skills",
        "education_pathway": "Diploma/Bachelor’s in Photography",
        "salary_min": 200000,
        "salary_max": 800000,
        "interests": ["arts", "design"],
    },
    ]


    for data in careers_data:
        career, created = Career.objects.get_or_create(
            title=data["title"],
            defaults={
                "category": data["category"],
                "description": data["description"],
                "skills_required": data["skills_required"],
                "education_pathway": data["education_pathway"],
                "salary_min": data.get("salary_min"),
                "salary_max": data.get("salary_max"),
                "is_active": True,
            },
        )
        # Add interests
        for interest_name in data["interests"]:
            interest, _ = Interest.objects.get_or_create(
                name=interest_name.capitalize(),
                slug=interest_name.lower(),
            )
            career.interests.add(interest)

        print(f"Added Career: {career.title}")

if __name__ == "__main__":
    run()
