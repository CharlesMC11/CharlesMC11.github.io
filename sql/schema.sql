CREATE TABLE job_employer
(
    id       INTEGER     NOT NULL PRIMARY KEY AUTOINCREMENT,
    name     VARCHAR(50) NOT NULL UNIQUE,
    location VARCHAR(50) NOT NULL
);

create table job_jobposition
(
    id          integer     not null
        primary key autoincrement,
    name        varchar(50) not null,
    start_date  date        not null,
    end_date    date        not null,
    employer_id bigint      not null
        references job_employer
            deferrable initially deferred
);

create table job_jobpositionhighlight
(
    id          integer not null
        primary key autoincrement,
    description text    not null,
    position_id bigint  not null
        references job_jobposition
            deferrable initially deferred
);

create table prj_project
(
    id   integer     not null
        primary key autoincrement,
    name varchar(50) not null
        unique,
    type varchar(50) not null,
    link varchar(200)
);

create table prj_projectroles
(
    id         integer      not null
        primary key autoincrement,
    start_date date         not null,
    end_date   date         not null,
    project_id bigint       not null
        references prj_project
            deferrable initially deferred,
    roles      varchar(100) not null
);


create table prj_projectroleshighlight
(
    id          integer not null
        primary key autoincrement,
    description text    not null,
    roles_id    bigint  not null
        references prj_projectroles
            deferrable initially deferred
);

create table edu_school
(
    id       integer     not null
        primary key autoincrement,
    name     varchar(50) not null
        unique,
    location varchar(50) not null
);

create table edu_concentration
(
    id            integer     not null
        primary key autoincrement,
    degree        varchar(50) not null,
    concentration varchar(50) not null,
    school_id     bigint      not null
        references edu_school (id)
            deferrable initially deferred,
    awarded       date        not null
);


create table skl_skillcategory
(
    id      integer     not null
        primary key autoincrement,
    name    varchar(50) not null
        unique,
    "order" integer     not null
);

create table skl_skill
(
    id          integer     not null
        primary key autoincrement,
    name        varchar(50) not null
        unique,
    subcategory varchar(50) not null,
    "order"     integer     not null,
    category_id bigint      not null
        references skl_skillcategory
            deferrable initially deferred,
    is_active   bool        not null
);

