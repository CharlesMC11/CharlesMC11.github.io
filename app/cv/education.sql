SELECT school.school_name,
       concentration.concentration_degree,
       concentration.concentration_name,
       concentration.concentration_award_date AS "award_date [py_date]"

FROM edu_schools AS school
         INNER JOIN edu_concentrations AS concentration
                    ON school.school_id = concentration.school_id

ORDER BY concentration.concentration_award_date DESC;
