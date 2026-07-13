from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from .models import Seeker, Wali, VerificationRequest
import json

class DashboardAPITests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_seeker_and_wali(self):
        url = reverse('api_seekers')
        payload = {
            'full_name': 'Aisha Kutigi',
            'gender': 'bride',
            'state': 'Niger',
            'wali_name': 'Alhaji Kutigi',
            'wali_relationship': 'Father',
            'wali_contact': '08012345678',
            'status': 'Unverified'
        }
        response = self.client.post(
            url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['user']['full_name'], 'Aisha Kutigi')
        self.assertEqual(data['user']['gender'], 'Female')

        # Verify database record
        seeker = Seeker.objects.get(full_name='Aisha Kutigi')
        self.assertEqual(seeker.state, 'Niger')
        self.assertEqual(seeker.status, 'Unverified')
        self.assertEqual(seeker.wali_name, 'Alhaji Kutigi')

        # Verify Wali record
        wali = Wali.objects.get(seeker=seeker)
        self.assertEqual(wali.name, 'Alhaji Kutigi')
        self.assertEqual(wali.relationship, 'Father')
        self.assertEqual(wali.contact_number, '08012345678')

    def test_submit_verification(self):
        seeker = Seeker.objects.create(
            full_name='Bilal Bida',
            gender='Male',
            state='Niger',
            status='Unverified',
            join_date=timezone.now().date()
        )

        url = reverse('api_submit_verification')
        payload = {
            'seeker_id': seeker.id,
            'document_type': 'NIN',
            'document_preview_url': 'http://example.com/id.jpg'
        }
        response = self.client.post(
            url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['user']['status'], 'Pending')

        # Verify seeker status updated
        seeker.refresh_from_db()
        self.assertEqual(seeker.status, 'Pending')

        # Verify VerificationRequest record created
        req = VerificationRequest.objects.get(user_name='Bilal Bida')
        self.assertEqual(req.document_type, 'NIN')
        self.assertEqual(req.document_preview_url, 'http://example.com/id.jpg')
        self.assertEqual(req.status, 'pending')
