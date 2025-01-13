from rest_framework.pagination import PageNumberPagination


def filterFunction(request, model):

    cat = request.query_params.get('cat', '')
    sort = request.query_params.get('sort', '')
    skills = request.query_params.get('skills', '')
    if cat:
        if sort:
            job = model.filter(category__name=cat).order_by(sort)
        else:
            job = model.filter(category__name=cat)
    elif sort:
        job = model.all().order_by(sort)
    else:
        job = model.all()
    if skills:
        job = job.filter(skills__name=skills)
    paginator = PageNumberPagination()
    paginator.page_size = request.query_params.get('limit', 10)
    paginated_jobs = paginator.paginate_queryset(job, request)

    return paginated_jobs, paginator
