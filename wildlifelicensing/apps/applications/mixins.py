from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from wildlifelicensing.apps.main.helpers import is_customer, is_officer, get_user_assessor_groups
from wildlifelicensing.apps.applications.models import Application, Assessment


class UserCanEditApplicationMixin(UserPassesTestMixin):
    """
    CBV mixin that check that the user is the applicant and that the status of the application is
    in editable mode.
    This mixin assume that the url contains the pk of the application on 2nd position.
    If the user is not logged-in it redirects to the login page, else it throws a 403
    Officers can edit an application
    """
    login_url = reverse_lazy('home')
    permission_denied_message = "You don't have the permission to access this resource."
    raise_exception = True

    def get_application(self):
        if len(self.args) > 1:
            return Application.objects.filter(pk=self.args[1]).first()
        else:
            return None

    def test_func(self):
        """
        implementation of the UserPassesTestMixin test_func
        """
        user = self.request.user
        if not user.is_authenticated():
            self.raise_exception = False
            return False
        if is_officer(user):
            return True
        self.raise_exception = True
        application = self.get_application()
        if application is not None:
            return application.applicant_profile.user == user and application.can_user_edit
        else:
            return True


class CanEditAssessmentMixin(UserPassesTestMixin):
    """
    CBV mixin that check the 'editability' of assessment that the user is a assessor and that he/she belongs to the right assessor group.
    This mixin assume that the url contains the pk of the assessment in 2nd position
    If the user is not logged-in it redirects to the login page, else it throws a 403
    """
    login_url = reverse_lazy('home')
    permission_denied_message = "You don't have the permission to access this resource."
    raise_exception = True

    def get_assessment(self):
        if len(self.args) > 1:
            return Assessment.objects.filter(pk=self.args[1]).first()
        else:
            return None

    def test_func(self):
        """
        implementation of the UserPassesTestMixin test_func
        """
        user = self.request.user
        if not user.is_authenticated():
            self.raise_exception = False
            return False
        self.raise_exception = True
        if is_customer(user):
            return False
        if is_officer(user):
            return True
        assessment = self.get_assessment()
        return assessment is not None and assessment.assessor_group in get_user_assessor_groups(user)


class UserCanViewApplicationMixin(UserPassesTestMixin):
    """
    CBV mixin that check that the user is the applicant or an officer and that the status of the 
    application is in approved mode.
    If the user is not logged-in it redirects to the login page, else it throws a 403
    """
    login_url = reverse_lazy('home')
    permission_denied_message = "You don't have the permission to access this resource."
    raise_exception = True

    def get_application(self):
        if len(self.args) > 1:
            return Application.objects.filter(pk=self.args[0]).first()
        else:
            return None

    def test_func(self):
        """
        implementation of the UserPassesTestMixin test_func
        """
        user = self.request.user
        if not user.is_authenticated():
            self.raise_exception = False
            return False
        if is_officer(user):
            return True
        self.raise_exception = True
        application = self.get_application()
        if application is not None:
            return application.applicant_profile.user == user and application.can_user_view
        else:
            return True
