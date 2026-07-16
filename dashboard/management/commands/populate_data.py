import random
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from dashboard.models import Seeker, Wali, Imam, Match, ChatMessage, Report, VerificationRequest, RevenueTransaction, Mosque

class Command(BaseCommand):
    help = 'Populates the database with rich mock data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        ChatMessage.objects.all().delete()
        Match.objects.all().delete()
        Wali.objects.all().delete()
        Seeker.objects.all().delete()
        Imam.objects.all().delete()
        Report.objects.all().delete()
        VerificationRequest.objects.all().delete()
        RevenueTransaction.objects.all().delete()
        Mosque.objects.all().delete()

        self.stdout.write('Seeding database with mock data...')

        # 1. Create Seekers (Male and Female)
        seekers_data = [
            # Males
            {
                'full_name': 'Yahaya Baba', 'gender': 'Male', 'state': 'Niger', 'wali_name': '', 'status': 'Verified', 'join_date': date(2025, 5, 10),
                'age': 32, 'state_of_origin': 'Niger', 'currently_based_in': 'Minna, Niger State', 'tribe': 'Nupe', 'marital_status': 'Single', 'children': 'None',
                'education': 'M.Sc.', 'occupation': 'Software Engineer', 'blood_group': 'O+', 'genotype': 'AA', 'health_status': 'Excellent health',
                'islamic_level': 'Observes daily prayers, attends weekly halaqah', 'mode_of_dressing': 'Casual & Modest', 'appearance': 'Tall, dark complexion',
                'open_to_polygamy': 'No', 'willing_to_relocate': 'Yes', 'marriage_timeline': 'Within 6 months',
                'about_me': 'I am a dedicated professional looking to settle down with a pious Muslimah. I value honesty, continuous self-improvement, and family values.',
                'spouse_age_range': '24-28 years', 'spouse_marital_status': 'Single', 'spouse_children': 'No children', 'spouse_location': 'Minna or Abuja',
                'spouse_desired_qualities': 'Pious, kind-hearted, respectful, and willing to build a family on Islamic principles.'
            },
            {
                'full_name': 'Mohammed Bida', 'gender': 'Male', 'state': 'Niger', 'wali_name': '', 'status': 'Verified', 'join_date': date(2025, 6, 12),
                'age': 29, 'state_of_origin': 'Niger', 'currently_based_in': 'Bida, Niger State', 'tribe': 'Nupe', 'marital_status': 'Single', 'children': 'None',
                'education': 'B.Sc.', 'occupation': 'Accountant', 'blood_group': 'B+', 'genotype': 'AS', 'health_status': 'No known medical issues',
                'islamic_level': 'Regular prayer observer, seeking knowledge', 'mode_of_dressing': 'Traditional Nupe/Islamic attire', 'appearance': 'Average height, athletic build',
                'open_to_polygamy': 'No', 'willing_to_relocate': 'No', 'marriage_timeline': 'Within a year',
                'about_me': 'Easy-going individual who loves reading and community service. Seeking a supportive life partner.',
                'spouse_age_range': '22-27 years', 'spouse_marital_status': 'Single', 'spouse_children': 'No children', 'spouse_location': 'Bida or Minna',
                'spouse_desired_qualities': 'Observant of prayers, family-oriented, and educated.'
            },
            {
                'full_name': 'Saidu Katcha', 'gender': 'Male', 'state': 'Kwara', 'wali_name': '', 'status': 'Verified', 'join_date': date(2025, 7, 20),
                'age': 35, 'state_of_origin': 'Kwara', 'currently_based_in': 'Ilorin, Kwara State', 'tribe': 'Yoruba', 'marital_status': 'Single', 'children': 'None',
                'education': 'HND', 'occupation': 'Businessman', 'blood_group': 'O+', 'genotype': 'AA', 'health_status': 'Healthy',
                'islamic_level': 'Practicing Muslim', 'mode_of_dressing': 'Modest', 'appearance': 'Slim build, dark complexion',
                'open_to_polygamy': 'Yes', 'willing_to_relocate': 'Yes', 'marriage_timeline': 'As soon as possible',
                'about_me': 'I run a retail business in Ilorin. I am family-oriented, responsible, and looking for a companion to walk the path of Deen with.',
                'spouse_age_range': '25-30 years', 'spouse_marital_status': 'Single or Divorced', 'spouse_children': 'Acceptable', 'spouse_location': 'Kwara or FCT',
                'spouse_desired_qualities': 'Religious, honest, business-minded, and loving.'
            },
            {
                'full_name': 'Usman Agaie', 'gender': 'Male', 'state': 'FCT', 'wali_name': '', 'status': 'Pending', 'join_date': date(2026, 1, 15),
                'age': 41, 'state_of_origin': 'Niger', 'currently_based_in': 'Garki, Abuja', 'tribe': 'Nupe', 'marital_status': 'Widower', 'children': '2 Children',
                'education': 'Ph.D.', 'occupation': 'University Lecturer', 'blood_group': 'A-', 'genotype': 'AA', 'health_status': 'Healthy',
                'islamic_level': 'Very committed to Islamic teachings', 'mode_of_dressing': 'Formal / Islamic modesty', 'appearance': 'Average height, wears a beard',
                'open_to_polygamy': 'Yes', 'willing_to_relocate': 'No', 'marriage_timeline': 'Within 3-6 months',
                'about_me': 'I am a widower with two young children. I am looking for a compassionate Muslimah who will be a caring wife and a loving mother figure for my kids.',
                'spouse_age_range': '30-38 years', 'spouse_marital_status': 'Widow, Divorced, or Single', 'spouse_children': 'Acceptable', 'spouse_location': 'Abuja, Niger or Kaduna',
                'spouse_desired_qualities': 'Kind, motherly, practicing Muslimah with good character and patience.'
            },
            {
                'full_name': 'Ibrahim Mokwa', 'gender': 'Male', 'state': 'Kogi', 'wali_name': '', 'status': 'Unverified', 'join_date': date(2026, 2, 10),
                'age': 28, 'state_of_origin': 'Kogi', 'currently_based_in': 'Lokoja, Kogi State', 'tribe': 'Ebira', 'marital_status': 'Single', 'children': 'None',
                'education': 'B.Sc.', 'occupation': 'Civil Servant', 'blood_group': 'B-', 'genotype': 'AA', 'health_status': 'Healthy',
                'islamic_level': 'Regular prayers observer', 'mode_of_dressing': 'Smart casual', 'appearance': 'Athletic build',
                'open_to_polygamy': 'No', 'willing_to_relocate': 'Yes', 'marriage_timeline': '1 year',
                'about_me': 'Honest, easy-going young man working with the state government. I love sports and reading Islamic history.',
                'spouse_age_range': '20-25 years', 'spouse_marital_status': 'Single', 'spouse_children': 'No', 'spouse_location': 'Kogi or Kwara',
                'spouse_desired_qualities': 'Pious, educated, humble, and supportive.'
            },
            {
                'full_name': 'Aliyu Lapai', 'gender': 'Male', 'state': 'Diaspora', 'wali_name': '', 'status': 'Verified', 'join_date': date(2025, 11, 5),
                'age': 34, 'state_of_origin': 'Niger', 'currently_based_in': 'London, UK', 'tribe': 'Nupe', 'marital_status': 'Single', 'children': 'None',
                'education': 'MBA', 'occupation': 'Financial Analyst', 'blood_group': 'O-', 'genotype': 'AA', 'health_status': 'Excellent health',
                'islamic_level': 'Strives to practice and attend Islamic lectures', 'mode_of_dressing': 'Modern modest wear', 'appearance': 'Tall, light complexion',
                'open_to_polygamy': 'No', 'willing_to_relocate': 'Yes', 'marriage_timeline': '6-12 months',
                'about_me': 'Living and working in London. I enjoy traveling, learning about history, and playing football. Looking for a spouse to join me here or relocate.',
                'spouse_age_range': '24-30 years', 'spouse_marital_status': 'Single', 'spouse_children': 'No', 'spouse_location': 'Willing to relocate to UK',
                'spouse_desired_qualities': 'Observant of hijab/modesty, educated, fluent in English, and family-oriented.'
            },
            # Females
            {
                'full_name': 'Zainab Usman', 'gender': 'Female', 'state': 'Niger', 'wali_name': 'Mallam Usman Isa', 'status': 'Verified', 'join_date': date(2025, 5, 11),
                'age': 25, 'state_of_origin': 'Niger', 'currently_based_in': 'Minna, Niger State', 'tribe': 'Nupe', 'marital_status': 'Single', 'children': 'None',
                'education': 'B.Sc. Microbiology', 'occupation': 'Lab Assistant', 'blood_group': 'A+', 'genotype': 'AA', 'health_status': 'Healthy',
                'islamic_level': 'Committed to prayers and hijab', 'mode_of_dressing': 'Hijab & Abaya', 'appearance': 'Average height, slim build',
                'open_to_polygamy': 'No', 'willing_to_relocate': 'Yes', 'marriage_timeline': 'Within 6 months',
                'about_me': 'I am a reserved and gentle person who loves reading and cooking. I seek to build a family built on the Sunnah.',
                'spouse_age_range': '28-35 years', 'spouse_marital_status': 'Single', 'spouse_children': 'None', 'spouse_location': 'Niger or Abuja',
                'spouse_desired_qualities': 'Pious, educated, gains halal livelihood, and takes responsibility.'
            },
            {
                'full_name': 'Amina Agaie', 'gender': 'Female', 'state': 'Niger', 'wali_name': 'Mallam Agaie Aliyu', 'status': 'Verified', 'join_date': date(2025, 6, 13),
                'age': 37, 'state_of_origin': 'Niger State', 'currently_based_in': 'Suleja, Niger State', 'tribe': 'Nupe', 'marital_status': 'Divorced', 'children': 'None',
                'education': 'B.Sc.', 'occupation': 'Teacher', 'blood_group': 'A+', 'genotype': 'AA', 'health_status': 'No known disability or medical condition.',
                'islamic_level': 'A well-practicing Muslimah who is committed to observing her daily prayers.', 'mode_of_dressing': 'Modest Islamic dressing with veils.',
                'appearance': 'Slim body size, average height, light complexion.', 'open_to_polygamy': 'Yes', 'willing_to_relocate': 'Yes',
                'marriage_timeline': 'As soon as a suitable match is found, In shaa Allah.',
                'about_me': 'I am an honest and introverted Muslimah who values cleanliness, sincerity, and peaceful living. I enjoy reading and listening to Qur\'an recitation, and I strive to strengthen my relationship with Allah through consistent worship. I hope to build a marriage founded on faith, mutual respect, and genuine companionship.',
                'spouse_age_range': '40 years and above', 'spouse_marital_status': 'Widower or any other marital status', 'spouse_children': 'Acceptable',
                'spouse_location': 'Abuja, Suleja, Kaduna, or Nasarawa.',
                'spouse_desired_qualities': 'I seek a trustworthy, practicing Muslim who observes his prayers consistently and earns a halal livelihood. He should be responsible, caring toward his family, and committed to building a peaceful home based on Islamic values, mutual respect, and compassion.'
            },
            {
                'full_name': 'Nana Etsu', 'gender': 'Female', 'state': 'Kwara', 'wali_name': 'Alhaji Etsu Mohammed', 'status': 'Verified', 'join_date': date(2025, 7, 22),
                'age': 27, 'state_of_origin': 'Kwara', 'currently_based_in': 'Ilorin, Kwara State', 'tribe': 'Yoruba', 'marital_status': 'Single', 'children': 'None',
                'education': 'M.Sc. Economics', 'occupation': 'Research Analyst', 'blood_group': 'O+', 'genotype': 'AA', 'health_status': 'Healthy',
                'islamic_level': 'Practicing Muslimah, hijab observer', 'mode_of_dressing': 'Hijab & Modest casuals', 'appearance': 'Chubby, average height',
                'open_to_polygamy': 'No', 'willing_to_relocate': 'Yes', 'marriage_timeline': '6 months',
                'about_me': 'I am a cheerful and goals-driven Muslimah who loves community work. Looking for an ambitious husband who values both Deen and Dunya.',
                'spouse_age_range': '30-36 years', 'spouse_marital_status': 'Single', 'spouse_children': 'No', 'spouse_location': 'Kwara, Abuja or Lagos',
                'spouse_desired_qualities': 'Pious, ambitious, supportive of his wife\'s career goals, and of excellent character.'
            },
            {
                'full_name': 'Fatima Ibrahim', 'gender': 'Female', 'state': 'Kogi', 'wali_name': 'Mallam Ibrahim Kolo', 'status': 'Pending', 'join_date': date(2026, 1, 20),
                'age': 23, 'state_of_origin': 'Kogi', 'currently_based_in': 'Lokoja, Kogi State', 'tribe': 'Igala', 'marital_status': 'Single', 'children': 'None',
                'education': 'Undergraduate', 'occupation': 'Student', 'blood_group': 'B+', 'genotype': 'AS', 'health_status': 'Healthy',
                'islamic_level': 'Learning and striving to improve daily prayers', 'mode_of_dressing': 'Modest clothing', 'appearance': 'Slim, dark skin',
                'open_to_polygamy': 'No', 'willing_to_relocate': 'Yes', 'marriage_timeline': 'After graduation (approx. 1 year)',
                'about_me': 'I am an final year student. I enjoy baking and spending time with my family. Seeking a partner to embark on a beautiful Islamic marriage journey.',
                'spouse_age_range': '26-30 years', 'spouse_marital_status': 'Single', 'spouse_children': 'No', 'spouse_location': 'Kogi or Abuja',
                'spouse_desired_qualities': 'Kind, understanding, religious, and financially capable.'
            },
            {
                'full_name': 'Aisha Bida', 'gender': 'Female', 'state': 'FCT', 'wali_name': 'Mallam Bida Umaru', 'status': 'Verified', 'join_date': date(2025, 9, 30),
                'age': 30, 'state_of_origin': 'Niger', 'currently_based_in': 'Gwarinpa, Abuja', 'tribe': 'Nupe', 'marital_status': 'Single', 'children': 'None',
                'education': 'B.Sc. Nursing', 'occupation': 'Registered Nurse', 'blood_group': 'O+', 'genotype': 'AA', 'health_status': 'Healthy',
                'islamic_level': 'Practicing Muslimah, wears hijab', 'mode_of_dressing': 'Hijab & Scrub/Modest casuals', 'appearance': 'Tall, medium build',
                'open_to_polygamy': 'No', 'willing_to_relocate': 'No', 'marriage_timeline': '6 months',
                'about_me': 'I am a nurse working in a private hospital. I am compassionate, hardworking, and committed to both my profession and Deen.',
                'spouse_age_range': '32-40 years', 'spouse_marital_status': 'Single or Divorced', 'spouse_children': 'No children or independent', 'spouse_location': 'Abuja',
                'spouse_desired_qualities': 'Responsible, praying Muslim, educated, and caring.'
            },
            {
                'full_name': 'Khadijah Kutigi', 'gender': 'Female', 'state': 'Diaspora', 'wali_name': 'Alhaji Kutigi Hassan', 'status': 'Unverified', 'join_date': date(2026, 3, 1),
                'age': 28, 'state_of_origin': 'Niger', 'currently_based_in': 'Washington DC, USA', 'tribe': 'Nupe', 'marital_status': 'Single', 'children': 'None',
                'education': 'M.Sc. Data Science', 'occupation': 'Data Scientist', 'blood_group': 'AB+', 'genotype': 'AA', 'health_status': 'Healthy',
                'islamic_level': 'Committed to prayers, striving for knowledge', 'mode_of_dressing': 'Hijab & Modest outfits', 'appearance': 'Average height, brown complexion',
                'open_to_polygamy': 'No', 'willing_to_relocate': 'Yes', 'marriage_timeline': 'Within a year',
                'about_me': 'Currently working as a Data Scientist in the US. I value intelligence, humor, and religiosity. Hoping to build a loving home.',
                'spouse_age_range': '30-36 years', 'spouse_marital_status': 'Single', 'spouse_children': 'No', 'spouse_location': 'USA or willing to relocate',
                'spouse_desired_qualities': 'Practicing Muslim, educated professional, caring, and open-minded.'
            }
        ]

        seekers = []
        for s in seekers_data:
            seeker = Seeker.objects.create(**s)
            seekers.append(seeker)

        # 2. Create Walis (for females)
        walis_data = [
            {'name': 'Mallam Usman Isa', 'seeker': Seeker.objects.get(full_name='Zainab Usman'), 'relationship': 'Father', 'contact_number': '+2348031234567'},
            {'name': 'Mallam Agaie Aliyu', 'seeker': Seeker.objects.get(full_name='Amina Agaie'), 'relationship': 'Brother', 'contact_number': '+2348057654321'},
            {'name': 'Alhaji Etsu Mohammed', 'seeker': Seeker.objects.get(full_name='Nana Etsu'), 'relationship': 'Father', 'contact_number': '+2348099887766'},
            {'name': 'Mallam Ibrahim Kolo', 'seeker': Seeker.objects.get(full_name='Fatima Ibrahim'), 'relationship': 'Father', 'contact_number': '+2348123456789'},
            {'name': 'Mallam Bida Umaru', 'seeker': Seeker.objects.get(full_name='Aisha Bida'), 'relationship': 'Uncle', 'contact_number': '+2348022334455'}
        ]

        for w in walis_data:
            Wali.objects.create(**w)

        # 3. Create Imams
        imams_data = [
            {'name': 'Mallam Umar Ibrahim', 'mosque': 'Minna Central Mosque', 'state': 'Niger', 'is_verified': True, 'matches_supervised': 18},
            {'name': 'Mallam Aliyu Mohammed', 'mosque': 'Bida Emirate Mosque', 'state': 'Niger', 'is_verified': True, 'matches_supervised': 24},
            {'name': 'Mallam Mohammed Usman', 'mosque': 'Ilorin Juma\'at Mosque', 'state': 'Kwara', 'is_verified': True, 'matches_supervised': 12},
            {'name': 'Mallam Idris Bida', 'mosque': 'Abuja National Mosque', 'state': 'FCT', 'is_verified': True, 'matches_supervised': 31},
            {'name': 'Mallam Abdullahi Kutigi', 'mosque': 'Lokoja Mosque', 'state': 'Kogi', 'is_verified': True, 'matches_supervised': 5}
        ]

        imams = []
        for im in imams_data:
            imam = Imam.objects.create(**im)
            imams.append(imam)

        # 4. Create Mosques
        mosques_data = [
            {'name': 'Minna Central Mosque', 'state': 'Niger', 'chief_imam': 'Mallam Umar Ibrahim', 'active_users': 1420},
            {'name': 'Bida Emirate Mosque', 'state': 'Niger', 'chief_imam': 'Mallam Aliyu Mohammed', 'active_users': 680},
            {'name': 'Ilorin Juma\'at Mosque', 'state': 'Kwara', 'chief_imam': 'Mallam Mohammed Usman', 'active_users': 640},
            {'name': 'Abuja National Mosque', 'state': 'FCT', 'chief_imam': 'Mallam Idris Bida', 'active_users': 510},
            {'name': 'Lokoja Town Mosque', 'state': 'Kogi', 'chief_imam': 'Mallam Abdullahi Kutigi', 'active_users': 310},
            {'name': 'London Islamic Centre', 'state': 'Diaspora', 'chief_imam': 'Sheikh Ahmed Al-Nupe', 'active_users': 240}
        ]

        for mq in mosques_data:
            Mosque.objects.create(**mq)

        # 5. Create Matches
        y_baba = Seeker.objects.get(full_name='Yahaya Baba')
        z_usman = Seeker.objects.get(full_name='Zainab Usman')
        m_bida = Seeker.objects.get(full_name='Mohammed Bida')
        a_agaie = Seeker.objects.get(full_name='Amina Agaie')
        s_katcha = Seeker.objects.get(full_name='Saidu Katcha')
        n_etsu = Seeker.objects.get(full_name='Nana Etsu')
        a_bida = Seeker.objects.get(full_name='Aisha Bida')
        al_lapai = Seeker.objects.get(full_name='Aliyu Lapai')

        match1 = Match.objects.create(seeker_male=y_baba, seeker_female=z_usman, imam=imams[0], status='active chat', created_at=date(2026, 6, 1))
        match2 = Match.objects.create(seeker_male=m_bida, seeker_female=a_agaie, imam=imams[1], status='closed', created_at=date(2026, 5, 10))
        match3 = Match.objects.create(seeker_male=s_katcha, seeker_female=n_etsu, imam=imams[2], status='meeting planned', created_at=date(2026, 6, 5))
        match4 = Match.objects.create(seeker_male=y_baba, seeker_female=a_bida, imam=imams[3], status='nikah', created_at=date(2026, 4, 12))
        match5 = Match.objects.create(seeker_male=al_lapai, seeker_female=a_agaie, imam=imams[4], status='closed', created_at=date(2026, 3, 15))

        # 6. Create Chat Messages
        # Match 1 messages (active chat)
        messages_m1 = [
            ('Yahaya Baba', 'Assalamu alaykum, I hope you are doing well.'),
            ('Mallam Usman Isa', 'Wa alaykum assalam. I am present to oversee this conversation.'),
            ('Zainab Usman', 'Wa alaykum assalam. I am doing well, Alhamdulillah. How are you?'),
            ('Yahaya Baba', 'Alhamdulillah, I wanted to ask about your family in Minna.'),
            ('Zainab Usman', 'Yes, my father resides in Minna, near the Central Mosque.'),
            # Flagged message
            ('Yahaya Baba', 'Great. Can we exchange numbers? Please text me at +2348039999999 so we can speak privately.'),
        ]

        now = timezone.now()
        for i, (sender, text) in enumerate(messages_m1):
            is_flagged = 'numbers' in text or 'text me' in text
            flag_reason = 'Attempted phone number exchange' if is_flagged else ''
            ChatMessage.objects.create(
                match=match1,
                sender=sender,
                text=text,
                timestamp=now - timedelta(hours=len(messages_m1) - i),
                is_flagged=is_flagged,
                flag_reason=flag_reason
            )

        # Let's create an AI flagged message without Wali present
        match_no_wali = Match.objects.create(seeker_male=y_baba, seeker_female=z_usman, imam=imams[0], status='active chat', created_at=date(2026, 6, 2))
        ChatMessage.objects.create(
            match=match_no_wali,
            sender='Yahaya Baba',
            text='Hello Zainab, just sending a message directly. I hope you don\'t mind.',
            timestamp=now - timedelta(minutes=30),
            is_flagged=True,
            flag_reason='Missing Wali in conversation'
        )

        # 7. Create Moderation Reports
        reports_data = [
            {'reporter': 'Zainab Usman', 'reported_user': 'Yahaya Baba', 'reason': 'Profile photo appears fake / stock image. It does not look like a real photo.', 'status': 'open', 'created_at': now - timedelta(days=2)},
            {'reporter': 'System AI', 'reported_user': 'Yahaya Baba', 'reason': 'Attempted phone number exchange: "Can we exchange numbers? Please text me at +2348039999999..."', 'status': 'open', 'created_at': now - timedelta(days=1)},
            {'reporter': 'System AI', 'reported_user': 'Mohammed Bida', 'reason': 'Off-platform contact request detected. Requesting to chat on WhatsApp.', 'status': 'reviewing', 'created_at': now - timedelta(hours=12)},
            {'reporter': 'System AI', 'reported_user': 'Saidu Katcha', 'reason': 'Inappropriate language flagged by AI during chat supervision.', 'status': 'resolved', 'created_at': now - timedelta(days=5)},
            {'reporter': 'System AI', 'reported_user': 'Yahaya Baba', 'reason': 'Missing Wali in conversation. Exchanged 3+ messages without Wali online or read-status.', 'status': 'open', 'created_at': now - timedelta(hours=2)},
            {'reporter': 'Fatima Ibrahim', 'reported_user': 'Mohammed Bida', 'reason': 'Sent inappropriate message despite Wali present in group.', 'status': 'reviewing', 'created_at': now - timedelta(hours=1)}
        ]

        for r in reports_data:
            Report.objects.create(**r)

        # 8. Create Verification Requests
        verifications_data = [
            {'user_name': 'Fatima Ibrahim', 'document_type': 'National ID Card', 'document_preview_url': '/static/dashboard/docs/id_fatima.jpg', 'created_at': date(2026, 7, 10), 'status': 'pending'},
            {'user_name': 'Ibrahim Mokwa', 'document_type': 'International Passport', 'document_preview_url': '/static/dashboard/docs/passport_ibrahim.jpg', 'created_at': date(2026, 7, 11), 'status': 'pending'},
            {'user_name': 'Usman Agaie', 'document_type': 'Drivers License', 'document_preview_url': '/static/dashboard/docs/license_usman.jpg', 'created_at': date(2026, 7, 9), 'status': 'pending'},
            {'user_name': 'Yahaya Baba', 'document_type': 'National ID Card', 'document_preview_url': '/static/dashboard/docs/id_yahaya.jpg', 'created_at': date(2026, 6, 1), 'status': 'approved'},
            {'user_name': 'Zainab Usman', 'document_type': 'National ID Card', 'document_preview_url': '/static/dashboard/docs/id_zainab.jpg', 'created_at': date(2026, 6, 2), 'status': 'approved'}
        ]

        for vr in verifications_data:
            VerificationRequest.objects.create(**vr)

        # 9. Create Revenue Transactions ( USD, last 8 months)
        # Create some transactions distributed over past months
        today = date.today()
        transaction_types = ['Subscription', 'Match Fee', 'Donation']
        transaction_amounts = [20.00, 15.00, 50.00, 100.00, 10.00]
        users = ['Yahaya Baba', 'Zainab Usman', 'Mohammed Bida', 'Amina Agaie', 'Saidu Katcha', 'Nana Etsu', 'Aliyu Lapai', 'Usman Agaie']

        for i in range(120):  # 120 mock transactions
            tx_date = today - timedelta(days=random.randint(1, 240))
            RevenueTransaction.objects.create(
                user_name=random.choice(users),
                transaction_type=random.choice(transaction_types),
                amount=random.choice(transaction_amounts),
                status='success' if random.random() > 0.05 else 'failed',
                created_at=tx_date
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated database with mock data!'))
