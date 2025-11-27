SELECT school.name,
       concentration.degree,
       concentration.concentration,
       concentration.awarded AS "awarded [date]"
FROM edu_school school
         INNER JOIN edu_concentration concentration
                    ON school.id = concentration.school_id
ORDER BY concentration.awarded DESC;
