-- Jobs -----------------------------------------------------------------------


INSERT INTO job_employers (employer_name)
VALUES ('San José State University'),
       ('FanimeCon'),
       ('Bodhi Meditation'),
       ('De Anza College'),
       ('Shutterfly Lifetouch, LLC');


INSERT INTO job_roles (employer_id, role_name, role_start_date, role_end_date)
VALUES (1, 'Shrunkenheadman Club Event Photographer', '2018-09-10',
        '2023-05-24'),
       (1, 'CG Rigging Courses Teacher’s Assistant', '2023-01-25',
        '2023-05-15'),
       (2, 'Cosplay Photographer', '2024-04-21', '2025-08-08'),
       (3, 'Volunteer Photographer', '2024-05-11', '2024-08-18');
INSERT INTO job_roles (employer_id, role_name, role_start_date)
VALUES (4, 'Instructional Assistant', '2024-10-01'),
       (5, 'Seasonal Photographer', '2025-10-17');

INSERT INTO job_highlights (role_id, highlight_description)
VALUES (2,
        'Answered 20+ students’ questions regarding assignments and lectures'),
       (2,
        'Gave step‐by‐step directions to troubleshoot issues that arose in the rigging process'),
       (5, 'Assists 20+ students in learning and using animation software'),
       (5,
        'Demos and creates guides for using film and animation production equipment'),
       (5,
        'Checks on and provides constructive feedback to students‘ work during lab time'),
       (5, 'Facilitates equipment checkouts, returns, and inventory'),
       (6, 'Guides customers in purchasing options that fit their needs'),
       (6,
        'Assists in front desk check-ins, photo room preparations, and transactions data entry');


-- Projects -------------------------------------------------------------------


INSERT INTO prj_projects (project_name, project_type)
VALUES ('The H(a)unt', '3D Animated Sequence'),
       ('Jet-Jacked', '3D Animated Sequence')
;

INSERT INTO prj_projects (project_name, project_type, project_url)
VALUES ('A Trace', '3D Animated Short Film',
        'https://linktr.ee/atraceshortfilm?utm_source=linktree_profile_share&ltsid=6c199482-8529-4dee-be50-4289d27a87a5'),
       ('Kiki’s Bakery', '3D Environment',
        'https://vimeo.com/795348460?fl=pl&fe=sh'),
       ('My Turn!', '2D Animated Short Film',
        'https://www.kickstarter.com/projects/myturnshortfilm/my-turn'),
       ('re:connection', '3D Animated Short Film',
        'https://re-connection.carrd.co/'),
       ('Spirit Driver', 'Visual Novel',
        'https://noodledonut.itch.io/spirit-driver')
;

INSERT INTO prj_roles (project_id, role_names, roles_start_date,
                       roles_end_date)
VALUES (1, 'Technical Lead, Animator', '2021-10-25', '2021-12-15'),
       (2, 'Technical Lead, Animator', '2022-04-10', '2022-05-25'),
       (3, 'Technical & Rigging Lead', '2022-06-16', '2023-05-25'),
       (4, 'Technical Lead, Rigger, Animator, Modeler', '2022-11-03',
        '2022-12-15'),
       (3, 'Character Animator', '2023-04-14', '2023-05-25'),
       (4, 'Technical  Assistance', '2024-01-06', '2024-05-20'),
       (5, 'Pipeline Technical Director', '2024-01-19', '2024-05-20'),
       (6, 'Programmer', '2024-09-01', '2024-09-30')
;

INSERT INTO prj_highlights (roles_id, highlight_description)
VALUES (1, 'Set up scene lights and render settings'),
       (1, 'Animated a character and a prop across four weeks'),
       (1,
        'Wrote MEL scripts for resetting rig controllers to their default positions'),
       (2, 'Rigged two vehicles and a character’s hair within a week'),
       (2,
        'Animated a character, two vehicles, and a camera across six weeks'),
       (2,
        'Wrote Python scripts for resetting rig controllers to their default positions'),
       (2,
        'Optimized 3D assets for responsive scene navigation and animation playback'),
       (3,
        'Provided solutions for technical challenges the core team of 10 artists encountered'),
       (3,
        'Enhanced team’s workflow by authoring scripts for tedious and repetitive tasks'),
       (3,
        'Led R&D for rigging a flat, paper character and 4 props across 9 months'),
       (3,
        'Optimized render settings, co‐wrote a guide, and coached the team to set up renders'),
       (3,
        'Co‐created a timeline spreadsheet for rendering and compositing all 54 shots of the film'),
       (4,
        'Rigged and animated a prop, scene lights, and a camera within a week'),
       (4, 'Sculpted, textured, rigged, and animated a cat across 5 weeks'),
       (4,
        'Provided methods to optimize scene that reduced rendering time nearly by 50%'),
       (4,
        'Troubleshot technical issues related to 3D modeling and rendering'),
       (6,
        'Wrote a script for exporting frames from Harmony to the proper shot folders on GDrive'),
       (7,
        'Sped up lighting and rendering pipeline by 80% by developing scripts for exporting and importing assets to and from the proper GDrive folders'),
       (7,
        'Troubleshot technical problems the artists encountered during production');


-- Skills ---------------------------------------------------------------------


INSERT INTO skl_categories (category_name, category_sort_index)
VALUES ('Languages', 99),
       ('Technical', 0),
       ('Software', 1),
       ('Adobe', 5);

INSERT INTO skl_skills (category_id, skill_name, skill_subcategory,
                        skill_sort_index)
VALUES (1, 'Python', 'Programming', 0),
       (1, 'C++', 'Programming', 0),
       (1, 'Z shell', 'Programming', 0),
       (1, 'Tagalog', 'Human', 98),
       (1, 'English', 'Human', 99),
       (1, 'Maya Embedded Langauge', 'Programming', 90)
;


-- Education ------------------------------------------------------------------


INSERT INTO edu_schools (school_name)
VALUES ('De Anza College'),
       ('San José State University');


INSERT INTO edu_concentrations (school_id, concentration_degree,
                                concentration_name, concentration_award_date)
VALUES (1, 'Associate in Arts', 'Film/TV: Animation', '2018-08-24'),
       (1, 'Associate in Arts', 'Liberal Arts (Arts and Letters Emphasis',
        '2018-08-24'),
       (2, 'Bachelor of Fine Arts', 'Animation & Illustration', '2023-05-26'),
       (1, 'Certificate of Achievement', 'Programming in C/C++', '2025-08-22'),
       (1, 'Certificate of Achievement', 'Programming in Python',
        '2025-08-22'),;

INSERT INTO edu_concentrations (school_id, concentration_degree,
                                concentration_name)
VALUES (1, 'Associate in Arts', 'Systems Programming');

