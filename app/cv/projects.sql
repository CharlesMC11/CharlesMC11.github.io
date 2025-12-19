SELECT project.project_name,
       project.project_type,
       project.project_url,
       roles.role_names,
       roles.roles_start_date AS "start_date [py_date]",
       roles.roles_end_date   AS "end_date [py_date]",
       highlight.highlight_description

FROM prj_projects AS project
         INNER JOIN prj_roles AS roles
                    ON roles.project_id = project.project_id
         LEFT JOIN prj_highlights AS highlight
                   ON highlight.roles_id = roles.roles_id

ORDER BY roles.roles_end_date DESC, roles.roles_start_date DESC;
