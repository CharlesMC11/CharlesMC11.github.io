SELECT category.name, skill.name
FROM skl_skillcategory category
         INNER JOIN skl_skill skill ON skill.category_id = category.id
WHERE skill.is_active is TRUE
ORDER BY category.sort_order, skill.sort_order;
