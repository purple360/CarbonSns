from django.views.generic import TemplateView

class landing_page(TemplateView):
	template_name = 'landing_page.html'


class HomePageView(TemplateView):
	template_name = 'home.html'

