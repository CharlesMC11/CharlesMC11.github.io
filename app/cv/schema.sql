-- Jobs -----------------------------------------------------------------------


CREATE TABLE job_employers
(
    employer_id   INTEGER     NOT NULL
        CONSTRAINT employer_pk PRIMARY KEY AUTOINCREMENT,
    employer_name VARCHAR(50) NOT NULL
        CONSTRAINT employer_name_uk UNIQUE
);

CREATE TABLE job_roles
(
    role_id         INTEGER                   NOT NULL
        CONSTRAINT role_pk PRIMARY KEY AUTOINCREMENT,
    employer_id     INTEGER                   NOT NULL
        CONSTRAINT employer_fk REFERENCES job_employers ON UPDATE CASCADE ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED,
    role_name       VARCHAR(50),
    role_start_date DATE                      NOT NULL,
    role_end_date   DATE DEFAULT '9999-12-31' NOT NULL
);

CREATE TABLE job_highlights
(
    highlight_id          INTEGER NOT NULL
        CONSTRAINT highlight_pk PRIMARY KEY AUTOINCREMENT,
    role_id               INTEGER NOT NULL
        CONSTRAINT role_fk REFERENCES job_roles ON UPDATE CASCADE ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED,
    highlight_description TEXT    NOT NULL
);


-- Projects -------------------------------------------------------------------


CREATE TABLE prj_projects
(
    project_id   INTEGER     NOT NULL
        CONSTRAINT project_pk PRIMARY KEY AUTOINCREMENT,
    project_name VARCHAR(50) NOT NULL
        CONSTRAINT project_name_uk UNIQUE,
    project_type VARCHAR(50) NOT NULL,
    project_url  VARCHAR(200)
);

CREATE TABLE prj_roles
(
    roles_id         INTEGER                   NOT NULL
        CONSTRAINT roles_pk PRIMARY KEY AUTOINCREMENT,
    project_id       INTEGER                   NOT NULL
        CONSTRAINT project_fk REFERENCES prj_projects ON UPDATE CASCADE ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED,
    role_names       VARCHAR(100)              NOT NULL,
    roles_start_date DATE                      NOT NULL,
    roles_end_date   DATE DEFAULT '9999-12-31' NOT NULL
);

CREATE TABLE prj_highlights
(
    highlight_id          INTEGER NOT NULL
        CONSTRAINT highlight_pk PRIMARY KEY AUTOINCREMENT,
    roles_id              INTEGER NOT NULL
        CONSTRAINT roles_fk REFERENCES prj_roles ON UPDATE CASCADE ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED,
    highlight_description TEXT    NOT NULL
);


-- Skills ---------------------------------------------------------------------


CREATE TABLE skl_categories
(
    category_id         INTEGER           NOT NULL
        CONSTRAINT category_pk PRIMARY KEY AUTOINCREMENT,
    category_name       VARCHAR(50)       NOT NULL
        CONSTRAINT category_name_uk UNIQUE,
    category_sort_index INTEGER DEFAULT 0 NOT NULL
);

CREATE TABLE skl_skills
(
    skill_id          INTEGER              NOT NULL
        CONSTRAINT skill_pk PRIMARY KEY AUTOINCREMENT,
    category_id       INTEGER              NOT NULL
        CONSTRAINT category_fk REFERENCES skl_categories ON UPDATE CASCADE ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED,
    skill_name        VARCHAR(50)          NOT NULL
        CONSTRAINT skill_name_uk UNIQUE,
    skill_subcategory VARCHAR(50)          NOT NULL,
    skill_sort_index  INTEGER DEFAULT 0    NOT NULL,
    skill_is_active   BOOL    DEFAULT TRUE NOT NULL
);


-- Education ------------------------------------------------------------------


CREATE TABLE edu_schools
(
    school_id   INTEGER     NOT NULL
        CONSTRAINT school_pk PRIMARY KEY AUTOINCREMENT,
    school_name VARCHAR(50) NOT NULL
        CONSTRAINT school_name_uk UNIQUE
);

CREATE TABLE edu_concentrations
(
    concentration_id         INTEGER                   NOT NULL
        CONSTRAINT concentration_pk PRIMARY KEY AUTOINCREMENT,
    school_id                INTEGER                   NOT NULL
        CONSTRAINT school_fk REFERENCES edu_schools ON UPDATE CASCADE ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED,
    concentration_degree     VARCHAR(50)               NOT NULL,
    concentration_name       VARCHAR(50)               NOT NULL,
    concentration_award_date DATE DEFAULT '9999-12-31' NOT NULL
);
