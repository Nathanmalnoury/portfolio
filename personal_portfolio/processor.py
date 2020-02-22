from personal_portfolio.settings import DEBUG


def debug_context(request):
    return {'debug_flag': DEBUG}
