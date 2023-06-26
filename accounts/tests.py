
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your tests here.
class SignUpPageTest(TestCase):


    def test_signup_form(self):
        response = self.client.post(
            reverse('signup'),
            {
             'username':'testuser',
             'email':'test@email.com',
             'password1':'testpassword',
             'password2':'testpassword'
             }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, 'testuser')
        self.assertEqual(get_user_model().objects.all()[0].email, 'test@email.com')



    def test_signup_url_exsists_at_correct_location(self):
        response = self.client.get('/accounts/signup')
        
        self.assertEqual(response.status_code, 200)

    def test_signup_url_by_available_name(self):
        response = self.client.get(reverse('signup'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sign Up')
        self.assertTemplateUsed(response, 'registration/signup.html')
