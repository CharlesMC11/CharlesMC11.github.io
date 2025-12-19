SELECT employer.employer_name,
       position.role_name,
       position.role_start_date AS "start_date [py_date]",
       position.role_end_date   AS "end_date [py_date]",
       highlight.highlight_description

FROM JOB_Employers AS employer
         INNER JOIN job_roles AS position
                    ON position.employer_id = employer.employer_id
         LEFT JOIN job_highlights AS highlight
                   ON highlight.role_id = position.role_id

ORDER BY position.role_end_date DESC, position.role_start_date DESC,
         highlight.highlight_id;
