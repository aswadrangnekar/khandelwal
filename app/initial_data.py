
from google.appengine.ext import db

projects = (
    {
        'title': u'Savgan Heights',
        'subtitle': u'2 & 3 BHK Premium Apartments with Terrace',
        'slogan': u'Where peace & tranquility reigns supreme...',
        'location': u'Four Bungalows, Andheri (W)',
        'cover_picture_url': 'http://dl.dropbox.com/u/4350742/khandelwal/photos/savgan_heights/savgan_heights.jpg',
        'cover_thumb_url': 'http://dl.dropbox.com/u/4350742/khandelwal/photos/thumb/savgan_heights/savgan_heights.jpg',
        'development_status': 'ongoing',
        'photos': [
            {
                'caption': 'Savgan Heights',
                'picture_url': 'http://dl.dropbox.com/u/4350742/khandelwal/photos/savgan_heights/savgan_heights.jpg',
                'thumb_url': 'http://dl.dropbox.com/u/4350742/khandelwal/photos/thumb/savgan_heights/savgan_heights.jpg',
            },
            {
                'caption': 'Location Map',
                'picture_url': 'http://dl.dropbox.com/u/4350742/khandelwal/photos/savgan_heights/savgan_location_map.jpg',
                'thumb_url': 'http://dl.dropbox.com/u/4350742/khandelwal/photos/thumb/savgan_heights/savgan_location_map.jpg',
            },
        ],
        'floor_plans': [
            {
                'caption': 'Floor Plan 1',
                'picture_url': 'http://dl.dropbox.com/u/4350742/khandelwal/photos/savgan_heights/savgan_floor_plan_1.jpg',
                'thumb_url': 'http://dl.dropbox.com/u/4350742/khandelwal/photos/thumb/savgan_heights/savgan_floor_plan_1.jpg',            
            },
            {
                'caption': 'Floor Plan 2',
                'picture_url': 'http://dl.dropbox.com/u/4350742/khandelwal/photos/savgan_heights/savgan_floor_plan_2.jpg',
                'thumb_url': 'http://dl.dropbox.com/u/4350742/khandelwal/photos/thumb/savgan_heights/savgan_floor_plan_2.jpg',            
            },
            {
                'caption': 'Floor Plan 3',
                'picture_url': 'http://dl.dropbox.com/u/4350742/khandelwal/photos/savgan_heights/savgan_floor_plan_3.jpg',
                'thumb_url': 'http://dl.dropbox.com/u/4350742/khandelwal/photos/thumb/savgan_heights/savgan_floor_plan_3.jpg',            
            },
            {
                'caption': 'Floor Plan 4',
                'picture_url': 'http://dl.dropbox.com/u/4350742/khandelwal/photos/savgan_heights/savgan_floor_plan_4.jpg',
                'thumb_url': 'http://dl.dropbox.com/u/4350742/khandelwal/photos/thumb/savgan_heights/savgan_floor_plan_4.jpg',            
            },
        ],
        'description': '''
## Project Highlights

* 10 storey tower with permium terrace flats adjoining sports club being developed by the famous and reputed MIG club.
* Opposite major Metro Hub.
* Close to Asia's best Ambani Hospital.
* Proximity to schools, temples, banks, markets, multiplex, food court, and various shopping avenues.
* Enhance lifestyle-Free club membership for entire family with top class sports, fitness, leisure facilities adjoining the site (being developed by the reputed promoters of famous MIG Club, Bandra).
* Nursing home on first floor.
* Showroom/Offices
* Reputed developers committed to excellent quality, complete satisfaction, and prompt possession.
* Vastu friendly.

## Amenities

* Wall-to-wall elegant vitrified flooring
* Granite kitchen platform with built-in stainless steel sink covered with full height ceramic tiles.
* Designer ceramic tiles upto full height in bathroom & WC.
* Good quality concealed copper wiring with adequate points.
* Anodized aluminium sliding windows.
* Superior quality distemper paint in entire flat.
* Landscape greenery.
* Majestic entrace and grand lobby.
* Automatic high speed modern elevators.
* Spacious and airy flats with cross ventilation.
* Excellent general and modern amenities.
        ''',
    },
)

def import_projects(projects=projects):
    from models import Project, ProjectPhoto, ProjectFloorPlan
    for p in projects:
        project = Project(title=p['title'],
            subtitle=p['subtitle'],
            slogan=p['slogan'],
            location=p['location'],
            cover_picture_url=p['cover_picture_url'],
            cover_thumb_url=p['cover_thumb_url'],
            development_status=p['development_status'],
            description=p['description'])
        project.put()
        fps = []
        for fp in p['floor_plans']:
            floor_plan = ProjectFloorPlan(caption=fp['caption'],
                thumb_url=fp['thumb_url'],
                picture_url=fp['picture_url'],
                project=project)
            fps.append(floor_plan)
        db.put(fps)
        photos = []
        for fp in p['photos']:
            photo = ProjectPhoto(caption=fp['caption'],
                thumb_url=fp['thumb_url'],
                picture_url=fp['picture_url'],
                project=project)
            photos.append(photo)
        db.put(photos)
