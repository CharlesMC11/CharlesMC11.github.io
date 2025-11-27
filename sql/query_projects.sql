SELECT project.name,
       project.type,
       project.link,
       roles.roles,
       roles.start_date AS "start_date [date]",
       roles.end_date   AS "end_date [date]",
       highlight.description
FROM prj_project project
         INNER JOIN prj_projectroles roles
                    ON roles.project_id = project.id
         LEFT JOIN prj_projectroleshighlight highlight
                   ON highlight.roles_id = roles.id
ORDER BY end_date DESC, start_date DESC;
