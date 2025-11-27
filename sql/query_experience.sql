SELECT employer.name,
       position.name,
       position.start_date AS "start_date [date]",
       position.end_date   AS "end_date [date]",
       highlight.description
FROM job_employer employer
         INNER JOIN job_jobposition position
                    ON position.employer_id = employer.id
         LEFT JOIN job_jobpositionhighlight highlight
                   ON highlight.position_id = position.id
ORDER BY end_date DESC, start_date DESC;
