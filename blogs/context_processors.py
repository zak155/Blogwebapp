from . models import Category
def get_category(request):
    categories=Category.objects.all()
    return dict(categories=categories)
def get_social_links(request):
    from about.models import Social_Link
    social_links=Social_Link.objects.all()
    return dict(social_links=social_links)