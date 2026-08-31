from django.shortcuts import render, get_object_or_404
from .models import Prompt


def home(request):
    query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()

    prompts = Prompt.objects.all().order_by("-created_at")

    if query:
        prompts = prompts.filter(
            title__icontains=query
        ) | prompts.filter(
            prompt_text__icontains=query
        ) | prompts.filter(
            category__icontains=query
        )

    if category:
        prompts = prompts.filter(category__iexact=category)

    return render(
        request,
        "gallery/home.html",
        {
            "prompts": prompts,
            "query": query,
            "category": category,
        }
    )



def prompt_detail(request, pk):
    prompt = get_object_or_404(Prompt, pk=pk)

    prompt.views += 1
    prompt.save(update_fields=["views"])

    return render(
        request,
        "gallery/detail.html",
        {"prompt": prompt}
    )