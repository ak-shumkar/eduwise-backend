from eduwise.institutions import InstitutionType


TYPES = [
    'Gurukula',
    'Academy',
    'College',
    'Career college',
    'Community college',
    'Junior college',
    'Liberal arts college',
    'Madrasah',
    'Residential college',
    'Sixth form college',
    'Technical college',
    'University college',
    'Graduate school',
    'Institute of technology',
    'University',
    'Corporate university',
    'International university',
    'Local university',
    'Jamiah',
    'Medieval university',
    'Nizamiyya',
    'Private university',
    'Public university',
    'Yeshiva',
    'Seminary',
]

print('GENERATING INSTITUTION TYPES...')
for tp in TYPES:
    try:
        InstitutionType.objects.create(name=tp)
    except Exception as e:
        print(e)
